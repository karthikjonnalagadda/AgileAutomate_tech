"""
clean_leads.py
--------------
Sunrise Interiors - lead list cleaning utility.

Takes a messy leads export and produces a clean one by:
  1. Standardising every phone number to the format +91XXXXXXXXXX
  2. Removing exact duplicate rows (rows identical in every column)

Order matters: normalisation runs FIRST, then deduplication. The same phone
number can be written several ways ("+919876500000" and "9876500000"), so two
rows are only comparable once their numbers are in one canonical format.

Usage:
    python clean_leads.py
"""

import re
from pathlib import Path

import pandas as pd

INPUT_FILE = Path("input.csv")
OUTPUT_FILE = Path("cleaned_leads.csv")

COUNTRY_CODE = "+91"
INDIA_DIALLING_CODE = "91"
MOBILE_NUMBER_LENGTH = 10
# Indian mobile numbers always begin with 6, 7, 8 or 9.
VALID_MOBILE_FIRST_DIGITS = ("6", "7", "8", "9")


def extract_digits(raw_phone):
    """Return only the digit characters from a phone number.

    This is what removes spaces, hyphens, plus signs, brackets and dots in a
    single pass, instead of stripping each separator one at a time.
    """
    return re.sub(r"\D", "", str(raw_phone))


def strip_prefix(digits):
    """Reduce a digit string to the bare 10-digit mobile number.

    Handled cases:
      13 digits starting '091' -> trunk '0' after country code   (0919876543210)
      12 digits starting '91'  -> country code present           (919876543210)
      11 digits starting '0'   -> domestic trunk prefix          (09876543210)
      10 digits                -> already bare, return unchanged
    """
    if len(digits) == 13 and digits.startswith("0" + INDIA_DIALLING_CODE):
        return digits[3:]
    if len(digits) == 12 and digits.startswith(INDIA_DIALLING_CODE):
        return digits[2:]
    if len(digits) == 11 and digits.startswith("0"):
        return digits[1:]
    return digits


def is_valid_mobile(digits):
    """A number is usable only if it is 10 digits and starts 6/7/8/9."""
    return (
        len(digits) == MOBILE_NUMBER_LENGTH
        and digits.startswith(VALID_MOBILE_FIRST_DIGITS)
    )


def normalize_phone(raw_phone):
    """Convert any supported phone format to +91XXXXXXXXXX.

    Returns None when the number cannot be trusted, so bad data is flagged
    for a human rather than silently reshaped into something wrong.
    """
    digits = extract_digits(raw_phone)
    bare_number = strip_prefix(digits)

    if not is_valid_mobile(bare_number):
        return None

    return COUNTRY_CODE + bare_number


def clean_leads(leads):
    """Normalise phone numbers, then drop exact duplicate rows.

    Returns (cleaned_dataframe, invalid_rows_dataframe).
    """
    cleaned = leads.copy()

    # Trim stray whitespace so " Ravi Kumar" and "Ravi Kumar" are not treated
    # as two different people.
    cleaned["Name"] = cleaned["Name"].astype(str).str.strip()

    cleaned["Original Phone"] = cleaned["Phone"]
    cleaned["Phone"] = cleaned["Phone"].apply(normalize_phone)

    invalid_rows = cleaned[cleaned["Phone"].isna()].copy()
    valid_rows = cleaned[cleaned["Phone"].notna()].copy()

    # Exact duplicate rows = identical in EVERY output column (Name AND Phone).
    # keep="first" preserves the earliest occurrence, so the original order of
    # the lead list is respected.
    deduplicated = valid_rows.drop_duplicates(
        subset=["Name", "Phone"], keep="first"
    )

    return deduplicated, invalid_rows


def print_report(original, cleaned, invalid):
    """Print validation output so the result can be checked at a glance."""
    print("=" * 62)
    print("SUNRISE INTERIORS - LEAD CLEANING REPORT")
    print("=" * 62)

    print("\nBEFORE -> AFTER (normalisation)")
    print("-" * 62)
    for _, row in cleaned.iterrows():
        print(f"  {row['Name']:<14} {row['Original Phone']:<18} -> {row['Phone']}")

    duplicates_removed = len(original) - len(cleaned) - len(invalid)

    print("\nSUMMARY")
    print("-" * 62)
    print(f"  Rows read from input          : {len(original)}")
    print(f"  Invalid numbers flagged       : {len(invalid)}")
    print(f"  Exact duplicate rows removed  : {duplicates_removed}")
    print(f"  Rows written to output        : {len(cleaned)}")

    if not invalid.empty:
        print("\n  NEEDS MANUAL REVIEW (not written to output):")
        for _, row in invalid.iterrows():
            shown = row["Original Phone"]
            shown = "(blank)" if pd.isna(shown) or str(shown).strip() == "" else shown
            print(f"    {row['Name']} - {shown}")

    # Confirm the stated requirement actually holds for every output row.
    pattern = re.compile(r"^\+91\d{10}$")
    all_formatted = cleaned["Phone"].apply(lambda p: bool(pattern.match(p))).all()
    print(f"\n  All numbers match +91XXXXXXXXXX : {all_formatted}")
    print(f"  Duplicate rows remaining        : {cleaned.duplicated().sum()}")
    print("=" * 62)


def main():
    if not INPUT_FILE.exists():
        raise SystemExit(f"Input file not found: {INPUT_FILE.resolve()}")

    # dtype=str stops pandas turning "9876543210" into a number and losing
    # the leading zero in values like "098-765-99887".
    leads = pd.read_csv(INPUT_FILE, dtype=str)

    cleaned, invalid = clean_leads(leads)
    print_report(leads, cleaned, invalid)

    cleaned[["Name", "Phone"]].to_csv(OUTPUT_FILE, index=False)
    print(f"\nCleaned file written to: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()

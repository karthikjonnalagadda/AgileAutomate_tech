# Task 2 — Python Data Cleaning

**Status: VERIFIED** — implemented, executed and tested on 19 Aug 2026.

## Files

| File | Purpose |
|------|---------|
| `input.csv` | The messy leads export, byte-exact from the assignment PDF |
| `clean_leads.py` | The cleaning script |
| `cleaned_leads.csv` | Actual output produced by running the script |
| `test_cases.md` | 17 normalisation edge cases + an end-to-end invalid-data test |

## Run it

```
cd C:\Users\karth\AgileAutomate_Assignment\02_Python
python clean_leads.py
```

Requires pandas. Must be run from this folder — the script reads `input.csv`
from the working directory.

## Result

6 input rows → 5 output rows. One exact duplicate removed. Zero invalid
numbers. All output matches `+91XXXXXXXXXX`.

## The interpretation decision

The raw file contains **zero exact duplicate rows** — `+919876500000` and
`9876500000` are different strings. Deduplicating before normalising would
remove nothing, making the requirement meaningless.

So the order is **normalise first, then remove exact duplicate rows**. After
normalisation both Sneha Reddy rows become the identical row
`Sneha Reddy,+919876500000`, and one is dropped.

This is still literally "remove exact duplicate rows" — the match is on the
**full row (Name AND Phone)**, not on phone alone. Two different people sharing
a number would both be kept, which is correct: that is a data-quality flag, not
a duplicate.

**Deliberately not implemented:** deduplication on phone number alone, which
would merge rows with different names. That is a judgement call for a human,
and the assignment asked for exact duplicate rows. Worth mentioning in the
interview as a production enhancement that was considered and rejected on
purpose.

## Normalisation logic

1. **Strip every non-digit** with one regex — removes spaces, hyphens, `+`,
   brackets and dots in a single pass.
2. **Remove the prefix, decided by length** — 13 digits starting `091`,
   12 digits starting `91`, or 11 digits starting `0`. Length is checked
   **before** the prefix, so a valid 10-digit number starting "91" survives
   untouched.
3. **Validate** — accept only 10 digits starting 6, 7, 8 or 9. Anything else
   returns `None` and is flagged for a human rather than force-fitted.

## Why pandas

The task is CSV in, CSV out, with row-level deduplication. `drop_duplicates()`
expresses "remove exact duplicate rows" in one line that reads like the
requirement. `dtype=str` on read also matters: without it pandas parses
`9876543210` as an integer and `098-765-99887` loses its leading zero before
the code ever sees it.

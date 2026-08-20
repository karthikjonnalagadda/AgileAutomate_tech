# Task 2 — Test Cases

**Status: VERIFIED** — every case below was executed against `clean_leads.py` on 19 Aug 2026. Results are actual output, not expected output.

## 1. Assignment data (the required result)

Input: `input.csv` — 6 rows. Output: `cleaned_leads.csv` — 5 rows.

```
Ravi Kumar     9876543210         -> +919876543210
Priya Shah     91 98765 12345     -> +919876512345
Amit Verma     098-765-99887      -> +919876599887
Sneha Reddy    +919876500000      -> +919876500000
Karan Mehta    +91-9876511111     -> +919876511111

Rows read from input          : 6
Invalid numbers flagged       : 0
Exact duplicate rows removed  : 1
Rows written to output        : 5
All numbers match +91XXXXXXXXXX : True
Duplicate rows remaining        : 0
```

## 2. Normalisation edge cases — 17 cases, all passing

| Input | Result | What it proves |
|-------|--------|----------------|
| `9876543210` | `+919876543210` | plain 10-digit |
| `91 98765 12345` | `+919876512345` | spaces + country code |
| `098-765-99887` | `+919876599887` | leading zero + hyphens |
| `+919876500000` | `+919876500000` | already correct, unchanged |
| `+91-9876511111` | `+919876511111` | `+91` with hyphen |
| `  9876543210  ` | `+919876543210` | surrounding whitespace |
| `(+91) 98765 43210` | `+919876543210` | brackets |
| `+91.98765.43210` | `+919876543210` | dots |
| `0919876543210` | `+919876543210` | trunk `0` **and** country code |
| **`9198765432`** | **`+919198765432`** | **10-digit starting "91" correctly NOT stripped** |
| `919876543210` | `+919876543210` | 12-digit with country code |
| `98765` | `None` | too short, flagged |
| `98765432101234` | `None` | too long, flagged |
| `1234567890` | `None` | invalid first digit |
| `5876543210` | `None` | invalid first digit |
| `abcdefghij` | `None` | no digits |
| *(empty)* | `None` | blank cell |

### The case that matters most

`9198765432` is a **valid 10-digit number that happens to start with "91"**. The obvious implementation — *"if it starts with 91, strip it"* — destroys this number, leaving an 8-digit fragment that then fails validation and gets silently dropped.

This script checks **length first, then prefix**:

```python
if len(digits) == 12 and digits.startswith(INDIA_DIALLING_CODE):
    return digits[2:]
```

A 10-digit number never matches, so it passes through untouched. Same principle for the leading `0`: stripped only when the number is 11 digits long.

## 3. Invalid and blank data — end-to-end test

Input:

```
Name,Phone
Ravi Kumar,9876543210
Ravi Kumar,+91 98765 43210
Bad Lead,12345
Blank Lead,
Karan Mehta,+91-9876511111
```

Actual output:

```
Rows read from input          : 5
Invalid numbers flagged       : 2
Exact duplicate rows removed  : 1
Rows written to output        : 2

NEEDS MANUAL REVIEW (not written to output):
  Bad Lead - 12345
  Blank Lead - (blank)
```

Cleaned file:

```
Name,Phone
Ravi Kumar,+919876543210
Karan Mehta,+919876511111
```

This proves three behaviours at once: the two Ravi Kumar rows in different formats collapse to one after normalisation, invalid numbers are **flagged rather than silently deleted**, and a blank cell is handled without crashing.

## 4. How to reproduce

```
cd C:\Users\karth\AgileAutomate_Assignment\02_Python
python clean_leads.py
```

The script must be run from that folder — it reads `input.csv` from the working directory.

Requires `pandas` (tested on pandas 2.3.3, Python 3.13.2).

# Technical Implementation Specialist (Intern)
## Agile Automate — Assignment Submission

**Candidate:** Karthik Jonnalagadda
**Client scenario:** Sunrise Interiors — 6-person interior design studio, Bengaluru


## 1. Overview

Sunrise Interiors runs a design studio out of WhatsApp groups and Excel files. That works until it doesn't: deadlines slip because nobody owns a handoff, vendors get paid twice because the record of payment lives in a chat thread nobody can search, and the owner cannot answer "which project is actually in trouble?" without calling three people.

These are not three problems. They are one problem — **no single searchable source of truth** — surfacing in three places.

| Task | Delivered | Status |
|------|-----------|--------|
| 1 | ClickUp workspace covering client projects (lead → handover), vendor payments, and task assignment across three designers | Built and verified |
| 2 | Python script standardising phone numbers to `+91XXXXXXXXXX` and removing exact duplicate rows | Implemented and tested |
| 3 | n8n workflow design for Google Form lead intake with a conditional team notification | Designed (theoretical, per the brief) |

The guiding constraint was to keep the system small enough that six people will actually use it. Every field, status and view earns its place; anything that did not change a decision was left out.

---

## 2. ClickUp Implementation

### 2.1 Workspace Architecture

```
Workspace: Sunrise Interiors
│
├── Space 1: Client Projects
│   ├── List: Projects        → 1 task = 1 client project (Lead → Handover)
│   └── List: Design Tasks    → 1 task = 1 work item assigned to a designer
│
└── Space 2: Vendors & Payments
    └── List: Vendor Payments → 1 task = 1 invoice / payable
```

Two Spaces, three Lists, no Folders.

**Why two Spaces.** ClickUp inherits statuses from the Space. A project lifecycle (`Lead → Handover`) and a payment lifecycle (`PO Raised → Paid`) are different state machines. Separating them lets each have an honest status set instead of one bloated list where half the statuses are meaningless. It also means the owner can later share only the Vendors space with an accountant.

**Why no Folders.** Folders group many Lists. There are three. Adding Folders would be hierarchy for its own sake.

**Why a project is a Task, not a List.** The obvious alternative is one List per project. Lists cannot hold custom fields, cannot carry a status, and cannot be counted by a view. Making a project a task puts Budget, Health, Expected Handover and Project Manager on it, so one view can filter and count every project at once. This decision is what makes the 10-second health check possible.

**Why Design Tasks is a separate List.** Work items need `To Do → In Progress → Ready for Review → Complete`; project shells need `Lead → … → Handover`. Same reasoning as the Spaces.

**Team:** the owner plus Meera Iyer (Senior Designer, acting PM), Arjun Rao (drawings and 3D), Divya Nair (materials and procurement).

*[Screenshot 01_workspace.png — sidebar showing both Spaces and all three Lists]*

### 2.2 Client Project Lifecycle

| # | Status | Why it exists |
|---|--------|---------------|
| 1 | Lead | Inquiry received, not yet won. Keeps the pipeline visible. Landing status for the n8n workflow in section 4. |
| 2 | Planning | Won. Site measurement, scope, budget, timeline. |
| 3 | Design | Drawings, 3D views, material palette. |
| 4 | Client Approval | Waiting on client sign-off. Most interior-design delays are client-side; without this status the owner blames the team for a delay the team did not cause. |
| 5 | Procurement | Materials ordered, vendors engaged. Signals money going out. |
| 6 | Execution | On-site work. |
| 7 | Handover | Snagging closed, handed to client. |
| 8 | Closed / Lost | Lead did not convert, or project archived. Dead leads leave the pipeline without being deleted. |

**There is deliberately no "On Hold" status.** A stalled project is flagged `At Risk` or `Delayed` via Project Health while staying in its real stage — moving it to On Hold would erase *where* it stalled, which is the useful part.

Six sample projects span six stages, including one in `Lead` and one in `Handover`, so lead-to-handover coverage is demonstrated rather than asserted.

*[Screenshot 03_project_lifecycle.png — Projects board grouped by lifecycle status]*

### 2.3 Custom Fields

**Projects list — five populated fields:**

| Field | Type | Example | Why it is useful |
|-------|------|---------|------------------|
| Client | Text | Mr. & Mrs. Nair | The billable party, which may differ from the project name. |
| Project Budget | Money (INR) | 18,00,000 | Lets the owner prioritise a delayed ₹18L project over a delayed ₹6.5L one. |
| Project Health | Dropdown | On Track / At Risk / Delayed | The field the entire owner view is built on. |
| Project Manager | People | Meera Iyer | One accountable name per project. |
| Expected Handover | Date | 30 Nov 2026 | The promise made to the client; overdue is measured against it. |

**Design Tasks and Vendor Payments use native ClickUp fields** — assignee, due date, status — rather than custom fields. This was partly a design preference and partly a platform constraint; see 2.6.

**Deliberately not created:** custom fields duplicating Assignee, Due Date, Priority, Comments or Attachments. ClickUp provides all of these natively. Recreating them produces two sources of truth and breaks every built-in filter and view that depends on the native versions.

*[Screenshot 02_projects.png — Projects list showing custom field columns and colour-coded Health]*

### 2.4 Vendor / Procurement Tracking

**The unit of record is one task per invoice, not one task per vendor.** A vendor has many invoices; if the vendor is the record, "is it paid?" has no single answer — and that ambiguity is exactly how a payment gets made twice.

Task naming: `INV-2314 - Sri Balaji Plywood - Rs 1,45,000`

| Data | Where it lives |
|------|----------------|
| Payment status | Native **Status**: PO Raised → Invoice Received → Approved for Payment → Paid, plus On Hold / Disputed |
| Payment due date | Native **Due Date** — drives the Payments Due view and overdue detection |
| Invoice number, vendor, amount | **Task name**, visible in every view without opening anything |
| Paid On + Payment Reference (UTR) | **Task description**, alongside the "search before you pay" rule |

**How duplicate payments are prevented.** This is a business process control, not a database constraint — ClickUp does not enforce uniqueness on an invoice number. The control works because of how the data is structured and used:

1. One payable equals one task, so there is exactly one place where "is INV-2314 paid?" is answered.
2. The invoice number is the unique reference. Before paying, search it; a hit already in `Paid` means stop.
3. `Approved for Payment` is a single approval gate held by the owner. Nothing is paid that is not in that status, so a WhatsApp message from a vendor cannot by itself cause a payment.
4. Reaching `Paid` requires recording the payment date and bank reference. A task in `Paid` with no UTR is a visible red flag.
5. One searchable source of truth. The root cause of double payment is not carelessness — it is that the record of payment was in a chat thread nobody could search.

**The sample data demonstrates this directly.** Sri Balaji Plywood appears twice: **INV-2287** for ₹98,000, paid 04 Aug 2026 with reference UTR8842019X, and **INV-2314** for ₹1,45,000, still unpaid. Under vendor-level tracking, "Sri Balaji Plywood — Paid" would suggest the account was settled. Because each invoice is its own record, the outstanding one stays visible.

**Current position:** 7 invoices, 1 paid, **6 outstanding totalling ₹8,57,100**, of which 2 are past their due date.

*[Screenshot 05_vendor_payments.png — Vendor Payments list, both Sri Balaji rows visible with differing statuses]*
*[Screenshot 10_payments_due.png — Payments Due view sorted by due date, overdue first]*

### 2.5 Design Team Task Management

Eleven work items are distributed across the three designers — currently **Meera Iyer 5, Arjun Rao 3, Divya Nair 3** — each carrying an assignee, a due date and a status.

The original split was 4 / 4 / 3. It reads 5 / 3 / 3 now because the automation in section 2.7 reassigned "Lighting design – common areas" from Arjun to Meera when it moved to Ready for Review. That is the system working as intended, and it is a useful illustration: workload distribution is live data, not a static plan.

**Assignment rule:** the project's Project Manager breaks the project into design tasks and assigns each to exactly one person. Shared ownership is no ownership.

**Tracking:**
- **By Designer** — board grouped by assignee, excluding completed work. Workload imbalance is visible without asking anyone.
- **Overdue** — due date before today, status not Complete. Currently returns **3 genuinely overdue tasks**, all on the Kapoor and Sharma projects.
- **Blocked** is a first-class status, because invisible blockers are the studio's core disease. A designer waiting on a site measurement says so in one click instead of a message that scrolls away.

**Project Health is maintained manually, by design.** An automatic formula could only read dates, and would report "On Track" on a project where the client has not approved anything for three weeks. Health is a judgement call made at the weekly review; the system's job is to make it visible, not to fake it.

*[Screenshot 04_design_tasks.png — By Designer board, three columns for Meera, Arjun and Divya]*
*[Screenshot 11_overdue.png — Overdue view returning 3 tasks]*

### 2.6 A platform constraint, and what I did about it

ClickUp's Free plan caps **custom-field usage at roughly 60 writes for the lifetime of the workspace**, and clearing values does not refund the quota — I verified this directly: usage dropped from 62 to 29 and the next write still failed with `FIELD_033`.

Rather than ask for a paid plan, I audited which fields actually drive a decision and moved everything else onto native fields, which cost nothing:

| Kept as custom fields | Moved to native fields |
|---|---|
| Client, Project Budget, Project Health, Project Manager, Expected Handover | Vendor due dates → native Due Date · Payment state → native Status · Invoice/vendor/amount → task name · Payment evidence → task description |

**Every business function survives**, including the duplicate-payment control. The one measurable cost: with no numeric Amount field, ClickUp cannot auto-sum outstanding payments, so **₹8,57,100 is a manually verified figure** rather than a calculated widget. It is stated as such here rather than faked.

The general principle this enforced is one I would apply regardless of plan: **anything the platform provides natively should not be a custom field.**

### 2.7 Automation — "Review Handoff"

| | |
|---|---|
| Scope | Design Tasks list |
| Trigger | Status changed → **Ready for Review** |
| Condition | None |
| Action 1 | Update assignees → **Meera Iyer** |
| Action 2 | Add comment: *"Ready for review — please check and approve or send back with changes."* |

**Business reason.** The studio's real failure mode is the handoff. A designer finishes a floor plan, posts it in a WhatsApp group, and it scrolls away — nobody owns the review and three days evaporate. This turns the handoff into a system event: the moment work is declared done, the reviewer becomes the assignee and a timestamped comment exists. No human memory required, and the delay becomes attributable.

The automation is deliberately **conditionless**. A condition adds a way for it to silently not fire, and for a studio adopting its first real system, an automation that always works matters more than one that is clever.

**Test performed and verified:**

```
BEFORE   status = In Progress        assignee = Arjun Rao      comments = 0
ACTION   status changed to "Ready for Review"
AFTER    status = Ready for Review   assignee = Meera Iyer     comments = 1
         comment: "Ready for review — please check and approve or send back with changes."
```

The task reassigned cleanly from Arjun to Meera, and the comment was posted by **ClickBot (Automations)** — visible in the activity feed, which proves it was generated by the rule rather than typed by a person.

*[Screenshot 06_automation_config.png — automation configuration]*
*[Screenshot 07_automation_before.png — In Progress, assigned to Arjun Rao]*
*[Screenshot 08_automation_after.png — Ready for Review, assigned to Meera Iyer, ClickBot comment visible]*

### 2.8 Owner Dashboard / View

Built around one sentence: **the owner should immediately know what is going well, what is at risk, and what needs action today.**

The **Owner Cockpit** is a board view on the Projects list grouped by **Project Health**, giving three colour-coded columns:

| Column | Count | Projects |
|--------|-------|----------|
| 🟢 On Track | **4** | Nair Residence, Rao Office Fitout, Iyer Apartment, Menon Duplex |
| 🟡 At Risk | **1** | Sharma Villa |
| 🔴 Delayed | **1** | Kapoor Kitchen Renovation |

Each card also shows its lifecycle stage, so the owner sees health *and* position in one glance — a delayed project in `Procurement` is a different problem from a delayed project in `Client Approval`.

Supporting views answer "what needs action today":
- **Overdue** — 3 design tasks past due
- **Payments Due** — 6 outstanding invoices, oldest first, 2 already overdue

**Why this satisfies the 10-second requirement.** The top row is three colour-coded counts, so the state of the business is answered before a word is read. Everything else on screen requires a decision today. There are no trend charts and no vanity metrics — anything that would not cause an action was left out on purpose. That editing decision is the real answer, not the widget count.

The assignment permits "1 Dashboard **or** View". A saved View was chosen deliberately: the free plan restricts dashboard widgets, and a board grouped by Health is both faster to read and visible to guests.

*[Screenshot 09_owner_cockpit.png — Owner Cockpit showing On Track 4, At Risk 1, Delayed 1]*

### 2.9 ClickUp Guest Access

**Workspace link:** https://app.clickup.com/90161754416/

Both reviewers have been invited directly as guests to the Sunrise Interiors workspace and should have access on their existing ClickUp accounts:

| Reviewer | Email | Access |
|----------|-------|--------|
| Amit | amit12@agileautomate.co | Guest |
| Aryansh | aryansh@agileautomate.co | Guest |

All four views — **Owner Cockpit**, **By Designer**, **Overdue** and **Payments Due** — are saved workspace views rather than personal views, so they are visible to guests rather than only to the account that created them.

Suggested starting point: open **Client Projects → Projects → Owner Cockpit** for the project health board, then **Vendors & Payments → Vendor Payments → Payments Due** for the outstanding invoices.

If access does not resolve, please reply and I will re-issue the invitation or generate public view links instead.

---

## 3. Python Data Cleaning

### 3.1 Problem

A leads export contains phone numbers written six different ways and a duplicated contact:

```
Name,Phone
Ravi Kumar,9876543210
Priya Shah,91 98765 12345
Amit Verma,098-765-99887
Sneha Reddy,+919876500000
Sneha Reddy,9876500000
Karan Mehta,+91-9876511111
```

The task: standardise every number to `+91XXXXXXXXXX` and remove exact duplicate rows.

### 3.2 Approach

**The order of operations is the key decision.** The raw file contains **zero exact duplicate rows** — `+919876500000` and `9876500000` are different strings. Deduplicating first would remove nothing and make the requirement meaningless.

```
Raw CSV → normalise phone numbers → remove exact duplicate rows → cleaned CSV
```

After normalisation both Sneha Reddy rows become the identical row `Sneha Reddy,+919876500000`, and one is removed. This remains **exact duplicate row removal** — the match is on the full row, Name *and* Phone, not on the phone alone. Two different people sharing a number would both be kept, because that is a data-quality flag for a human, not a duplicate.

Deduplication on phone number alone was considered and deliberately rejected: it would merge rows with differing names, which is a judgement call that belongs to a person.

**Normalisation is three steps:**

1. **Extract digits.** One regex removes spaces, hyphens, plus signs, brackets and dots in a single pass, rather than a chain of replacements covering only the separators someone thought of.
2. **Strip the prefix, decided by length.** Thirteen digits starting `091`, twelve starting `91`, or eleven starting `0` reduce to the bare ten. Length is checked **before** the prefix — a naive "if it starts with 91, strip it" rule would destroy the valid ten-digit number `9198765432`.
3. **Validate.** Only ten digits beginning 6, 7, 8 or 9 are accepted. Anything else is flagged for manual review rather than force-fitted into a `+91` string.

**Why pandas:** the task is CSV in, CSV out with row-level deduplication. `drop_duplicates()` states the requirement in one readable line. Reading with `dtype=str` also matters — without it pandas parses `9876543210` as an integer and `098-765-99887` loses its leading zero before the code runs.

### 3.3 Python Implementation

```python
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
    """Return only the digit characters from a phone number."""
    return re.sub(r"\D", "", str(raw_phone))


def strip_prefix(digits):
    """Reduce a digit string to the bare 10-digit mobile number.

    Handled cases:
      13 digits starting '091' -> trunk '0' after country code
      12 digits starting '91'  -> country code present
      11 digits starting '0'   -> domestic trunk prefix
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
    """Normalise phone numbers, then drop exact duplicate rows."""
    cleaned = leads.copy()

    cleaned["Name"] = cleaned["Name"].astype(str).str.strip()

    cleaned["Original Phone"] = cleaned["Phone"]
    cleaned["Phone"] = cleaned["Phone"].apply(normalize_phone)

    invalid_rows = cleaned[cleaned["Phone"].isna()].copy()
    valid_rows = cleaned[cleaned["Phone"].notna()].copy()

    # Exact duplicate rows = identical in EVERY output column (Name AND Phone).
    deduplicated = valid_rows.drop_duplicates(
        subset=["Name", "Phone"], keep="first"
    )

    return deduplicated, invalid_rows


def main():
    if not INPUT_FILE.exists():
        raise SystemExit(f"Input file not found: {INPUT_FILE.resolve()}")

    # dtype=str stops pandas turning "9876543210" into a number and losing
    # the leading zero in values like "098-765-99887".
    leads = pd.read_csv(INPUT_FILE, dtype=str)

    cleaned, invalid = clean_leads(leads)
    print_report(leads, cleaned, invalid)

    cleaned[["Name", "Phone"]].to_csv(OUTPUT_FILE, index=False)


if __name__ == "__main__":
    main()
```

*(The reporting function `print_report` is included in the submitted `clean_leads.py`; it prints the before/after table, the summary counts and a self-check that every output row matches the required format.)*

### 3.4 Cleaned Output

`cleaned_leads.csv` — 6 input rows, 5 output rows:

```
Name,Phone
Ravi Kumar,+919876543210
Priya Shah,+919876512345
Amit Verma,+919876599887
Sneha Reddy,+919876500000
Karan Mehta,+919876511111
```

### 3.5 Validation

Actual console output:

```
BEFORE -> AFTER (normalisation)
--------------------------------------------------------------
  Ravi Kumar     9876543210         -> +919876543210
  Priya Shah     91 98765 12345     -> +919876512345
  Amit Verma     098-765-99887      -> +919876599887
  Sneha Reddy    +919876500000      -> +919876500000
  Karan Mehta    +91-9876511111     -> +919876511111

SUMMARY
--------------------------------------------------------------
  Rows read from input          : 6
  Invalid numbers flagged       : 0
  Exact duplicate rows removed  : 1
  Rows written to output        : 5

  All numbers match +91XXXXXXXXXX : True
  Duplicate rows remaining        : 0
```

The script validates its own output — it re-checks every written row against `^\+91\d{10}$` and confirms no duplicates remain, so the result is asserted by the program rather than by eye.

**Edge cases tested — 17 cases, all passing:**

| Input | Result | Case covered |
|-------|--------|--------------|
| `9876543210` | `+919876543210` | plain 10-digit |
| `91 98765 12345` | `+919876512345` | spaces with country code |
| `098-765-99887` | `+919876599887` | leading zero with hyphens |
| `+919876500000` | unchanged | already correct |
| `+91-9876511111` | `+919876511111` | plus and hyphen |
| `  9876543210  ` | `+919876543210` | surrounding whitespace |
| `(+91) 98765 43210` | `+919876543210` | brackets |
| `+91.98765.43210` | `+919876543210` | dots |
| `0919876543210` | `+919876543210` | trunk zero **and** country code |
| **`9198765432`** | **`+919198765432`** | **10-digit starting "91" — correctly not stripped** |
| `919876543210` | `+919876543210` | 12-digit with country code |
| `98765` / `98765432101234` | flagged | too short / too long |
| `1234567890` / `5876543210` | flagged | invalid first digit |
| `abcdefghij` / *(blank)* | flagged | no digits / empty |

The tenth case is the one that matters. `9198765432` is a valid ten-digit number that happens to begin with "91". A prefix-only rule truncates it to eight digits and then silently drops it as invalid. Checking length before prefix avoids this.

A separate end-to-end run against deliberately broken input confirmed invalid and blank numbers are reported under "needs manual review" and excluded from the output rather than silently deleted — for a small studio, a quietly dropped lead is lost revenue nobody notices.

---

## 4. n8n Automation Logic

Theoretical, as the assignment specifies. No n8n account was used and no execution is claimed.

### 4.1 Trigger

A new response submitted to the Sunrise Interiors inquiry Google Form, which appears as a new row in the linked Google Sheet. n8n watches that sheet for new rows.

The sheet is used rather than a direct form webhook because it gives a durable, human-readable record that survives an automation failure, and a place to write status back to — which is what makes the workflow safely re-runnable.

**Input captured:** timestamp, client name, phone, email, project type, budget, location, requirements.

The budget field must be numeric or a dropdown of ranges. If a client types "around 5 lakhs", a numeric comparison cannot be trusted. Fixing that at the form is cheaper than parsing it downstream.

### 4.2 Workflow

```
Google Form submission
        |
        v
[1] TRIGGER - new response row appears
        |
        v
[2] Validate & clean lead data
        |
        v
[3] CREATE ClickUp lead card ---- fails? ---> retry x3 -> error branch
        |
        v
[4] Write ClickUp task ID back to the sheet   <- idempotency marker
        |
        v
[5] Send client confirmation (email / WhatsApp)
        |
        v
[6] CONDITION - is Budget > Rs 5,00,000?
        |
        +-- YES --> [7] Notify design team --> END
        |
        +-- NO  --> END (lead recorded, no internal notification)
```

1. New row detected.
2. Validate required fields; convert budget to an integer; normalise the phone to `+91XXXXXXXXXX` using the same rule as Task 2, so the CRM holds one phone format everywhere.
3. Create the lead card in the **Projects** list with status **Lead**, mapping Client, Project Budget, Project Type and Location.
4. Write the returned ClickUp task ID back into the sheet row.
5. Send the client confirmation.
6. Evaluate the budget condition.
7. On the YES branch only, notify the design team with the lead details and a direct link to the card.

### 4.3 ₹5 Lakh Conditional Logic

**The condition sits at step 6 — after the ClickUp card is created and after the client confirmation is sent.** It gates **only** the internal team notification.

```
IF Budget > 500000  → notify design team
ELSE                → end
```

**Why that placement:**

- **Every lead is recorded, regardless of size.** If the check sat at the top, a ₹3 lakh inquiry would never reach ClickUp and the studio would lose leads it never knew existed. A small kitchen job today is a full-home referral next year.
- **Every client gets a reply, regardless of size.** Withholding a confirmation from a smaller inquiry is a reputational cost for no gain.
- **Only the interruption is conditional.** The rule protects the designers' attention; it is not a filter on the business.

**Strictly greater than**, because the brief says *above* ₹5 lakh. A budget of exactly ₹5,00,000 therefore does not trigger a notification. That is a one-character decision (`>` vs `>=`) with real business consequence — implemented as specified, and flagged as something to confirm with the owner rather than assume.

### 4.4 Failure Handling

**Scenario: the ClickUp API call fails** — outage, expired token, or rate limiting during a burst of submissions.

Without handling, the client receives a warm "we've received your inquiry" email while no card exists in ClickUp. Nobody follows up. The studio has made a promise it has no record of — precisely the failure the system exists to eliminate.

**Four layers:**

1. **Order the risky step first.** ClickUp creation runs before the client email, so a failure leaves the client uncontacted and the whole run safely retryable.
2. **Retry with exponential backoff** — three attempts. Most API failures are transient.
3. **Error branch on final failure** — log the lead to a "Failed Leads" sheet and alert the owner: *"Lead capture failed for [name] ([phone]) — please add manually."* The lead is escalated, never lost.
4. **Idempotency via the written-back task ID.** Before creating a card, the workflow checks whether the row already carries one. If it does, creation is skipped — so a retry cannot create the lead twice or email the client twice.

**Duplicate lead prevention:** before creating a card, check whether an open Lead already exists with the same phone or email. Clients often submit twice. If one exists, comment on the existing card instead of creating a second — the same one-record-per-real-world-thing principle used for vendor invoices.

---

## 5. Conclusion

Sunrise Interiors' three symptoms — missed deadlines, duplicate vendor payments, no project visibility — share one cause: no single searchable source of truth. The system addresses each at its root. Project stages and health make delays visible before they become client conversations. One record per invoice, with an approval gate and a payment reference, makes a second payment obvious rather than possible. A view built on three colour-coded counts answers "what needs my attention?" without a meeting.

The design was kept deliberately small: two Spaces, three Lists, no Folders, one automation, and only fields that change a decision. Where the free plan imposed a limit, I moved work onto native functionality rather than request a paid tier — a constraint that improved the design, since anything the platform already provides should never have been a custom field.

For a six-person studio moving off WhatsApp and Excel, a system they will actually maintain matters more than one that demonstrates every available feature.

---

**Submitted by:** Karthik Jonnalagadda

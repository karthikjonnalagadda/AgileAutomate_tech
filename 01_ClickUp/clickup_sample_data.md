# ClickUp Sample Data — Sunrise Interiors

**Status: PREPARED** (not yet entered into ClickUp)

All data is fictional. No real personal information is used.

Dates are anchored to **today = 19 August 2026**. If you build this on a later date, shift the overdue items so they remain in the past — the demo depends on some items genuinely being overdue.

---

## 1. Team members

| Name | Role | Purpose in the system |
|------|------|----------------------|
| *(your account)* | Owner / Studio Head | Approves payments, reads the Owner Cockpit |
| Meera Iyer | Senior Designer / Project Manager | Default Project Manager; reviewer in the automation |
| Arjun Rao | Designer — drawings & 3D | Designer 2 |
| Divya Nair | Designer — materials & procurement | Designer 3 |

Three design team members, exactly as the assignment requires, plus the owner.

---

## 2. Projects list — 6 tasks

Projects 1–4 are the assignment-specified set. Projects 5 and 6 are **recommended additions**: the assignment requires the system to cover "lead to handover", and without a task actually sitting in `Lead` and one in `Handover`, that claim is asserted rather than demonstrated. They cost two minutes to add.

| # | Task name | Status | Client | Project Type | Project Budget | Project Health | Project Manager | Start Date | Expected Handover | Client Payment Status | Location |
|---|-----------|--------|--------|--------------|----------------|----------------|-----------------|------------|-------------------|----------------------|----------|
| 1 | Nair Residence – 3BHK | Design | Mr. & Mrs. Nair | Residential – Full Home | 1800000 | 🟢 On Track | Meera Iyer | 12 Aug 2026 | 30 Nov 2026 | Advance Received | Whitefield |
| 2 | Sharma Villa | Execution | Mr. Rajeev Sharma | Residential – Full Home | 4200000 | 🟡 At Risk | Meera Iyer | 05 May 2026 | 10 Sep 2026 | Milestone 2 Due | Sarjapur Road |
| 3 | Kapoor Kitchen Renovation | Procurement | Ms. Anjali Kapoor | Residential – Modular Kitchen | 650000 | 🔴 Delayed | Divya Nair | 20 Jun 2026 | 14 Aug 2026 | Milestone 2 Due | Indiranagar |
| 4 | Rao Office Fitout | Client Approval | Rao & Associates LLP | Commercial – Office | 3500000 | 🟢 On Track | Meera Iyer | 01 Jul 2026 | 15 Sep 2026 | Advance Received | Koramangala |
| 5 | Iyer Apartment – 2BHK | Lead | Ms. Lakshmi Iyer | Residential – Full Home | 900000 | 🟢 On Track | Meera Iyer | *(leave blank)* | *(leave blank)* | Advance Pending | HSR Layout |
| 6 | Menon Duplex – Handover | Handover | Mr. Suresh Menon | Residential – Full Home | 2600000 | 🟢 On Track | Meera Iyer | 10 Jan 2026 | 05 Aug 2026 | Fully Paid | Jayanagar |

**What this data deliberately demonstrates:**
- One On Track, one At Risk, one Delayed → the Owner Cockpit shows 4 / 1 / 1, not all-green
- Budgets from ₹6.5L to ₹42L → priority differences are visible
- Six different lifecycle stages including `Lead` and `Handover` → proves lead-to-handover coverage
- Project 3 has an Expected Handover of 14 Aug 2026, already in the past → its 🔴 Delayed health is justified by the data, not arbitrary
- Project 5 has no dates because a lead has not been scoped yet — realistic, and shows the system tolerates incomplete early-stage records

**Project Type dropdown options to create:**
Residential – Full Home / Residential – Modular Kitchen / Residential – Single Room / Commercial – Office / Commercial – Retail

**Location dropdown options to create:**
Whitefield / Indiranagar / Koramangala / HSR Layout / Sarjapur Road / Jayanagar

---

## 3. Design Tasks list — 11 tasks

| # | Task name | Assignee | Project | Work Type | Due Date | Status |
|---|-----------|----------|---------|-----------|----------|--------|
| 1 | Prepare floor plan – Nair Residence | Arjun Rao | Nair Residence – 3BHK | Floor Plan | 22 Aug 2026 | In Progress |
| 2 | 3D render – living & dining | Arjun Rao | Nair Residence – 3BHK | 3D / Render | 28 Aug 2026 | To Do |
| 3 | Client design approval presentation | Meera Iyer | Nair Residence – 3BHK | Client Presentation | 02 Sep 2026 | To Do |
| 4 | Furniture selection – master bedroom | Divya Nair | Sharma Villa | Furniture Selection | 15 Aug 2026 | In Progress |
| 5 | Lighting design – common areas | Arjun Rao | Sharma Villa | Lighting Design | 25 Aug 2026 | In Progress |
| 6 | Site inspection – carpentry progress | Meera Iyer | Sharma Villa | Site Inspection | 21 Aug 2026 | To Do |
| 7 | Material & finish selection – kitchen | Divya Nair | Kapoor Kitchen Renovation | Material Selection | 12 Aug 2026 | Blocked |
| 8 | Raise PO for modular units | Divya Nair | Kapoor Kitchen Renovation | Material Selection | 18 Aug 2026 | In Progress |
| 9 | Furniture layout – workstations | Arjun Rao | Rao Office Fitout | Furniture Selection | 29 Aug 2026 | To Do |
| 10 | Client presentation – office concept | Meera Iyer | Rao Office Fitout | Client Presentation | 26 Aug 2026 | In Progress |
| 11 | Snagging list & final handover | Meera Iyer | Menon Duplex – Handover | Snagging & Handover | 04 Aug 2026 | Complete |

**Workload distribution:** Arjun Rao 4, Meera Iyer 4, Divya Nair 3 — realistic and roughly even, which is what the By Designer view is there to show.

**Overdue tasks by design:** #4 (15 Aug), #7 (12 Aug), #8 (18 Aug). Three overdue items means the Overdue view and the 🔥 Overdue Tasks widget return real rows instead of an empty state. An empty view proves nothing to a reviewer.

**Task #7 is `Blocked`** — it demonstrates the Blocked status doing its job, and it explains why project 3 is 🔴 Delayed. The data tells a coherent story: material selection is blocked, so procurement stalled, so the handover date slipped.

> **IMPORTANT — Task #5 is the automation test subject.**
> Create it as **In Progress, assigned to Arjun Rao**. Do not set it to Ready for Review while entering data. In step 2Q you will change its status to Ready for Review *after* the automation exists, so the automation actually fires and you can capture before/after evidence.

---

## 4. Vendor Payments list — 7 tasks

Task naming convention: `INVOICE-NUMBER · Vendor · ₹Amount`

| # | Task name | Status | Vendor Name | Invoice / PO Number | Related Project | Amount (₹) | Payment Due Date | Paid On | Payment Reference / UTR |
|---|-----------|--------|-------------|---------------------|-----------------|-----------|------------------|---------|------------------------|
| 1 | INV-2314 · Sri Balaji Plywood · ₹1,45,000 | Approved for Payment | Sri Balaji Plywood | INV-2314 | Nair Residence – 3BHK | 145000 | 28 Aug 2026 | *(blank)* | *(blank)* |
| 2 | INV-2287 · Sri Balaji Plywood · ₹98,000 | Paid | Sri Balaji Plywood | INV-2287 | Sharma Villa | 98000 | 05 Aug 2026 | 04 Aug 2026 | UTR8842019X |
| 3 | INV-4471 · Kanakadurga Modular · ₹3,20,000 | Invoice Received | Kanakadurga Modular Interiors | INV-4471 | Kapoor Kitchen Renovation | 320000 | 14 Aug 2026 | *(blank)* | *(blank)* |
| 4 | PO-1102 · Deccan Lighting Works · ₹62,500 | Invoice Received | Deccan Lighting Works | PO-1102 | Sharma Villa | 62500 | 22 Aug 2026 | *(blank)* | *(blank)* |
| 5 | INV-9033 · Vibgyor Paints · ₹41,200 | PO Raised | Vibgyor Paints & Finishes | INV-9033 | Rao Office Fitout | 41200 | 30 Aug 2026 | *(blank)* | *(blank)* |
| 6 | INV-5567 · Sagar Marble & Granite · ₹2,10,000 | On Hold / Disputed | Sagar Marble & Granite | INV-5567 | Nair Residence – 3BHK | 210000 | 11 Aug 2026 | *(blank)* | *(blank)* |
| 7 | INV-7781 · Prakash Electricals · ₹78,400 | Approved for Payment | Prakash Electricals | INV-7781 | Rao Office Fitout | 78400 | 26 Aug 2026 | *(blank)* | *(blank)* |

**Vendor Name dropdown options to create:**
Sri Balaji Plywood / Kanakadurga Modular Interiors / Deccan Lighting Works / Vibgyor Paints & Finishes / Sagar Marble & Granite / Prakash Electricals

**Coverage of the four required payment states:**
- **Paid** → #2
- **Pending** (not yet approved) → #3, #5
- **Upcoming** (approved, due soon) → #1, #7
- **Overdue** → #3 (due 14 Aug), #6 (due 11 Aug)

**Total outstanding (everything not Paid): ₹8,57,100**
`145000 + 320000 + 62500 + 41200 + 210000 + 78400 = 857100`
Check this against the 💸 Total Outstanding widget once built — if it does not read ₹8,57,100, a filter is wrong.

**Payments Due view should return exactly 4 rows** (status ≠ Paid, due on or before 26 Aug 2026): #3, #4, #6, #7. Items #1 (28 Aug) and #5 (30 Aug) fall outside the 7-day window. This is a precise, checkable result — use it to verify the filter rather than eyeballing it.

### The duplicate-payment demonstration

**Rows #1 and #2 are the point.** Both are Sri Balaji Plywood:

- **INV-2287** — ₹98,000 — **Paid** on 04 Aug 2026, UTR8842019X
- **INV-2314** — ₹1,45,000 — **still unpaid**

Under the studio's old method — a WhatsApp message saying "paid Sri Balaji" and a vendor-name row in Excel — the vendor reads as settled and INV-2314 either gets missed or gets paid a second time when the vendor follows up.

Because each **invoice** is its own task with its own status, due date and UTR, the two are impossible to confuse. When Sri Balaji calls asking for payment, the owner searches `INV-2314`, sees one task, sees it is not Paid and has no UTR, and pays once.

When explaining this in the interview, be precise: **ClickUp does not enforce uniqueness on the Invoice / PO Number field.** This is a process control that works because the data is structured one-record-per-payable and there is a single searchable place to check. Claiming it is a database constraint would be wrong and a sharp interviewer will test it.

# ClickUp Architecture — Sunrise Interiors

**Status: DESIGNED** (not yet built in ClickUp)

## 1. Hierarchy

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

2 Spaces, 3 Lists, **no Folders**. That is the entire hierarchy.

### Why two Spaces
In ClickUp, statuses are inherited from the Space. A project lifecycle (`Lead → Handover`) and a payment lifecycle (`PO Raised → Paid`) are two different state machines. Separating them lets each have an honest status set instead of one bloated list where half the statuses are meaningless.

Secondary benefit: the owner can later share only the Vendors space with an accountant without exposing client design work.

### Why no Folders
Folders exist to group many Lists. We have three. Adding Folders would be hierarchy for its own sake.

### Why a project is a Task, not a List
The obvious alternative is one List per client project. Rejected because Lists cannot hold custom fields, cannot carry a status, and cannot be counted by a dashboard widget. Making a project a **task** puts Budget, Health, Expected Handover and Project Manager on it, so the owner's view can filter and count projects in one query. This is what makes the 10-second health check possible.

### Why Design Tasks is a separate List
Design work items need `To Do → In Progress → Ready for Review → Complete`. Project shells need `Lead → … → Handover`. Same reasoning as the Spaces — different state machines. The two Lists are joined by a **Project** field on each design task.

### Why no separate Space for the design team
People are handled by assignees and views, not by structure. A "Team" space would duplicate the same tasks in two places — which is exactly the Excel-and-WhatsApp problem being solved.

## 2. Statuses

### Projects list

| # | Status | Type | Why it exists |
|---|--------|------|---------------|
| 1 | Lead | Not Started | Inquiry received, not yet won. Keeps the pipeline visible. Landing status for the n8n automation in Task 3. |
| 2 | Planning | Active | Won. Site measurement, scope, budget, timeline. Separates "we have the job" from "we're designing". |
| 3 | Design | Active | Drawings, 3D views, material palette in progress. |
| 4 | Client Approval | Active | Waiting on client sign-off. Most interior-design delays are client-side; if this is not a visible status the owner blames the team for a delay the team did not cause. |
| 5 | Procurement | Active | Materials ordered, vendors engaged. Signals that money is now going out. |
| 6 | Execution | Active | On-site work: carpentry, civil, electrical, installation. |
| 7 | Handover | Done | Snagging closed, handed to client. |
| 8 | Closed / Lost | Closed | Lead did not convert, or project archived. Dead leads leave the active pipeline without being deleted. |

**No "On Hold" status by design.** A stalled project is marked `At Risk` or `Delayed` via Project Health while remaining in its real lifecycle stage — otherwise the owner loses the information about *where* it stalled.

### Design Tasks list
`To Do → In Progress → Blocked → Ready for Review → Complete`

- **Blocked** exists because invisible blockers are the studio's core disease. A designer waiting on a measurement can say so in one click instead of a WhatsApp message that scrolls away.
- **Ready for Review** is the handoff point, and the automation trigger.

### Vendor Payments list
`PO Raised → Invoice Received → Approved for Payment → Paid`, plus `On Hold / Disputed`.

**Approved for Payment** is a deliberate single approval gate — see section 4.

## 3. Custom fields

### Projects (9 fields)

| Field | Type | Example | Why |
|-------|------|---------|-----|
| Client | Text | Mr. & Mrs. Nair | Billable party, which may differ from the project name. |
| Project Type | Dropdown | Residential – Full Home | Effort and margin differ hugely by type. |
| Project Budget | Money / Number | 1800000 | Lets the owner prioritise a delayed ₹18L project over a delayed ₹2L one. Also the field the Task 3 ₹5 lakh rule reads. |
| Project Health | Dropdown | 🟢 On Track | The single most important field — it is what makes the owner view a 10-second read. |
| Project Manager | People | Meera Iyer | One accountable name per project. |
| Start Date | Date | 12 Aug 2026 | Baseline for elapsed time. |
| Expected Handover | Date | 30 Nov 2026 | The promise made to the client; everything overdue is measured against it. |
| Client Payment Status | Dropdown | Milestone 2 Due | Cash coming *in*. |
| Location | Dropdown | Whitefield | Operationally real in Bengaluru — site visits get batched by area because cross-city travel eats half a day. |

**Project Health options:** 🟢 On Track / 🟡 At Risk / 🔴 Delayed

**Client Payment Status options:** Advance Pending / Advance Received / Milestone 2 Due / Final Due / Fully Paid

### Design Tasks (2 fields)

| Field | Type | Why |
|-------|------|-----|
| Project | Relationship → Projects (fallback: Dropdown) | Rolls each work item up to its project. Without it, tasks are orphans. |
| Work Type | Dropdown | Shows the *mix* of work per designer, not just the count. |

**Work Type options:** Floor Plan / 3D / Render / Furniture Selection / Lighting Design / Material Selection / Site Inspection / Client Presentation / Snagging & Handover

### Vendor Payments (7 fields)

| Field | Type | Example | Why |
|-------|------|---------|-----|
| Vendor Name | Dropdown | Sri Balaji Plywood | Dropdown, not free text — free text produces "Sri Balaji", "Sri Balaji Plywoods", "SB Plywood" as three vendors, which hides the fact that you already paid them. |
| Invoice / PO Number | Text | INV-2314 | The unique reference. The anti-duplicate control. |
| Related Project | Relationship → Projects (fallback: Dropdown) | Nair Residence – 3BHK | Ties spend to a project. |
| Amount (₹) | Money / Number | 145000 | Summable, so the owner sees what is owed right now. |
| Payment Due Date | Date | 28 Aug 2026 | Drives the overdue filter. |
| Paid On | Date | 04 Aug 2026 | Proof of when. Empty means not paid. |
| Payment Reference / UTR | Text | UTR8842019X | Hard proof of payment from the bank. |

**Payment status is the task Status, not a custom field.** Two places recording "paid" produces conflicts; one workflow field means one truth.

### Deliberately NOT created as custom fields
Assignee, Due Date, Priority, Comments, Attachments — ClickUp has all of these natively. Recreating them creates two sources of truth and breaks every built-in filter and dashboard widget.

## 4. Duplicate-payment prevention

This is a **business process control, not a database constraint.** ClickUp does not technically enforce uniqueness on the Invoice / PO Number field. The control works because of how the data is structured and used:

1. **One payable = one task.** There is exactly one place where "is INV-2314 paid?" is answered. Not one task per vendor — a vendor has many invoices, so a vendor-level record has no single answer to "is it paid?".
2. **Invoice / PO Number is the unique reference.** Before any payment, search that number in ClickUp. A hit already in `Paid` means stop.
3. **A single approval gate.** Only the owner moves a task to `Approved for Payment`. Nothing is paid that is not in that status, so a WhatsApp message from a vendor cannot itself cause a payment.
4. **`Paid On` + `Payment Reference / UTR` are filled when reaching `Paid`.** A task in `Paid` with a blank UTR is a visible red flag.
5. **One searchable source of truth** — the Payments Due view. The root cause of double payment is not carelessness; it is that the record of payment was in a WhatsApp thread nobody could search.

The sample data demonstrates this: **Sri Balaji Plywood appears twice** — INV-2287 (Paid) and INV-2314 (unpaid). Under vendor-level tracking, seeing "Sri Balaji Plywood — Paid" would wrongly suggest everything is settled. Because each invoice is its own task, INV-2314 is visibly still outstanding.

## 5. Design team task management

- **Assignment rule:** the project's Project Manager breaks the project into design tasks and assigns each to **one** person. Shared ownership is no ownership.
- **By Designer view** (Board, grouped by Assignee, excluding Complete) shows workload balance instantly — if Arjun has 9 open tasks and Divya has 2, that is visible without asking anyone.
- **Overdue view** (due date < today, status ≠ Complete) is the missed-deadline early-warning system.
- **Escalation:** anything Blocked or overdue surfaces in the owner view, and the project's Project Health is moved to At Risk or Delayed at the weekly review.

**Project Health is maintained manually, on purpose.** A formula could only see dates, and would happily call a project "On Track" while the client has not approved anything for three weeks. Health is a judgement call; the system's job is to make it visible, not to fake it. An auto-calculated health field is a genuine production enhancement, not a 6-hour deliverable.

## 6. Automation — "Review Handoff"

| | |
|---|---|
| Where | Design Tasks list |
| Trigger | Status changes to **Ready for Review** |
| Condition | None — intentionally conditionless so it cannot silently fail to fire |
| Action 1 | Assign to **Meera Iyer** |
| Action 2 | Comment: *"Ready for review — please check and approve or send back with changes."* |

**Business reason:** the studio's real failure mode is the handoff. A designer finishes a floor plan, posts it in a WhatsApp group, and it scrolls away — nobody owns the review and three days evaporate. This makes the handoff a system event: the moment work is declared done, the reviewer becomes the assignee and a timestamped comment exists. No human memory required, and the delay becomes attributable.

## 7. Owner view — "Owner Cockpit"

Designed around one sentence: **the owner should immediately know what is going well, what is at risk, and what needs action today.**

**Row 1 — going well / at risk** (three counts, about 2 seconds)
- 🟢 On Track · 🟡 At Risk · 🔴 Delayed — count of Projects by Project Health

**Row 2 — needs action** (about 8 seconds)
- 🔥 Overdue Tasks — Design Tasks past due, not Complete, grouped by assignee
- 💰 Vendor Payments Due — not Paid, due within 7 days or overdue, Amount visible
- 💸 Total Outstanding — sum of Amount where status ≠ Paid

Nothing that does not cause an action is included. That editing decision is the actual answer to the 10-second requirement.

**Fallback if the Free plan limits dashboard widgets:** the assignment allows "1 Dashboard **or** View". The fallback is a **Board view on Projects grouped by Project Health** (three coloured columns with counts) plus the **Payments Due** view. This satisfies the requirement literally.

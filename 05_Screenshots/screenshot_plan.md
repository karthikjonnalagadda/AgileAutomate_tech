# Screenshot Plan

**Status: PLAN ONLY — no screenshots captured yet.**

Capture these after the ClickUp build is complete and QA has passed. Save them
into this folder using the file names given. Nine screenshots — enough to prove
every requirement, few enough to keep the document readable.

Before capturing: close unrelated browser tabs, collapse the sidebar if it is
noisy, and make sure the window is wide enough that custom field columns are
readable. A screenshot nobody can read proves nothing.

---

## 1. `01_workspace_structure.png`

**Shows:** the left sidebar expanded — `Sunrise Interiors` at the top, both
Spaces, all three Lists.

**Proves:** the workspace architecture exists as designed, and that it is
deliberately small — 2 Spaces, 3 Lists, no Folders.

**Goes in:** section 2.2 Workspace Architecture

---

## 2. `02_projects_list_custom_fields.png`

**Shows:** the Projects list in **Table view**, all 6 projects, with Client,
Project Type, Project Budget, Project Health, Project Manager and Expected
Handover columns visible. The Health column should show green, amber and red.

**Proves:** client projects are tracked with relevant custom fields, and
projects sit at different lifecycle stages.

**Goes in:** section 2.3 Custom Fields

---

## 3. `03_project_lifecycle_statuses.png`

**Shows:** a task's status dropdown open, listing all 8 statuses from `Lead` to
`Closed / Lost` — **or** a Board view of Projects grouped by Status.

**Proves:** projects are handled from lead to handover. This is the single
clearest piece of evidence for that requirement.

**Goes in:** section 2.2 Project Lifecycle

---

## 4. `04_design_tasks_by_designer.png`

**Shows:** the `By Designer` Board view — three columns for Meera Iyer, Arjun
Rao and Divya Nair, with task cards and due dates visible.

**Proves:** task assignment across three design team members, and that
workload distribution is visible at a glance.

**Goes in:** section 2.5 Design Team Task Management

---

## 5. `05_vendor_payments.png`

**Shows:** the Vendor Payments list in Table view — all 7 records with Vendor
Name, Invoice / PO Number, Amount, Payment Due Date, Paid On and UTR columns.
**Both Sri Balaji Plywood rows must be visible**, one Paid with a UTR and one
unpaid with blanks.

**Proves:** vendor/procurement tracking, and the duplicate-payment control in
one image. This is the screenshot to point at when explaining that control.

**Goes in:** section 2.4 Vendor / Procurement Tracking

---

## 6. `06_automation_config.png`

**Shows:** the Review Handoff automation configuration — trigger
`Status changes to Ready for Review`, both actions, and its Active state.

**Proves:** at least one automation exists.

**Goes in:** section 2.6 Automation

---

## 7. `07_automation_before.png` and `08_automation_after.png`

**Shows:** the same design task twice — before, assigned to **Arjun Rao**, and
after the status change, assigned to **Meera Iyer** with the review comment
visible in the activity feed.

**Proves:** the automation actually fires. A configuration screenshot alone
only proves a rule was written, not that it works. This pair is the difference
between "configured" and "tested", and it is what the assignment is checking.

**Goes in:** section 2.6 Automation, directly under the config screenshot

---

## 8. `09_owner_cockpit.png`

**Shows:** the Owner Cockpit — either the dashboard with the three health
counts and the action widgets, or the Board view grouped by Project Health
showing three colour-coded columns with counts.

**Proves:** the owner can understand project health in under 10 seconds.

**Goes in:** section 2.7 Owner Dashboard / View

---

## 9. `10_payments_due.png`

**Shows:** the `Payments Due` view — 4 rows, sorted by due date, Amount column
visible, overdue items flagged.

**Proves:** the owner can identify pending and overdue vendor payments.

**Goes in:** section 2.4, alongside the vendor payments screenshot

---

## 10. `11_python_output.png`

**Shows:** the terminal after running `python clean_leads.py` — the
before/after normalisation table and the summary block.

**Proves:** the Python script runs and produces the stated result. The
assignment explicitly permits a screenshot or pasted text.

**Goes in:** section 3.5 Validation

---

## Not worth capturing

- Custom field creation dialogs — the populated table already proves the fields exist
- Every individual task card — the list views cover it
- Settings pages — the working guest link is the proof, not a screenshot of the toggle
- The empty state of any view — an empty view proves nothing

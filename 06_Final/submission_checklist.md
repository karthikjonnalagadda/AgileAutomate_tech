# Submission Checklist

Verified against live ClickUp data on 20 Aug 2026. Every ✅ below was confirmed
through the API or a captured screenshot, not assumed.

---

## TASK 1 — CLICKUP

**Structure**
- [x] Workspace `Sunrise Interiors` (team 90161754416, Free plan)
- [x] Space `Client Projects`
- [x] Space `Vendors & Payments`
- [x] Lists: Projects, Design Tasks, Vendor Payments
- [x] No Folders — hierarchy kept deliberately flat
- [x] 4 members: owner + Meera Iyer + Arjun Rao + Divya Nair

**Statuses (18/18 required)**
- [x] Projects — Lead, Planning, Design, Client Approval, Procurement, Execution, Handover, Closed / Lost
- [x] Design Tasks — To Do, In Progress, Blocked, Ready for Review, Complete
- [x] Vendor Payments — PO Raised, Invoice Received, Approved for Payment, Paid, On Hold / Disputed

**Data (24/24 records)**
- [x] 6 projects spanning 6 lifecycle stages, including one Lead and one Handover
- [x] Health spread: On Track 4 / At Risk 1 / Delayed 1
- [x] 11 design tasks — Arjun 4, Meera 4, Divya 3
- [x] 3 design tasks genuinely overdue
- [x] 1 task in Blocked
- [x] 7 vendor payment records, 1 paid with date + UTR
- [x] Sri Balaji Plywood appears twice with different invoice numbers and statuses

**Automation**
- [x] Review Handoff created on the Design Tasks list
- [x] Trigger: Status changed → Ready for Review
- [x] Action 1: Update assignees → Meera Iyer
- [x] Action 2: Add comment
- [x] **TESTED** — Arjun Rao → Meera Iyer, ClickBot comment posted, API-verified

**Views**
- [x] Owner Cockpit — board grouped by Project Health, change saved
- [x] By Designer — board grouped by assignee
- [x] Overdue — 3 tasks
- [x] Payments Due — outstanding invoices sorted by due date
- [x] All saved as workspace views, not personal views

**Sharing**
- [ ] Guest access granted to amit12@agileautomate.co and aryansh@agileautomate.co
- [ ] Verified in a logged-out incognito window
- [ ] Link pasted into section 2.9 of the document

**Evidence — 10 of 11 captured**
- [x] 01_workspace · 02_projects · 03_project_lifecycle · 04_design_tasks
- [x] 05_vendor_payments · 07_automation_before · 08_automation_after
- [x] 09_owner_cockpit · 10_payments_due · 11_overdue
- [ ] 06_automation_config — the automation builder screen

---

## TASK 2 — PYTHON — COMPLETE

- [x] `input.csv` byte-exact to the assignment PDF
- [x] `clean_leads.py` implemented
- [x] `cleaned_leads.csv` — 6 rows in, 5 out, produced by an actual run
- [x] 17 edge cases documented and passing
- [x] Output self-validated by the script
- [x] Approach explained in section 3.2

---

## TASK 3 — N8N — COMPLETE (theoretical, as required)

- [x] Trigger explained
- [x] Action sequence explained
- [x] ClickUp lead creation explained
- [x] Client confirmation explained
- [x] ₹5 lakh condition explained, using `>` not `>=`
- [x] Notification gated to the YES branch only
- [x] Failure scenario and four-layer handling explained
- [x] Text flow diagram included

---

## SUBMISSION

- [ ] `[GUEST LINK]` placeholder in section 2.9 replaced
- [ ] "BEFORE SUBMITTING" block deleted from the top of the document
- [ ] Content pasted into a Google Doc
- [ ] Screenshots inserted at their referenced sections
- [ ] Google Doc set to **comment or edit access** for anyone with the link
- [ ] Doc named `KarthikJonnalagadda_AgileAutomate_tech`
- [ ] To: `amit12@agileautomate.co`
- [ ] CC: `aryansh@agileautomate.co`
- [ ] Subject: `Technical Implementation Specialist Assignment - Karthik Jonnalagadda`
- [ ] Sent within 48 hours of receipt

---

## Known constraints — stated in the document, not hidden

| Constraint | Handling |
|---|---|
| Free plan caps custom-field usage (~60 lifetime writes, non-refundable) | Vendor data moved to native Due Date + Status + task name + description. Documented in section 2.6 as a design decision. |
| No numeric Amount field → no auto-sum | ₹8,57,100 stated as a **manually verified** figure, explicitly labelled |
| Payments Due shows all 6 outstanding, not a 7-day slice | ClickUp ignored the relative date filter; showing everything owed, oldest first, is more useful |
| Cosmetic leftovers | `__probe_delete_me` field on Projects; extra `to do`/`complete` statuses on Projects and Vendor Payments — delete before final screenshots if time permits |

Stating an adaptation is a strength. A quietly missing feature reads as an unfinished job.

---

## Post-submission housekeeping

- [ ] Revoke the ClickUp API token (Settings → Apps → API Token)
- [ ] Clear it locally: `[Environment]::SetEnvironmentVariable("CLICKUP_TOKEN", $null, "User")`

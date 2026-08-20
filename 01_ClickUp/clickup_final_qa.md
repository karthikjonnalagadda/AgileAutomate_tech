# ClickUp Final QA — Sunrise Interiors

Work through this **after** building. Tick a line only if you can demonstrate it by clicking, live, right now. Anything you cannot click to is not done.

**Status labels used throughout this project:**

| Label | Meaning |
|-------|---------|
| DESIGNED | Specified on paper. Not built. |
| IMPLEMENTED | Built in ClickUp and visible. |
| TESTED | Executed and the outcome observed. |
| VERIFIED | Outcome observed **and** captured as evidence. |

---

## A. Assignment requirements (from the official PDF)

| # | Requirement | Check | Status |
|---|-------------|-------|--------|
| 1 | Client projects handled **lead to handover** | At least one task in `Lead` and one in `Handover`; all 8 statuses exist | ☐ |
| 2 | Vendor / procurement tracking — "who's owed what, by when" | Vendor Payments list with amounts and due dates | ☐ |
| 3 | Task assignment across **3 design team members** | Meera, Arjun and Divya each own tasks | ☐ |
| 4 | Custom fields relevant to interior design | 9 project + 2 task + 7 vendor fields present | ☐ |
| 5 | **At least 1 Automation** | Review Handoff exists and is Active | ☐ |
| 6 | Automation actually fires | Tested in 2Q with before/after evidence | ☐ |
| 7 | **1 Dashboard OR View** for health in under 10 seconds | Owner Cockpit (dashboard or Board fallback) | ☐ |
| 8 | **Guest link** via Settings → Sharing | Opens in incognito while logged out | ☐ |

---

## B. Structure

| Check | Expected | ☐ |
|-------|----------|---|
| Workspace name | `Sunrise Interiors` | ☐ |
| Spaces | exactly 2 — `Client Projects`, `Vendors & Payments` | ☐ |
| Lists | exactly 3 — `Projects`, `Design Tasks`, `Vendor Payments` | ☐ |
| Folders | none | ☐ |
| Members | owner + Meera Iyer + Arjun Rao + Divya Nair | ☐ |

---

## C. Data

| Check | Expected | ☐ |
|-------|----------|---|
| Projects count | 6 | ☐ |
| Project Health spread | 4 On Track, 1 At Risk, 1 Delayed | ☐ |
| A project in `Lead` | Iyer Apartment – 2BHK | ☐ |
| A project in `Handover` | Menon Duplex – Handover | ☐ |
| Design Tasks count | 11 | ☐ |
| Assignee spread | Arjun 4, Meera 4, Divya 3 | ☐ |
| Overdue design tasks | exactly 3 (#4, #7, #8) | ☐ |
| A `Blocked` task | #7 Material & finish selection | ☐ |
| Vendor payment records | 7 | ☐ |
| Paid records | exactly 1 (INV-2287), with `Paid On` **and** UTR filled | ☐ |
| Unpaid records | `Paid On` and UTR both blank | ☐ |
| Duplicate-payment demo | Sri Balaji Plywood appears twice, different invoice numbers, different statuses | ☐ |

---

## D. Numeric verification

These are exact, checkable values. A mismatch means a filter is wrong — fix it before screenshotting.

| Metric | Expected | Actual | ☐ |
|--------|----------|--------|---|
| On Track count | 4 | | ☐ |
| At Risk count | 1 | | ☐ |
| Delayed count | 1 | | ☐ |
| Overdue Tasks | 3 | | ☐ |
| Payments Due rows | 4 (INV-4471, PO-1102, INV-5567, INV-7781) | | ☐ |
| Total Outstanding | ₹8,57,100 | | ☐ |

---

## E. Automation — evidence required

| Check | ☐ |
|-------|---|
| Automation named `Review Handoff` | ☐ |
| Scoped to the **Design Tasks** list (not the Space) | ☐ |
| Trigger is exactly `Status changes to Ready for Review` | ☐ |
| Action 1 assigns Meera Iyer | ☐ |
| Action 2 posts the review comment | ☐ |
| Status shows Active / Enabled | ☐ |
| **Screenshot: configuration screen** | ☐ |
| **Screenshot: task BEFORE — assignee Arjun Rao** | ☐ |
| **Screenshot: task AFTER — assignee Meera Iyer + comment visible** | ☐ |

> Do not describe this automation as working in the submission document until all three screenshots exist. "Configured" and "tested" are different claims, and the second one is what the assignment is checking.

---

## F. Views

| View | Location | Expected result | ☐ |
|------|----------|-----------------|---|
| Owner Cockpit | Dashboard, or Board on Projects grouped by Project Health | 3 colour-coded groups with counts | ☐ |
| By Designer | Design Tasks, Board grouped by Assignee, excludes Complete | 3 columns ~4/4/3 | ☐ |
| Overdue | Design Tasks, due < today, status ≠ Complete | 3 tasks | ☐ |
| Payments Due | Vendor Payments, status ≠ Paid, due ≤ today+7d | 4 rows | ☐ |
| All views saved **for everyone**, not as personal views | — | guests can see them | ☐ |

**The "saved for everyone" line matters.** A personal view is invisible to guests, so the reviewers open the link and find none of your work. Check this explicitly.

---

## G. Sharing

| Check | ☐ |
|-------|---|
| Guest access enabled in Settings → Sharing | ☐ |
| Link tested in a private/incognito window **while logged out** | ☐ |
| Owner Cockpit reachable from the link | ☐ |
| Projects, Design Tasks and Vendor Payments reachable | ☐ |
| Link pasted into the submission document | ☐ |

---

## H. The "is this over-engineered?" test

The assignment rewards practicality. Confirm you did **not** add:

| Check | ☐ |
|-------|---|
| No Folders | ☐ |
| No extra Spaces beyond the 2 | ☐ |
| No custom fields duplicating native ones (Assignee, Due Date, Priority) | ☐ |
| No second "Payment Status" field — status carries it | ☐ |
| No vanity dashboard charts that drive no action | ☐ |
| No automations beyond the one required | ☐ |
| Every field on screen is one you can justify in a sentence | ☐ |

---

## I. Honesty check

| Check | ☐ |
|-------|---|
| Every screenshot is of something that actually exists | ☐ |
| The automation claim matches what was observed | ☐ |
| The guest link genuinely resolves for a logged-out visitor | ☐ |
| Nothing in the document describes a feature you have not built | ☐ |
| Anything adapted for a ClickUp limitation is stated plainly in the doc | ☐ |

Stating an adaptation is a strength, not a weakness. "The free plan limits dashboard widgets, so I used a Board view grouped by Project Health — the assignment permits a Dashboard *or* a View" reads as sound judgement. A quietly missing feature reads as an unfinished job.

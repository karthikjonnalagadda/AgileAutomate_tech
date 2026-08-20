# ClickUp Implementation Guide — Sunrise Interiors

**Status: INSTRUCTIONS ONLY — nothing here has been executed.**
Every step must be performed manually in a browser.

Estimated time: **90–120 minutes**, most of it data entry.

---

## Before you start — read this once

**ClickUp changes its interface regularly.** Where a label on your screen differs from the label written here, the *intent* of the step is what matters, not the wording. Do not force a match. If you cannot find something, note what you *do* see and adapt — the architecture survives almost any UI difference.

Labels most likely to differ from this guide: "Space settings", "Statuses", "Custom Fields", "Automations", "Sharing & Permissions". Treat all of them as *approximately* named.

**Five things to verify in the first ten minutes** (Phase 2B-check below). Each has a defined fallback, so none of them breaks the design — but discovering a limit at hour four is expensive.

---

## Phase 2A — Create the workspace

1. Go to **clickup.com** → **Sign Up**. Google sign-in is fastest. No credit card is required.
   - Already have an account? Go to **app.clickup.com**, click the **workspace name in the top-left corner**, and look for **"Create a new Workspace"**. Build clean — the guest link should open onto assignment material only.
2. **Workspace name:** `Sunrise Interiors`
3. **Skip** the "invite your team" prompt (we do invites in 2A-2 deliberately).
4. **Decline** any template, sample content, or "let ClickUp set this up for you" offer. Pre-built content only has to be deleted later.
5. If offered a paid trial, choose **Free Forever**. A trial expiring mid-assessment would gate features exactly when the reviewers open your link.

**Verify:** the top-left corner reads `Sunrise Interiors`, and a left sidebar lists your Spaces.

**Note:** ClickUp usually auto-creates one Space (often named after you, or "Team Space", or "Project Management"). Do not delete it yet — you can **rename it to `Client Projects`** in 2B and save yourself a step.

### 2A-2 — Invite the three designers

1. Click your **avatar / workspace name** → look for **People**, **Manage Users**, or **Settings → People**.
2. Invite three email addresses. Use Gmail plus-aliases you control so the invites actually arrive and you keep access:
   - `youraddress+meera@gmail.com` → will display as Meera Iyer
   - `youraddress+arjun@gmail.com` → Arjun Rao
   - `youraddress+divya@gmail.com` → Divya Nair
3. Accept each invite (they land in your inbox) and set the **display name** on each account to `Meera Iyer`, `Arjun Rao`, `Divya Nair`.

**Why plus-aliases:** Gmail delivers `you+anything@gmail.com` to your own inbox, so you can complete three real signups without three real mailboxes. The reviewers see three named team members; you retain control of every account.

**Verify:** all three names appear in the workspace People list.

**If the free plan blocks invites,** tell me and we will fall back to a `Designer` dropdown field on Design Tasks. This is weaker — it loses native assignee filtering — so try invites first.

---

## Phase 2B — Create the Client Projects Space

1. In the left sidebar, click **+ Space** (or **+ New Space**, or the **+** beside "Spaces").
   - *Or*: right-click the auto-created Space → **Rename** → `Client Projects`, then skip to the verify step.
2. **Name:** `Client Projects`
3. Choose an icon and colour if offered — cosmetic only.
4. If asked which **ClickApps / features** to enable, make sure **Custom Fields** and **Automations** are on. Leave the rest off.
5. If asked to create a default List, name it `Projects` — that completes 2C in the same breath.

**Verify:** `Client Projects` appears in the sidebar.

### 2B-check — The five-minute limitation check

Do these now, before entering any data:

| # | Check | Where | If unavailable |
|---|-------|-------|----------------|
| 1 | Can a **List** use different statuses from its Space? | List menu → Statuses | Put Design Tasks in its own Space |
| 2 | Is the **Relationship** custom field type available? | Any List → + custom field → browse types | Use **Dropdown** for `Project` and `Related Project` |
| 3 | Is the **Money** field type available? | Same place | Use **Number** |
| 4 | Do **Dashboards** allow Task List + Calculation widgets? | Sidebar → Dashboards | Use the Board-view fallback (2R-alt) |
| 5 | Can invited members be **assigned** before they accept? | Any task → assignee picker | Accept the invites first |

Report anything that fails and the design adapts. None of these is fatal.

---

## Phase 2C — Create the Projects list

1. Hover over **Client Projects** in the sidebar → click **+** → **List**.
2. **Name:** `Projects`

**Verify:** `Projects` sits nested under `Client Projects`.

---

## Phase 2D — Configure Projects statuses

1. Open the `Projects` list.
2. Click the **… (ellipsis)** beside the list name → look for **Statuses** (may be under "List settings" or "Customize").
3. If asked, choose to **customise statuses for this List** rather than inherit from the Space.
4. Create these eight, in order, mapping each to the correct status *group*:

| Status | Group |
|--------|-------|
| Lead | Not Started / To Do |
| Planning | Active / In Progress |
| Design | Active |
| Client Approval | Active |
| Procurement | Active |
| Execution | Active |
| Handover | Done / Complete |
| Closed / Lost | Closed |

5. Delete any default statuses ClickUp pre-created (usually "to do", "in progress", "complete") **after** adding yours — ClickUp will not let you delete the last remaining status.

**Verify:** open the list, click any task's status dropdown, and see all eight in the right order.

**Interview point:** the *group* assignment matters, not just the name. `Handover` mapped to Done and `Closed / Lost` mapped to Closed is what lets a view filter "active projects only" without listing every status by hand.

---

## Phase 2E — Create Projects custom fields

In the `Projects` list, switch to **List** or **Table** view. Scroll right to the **+** at the end of the column headers → **Create / Add field**.

Create all nine. Exact names, exact types:

| Field name | Type | Options / notes |
|------------|------|-----------------|
| `Client` | Text | — |
| `Project Type` | Dropdown | Residential – Full Home · Residential – Modular Kitchen · Residential – Single Room · Commercial – Office · Commercial – Retail |
| `Project Budget` | Money (fallback: Number) | Set currency to INR if offered |
| `Project Health` | Dropdown | `🟢 On Track` (green) · `🟡 At Risk` (yellow/orange) · `🔴 Delayed` (red) |
| `Project Manager` | People | Single assignee if that option exists |
| `Start Date` | Date | — |
| `Expected Handover` | Date | — |
| `Client Payment Status` | Dropdown | Advance Pending · Advance Received · Milestone 2 Due · Final Due · Fully Paid |
| `Location` | Dropdown | Whitefield · Indiranagar · Koramangala · HSR Layout · Sarjapur Road · Jayanagar |

**Set the colours on `Project Health` deliberately** — green, amber, red. The whole 10-second dashboard rests on those three colours being readable at a glance. The emoji in the option name is belt-and-braces so the colour survives a greyscale print or a screenshot.

**Verify:** Table view shows nine new columns.

---

## Phase 2F — Enter the sample Projects

Use **Table view** — it behaves like a spreadsheet and is far faster than opening six task cards.

Enter all six rows from `clickup_sample_data.md` section 2. Set the task **Status** per row as well as the custom fields.

**Verify:** six tasks; Project Health shows 4 green, 1 amber, 1 red; at least one task sits in `Lead` and one in `Handover`.

**Why the Lead and Handover rows matter:** the assignment says the system must handle projects "from lead to handover". With a task actually in each, that claim is *demonstrated* rather than asserted. A reviewer clicking through will notice.

---

## Phase 2G — Create the Design Tasks list

1. Hover over **Client Projects** → **+** → **List**
2. **Name:** `Design Tasks`

**Verify:** `Client Projects` now contains two Lists.

---

## Phase 2H — Configure Design Tasks statuses

Same route as 2D — **… → Statuses**, customise for this List.

| Status | Group |
|--------|-------|
| To Do | Not Started |
| In Progress | Active |
| Blocked | Active |
| Ready for Review | Active |
| Complete | Done |

**Verify:** the two Lists in the same Space now show *different* status sets. That is the point of the customisation, and it is worth a screenshot.

**If ClickUp will not allow per-List statuses on your plan:** create a third Space named `Design Tasks` and put the list there. The business architecture is unchanged; only the container moves. Tell me if you hit this.

---

## Phase 2I — Create Design Tasks custom fields

| Field name | Type | Options / notes |
|------------|------|-----------------|
| `Project` | Relationship → `Projects` list | Fallback: Dropdown with the six project names |
| `Work Type` | Dropdown | Floor Plan · 3D / Render · Furniture Selection · Lighting Design · Material Selection · Site Inspection · Client Presentation · Snagging & Handover |

**Create nothing else here.** Assignee, Due Date and Priority are native ClickUp fields — using them instead of custom duplicates is a deliberate decision and a good interview answer.

**Verify:** two new columns only.

---

## Phase 2J — Enter the Design Tasks

Table view again. Enter all 11 rows from `clickup_sample_data.md` section 3: name, assignee, Project, Work Type, Due Date, Status.

> **Do not set task #5 ("Lighting design – common areas") to Ready for Review.** Create it as **In Progress, assigned to Arjun Rao**. It is the automation test subject in 2Q.

**Verify:**
- 11 tasks
- Assignees split roughly 4 / 4 / 3 across Arjun, Meera, Divya
- Three tasks show an overdue due-date indicator (#4, #7, #8)
- One task is `Blocked` (#7)

**Why deliberately overdue data:** an Overdue view that returns zero rows proves nothing. Seeded overdue items make the view and the dashboard widget demonstrably work.

---

## Phase 2K — Create the Vendors & Payments Space

1. Sidebar → **+ Space**
2. **Name:** `Vendors & Payments`
3. Ensure **Custom Fields** is enabled.

**Verify:** two Spaces in the sidebar.

---

## Phase 2L — Create the Vendor Payments list

Hover **Vendors & Payments** → **+** → **List** → name it `Vendor Payments`.

---

## Phase 2M — Configure Vendor Payments statuses

| Status | Group |
|--------|-------|
| PO Raised | Not Started |
| Invoice Received | Active |
| Approved for Payment | Active |
| Paid | Done |
| On Hold / Disputed | Active |

**Verify:** all five appear; `Paid` is in the Done group.

**Why `Paid` must be a Done-group status:** it lets every "outstanding" filter be written as *not Paid* rather than enumerating four other statuses — simpler filters that do not break when a status is added later.

---

## Phase 2N — Create Vendor Payment custom fields

| Field name | Type | Options / notes |
|------------|------|-----------------|
| `Vendor Name` | Dropdown | Sri Balaji Plywood · Kanakadurga Modular Interiors · Deccan Lighting Works · Vibgyor Paints & Finishes · Sagar Marble & Granite · Prakash Electricals |
| `Invoice / PO Number` | Text | — |
| `Related Project` | Relationship → `Projects` (fallback: Dropdown) | — |
| `Amount (₹)` | Money (fallback: Number) | INR |
| `Payment Due Date` | Date | — |
| `Paid On` | Date | — |
| `Payment Reference / UTR` | Text | — |

**Do not create a "Payment Status" field.** The task Status is the payment status. Two fields recording the same fact is how records disagree.

---

## Phase 2O — Enter the vendor payment records

Enter all seven rows from `clickup_sample_data.md` section 4.

**Verify:**
- Seven tasks
- Exactly one in `Paid` (INV-2287) with both `Paid On` and `Payment Reference / UTR` filled
- Every unpaid task has **blank** `Paid On` and **blank** UTR
- Two tasks show Sri Balaji Plywood with different invoice numbers and different statuses

**Why the blanks matter:** "unpaid" is proven by absence of evidence, not by a checkbox someone forgot to tick. A Paid task with no UTR is visibly wrong.

---

## Phase 2P — Create the "Review Handoff" automation

1. Open the **Design Tasks** list.
2. Click the **… (ellipsis)** near the list name → **Automations** (may sit under "Settings", or as a ⚡/robot icon in the toolbar).
3. Click **+ Add Automation** / **Create Custom Automation** — if ClickUp offers pre-built templates, choose the custom/blank option.
4. Configure:

| Part | Value |
|------|-------|
| **When** (trigger) | `Status changes` → to `Ready for Review` |
| **Condition** | none — leave empty |
| **Then** (action 1) | `Change assignee` / `Assign to` → **Meera Iyer** |
| **Then** (action 2) | `Post a comment` → `Ready for review — please check and approve or send back with changes.` |

5. Name it **`Review Handoff`** if naming is offered.
6. **Save**, and confirm it shows as **Active / Enabled**.

**Verify:** the automation appears in the list's Automations panel, scoped to `Design Tasks`, status Active.

**Common gotchas:**
- If the action is "Add assignee" rather than "Change assignee", prefer **Change/Set** so Meera *replaces* Arjun. If only "Add" exists, that is acceptable — say so honestly in the doc; the handoff still happens.
- Check the automation is scoped to the **Design Tasks list**, not the whole Space. Space scope would try to fire on Projects, which has no `Ready for Review` status.
- Some accounts have a setting like "don't run automations triggered by me". If your test does not fire, look for that first.

**⚠️ Do not record this as working yet. It is CONFIGURED, not TESTED.**

---

## Phase 2Q — Test the automation

This is the step that converts DESIGNED into VERIFIED. Do not skip it and do not describe the result before you see it.

1. Open **"Lighting design – common areas"** (Design Task #5).
2. **📸 Screenshot now** — the assignee must visibly read **Arjun Rao**. This is your "before" evidence.
3. Change its status to **Ready for Review**.
4. Wait ~5–10 seconds and refresh.
5. **Check both outcomes:**
   - Assignee is now **Meera Iyer**
   - The comment *"Ready for review — please check and approve or send back with changes."* appears in the activity/comment feed
6. **📸 Screenshot now** — the "after" evidence, showing the new assignee and the comment together if possible.
7. **📸 Screenshot the automation configuration screen** from 2P.

**If nothing happens:** check (a) the automation is Active, (b) it is scoped to the Design Tasks list, (c) the trigger status is exactly `Ready for Review`, (d) any "skip my own actions" setting. Report what you see and I will help debug — I will not assume it worked.

---

## Phase 2R — Owner Cockpit (dashboard)

**Try the dashboard first.**

1. Sidebar → **Dashboards** → **+ New Dashboard** → name it `Owner Cockpit`.
2. Add widgets. Look for **Task Count**, **Calculation**, **Task List**, or similar.

**Row 1 — three counts (Projects list):**

| Widget name | Source | Filter |
|-------------|--------|--------|
| `🟢 On Track` | Projects | Project Health is `🟢 On Track` AND Status is not `Handover`, `Closed / Lost` |
| `🟡 At Risk` | Projects | Project Health is `🟡 At Risk` AND same status exclusion |
| `🔴 Delayed` | Projects | Project Health is `🔴 Delayed` AND same status exclusion |

**Row 2 — three action lists:**

| Widget name | Source | Filter |
|-------------|--------|--------|
| `🔥 Overdue Tasks` | Design Tasks | Due Date is before today AND Status is not `Complete`; group by Assignee |
| `💰 Vendor Payments Due` | Vendor Payments | Status is not `Paid` AND Payment Due Date on or before today + 7 days; sort by due date; show Amount |
| `💸 Total Outstanding` | Vendor Payments | Status is not `Paid`; calculation = **Sum of `Amount (₹)`** |

**Verify against known numbers** — this is a real correctness check, not a glance:
- On Track = **4**, At Risk = **1**, Delayed = **1**
- Overdue Tasks = **3**
- Vendor Payments Due = **4** rows
- Total Outstanding = **₹8,57,100**

If a number is wrong, a filter is wrong. Fix it before screenshotting.

### 2R-alt — Fallback if the Free plan limits widgets

The assignment allows "1 Dashboard **or** View", so this is fully compliant — not a compromise. **Do not burn time fighting plan limits.**

1. Open the **Projects** list → **+ View** → **Board**
2. Name it `Owner Cockpit`
3. **Group by:** `Project Health`
4. Filter: Status is not `Closed / Lost`
5. Show `Expected Handover` and `Project Budget` on the cards if the option exists
6. **Save the view for everyone** (look for "Save"/"Pin" — an unsaved personal view will not appear for guests)

Result: three colour-coded columns — On Track / At Risk / Delayed — with counts in the headers. That *is* project health in under 10 seconds. Pair it with the Payments Due view from 2U.

---

## Phase 2S — "By Designer" view

1. Open **Design Tasks** → **+ View** → **Board**
2. **Name:** `By Designer`
3. **Group by:** `Assignee`
4. **Filter:** Status is not `Complete`
5. Save for everyone

**Verify:** three columns (Meera, Arjun, Divya) with roughly 4 / 4 / 3 cards.

---

## Phase 2T — "Overdue" view

1. **Design Tasks** → **+ View** → **List**
2. **Name:** `Overdue`
3. **Filter:** `Due Date` is `before` `today` **AND** `Status` is not `Complete`
4. Sort by Due Date ascending
5. Save for everyone

**Verify:** exactly **3** tasks — #4 Furniture selection, #7 Material & finish selection, #8 Raise PO for modular units.

---

## Phase 2U — "Payments Due" view

1. **Vendor Payments** → **+ View** → **Table**
2. **Name:** `Payments Due`
3. **Filter:** `Status` is not `Paid` **AND** `Payment Due Date` on or before `today + 7 days`
   - If relative dates are unavailable, use a fixed date 7 days out and note it
4. Sort by `Payment Due Date` ascending
5. Show columns: Vendor Name, Invoice / PO Number, Amount (₹), Payment Due Date, Related Project
6. If a column **Sum** is available, enable it on `Amount (₹)`
7. Save for everyone

**Verify:** exactly **4** rows — INV-4471, PO-1102, INV-5567, INV-7781.

---

## Phase 2V — Final QA and the guest link

### QA pass
Work through `clickup_final_qa.md` and tick every line honestly. Anything you cannot demonstrate by clicking is not done.

### Generate the guest link

The assignment says: *"Share the workspace with us via a guest link (Settings → Sharing)."*

1. Go to **Settings** (avatar or workspace menu) → look for **Sharing**, **Sharing & Permissions**, or **Security & Permissions**.
2. Enable public/guest sharing if it is off.
3. Then either:
   - **Preferred — invite as guests:** People / Manage Users → **Invite guest** → `amit12@agileautomate.co` and `aryansh@agileautomate.co`, with **view (read-only)** access to both Spaces, **or**
   - **Public link:** on each key view (Owner Cockpit, Projects, Payments Due), open **… → Sharing → Share publicly** and copy the link.
4. **Test the link in a private/incognito window while logged out.** A link that only works while you are signed in is the single most common way this requirement silently fails.

**Verify:** the link opens the workspace content in an incognito window with no login.

**If the free plan limits guest seats,** use public view links instead and include all of them in the doc. Say which method you used — the reviewers care that they can see it, not how.

---

## After you finish

Report back with:
1. Which steps completed cleanly
2. Any label or feature that differed, and what you did instead
3. The automation test result — **actual observed behaviour**
4. Whether you used the dashboard or the Board-view fallback
5. The guest link, confirmed working in incognito

Then the screenshot plan and the final submission document get assembled around the real evidence.

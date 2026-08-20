# Task 3 — n8n Automation Logic

**Status: DESIGNED (conceptual)** — the assignment states *"No n8n account needed — this is theoretical."* Nothing here has been built or executed in n8n, and no execution results are claimed.

---

## 4.1 Trigger

**A new response is submitted to the Sunrise Interiors inquiry Google Form**, which appears as a new row in the linked Google Sheet. n8n watches that sheet for new rows, polling every 1–5 minutes.

**Why the Sheet rather than a direct form webhook:** the sheet gives a durable, human-readable record that survives an automation failure, *and* a place to write status back to. That write-back is what makes the workflow safely re-runnable (see 4.4). An instant webhook via Apps Script is the alternative if a 1–5 minute delay is unacceptable — for a studio replying to design inquiries, it is not.

---

## 4.2 Input data captured

| Field | Type | Example |
|-------|------|---------|
| Timestamp | auto | 19 Aug 2026, 14:32 |
| Client Name | text | Ananya Nair |
| Phone | text | +91 98765 43210 |
| Email | email | ananya@example.com |
| Project Type | dropdown | Residential – Full Home |
| Budget (₹) | **number** | 1800000 |
| Location | dropdown | Whitefield |
| Requirements | long text | "3BHK, need modular kitchen…" |

**Budget must be a number field or a dropdown of ranges on the form — not free text.** If a client types "around 5 lakhs" or "₹5,00,000", a numeric comparison cannot be trusted. If free text is unavoidable, the validation step strips `₹`, commas and spaces and expands "lakh"/"L" before comparing. The cheaper fix is form-side validation — fixing it at the source rather than patching downstream.

---

## 4.3 Sequence of actions

```
Google Form submission
        ↓
[1] TRIGGER — new response row appears
        ↓
[2] Validate & clean lead data
        ↓
[3] CREATE ClickUp lead card  ──── fails? ──→ retry ×3 → error branch
        ↓
[4] Write ClickUp task ID back to the sheet   ← idempotency marker
        ↓
[5] Send client confirmation (email / WhatsApp)
        ↓
[6] CONDITION — is Budget > ₹5,00,000?
        │
        ├── YES → [7] Notify design team → END
        │
        └── NO  → END (lead recorded, no internal ping)
```

1. **Trigger** — new row detected.
2. **Validate and clean** — confirm Name, Phone and Budget are present; convert Budget to an integer; normalise the phone to `+91XXXXXXXXXX` using the same rule as Task 2, so the CRM holds one phone format everywhere. A missing required field routes to the error branch instead of creating a broken card.
3. **Create the ClickUp lead card** in the **Projects** list:
   - Name: `Ananya Nair – Residential Full Home`
   - Status: **Lead** — the first status in the approved lifecycle
   - Custom fields mapped: `Client`, `Project Budget`, `Project Type`, `Location`
   - Description: the requirements text plus the form timestamp
4. **Write the returned ClickUp task ID back into the sheet row.** That row now proves the lead was processed.
5. **Send the client confirmation** — email or WhatsApp: *"Thanks for reaching out to Sunrise Interiors. We've received your inquiry and a designer will contact you within 24 hours."*
6. **Evaluate the budget condition.**
7. **Notify the design team** — YES branch only.

---

## 4.4 The ₹5 lakh conditional — placement and logic

**The condition sits at step 6: after the ClickUp card is created and after the client confirmation is sent.** It gates **only** the internal team notification.

**Why there, specifically:**

- **Every lead gets recorded, regardless of size.** If the budget check were at the top of the flow, a ₹3 lakh inquiry would never reach ClickUp and the studio would silently lose leads it never knew existed. A small kitchen job today is a full-home referral next year.
- **Every client gets a reply, regardless of size.** Withholding a confirmation from a ₹2 lakh inquiry is a reputational cost for zero gain.
- **Only the interruption is conditional.** The ₹5 lakh rule exists to protect the designers' attention, not to filter the business. So it guards the notification and nothing else.

**Logic:**

```
IF Budget > 500000  → notify design team
ELSE                → end (no notification)
```

**Strictly greater than**, because the brief says *"above ₹5 lakh"*.

**Ambiguity worth raising:** a budget of exactly ₹5,00,000 does **not** trigger a notification under a literal reading. That is a one-character decision (`>` vs `>=`) with real business consequence, and it is the kind of thing to confirm with the owner rather than assume. Implemented as `>` per the brief, and flagged.

**YES branch** — message the design team: a WhatsApp group message or email to Meera Iyer (PM) and the owner:

> 🔥 High-value lead: Ananya Nair — ₹18,00,000 — Residential Full Home, Whitefield. ClickUp card: [link]

Including the direct card link makes the notification actionable in one tap rather than a prompt to go hunting.

**NO branch** — the workflow ends. The lead is already safely in ClickUp with status **Lead** and is picked up in the normal pipeline review.

---

## 4.5 Failure handling

**Failure scenario: the ClickUp API call fails** — service outage, expired API token, or rate limiting during a burst of submissions.

**Why this is the dangerous one:** without handling, the client receives a warm "we've received your inquiry" email while **no card exists in ClickUp**. Nobody follows up. The studio has made a promise it has no record of — precisely the failure mode the whole system exists to eliminate. Silent failure is worse than loud failure here.

**Handling, in four layers:**

1. **Order the steps so the risky one runs first.** ClickUp creation happens *before* the client email. If ClickUp fails, the client has not been contacted yet, so the whole run can be retried safely.
2. **Retry with exponential backoff** — 3 attempts, roughly 1s / 5s / 25s. Most API failures are transient and clear without a human.
3. **Error branch on final failure** — write the lead to a "Failed Leads" sheet **and** alert the owner directly: *"Lead capture failed for Ananya Nair (+919876543210) — please add manually."* The lead is never lost; it is escalated to a human.
4. **Idempotency via the step-4 write-back.** Before creating a card, the workflow checks whether the row already carries a ClickUp task ID. If it does, creation is skipped. This is what stops a retry — or a re-run — from creating the lead twice or emailing the client twice.

**Related safeguard — duplicate lead prevention:** before creating a card, look up whether an open **Lead** already exists with the same phone or email. Clients often submit the form twice. If one exists, add a comment to the existing card rather than creating a duplicate — the same "one record per real-world thing" principle used for vendor invoices in the ClickUp design.

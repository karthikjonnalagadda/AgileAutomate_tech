# Task 3 — n8n Automation Logic

**Status: DESIGNED (conceptual).** The assignment states: *"No n8n account
needed — this is theoretical."* Nothing here has been built or executed in n8n,
and no execution results are claimed.

## Files

| File | Purpose |
|------|---------|
| `automation_logic.md` | Full write-up: trigger, inputs, actions, condition, failure handling |
| `workflow_diagram.txt` | Text flow diagram (the assignment permits text) |

## The four things the assignment asks for

1. **What triggers it** — a new Google Form response landing as a row in the
   linked Google Sheet, polled by n8n.
2. **Sequence of actions** — validate → create ClickUp lead card → write task ID
   back to the sheet → send client confirmation → evaluate budget → notify team.
3. **Where the ₹5 lakh check fits** — after ClickUp creation and after the
   client confirmation. It gates only the internal team notification, so every
   lead is still recorded and every client still gets a reply.
4. **One failure and its handling** — the ClickUp API call fails. Handled by
   ordering ClickUp before the client email, retrying with backoff, routing to
   an error branch that logs and alerts, and using the written-back task ID to
   keep retries idempotent.

## Condition

```
Budget > 500000
```

Strictly greater than, because the brief says "above ₹5 lakh". Exactly
₹5,00,000 does not notify — flagged as a point to confirm with the owner
rather than silently assumed.

# Submission Email — Draft

**NOT SENT.** The Google Doc link is in place — send this manually once the doc's sharing settings are confirmed.

---

**To:** amit12@agileautomate.co
**CC:** aryansh@agileautomate.co
**Subject:** Technical Implementation Specialist Assignment - Karthik Jonnalagadda

---

Hi Amit,

Please find my submission for the Technical Implementation Specialist (Intern) assignment below.

**Submission document:** https://docs.google.com/document/d/13X4d1J55h8V-RsZwattpTGsrY-sqWSsTjsGBIqQFYeQ/edit?usp=sharing

It covers all three tasks:

**1. ClickUp** — a working workspace for Sunrise Interiors covering client projects from lead to handover, vendor payment tracking, and task assignment across three designers. It includes a "Review Handoff" automation (tested, with before/after evidence in the document) and an Owner Cockpit view built for a 10-second project health check.

I've invited you and Aryansh as guests to the workspace, so you should have direct access:
https://app.clickup.com/90161754416/

**2. Python** — a script that standardises the lead phone numbers to `+91XXXXXXXXXX` and removes exact duplicate rows. Script, cleaned output and 17 documented test cases are in section 3.

**3. n8n** — the automation logic write-up for Google Form lead intake, including where the ₹5 lakh condition sits and how a ClickUp failure is handled. Section 4.

Two notes on decisions I made and documented rather than hid:

- The raw lead data contains no exact duplicate rows until the phone numbers are normalised, so the script normalises first and then removes duplicates on the full row. Reasoning is in section 3.2.
- ClickUp's free plan caps custom-field usage for the lifetime of a workspace. Rather than request a paid plan, I moved vendor tracking onto native fields — due dates, statuses, task titles and descriptions — and kept custom fields for the five that actually drive a decision. Section 2.6 explains the trade-off, including the one thing it costs: the outstanding total is a manually verified figure rather than a calculated widget.

Happy to walk through any part of it.

Thanks for the opportunity.

Best regards,
Karthik Jonnalagadda
ai.data@invarianceai.io

---

## Pre-send checklist

- [x] Google Doc created and link pasted above
- [ ] Doc named `KarthikJonnalagadda_AgileAutomate_tech`
- [ ] Doc set to **comment or edit access** for anyone with the link
- [ ] Screenshots inserted at their marked positions
- [ ] Google Doc link opens correctly in an incognito window
- [ ] ClickUp workspace link opens for a logged-in reviewer
- [ ] Subject line matches exactly
- [ ] CC present
- [ ] Sent within 48 hours of receiving the assignment

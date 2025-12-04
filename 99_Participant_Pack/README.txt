
Participant Pack - Contents

This folder contains the resources you will send to participants after the workshop.

Include:
- Agenda (PDF)
- Presentation slides
- Exercise files (folders `02_*/03_*/04_*/`)
- Instructions for retrieving secrets (do not include `Access_Credentials.txt` in the ZIP)

Note: Replace placeholders (images, actual PDFs) before zipping and sending.

**SOX Gate - English Analysis & Guidance**

Prompt to use (English):
"Analyze this code. Generate a step-by-step explanation intended for a non-technical analyst. Explain the business logic: why are we filtering negative prices? Create a bulleted list of 'Points of Vigilance' for the audit."

Source referenced: `03_Mission_SOX/2_n8n_sox_gate_FINAL.json` (n8n workflow)

Step-by-step explanation for a non-technical analyst:
- Step 1 — Start: The automation begins when triggered; it runs the workflow that checks product data.
- Step 2 — Load Dataset: The workflow reads the anomalies dataset CSV which contains product records, prices and identifiers.
- Step 3 — Detect Anomalies: A Function node filters rows where the price is less than or equal to zero (`price <= 0`). These rows are flagged because they indicate data problems (missing prices, entry errors, or potential fraudulent listings).
- Step 4 — Create Ticket: For each flagged record, the workflow sends an HTTP request to an external ticketing system to open a remediation ticket. This creates a traceable record for follow-up by operations or data teams.
- Step 5 — Suggest Remediation (optional): An AI Agent node can propose corrective actions (for example, suggest a corrected price based on similar products or request confirmation). Any suggested change should be reviewed by a human before applying.

Business logic — why filter prices <= 0:
- Data correctness: A price of zero or negative is almost always invalid for a sold product and signals incorrect or incomplete data entry.
- Financial integrity: Incorrect prices affect revenue reporting, financial reconciliations, and controls required under SOX (Sarbanes–Oxley) for accurate financial statements.
- Customer experience & fraud prevention: Negatives or zero prices can be exploited or confuse customers; they may indicate listing manipulation or system errors.
- Operational efficiency: Early detection lets the operations team correct the data before it propagates downstream (catalog, billing, analytics).

Points of Vigilance (audit checklist):
- **Secrets & Credentials**: Ensure the ticketing `HTTP Request` uses Vault or a secure secrets manager; do not store credentials in plain text.
- **Audit Trail**: Tickets must include product identifiers, original price, timestamp, and the user or system that opened the ticket to maintain a complete audit trail.
- **Idempotency & Duplication**: Ensure the workflow avoids creating duplicate tickets for the same anomaly (use a unique key or check existing tickets).
- **False Positives**: Validate the filter and thresholds (e.g., some legitimate promotional items may temporarily be zero-priced); provide a manual review step.
- **Rate Limits & Error Handling**: The HTTP requests to create tickets should handle failures and respect rate limits; implement retries with backoff and logging.
- **Data Privacy**: Remove or mask any PII before sending to external services; ensure ticket content follows privacy policies.
- **Remediation Governance**: Any AI-suggested remediation must be verified by a human — do not apply automated price changes without authorization.
- **Logging & Monitoring**: Log each detection and ticket creation in an internal system to enable reconciliation and audits.
- **Reconciliation After Fix**: After remediation, verify the fix by re-running checks and ensuring the corrective action is reflected in reports.
- **Test Safety**: During testing, use a `LIMIT` or a sandbox ticketing endpoint to avoid spamming production systems.

Quick references for participants:
- File: `03_Mission_SOX/2_n8n_sox_gate_FINAL.json` — n8n workflow to review.
- Dataset: `03_Mission_SOX/anomalies_dataset.csv` — sample data used by the workflow.
- Tip: When importing to n8n, replace credentials with Vault references and test with a small subset of rows.

If you want, I can shorten this into a one-page handout or create a slide with the workflow diagram and these audit points.


# Roadmap

##  1. Establishing the Foundations (Sprint 0 - Planning & Setup)

### Kick-Off & Alignment:

[ ] Host a project kick-off meeting with all stakeholders (engineers, designers, product managers) to review the PRD and our overall vision.
[ X] Confirm our technical stack: Frontend (React, Vue, or Angular), Backend (Node.js/Express, Django, etc.), Database (PostgreSQL or similar), and integrations (ClickUp API, Google Sheets API).

### Project Setup:

[ X] Set up version control (Git repository) and CI/CD pipelines.
[ ] Establish environments for development, staging, and production.
[ ] Create a detailed project management board (using Jira, Trello, etc.) to track tasks and sprints.

## 2. Data Modeling & Core Infrastructure (Sprint 1)

### Database & Schema Design:

[ X] Create ER diagrams for our core entities: Budgets, Clients, Jobs, Users, PayrollLogs, PurchaseOrders, Activity Logs, and Audit Logs.
[ ] Develop migration scripts and set up the database.
[ X] Document relationships and key fields (e.g., versioning, tagging).

### Authentication & User Management:

[ ] Build the user authentication system (login, signup, password recovery) with JWT or session-based auth.
[ ] Create basic user roles—even if MVP permissions are minimal—to allow future scaling.

## 3. Building Core Budget Management Features (Sprint 2)

### Spreadsheet-like Interface:

[ ] Develop the inline-editable grid component mimicking a spreadsheet (focus on responsiveness and performance).
[ ] Implement CRUD operations for budget line items with real-time editing.
[ ] Versioning & Activity Logging:

[ ] Set up a versioning system for budgets (support multiple versions and side-by-side comparisons).
[ ] Integrate an activity log that captures what changed, who made the change, and when.

## 4. Integrations & Data Sync (Sprint 3)

### ClickUp Integration:

[ ] Develop a service to pull actuals from ClickUp’s time-tracking data.
[ ] Implement logic to push updated estimates back to ClickUp in real time (upon saving/marking the budget as current).

### Google Sheets & Import/Export:

[ ] Build the import feature to sync entire budgets from Google Drive or Excel, mapping them to our AICP template.
[ ] Develop two-way sync with Google Sheets:
[ ] Allow editing within an embedded Google Sheet interface.
[ ] Implement a manual save function with a conflict review process.
[ ] For MVP, enforce a single-user edit lock to keep it simple.

## 5. Actuals, Payments & Notification Features (Sprint 4)

### Actuals Tracking:

[ ] Support manual entry for vendor invoices and credit card transactions.
[ ] Integrate discrepancy alerts if actuals exceed estimates.

### Payments Module:

[ ] Create UI and API endpoints to track payments received and due to contractors, with status labels (pending, paid, unpaid).

### Notifications & Audit Logs:

[ ] Set up automated alerts via email/Slack for key updates (budget changes, payment updates).
[ ] Build an audit log system to capture all actions for one year.

## 6. Dashboard, Job & Client Management (Sprint 5)

### Dashboard & Reporting:

[ ] Build a simple dashboard that aggregates and displays:
[ ] Expected income
[ ] Outstanding payments
[ ] Estimated vs. actual percentages
[ ] Develop backend endpoints to support these aggregated metrics.

### Job & Client Management:

[ ] Develop CRUD interfaces for creating new jobs and clients.
[ ] Implement a tagging system for jobs (e.g., animation, shoot, rework) to support future reporting.

### XLSX Export:

[ ] Build an export feature to generate XLSX reports with header/footer details (company name, client name, project name, date).

## 7. Testing, Documentation & Deployment (Sprint 6)

### Comprehensive Testing:

[ ] Write unit tests and integration tests for all modules.
[ ] Conduct user acceptance testing (UAT) in the staging environment.
[ ] Perform security and performance audits.

### Deployment:

[ ] Prepare and deploy the MVP to production.
[ ] Set up monitoring, logging, and error tracking systems (e.g., Sentry).

### Documentation:

[ ] Document API endpoints, data models, integration details, and user guides.
[ ] Maintain an internal wiki or documentation portal.
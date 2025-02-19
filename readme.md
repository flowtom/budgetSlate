# Product Requirements Document (PRD)
## SaaS Application for AICP Budget Management

**Version:** 1.0  
**Owner:** Alaena VanderMost  
**Last Updated:** [Date]  

---

## 1. Overview  
This SaaS application is designed for line producers in the film industry to efficiently manage and track complex **AICP budgets**. It provides **real-time cost tracking, version control, integrations with industry tools like ClickUp**, and a **spreadsheet-like interface** for seamless budgeting.  

The application will allow producers to create budgets, compare estimates vs. actuals, track payments, and generate reports. Users can **customize budget layouts**, track multiple versions, and push/pull data between ClickUp for synchronization with production workflows.

---

## 2. Goals & Objectives  
- Provide an **intuitive, spreadsheet-like interface** for budget management.  
- Enable **real-time tracking** of **estimates vs. actuals**.  
- Support **multiple budget versions** with side-by-side comparisons.  
- Integrate **ClickUp** for **time-tracking actuals** and **pushing updated estimates**.  
- Allow **manual input** of **vendor invoices and credit card transactions** for actuals.  
- Track **payments received and payments due to contractors**, with statuses (**pending, paid, unpaid**).  
- Offer a **dashboard** summarizing **expected income, outstanding payments, and estimate vs. actual percentages**.  
- Provide **inline editing** with a **detailed activity log** (who changed what, when).  
- Enable **customizable AICP category templates**, including **one prebuilt template** and **layout customization**.  
- Allow **exporting budgets to XLSX format** with company and project details.  
- Support **importing and syncing entire budgets from Google Drive or Excel**, with **two-way sync**.  
- Ensure **multi-user support**, initially with **open access**, but **built for future permissions**.  
- Lock editing to **one user at a time in the MVP** to avoid conflicts.  

---

## 3. Core Features & Functionality  

### 3.1 Budget Management  
- **Spreadsheet-like interface** allowing users to interact with budgets naturally.  
- **Inline editing** for all budget fields.  
- **Activity log** capturing:  
  - What was changed  
  - Who made the change  
  - Timestamp of the change  
- **Multiple versions of budgets**, with:  
  - Ability to **compare versions side by side**.  
  - Versioning system allowing **tracking of changes before client approval**.  
  - Ability to **adjust budgets mid-project** if scope/timeline changes.  

### 3.2 Actuals Tracking  
- **Time-tracking actuals pulled from ClickUp**.  
- **Manual input for vendor invoices and credit card transactions**.  
- **Discrepancy alerts** to flag overages when actuals exceed estimates.  

### 3.3 Payments Tracking  
- Track **payments received** from clients.  
- Track **payments due to contractors**.  
- Payments marked as **pending, paid, unpaid**.  

### 3.4 Reporting & Dashboard  
- **Simple dashboard** displaying:  
  - **Expected income**  
  - **Outstanding payments**  
  - **Estimated vs. actual percentage**  
- **Search & filtering architecture** for future reporting (query by client, project type, etc.).  

### 3.5 Budget Customization & AICP Templates  
- Producers can **select the AICP categories** needed for their budget.  
- Ability to **save specific layouts as templates**.  
- **One prebuilt template** included.  
- Layout customization, allowing agencies to **organize multiple budget tabs horizontally** for easy comparison.  

### 3.6 ClickUp Integration  
- **Pull actuals from ClickUp’s time-tracking tool**.  
- **Push updated estimates back to ClickUp** when a budget is saved or marked as current (**real-time sync**).  

### 3.7 Job & Client Management  
- **New job creation** feature.  
- **New client creation** feature.  
- **Database storing jobs, clients, budgets, and budget details**.  
- **Tagging system** for categorizing jobs (e.g., animation, shoot, rework).  

### 3.8 Importing & Data Sync  
- **Import and sync entire budgets from Google Drive or Excel**.  
- **Two-way sync with Google Sheets**, ensuring updates reflect in both the SaaS app and Google Sheets.  
- **Manual save function** to prevent unintended changes.  
- **Conflict review process** before applying changes.  
- **Lock editing to one user at a time** in MVP.  

### 3.9 Exporting & Data Handling  
- **XLSX export** including:  
  - Company name  
  - Client name  
  - Project name  
  - Date (in header/footer)  
- **PDF export planned for future iterations**.  

### 3.10 User Management & Permissions  
- **Multiple user accounts supported**.  
- **Open access initially**, but **architected for future permissions and role-based access**.  

### 3.11 Notifications & Audit Logs  
- **Automated alerts via email or Slack** for important budget updates.  
- **Audit log for all actions**, stored for **one year**.  

---

## 4. Technical Requirements  
### 4.1 Platform & Architecture  
- **Web-based application** (no mobile version for now).  
- **Scalable database** to track budgets, clients, jobs, and actuals.  
- **Cloud-hosted architecture** for multi-user access.  

### 4.2 Integrations  
- **ClickUp API** for pulling time-tracking actuals and pushing updated estimates.  
- **Google Sheets API** for two-way sync.  

### 4.3 Data & Security  
- **Structured database** enabling easy querying for reporting features.  
- **Change tracking system** ensuring auditability of budget updates.  
- **Secure authentication system** for multi-user access.  

---

## 5. Future Considerations  
- **Annotations/comments** on budget line items (low priority).  
- **Advanced reporting features** (filtering jobs by client, tags, overages).  
- **Audit trail for payments** (who marked them as paid/unpaid).  
- **Bulk data import/export beyond XLSX**.  
- **Approval workflows** for budget changes (if needed).  

---

## 6. MVP Scope Summary  
✅ **Spreadsheet-like UI with inline editing**  
✅ **Versioning & side-by-side comparison**  
✅ **ClickUp integration for actuals & estimates**  
✅ **Manual input for vendor invoices & credit card transactions**  
✅ **Budget customization with AICP category selection & template saving**  
✅ **New job & client creation with tagging system**  
✅ **Dashboard for income, outstanding payments, and estimate vs. actuals**  
✅ **Payments tracking (pending, paid, unpaid)**  
✅ **XLSX export with project details**  
✅ **Multi-user support (initially open access, future permissions possible)**  
✅ **Import/sync budgets from Google Drive & Excel**  
✅ **Two-way sync with Google Sheets**  
✅ **Automated alerts via Slack/email**  
✅ **Audit log stored for one year**  
✅ **Lock editing to one user at a time in MVP**  

---

## 7. Next Steps  
1. **Confirm MVP scope** – Does anything need to be added or adjusted?  
2. **Define the tech stack** – Which database, framework, and hosting solution should we use?  
3. **Outline development roadmap** – Prioritize features and set milestones.  

"""
# AICP Budget Management Database Schema

This document describes the AICP Budget Management System’s database schema, including entity definitions, relationships, and business rules. It reflects the latest decisions:

1. **No `BudgetPage`** (pages are handled at the UI level or via a simple field in `BudgetClass`).
2. **Concurrent Budget Versions** (multiple versions can exist in parallel).
3. **Read-only Lock** happens when the project status moves to “wrap,” rather than automatically for older versions.

---

## Table of Contents
1. [Overview](#overview)
2. [Core Entities](#core-entities)
   - [User](#user)
   - [Client](#client)
   - [Job](#job)
   - [Budget](#budget)
   - [BudgetVersion](#budgetversion)
   - [BudgetClass](#budgetclass)
   - [BudgetLineItem](#budgetlineitem)
3. [Entity Relationships](#entity-relationships)
4. [Business Rules](#business-rules)
5. [Notes & Future Considerations](#notes--future-considerations)

---

## Overview

The **AICP Budget Management System** helps line producers manage and track production budgets following AICP standards. Each budget can have multiple versions, allowing producers to propose different scenarios (e.g., “Option A,” “Option B”) simultaneously. Once a project moves to “wrap,” all versions become read-only, preserving final numbers.

---

## Core Entities

### User
Represents system users (e.g., administrators, line producers).

| Field         | Type         | Constraints/Notes                                 |
|---------------|-------------|---------------------------------------------------|
| **id (PK)**   | UUID         | Unique identifier                                |
| **email**     | String       | Must be unique, valid format                     |
| **name**      | String       | User’s full name                                 |
| **role**      | String       | One of: `ADMIN`, `LINE_PRODUCER`                |
| **created_at**| Timestamp    | Stored in UTC                                    |
| **updated_at**| Timestamp    | Stored in UTC (nullable)                         |

- **Constraints**:  
  - `email` must be unique.  
  - `role` must be one of the predefined values.  

---

### Client
Represents a production client.

| Field         | Type         | Constraints/Notes                     |
|---------------|-------------|----------------------------------------|
| **id (PK)**   | UUID         | Unique identifier                     |
| **name**      | String       | Must be unique                        |
| **contact_name**| String     | Primary contact person                |
| **contact_email**| String    | Valid email format                    |
| **created_at**| Timestamp    | Stored in UTC                         |
| **updated_at**| Timestamp    | Stored in UTC (nullable)             |

- **Constraints**:  
  - `name` must be unique.  
  - `contact_email` must be a valid email.

---

### Job
Represents a production project.

| Field               | Type       | Constraints/Notes                              |
|---------------------|-----------|-----------------------------------------------|
| **id (PK)**         | UUID       | Unique identifier                             |
| **client_id (FK)**  | UUID       | References **Client**                        |
| **project_title**   | String     | Name of the project                          |
| **production_company**| String   | Production company name                      |
| **contact_phone**   | String     | Contact number                               |
| **core_team**       | JSONB      | Flexible storage for team members            |
| **director**        | String     | Optional                                     |
| **producer**        | String     | Optional                                     |
| **writer**          | String     | Optional                                     |
| **pre_prod_days**   | Integer    | Various production day counts               |
| **build_days**      | Integer    |                                             |
| **pre_light_days**  | Integer    |                                             |
| **studio_days**     | Integer    |                                             |
| **location_days**   | Integer    |                                             |
| **wrap_days**       | Integer    |                                             |
| **status**          | String     | Current job status (Draft, Shooting, Wrap…)  |
| **created_at**      | Timestamp  | Stored in UTC                                |
| **updated_at**      | Timestamp  | Stored in UTC (nullable)                     |

- **Relationships**:  
  - Belongs to a **Client**.  
  - Has many **Budgets** (one job can have multiple budgets).  

---

### Budget
Container for one or more budget versions.

| Field           | Type       | Constraints/Notes              |
|-----------------|-----------|---------------------------------|
| **id (PK)**     | UUID       | Unique identifier              |
| **job_id (FK)** | UUID       | References **Job**             |
| **name**        | String     | Budget name                    |
| **status**      | String     | Current status (Draft, etc.)   |
| **created_at**  | Timestamp  | Stored in UTC                  |
| **updated_at**  | Timestamp  | Stored in UTC (nullable)       |

- **Relationships**:  
  - Belongs to a **Job**.  
  - Has many **BudgetVersions**.  

---

### BudgetVersion
Represents a specific version of a budget (e.g., “Option A,” “Option B,” etc.).

| Field             | Type          | Constraints/Notes                                  |
|-------------------|--------------|----------------------------------------------------|
| **id (PK)**       | UUID          | Unique identifier                                 |
| **budget_id (FK)**| UUID          | References **Budget**                            |
| **version_number**| Integer       | Numeric label (optional to enforce uniqueness)    |
| **version_name**  | String        | Human-readable name (e.g., “Option A”)            |
| **status**        | String        | e.g., Draft, Client Review, Approved…             |
| **total_estimate**| Decimal(10,2) | Summed from **BudgetLineItem** entries            |
| **total_actual**  | Decimal(10,2) | Summed from **BudgetLineItem** entries            |
| **created_at**    | Timestamp     | Stored in UTC                                     |
| **updated_at**    | Timestamp     | Stored in UTC (nullable)                          |

- **Concurrent Versions**: Multiple `BudgetVersion` rows can exist under the same **Budget** at the same time.  
- **Locking**: When the **Job** status moves to “wrap,” you can lock these versions, making them read-only.

---

### BudgetClass
Defines which classes (A–P) a given budget version uses.

| Field                    | Type            | Constraints/Notes                              |
|--------------------------|-----------------|-----------------------------------------------|
| **id (PK)**             | UUID            | Unique identifier                             |
| **budget_version_id (FK)**| UUID           | References **BudgetVersion**                  |
| **class_code**, `class_name` | String     | e.g., “A”, “Preproduction Crew”               |
| **estimate_fields**      | String[]        | Which estimate columns apply                  |
| **actual_fields**        | String[]        | Which actual columns apply                    |
| **calculation_type**     | String          | e.g., “QTY_RATE”, “HOURS_RATE”                |
| **quantity_label**       | String          | e.g., “HOURS” or “DAYS”                       |
| **has_client_total**     | Boolean         | For classes like K, L, O, P                   |
| **allows_percentage_rates**| Boolean       | For classes like M2                           |
| **pw_percentage**        | Decimal(5,2)    | Default P&W rate, if applicable              |
| **display_order**        | Integer         | Order in the version                          |
| **total_estimate**       | Decimal(10,2)   | Summed from **BudgetLineItem** entries        |
| **total_actual**         | Decimal(10,2)   | Summed from **BudgetLineItem** entries        |
| **created_at**, `updated_at` | Timestamp  | Stored in UTC                                 |

- **One-to-Many** with **BudgetLineItem**.  
- If a class is **not used**, you simply **don’t create** a `BudgetClass` row for that version.

---

### BudgetLineItem
Individual entries within each budget class.

| Field                | Type            | Constraints/Notes                            |
|----------------------|-----------------|----------------------------------------------|
| **id (PK)**          | UUID            | Unique identifier                            |
| **budget_class_id (FK)**| UUID         | References **BudgetClass**                  |
| **line_number**      | Integer         | Display order within the class              |
| **description**      | String          | Item description                            |
| **quantity_estimate**| Decimal(5,2)    | If class uses quantity (A, F, etc.)         |
| **days_estimate**    | Decimal(5,2)    | If class uses days                          |
| **hours_estimate**   | Decimal(5,2)    | If class uses hours (K, etc.)               |
| **rate_estimate**    | Decimal(10,2)   | Monetary rate                               |
| **total_estimate**   | Decimal(10,2)   | Summed from estimate fields                 |
| **ot_rate_estimate** | Decimal(10,2)   | For classes with OT (B)                     |
| **ot_hours_estimate**| Decimal(5,2)    | Time measurement for OT                     |
| **quantity_actual**  | Decimal(5,2)    | Actual quantity if used                     |
| **days_actual**      | Decimal(5,2)    | Actual days if used                         |
| **hours_actual**     | Decimal(5,2)    | Actual hours if used                        |
| **rate_actual**      | Decimal(10,2)   | Actual monetary rate                        |
| **total_actual**     | Decimal(10,2)   | Summed from actual fields                   |
| **ot_rate_actual**   | Decimal(10,2)   | OT rate if used                             |
| **ot_hours_actual**  | Decimal(5,2)    | OT hours if used                            |
| **pw_percentage**    | Decimal(10,2)   | e.g., M2 percentage rates                   |
| **pw_amount**        | Decimal(10,2)   | If needed                                   |
| **is_subtotal**      | Boolean         | Marks this line item as a subtotal row      |
| **requires_po**      | Boolean         | If a PO is needed                           |
| **vendor_name**      | String          | Optional vendor reference                   |
| **po_number**        | String          | Optional PO reference                       |
| **notes**            | String          | Free-form notes                             |
| **created_at**, `updated_at`| Timestamp| Stored in UTC                               |

- **Key Constraint**: `line_number` must be unique within the same `BudgetClass`.  
- **Monetary Fields** typically `(10,2)`, **Time Fields** `(5,2)`.

---

## Entity Relationships

```mermaid
erDiagram

    %% Relationship Overviews
    User ||--o{ Job : manages (optional)
    Client ||--o{ Job : has
    Job ||--o{ Budget : has
    Budget ||--o{ BudgetVersion : has
    BudgetVersion ||--o{ BudgetClass : has
    BudgetClass ||--o{ BudgetLineItem : has

    %% TABLE DEFINITIONS (simplified for illustration)
    User {
        uuid id
        string email
        string name
        string role
        datetime created_at
        datetime updated_at
    }

    Client {
        uuid id
        string name
        string contact_name
        string contact_email
        datetime created_at
        datetime updated_at
    }

    Job {
        uuid id
        uuid client_id
        string project_title
        string production_company
        string contact_phone
        jsonb core_team
        string director
        string producer
        string writer
        integer pre_prod_days
        integer build_days
        integer pre_light_days
        integer studio_days
        integer location_days
        integer wrap_days
        string status
        datetime created_at
        datetime updated_at
    }

    Budget {
        uuid id
        uuid job_id
        string name
        string status
        datetime created_at
        datetime updated_at
    }

    BudgetVersion {
        uuid id
        uuid budget_id
        integer version_number
        string version_name
        string status
        decimal total_estimate
        decimal total_actual
        datetime created_at
        datetime updated_at
    }

    BudgetClass {
        uuid id
        uuid budget_version_id
        string class_code
        string class_name
        string[] estimate_fields
        string[] actual_fields
        string calculation_type
        string quantity_label
        boolean has_client_total
        boolean allows_percentage_rates
        decimal pw_percentage
        integer display_order
        decimal total_estimate
        decimal total_actual
        datetime created_at
        datetime updated_at
    }

    BudgetLineItem {
        uuid id
        uuid budget_class_id
        integer line_number
        string description
        decimal quantity_estimate
        decimal days_estimate
        decimal hours_estimate
        decimal rate_estimate
        decimal total_estimate
        decimal ot_rate_estimate
        decimal ot_hours_estimate
        decimal quantity_actual
        decimal days_actual
        decimal hours_actual
        decimal rate_actual
        decimal total_actual
        decimal ot_rate_actual
        decimal ot_hours_actual
        decimal pw_percentage
        decimal pw_amount
        boolean is_subtotal
        boolean requires_po
        string vendor_name
        string po_number
        string notes
        datetime created_at
        datetime updated_at
    }

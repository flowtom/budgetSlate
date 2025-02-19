# AICP Budget Class Patterns

## Overview
This document outlines the different patterns found in AICP budget classes A through P, documenting their structure, fields, and special characteristics.

## Class Patterns

### Pattern 1: Basic Labor (Classes A, C, D, E)
**Structure:**
- ESTIMATED: #, DAYS, RATE, TOTAL
- ACTUAL: TOTAL only

**Examples:**
- Class A: PREPRODUCTION & WRAP CREW
- Class C: PRE-PRODUCTION
- Class D: LOCATION EXPENSES
- Class E: PROPS & WARDROBE & ANIMALS

### Pattern 2: Labor with Overtime (Class B)
**Structure:**
- ESTIMATED: DAYS, RATE, OT_RATE, OT_HOURS, TOTAL
- ACTUAL: TOTAL only

**Example:**
- Class B: SHOOTING CREW

### Pattern 3: Studio/Equipment (Class F)
**Structure:**
- ESTIMATED: #, RATE, TOTAL (no DAYS)
- ACTUAL: TOTAL only

**Example:**
- Class F: STUDIO RENTAL & EXPENSES-STAGE

### Pattern 4: Art Labor (Class G)
**Structure:**
- ESTIMATED: DAYS, RATE, TOTAL
- ACTUAL: DAYS, RATE, TOTAL (full breakdown)

**Example:**
- Class G: ART DEPT LABOR

### Pattern 5: Cost Plus (Class H)
**Structure:**
- ESTIMATED: #, RATE, TOTAL
- ACTUAL: TOTAL only
**Note:** Often remains empty

### Pattern 6: Equipment with Days (Class I)
**Structure:**
- ESTIMATED: #, DAYS, RATE, TOTAL
- ACTUAL: TOTAL only
**Note:** Often only RATE is filled in

### Pattern 7: Miscellaneous (Class J)
**Structure:**
Similar to Class I:
- ESTIMATED: #, DAYS, RATE, TOTAL
- ACTUAL: TOTAL only

### Pattern 8: Creative Hours with Client Total (Classes K, L, O)
**Structure:**
- ESTIMATED: HOURS/DAYS, RATE, TOTAL
- ACTUAL: HOURS, TOTAL, Client-Total

**Variations:**
- Class K (CREATIVE FEES): Uses HOURS for both estimate and actual
- Class L (DIRECTOR FEES): Uses DAYS for estimate, HOURS for actual
- Class O (AGENCY SERVICES): Uses HOURS for both, like Class K

### Pattern 9: Talent Classes (M1, M2, N)
**Structure:**
M1 (TALENT):
- ESTIMATED: #, DAYS, RATE, TOTAL
- ACTUAL: TOTAL only

M2 (ADDITIONAL TALENT EXPENSES):
- Same structure as M1
- Supports percentage rates (e.g., 20% for agency fees)
- Supports flat rates

N (TALENT EXPENSES):
- Same structure as M1
- Typically uses flat rates

### Pattern 10: Post Production (Class P)
**Structure:**
- ESTIMATED: # / HOURS (combined), RATE, TOTAL
- ACTUAL: HOURS, TOTAL, Client-Total
**Note:** Flexible use of #/HOURS column (can be quantity or hours)

## Special Characteristics

### Client Total Field
Present in:
- Class K (CREATIVE FEES)
- Class L (DIRECTOR FEES)
- Class O (AGENCY SERVICES)
- Class P (POST EXPENSES)

### Percentage Rates
Supported in:
- Class M2 (ADDITIONAL TALENT EXPENSES)

### Time Units
- Most classes use DAYS
- Some use HOURS (K, O)
- Some use both (L - DAYS for estimate, HOURS for actual)
- Some combine both in one column (P - # / HOURS)

### Calculation Types
1. FLAT_RATE: Just rate entered
2. QTY_RATE: Quantity * Rate
3. DAYS_RATE: Days * Rate
4. QTY_DAYS_RATE: Quantity * Days * Rate
5. HOURS_RATE: Hours * Rate
6. PERCENTAGE: Rate is a percentage

## Notes
- All monetary values should support 2 decimal places
- Hours and days should support 2 decimal places for partial units
- Some classes may be typically empty (like Class H)
- Some classes primarily use only certain fields despite having more available
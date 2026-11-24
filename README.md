# Campus-festival
# Campus Festival Registration and Financial Audit System

## 1. Project Overview

The **Campus Festival Registration and Financial Audit System** is a Python-based application designed to manage participant registrations and festival financial transactions.

The system maintains participant registration records, detects duplicate registrations, calculates registration fees collected and pending, records sponsorship contributions, and tracks festival expenses.

It also calculates the final financial balance and identifies whether the festival has a surplus, deficit, or balanced budget.

## 2. Objectives

- To maintain campus festival participant records.
- To identify duplicate participant registrations.
- To calculate registration fees collected.
- To calculate pending registration fees.
- To record sponsorship contributions.
- To calculate total festival expenses.
- To determine total festival income.
- To calculate the final financial balance.
- To generate a consolidated financial audit report.

## 3. Assumptions

1. Each participant has a unique registration ID.
2. The sample registration fee is ₹500 per participant.
3. Duplicate registration IDs are detected and excluded.
4. Partial registration fee payments are allowed.
5. Amount paid cannot exceed the registration fee due.
6. Sponsorship contributions are included in total income.
7. Festival expenses are recorded separately.
8. All financial amounts are calculated in Indian Rupees.
9. Only valid registration records are included in the final audit.

## 4. Formulas Used

### Total Registration Fees Collected

Total Fees Collected = Sum of Amount Paid by Valid Participants

### Pending Registration Fees

Pending Fees = Total Fees Due − Total Fees Collected

### Total Sponsorship

Total Sponsorship = Sum of All Sponsorship Contributions

### Total Festival Income

Total Income = Registration Fees Collected + Sponsorship Contributions

### Total Festival Expenses

Total Expenses = Sum of All Festival Expenses

### Final Financial Balance

Final Balance = Total Income − Total Expenses

**Financial Status:**

- Positive balance: SURPLUS
- Negative balance: DEFICIT
- Zero balance: BALANCED

## 5. Algorithm

1. Start the program.
2. Define participant registration records.
3. Define sponsorship records.
4. Define festival expense records.
5. Create an empty list for valid registrations.
6. Read each participant registration record.
7. Check whether the registration ID already exists.
8. If duplicate, identify and reject the registration.
9. Otherwise, add the registration to the valid participant list.
10. Calculate registration fees due.
11. Calculate total registration fees collected.
12. Calculate pending registration fees.
13. Calculate total sponsorship contributions.
14. Calculate total festival expenses.
15. Calculate total festival income.
16. Calculate the final financial balance.
17. Determine whether the financial result is surplus, deficit, or balanced.
18. Display the complete financial audit report.
19. Stop the program.

## 6. Pseudocode

```text
START

DEFINE participant registrations
DEFINE sponsorship records
DEFINE expense records

CREATE empty valid registration list
CREATE empty registered ID list

FOR each participant record:

    CHECK registration ID

    IF registration ID already exists:

        DISPLAY duplicate registration
        INCREASE duplicate count

    ELSE:

        ADD registration ID
        ADD participant to valid list

CALCULATE total registration fees due

CALCULATE total fees collected

CALCULATE pending registration fees

CALCULATE total sponsorship contributions

CALCULATE total festival expenses

total income = fees collected + sponsorship

final balance = total income - expenses

IF final balance > 0:

    DISPLAY SURPLUS

ELSE IF final balance < 0:

    DISPLAY DEFICIT

ELSE:

    DISPLAY BALANCED

DISPLAY financial audit report

STOP
```

## 7. Test Cases

| Test Case | Registration ID | Fee Due | Amount Paid | Expected Result |
|---|---|---:|---:|---|
| 1 | REG101 | ₹500 | ₹500 | Paid |
| 2 | REG102 | ₹500 | ₹300 | ₹200 pending |
| 3 | REG103 | ₹500 | ₹500 | Paid |
| 4 | REG102 | ₹500 | ₹300 | Duplicate |
| 5 | REG104 | ₹500 | ₹0 | ₹500 pending |

### Additional Financial Test Cases

| Test Case | Total Income | Expenses | Expected Result |
|---|---:|---:|---|
| 1 | ₹16,300 | ₹9,500 | Surplus ₹6,800 |
| 2 | ₹8,000 | ₹10,000 | Deficit ₹2,000 |
| 3 | ₹10,000 | ₹10,000 | Balanced |

## 8. Sample Output

```text
==============================================
          FINAL FINANCIAL AUDIT
==============================================

Total Participants: 4
Duplicate Registrations: 1

Total Registration Fees Due: Rs. 2000
Total Fees Collected: Rs. 1300
Pending Registration Fees: Rs. 700

Total Sponsorship: Rs. 15000

Total Festival Income: Rs. 16300
Total Festival Expenses: Rs. 9500

Final Financial Balance: Rs. 6800

Financial Status: SURPLUS

==============================================
Festival financial audit completed successfully.
==============================================
```

## 9. Python Concepts Used

- Variables and data types
- Input and output statements
- Tuples
- Lists
- Conditional statements (if, elif, else)
- For loops
- Functions
- Function arguments and return values
- Arithmetic operators
- Logical operators
- List membership operations
- Tuple indexing

## 10. Conclusion

The Campus Festival Registration and Financial Audit System successfully manages participant registrations and festival financial records.

It identifies duplicate registrations, calculates registration fees, tracks sponsorship contributions, analyses expenses, and determines the final financial balance.

This project demonstrates the practical application of Python concepts such as tuples, lists, loops, functions, and conditional statements in solving real-world event management and financial auditing problems.

## 11. Project Structure

```text
Campus-Festival-Financial-Audit/
│
├── campus_festival_audit.py
├── README.md
│
└── screenshots/
    └── output.png
```

## 12. Execution Instructions

1. Install Python on your computer.
2. Open the project folder in Visual Studio Code.
3. Open `campus_festival_audit.py`.
4. Run the program using:

```bash
python campus_festival_audit.py
```

5. View participant registration details.
6. Check duplicate registration detection.
7. View sponsorship contributions and festival expenses.
8. Check the final financial audit report.
9. Capture the actual program output screenshot.
10. Upload the Python file, README, and screenshot to GitHub.

## 13. Author Details

- **Name:** v.v.s.s.gayathri
- **Roll Number:** N26V01A0388
- **Branch:** CSE
- **Section:** Section-5
- **Subject:** Python Programming
- **Project:** Campus festival

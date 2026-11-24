
# Campus Festival Registration and Financial Audit System

# Registration records:
# (Registration ID, Participant Name, Fee Due, Amount Paid)

registrations = [
    ("REG101", "Anu", 500, 500),
    ("REG102", "Rahul", 500, 300),
    ("REG103", "Priya", 500, 500),
    ("REG102", "Rahul", 500, 300),
    ("REG104", "Kiran", 500, 0)
]

# Sponsorship records:
# (Sponsor Name, Contribution Amount)

sponsorships = [
    ("ABC Company", 10000),
    ("XYZ Technologies", 5000)
]

# Expense records:
# (Expense Description, Amount)

expenses = [
    ("Venue Booking", 4000),
    ("Decoration", 1500),
    ("Food", 3000),
    ("Sound System", 1000)
]


# Function to identify duplicate registrations
def check_duplicate(registration_id, registered_ids):

    if registration_id in registered_ids:
        return True

    return False


# Function to calculate total fees collected
def calculate_fees(registration_records):

    total = 0

    for record in registration_records:
        total += record[3]

    return total


# Function to calculate total sponsorship
def calculate_sponsorship(sponsor_records):

    total = 0

    for sponsor in sponsor_records:
        total += sponsor[1]

    return total


# Function to calculate total expenses
def calculate_expenses(expense_records):

    total = 0

    for expense in expense_records:
        total += expense[1]

    return total


# Main program
print("==============================================")
print(" CAMPUS FESTIVAL REGISTRATION AND FINANCIAL AUDIT")
print("==============================================")


# Remove duplicate registrations
valid_registrations = []
registered_ids = []
duplicate_count = 0

for record in registrations:

    registration_id = record[0]
    fee_due = record[2]
    amount_paid = record[3]

    if fee_due < 0 or amount_paid < 0 or amount_paid > fee_due:
        print("Invalid payment record:", registration_id)
        continue

    if check_duplicate(registration_id, registered_ids):

        print("Duplicate registration detected:", registration_id)
        duplicate_count += 1

    else:

        registered_ids.append(registration_id)
        valid_registrations.append(record)


# Display participant registration details
print("\n==============================================")
print("          PARTICIPANT REGISTRATION")
print("==============================================")

for record in valid_registrations:

    registration_id = record[0]
    name = record[1]
    fee_due = record[2]
    amount_paid = record[3]

    pending = fee_due - amount_paid

    print("\nRegistration ID:", registration_id)
    print("Participant Name:", name)
    print("Registration Fee:", fee_due)
    print("Amount Paid:", amount_paid)
    print("Pending Fee:", pending)

    if pending == 0:
        print("Payment Status: Paid")
    else:
        print("Payment Status: Pending")


# Calculate registration fee details
total_fee_due = 0

for record in valid_registrations:
    total_fee_due += record[2]

total_fees = calculate_fees(valid_registrations)

pending_fees = total_fee_due - total_fees


# Display sponsorship details
print("\n==============================================")
print("          SPONSORSHIP DETAILS")
print("==============================================")

for sponsor in sponsorships:

    print(sponsor[0], ": Rs.", sponsor[1])

total_sponsorship = calculate_sponsorship(sponsorships)


# Display expense details
print("\n==============================================")
print("             FESTIVAL EXPENSES")
print("==============================================")

for expense in expenses:

    print(expense[0], ": Rs.", expense[1])

total_expenses = calculate_expenses(expenses)


# Calculate final financial balance
total_income = total_fees + total_sponsorship

final_balance = total_income - total_expenses


# Display final audit report
print("\n==============================================")
print("          FINAL FINANCIAL AUDIT")
print("==============================================")

print("Total Participants:", len(valid_registrations))
print("Duplicate Registrations:", duplicate_count)

print("Total Registration Fees Due: Rs.", total_fee_due)
print("Total Fees Collected: Rs.", total_fees)
print("Pending Registration Fees: Rs.", pending_fees)

print("Total Sponsorship: Rs.", total_sponsorship)

print("Total Festival Income: Rs.", total_income)
print("Total Festival Expenses: Rs.", total_expenses)

print("----------------------------------------------")

print("Final Financial Balance: Rs.", final_balance)

if final_balance > 0:
    print("Financial Status: SURPLUS")

elif final_balance < 0:
    print("Financial Status: DEFICIT")

else:
    print("Financial Status: BALANCED")

print("==============================================")
print("Festival financial audit completed successfully.")
print("==============================================")

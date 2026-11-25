
expenses = []

print("==============================")
print("      DAILY EXPENSE TRACKER")
print("==============================")

while True:

    amount = float(input("\nEnter expense amount: ₹"))

    category = input("Enter expense category: ").strip()

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense added successfully!")

    choice = input("\nDo you want to add another expense? (yes/no): ").lower()

    if choice != "yes":
        break


print("\n========== ALL EXPENSES ==========")

for expense in expenses:
    print("Category:", expense["category"],
          "| Amount: ₹", expense["amount"])
total = sum(expense["amount"] for expense in expenses)

print("\n==============================")
print("Total Daily Spending: ₹", total)
print("==============================")

print("\n========== CATEGORY-WISE SPENDING ==========")

category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

for category, total in category_totals.items():
    print(category, ": ₹", total)
    
print("\nTotal Number of Expenses:", len(expenses))
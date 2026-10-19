import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    """Load saved expenses from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved expenses.")
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
        return True
    except OSError:
        print("Error: Could not save expenses.")
        return False


def add_expense(expenses):
    """Add a new expense."""
    try:
        amount = float(input("Enter amount (₹): "))

        if not 0 < amount < float("inf"):
            print("Please enter a valid positive amount.")
            return

    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    category = input("Enter category (Food/Travel/Shopping/Other): ").strip()
    description = input("Enter description: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    expense = {
        "id": max((item.get("id", 0) for item in expenses), default=0) + 1,
        "amount": round(amount, 2),
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)

    if save_expenses(expenses):
        print("Expense added successfully!")


def view_expenses(expenses):
    """Display all expenses."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n========== ALL EXPENSES ==========")

    for expense in expenses:
        print(f"""
ID: {expense['id']}
Date: {expense['date']}
Category: {expense['category']}
Description: {expense['description']}
Amount: ₹{expense['amount']:.2f}
-----------------------------------
""")


def total_expenses(expenses):
    """Calculate total spending."""
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")


def category_summary(expenses):
    """Show expenses grouped by category."""
    if not expenses:
        print("\nNo expenses available.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = (
            summary.get(category, 0) + expense["amount"]
        )

    print("\n======= CATEGORY SUMMARY =======")

    for category, amount in sorted(summary.items()):
        print(f"{category}: ₹{amount:.2f}")


def delete_expense(expenses):
    """Delete an expense using its ID."""
    if not expenses:
        print("\nNo expenses available to delete.")
        return

    try:
        expense_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)

            if save_expenses(expenses):
                print("Expense deleted successfully!")
            return

    print("Expense ID not found.")


def main():
    expenses = load_expenses()

    while True:
        print("""
===================================
       PERSONAL EXPENSE TRACKER
===================================
1. Add Expense
2. View All Expenses
3. View Total Expenses
4. Category-wise Summary
5. Delete Expense
6. Exit
===================================
""")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")


if __name__ == "__main__":
    main()
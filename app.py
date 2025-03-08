import json
import os
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# File to store expense data
EXPENSE_FILE = "expenses.json"

# Load existing data
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    return []

# Save data to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., food, travel, rent): ").lower()
    amount = float(input("Enter amount spent: "))
    description = input("Enter description: ")

    expense = {"date": date, "category": category, "amount": amount, "description": description}
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    if not expenses:
        print("❌ No expenses recorded yet.")
        return
    print("\n📌 All Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. Date: {expense['date']}, Category: {expense['category']}, Amount: ₹{expense['amount']}, Description: {expense['description']}")

# View total spending
def total_spending():
    total = sum(expense["amount"] for expense in expenses)
    print(f"💰 Total expenses so far: ₹{total:.2f}")

# View expenses by category
def expenses_by_category():
    category = input("Enter category to filter (e.g., food, travel, rent): ").lower()
    filtered = [exp for exp in expenses if exp["category"] == category]
    
    if not filtered:
        print(f"❌ No expenses found under category: {category}")
        return

    print(f"\n📂 Expenses under {category}:")
    for exp in filtered:
        print(f"Date: {exp['date']}, Amount: ₹{exp['amount']}, Description: {exp['description']}")

    total = sum(exp["amount"] for exp in filtered)
    print(f"💳 Total spent in {category}: ₹{total:.2f}")

# Search expenses by description
def search_expenses():
    keyword = input("🔎 Enter keyword to search in descriptions: ").lower()
    results = [exp for exp in expenses if keyword in exp["description"].lower()]
    
    if not results:
        print("❌ No matching expenses found.")
        return

    print("\n🔍 Search Results:")
    for exp in results:
        print(f"📅 Date: {exp['date']}, 🏷 Category: {exp['category']}, 💰 Amount: ₹{exp['amount']}, 📜 Description: {exp['description']}")

# Generate monthly report
def monthly_report():
    month = input("Enter month (e.g., 2025-03): ")
    filtered = [exp for exp in expenses if exp["date"].startswith(month)]
    
    if not filtered:
        print(f"❌ No expenses found for {month}")
        return

    total = sum(exp["amount"] for exp in filtered)
    print(f"📊 Total spending in {month}: ₹{total:.2f}")

# Export expenses to CSV
def export_to_csv():
    filename = "expenses_report.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for exp in expenses:
            writer.writerow([exp["date"], exp["category"], exp["amount"], exp["description"]])
    
    print(f"✅ Expenses exported to {filename}")

# Generate spending graph
def spending_graph():
    if not expenses:
        print("❌ No data available for graph.")
        return

    categories = {}
    for exp in expenses:
        categories[exp["category"]] = categories.get(exp["category"], 0) + exp["amount"]

    plt.figure(figsize=(8,5))
    plt.bar(categories.keys(), categories.values(), color='skyblue')
    plt.xlabel("Categories")
    plt.ylabel("Total Spending (₹)")
    plt.title("Expense Tracker - Spending by Category")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Delete an expense
def delete_expense():
    view_expenses()
    try:
        choice = int(input("Enter expense number to delete: ")) - 1
        if 0 <= choice < len(expenses):
            deleted_expense = expenses.pop(choice)
            save_expenses(expenses)
            print(f"🗑 Deleted expense: {deleted_expense}")
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

# Main program loop
expenses = load_expenses()

while True:
    print("\n🔹 Expense Tracker Menu 🔹")
    print("1️⃣ Add Expense")
    print("2️⃣ View All Expenses")
    print("3️⃣ View Total Spending")
    print("4️⃣ View Expenses by Category")
    print("5️⃣ Search Expenses")
    print("6️⃣ Generate Monthly Report")
    print("7️⃣ Export Expenses to CSV")
    print("8️⃣ View Spending Graph")
    print("9️⃣ Delete Expense")
    print("🔟 Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spending()
    elif choice == "4":
        expenses_by_category()
    elif choice == "5":
        search_expenses()
    elif choice == "6":
        monthly_report()
    elif choice == "7":
        export_to_csv()
    elif choice == "8":
        spending_graph()
    elif choice == "9":
        delete_expense()
    elif choice == "10":
        print("🚪 Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please enter a valid option.")
import json
import os
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# File to store expense data
EXPENSE_FILE = "expenses.json"

# Load existing data
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    return []

# Save data to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., food, travel, rent): ").lower()
    amount = float(input("Enter amount spent: "))
    description = input("Enter description: ")

    expense = {"date": date, "category": category, "amount": amount, "description": description}
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    if not expenses:
        print("❌ No expenses recorded yet.")
        return
    print("\n📌 All Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. Date: {expense['date']}, Category: {expense['category']}, Amount: ₹{expense['amount']}, Description: {expense['description']}")

# View total spending
def total_spending():
    total = sum(expense["amount"] for expense in expenses)
    print(f"💰 Total expenses so far: ₹{total:.2f}")

# View expenses by category
def expenses_by_category():
    category = input("Enter category to filter (e.g., food, travel, rent): ").lower()
    filtered = [exp for exp in expenses if exp["category"] == category]
    
    if not filtered:
        print(f"❌ No expenses found under category: {category}")
        return

    print(f"\n📂 Expenses under {category}:")
    for exp in filtered:
        print(f"Date: {exp['date']}, Amount: ₹{exp['amount']}, Description: {exp['description']}")

    total = sum(exp["amount"] for exp in filtered)
    print(f"💳 Total spent in {category}: ₹{total:.2f}")

# Search expenses by description
def search_expenses():
    keyword = input("🔎 Enter keyword to search in descriptions: ").lower()
    results = [exp for exp in expenses if keyword in exp["description"].lower()]
    
    if not results:
        print("❌ No matching expenses found.")
        return

    print("\n🔍 Search Results:")
    for exp in results:
        print(f"📅 Date: {exp['date']}, 🏷 Category: {exp['category']}, 💰 Amount: ₹{exp['amount']}, 📜 Description: {exp['description']}")

# Generate monthly report
def monthly_report():
    month = input("Enter month (e.g., 2025-03): ")
    filtered = [exp for exp in expenses if exp["date"].startswith(month)]
    
    if not filtered:
        print(f"❌ No expenses found for {month}")
        return

    total = sum(exp["amount"] for exp in filtered)
    print(f"📊 Total spending in {month}: ₹{total:.2f}")

# Export expenses to CSV
def export_to_csv():
    filename = "expenses_report.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for exp in expenses:
            writer.writerow([exp["date"], exp["category"], exp["amount"], exp["description"]])
    
    print(f"✅ Expenses exported to {filename}")

# Generate spending graph
def spending_graph():
    if not expenses:
        print("❌ No data available for graph.")
        return

    categories = {}
    for exp in expenses:
        categories[exp["category"]] = categories.get(exp["category"], 0) + exp["amount"]

    plt.figure(figsize=(8,5))
    plt.bar(categories.keys(), categories.values(), color='skyblue')
    plt.xlabel("Categories")
    plt.ylabel("Total Spending (₹)")
    plt.title("Expense Tracker - Spending by Category")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Delete an expense
def delete_expense():
    view_expenses()
    try:
        choice = int(input("Enter expense number to delete: ")) - 1
        if 0 <= choice < len(expenses):
            deleted_expense = expenses.pop(choice)
            save_expenses(expenses)
            print(f"🗑 Deleted expense: {deleted_expense}")
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

# Main program loop
expenses = load_expenses()

while True:
    print("\n🔹 Expense Tracker Menu 🔹")
    print("1️⃣ Add Expense")
    print("2️⃣ View All Expenses")
    print("3️⃣ View Total Spending")
    print("4️⃣ View Expenses by Category")
    print("5️⃣ Search Expenses")
    print("6️⃣ Generate Monthly Report")
    print("7️⃣ Export Expenses to CSV")
    print("8️⃣ View Spending Graph")
    print("9️⃣ Delete Expense")
    print("🔟 Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spending()
    elif choice == "4":
        expenses_by_category()
    elif choice == "5":
        search_expenses()
    elif choice == "6":
        monthly_report()
    elif choice == "7":
        export_to_csv()
    elif choice == "8":
        spending_graph()
    elif choice == "9":
        delete_expense()
    elif choice == "10":
        print("🚪 Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please enter a valid option.")
# expense-tracker

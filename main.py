import json
from datetime import datetime

# ----------------------------
# 1) Load data from file
# ----------------------------
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# ----------------------------
# 2) Save data to file
# ----------------------------
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


# ----------------------------
# 3) Add new expense
# ----------------------------
def add_expense(expenses):
    amount = float(input("Enter amount (DA): "))
    category = input("Enter category (Food / Transport / Study / Other): ")
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\n✔ Expense added successfully!\n")


# ----------------------------
# 4) Show all expenses
# ----------------------------
def show_expenses(expenses):
    if not expenses:
        print("\nNo expenses found!\n")
        return

    print("\n------ All Expenses ------")
    for i, exp in enumerate(expenses):
        print(f"{i+1}. {exp['amount']} DA - {exp['category']} - {exp['date']}")
    print("---------------------------\n")


# ----------------------------
# 5) Show statistics
# ----------------------------
def show_statistics(expenses):
    if not expenses:
        print("\nNo data to analyze!\n")
        return

    total = sum(exp["amount"] for exp in expenses)
    biggest = max(expenses, key=lambda x: x["amount"])
    average = total / len(expenses)

    print("\n------ Statistics ------")
    print(f"Total spending: {total} DA")
    print(f"Biggest purchase: {biggest['amount']} DA ({biggest['category']})")
    print(f"Average spending: {average:.2f} DA per expense")
    print("------------------------\n")


# ----------------------------
# 6) Delete an expense
# ----------------------------
def delete_expense(expenses):
    show_expenses(expenses)
    if not expenses:
        return

    index = int(input("Enter number of expense to delete: ")) - 1

    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        save_expenses(expenses)
        print(f"\n✔ Deleted: {removed['amount']} DA - {removed['category']}\n")
    else:
        print("\nInvalid number!\n")


# ----------------------------
# 7) Main Menu
# ----------------------------
def main():
    expenses = load_expenses()

    while True:
        print("==========================")
        print("      EXPENSE TRACKER     ")
        print("==========================")
        print("1. Add new expense")
        print("2. Show statistics")
        print("3. Show all expenses")
        print("4. Delete an expense")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_statistics(expenses)
        elif choice == "3":
            show_expenses(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice! Try again.\n")


# Run the program
main()

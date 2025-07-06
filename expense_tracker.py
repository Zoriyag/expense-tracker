expenses = {}

def add_expense():
    category = input("Enter category (e.g., Food, Transport, Bills): ")
    amount = float(input("Enter amount: $"))

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

    print(f"Added ${amount:.2f} to {category}.\n")

def show_summary():
    print("\n--- Expense Summary ---")
    total = 0
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")
        total += amount
    print(f"\nTotal Spent: ${total:.2f}\n")

while True:
    print("1. Add Expense")
    print("2. Show Summary")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        show_summary()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.\n")
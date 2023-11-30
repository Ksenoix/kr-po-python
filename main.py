expenses = []

def add_expense(amount, category, description):
    expense = {'amount': amount, 'category': category, 'description': description}
    expenses.append(expense)

def generate_report():
    if not expenses:
        print("No expenses to generate a report.")
        return

    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

def track_expenses_by_category(category):
    category_expenses = [expense for expense in expenses if expense['category'] == category]

    if not category_expenses:
        print(f"No expenses found for category: {category}")
        return

    for expense in category_expenses:
        print(f"Amount: {expense['amount']}, Description: {expense['description']}")

while True:
    print("\n1. Add Expense\n2. Generate Report\n3. Track Expenses by Category\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        description = input("Enter the description: ")
        add_expense(amount, category, description)
    elif choice == '2':
        generate_report()
    elif choice == '3':
        category = input("Enter the category to track: ")
        track_expenses_by_category(category)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

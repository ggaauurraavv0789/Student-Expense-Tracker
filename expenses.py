def add_expense(expenses):
    amount = float(input("Enter amount : "))
    category = input("Enter category : ")
    description = input("Enter description : ")
    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    print("\nYour Expenses:")
    print("------------------------------")
    for i, expense in enumerate(expenses, start=1):
        print(i, "| ₹", expense["amount"], "|", expense["category"], "|", expense["description"])

def delete_expense(expenses):
    if len(expenses) == 0:
        print("No expenses to delete.")
        return
    view_expenses(expenses)
    try:
        number = int(input("Enter the expense number to delete: "))
        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return
        deleted = expenses.pop(number - 1)
        print("Deleted :", deleted["description"])
    except ValueError:
        print("Please enter a valid number.")
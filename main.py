from expenses import add_expense, view_expenses, delete_expense
from data import save_expenses, load_expenses
from budget import set_budget, view_budget
from reports import spending_report

def show_menu():
    print("\n==============================")
    print("   STUDENT EXPENSE TRACKER")
    print("==============================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Set Budget")
    print("5. View Budget")
    print("6. Spending Report")
    print("7. Exit")

expenses = load_expenses()
budget = 0

while True:
    show_menu()
    choice = input("Enter your choice : ")
    if choice == "1":
        add_expense(expenses)
        save_expenses(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        delete_expense(expenses)
        save_expenses(expenses)
    elif choice == "4":
        budget = set_budget()
    elif choice == "5":
        view_budget(budget, expenses)
    elif choice == "6":
        spending_report(expenses)
    elif choice == "7":
        print("Thank you for using Student Expense Tracker!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
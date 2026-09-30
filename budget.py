def set_budget():
    try:
        budget = float(input("Enter your monthly budget: "))
        if budget < 0:
            print("Budget cannot be negative.")
            return 0
        print("Budget set successfully!")
        return budget
    except ValueError:
        print("Please enter a valid amount.")
        return 0

def view_budget(budget, expenses):
    total_spent = 0
    for expense in expenses:
        total_spent += expense["amount"]
    remaining = budget - total_spent
    print("\n----- Budget Summary -----")
    print("Monthly Budget :", budget)
    print("Total Spent :", total_spent)
    print("Remaining :", remaining)
def spending_report(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    total_spent = 0
    categories = {}
    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]
        total_spent += amount
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
    print("\n----- Spending Report -----")
    print("Total Spent :", total_spent)
    print("\nCategory-wise Spending:")
    print("------------------------------")
    for category, amount in categories.items():
        print(category, ":", amount)
expenses = []

while True:
    print("\n1. Add Expense  2. View Expenses  3. Total  4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append({"name": name, "amount": amount})

    elif choice == "2":
        for e in expenses:
            print(f"{e['name']} - {e['amount']}")

    elif choice == "3":
        total = sum(e["amount"] for e in expenses)
        print("Total expenses:", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
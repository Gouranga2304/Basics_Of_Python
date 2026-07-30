accounts = {}
next_account_no = 1001  # starting account number

def create_account():
    global next_account_no
    name = input("Enter account holder name: ")
    initial_deposit = float(input("Enter initial deposit: "))

    accounts[next_account_no] = {
        "name": name,
        "balance": initial_deposit,
        "transactions": [f"Account opened with {initial_deposit}"]
    }

    print(f"Account created! Your account number is {next_account_no}")
    next_account_no += 1

def deposit():
    acc_no = int(input("Enter account number: "))

    if acc_no not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter deposit amount: "))
    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["transactions"].append(f"Deposited {amount}")
    print(f"Deposited {amount}. New balance: {accounts[acc_no]['balance']}")

while True:
    print("\n--- Banking System ---")
    print("1. Create Account\n2. Deposit\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
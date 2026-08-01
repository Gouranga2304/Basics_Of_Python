menu = {
    "Burger": 150,
    "Pizza": 300,
    "Pasta": 250,
    "Coke": 60,
    "Fries": 100,
}

order = {}

def show_menu():
    print("\n--- Menu ---")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")

def add_to_order():
    show_menu()
    item = input("\nEnter item name to add: ").title()

    if item not in menu:
        print("Item not found on menu.")
        return

    qty = int(input(f"Enter quantity of {item}: "))
    order[item] = order.get(item, 0) + qty
    print(f"Added {qty} x {item} to your order.")

while True:
    print("\n--- Restaurant Ordering System ---")
    print("1. Show Menu\n2. Add to Order\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        show_menu()
    elif choice == "2":
        add_to_order()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
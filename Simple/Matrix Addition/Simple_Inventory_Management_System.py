inventory = {}

def add_stock():
    item = input("Enter item name: ")
    qty = int(input("Enter quantity to add: "))
    inventory[item] = inventory.get(item, 0) + qty
    print(f"Added {qty} units of '{item}'.")

def remove_stock():
    item = input("Enter item name: ")
    qty = int(input("Enter quantity sold: "))

    if item not in inventory:
        print("Item not found.")
    elif inventory[item] < qty:
        print("Not enough stock available!")
    else:
        inventory[item] -= qty
        print(f"Removed {qty} units of '{item}'.")
        if inventory[item] < 5:
            print(f"⚠️ Low stock warning: only {inventory[item]} left!")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, qty in inventory.items():
            print(f"{item}: {qty} units")

while True:
    print("\n1. Add Stock\n2. Remove Stock (Sale)\n3. View Inventory\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_stock()
    elif choice == "2":
        remove_stock()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
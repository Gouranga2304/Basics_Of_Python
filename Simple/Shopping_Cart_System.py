cart = {}

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    cart[name] = {"price": price, "quantity": quantity}
    print(f"'{name}' added to cart.")

def view_cart():
    if not cart:
        print("Cart is empty.")
    else:
        for item, details in cart.items():
            print(f"{item}: {details['quantity']} x {details['price']}")

def checkout():
    subtotal = 0
    for item, details in cart.items():
        subtotal += details["price"] * details["quantity"]

    tax = subtotal * 0.05  # 5% tax
    total = subtotal + tax

    print(f"Subtotal: {subtotal:.2f}")
    print(f"Tax (5%): {tax:.2f}")
    print(f"Total: {total:.2f}")

while True:
    print("\n1. Add Item\n2. View Cart\n3. Checkout\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        view_cart()
    elif choice == "3":
        checkout()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
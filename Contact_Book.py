contacts = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    contacts[name] = number
    print(f"Contact '{name}' added.")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def view_all():
    if not contacts:
        print("No contacts saved yet.")
    else:
        for name, number in contacts.items():
            print(f"{name}: {number}")

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. View All\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        view_all()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
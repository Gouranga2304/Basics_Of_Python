rooms = {
    101: {"type": "Single", "price": 1000, "booked": False, "guest": None},
    102: {"type": "Single", "price": 1000, "booked": False, "guest": None},
    201: {"type": "Double", "price": 1800, "booked": False, "guest": None},
    202: {"type": "Double", "price": 1800, "booked": False, "guest": None},
    301: {"type": "Suite", "price": 3000, "booked": False, "guest": None},
}

def view_available():
    print("\n--- Available Rooms ---")
    for room_no, info in rooms.items():
        if not info["booked"]:
            print(f"Room {room_no} | {info['type']} | ₹{info['price']}/night")

def book_room():
    view_available()
    room_no = int(input("\nEnter room number to book: "))

    if room_no not in rooms:
        print("Invalid room number.")
        return

    if rooms[room_no]["booked"]:
        print("This room is already booked!")
        return

    guest_name = input("Enter guest name: ")
    rooms[room_no]["booked"] = True
    rooms[room_no]["guest"] = guest_name
    print(f"Room {room_no} booked successfully for {guest_name}!")

while True:
    print("\n--- Hotel Booking System ---")
    print("1. View Available Rooms\n2. Book a Room\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        view_available()
    elif choice == "2":
        book_room()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
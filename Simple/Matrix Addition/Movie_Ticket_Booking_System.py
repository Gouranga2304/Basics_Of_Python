movies = {
    1: {"title": "Inception", "total_seats": 10, "booked_seats": []},
    2: {"title": "Interstellar", "total_seats": 10, "booked_seats": []},
    3: {"title": "The Matrix", "total_seats": 10, "booked_seats": []},
}

def view_movies():
    print("\n--- Now Showing ---")
    for movie_id, info in movies.items():
        available = info["total_seats"] - len(info["booked_seats"])
        print(f"{movie_id}. {info['title']} | Seats available: {available}")

def book_seat():
    view_movies()
    movie_id = int(input("\nEnter movie number: "))

    if movie_id not in movies:
        print("Invalid movie selection.")
        return

    movie = movies[movie_id]
    available = movie["total_seats"] - len(movie["booked_seats"])

    if available == 0:
        print("Sorry, this show is fully booked!")
        return

    seat_no = int(input(f"Enter seat number (1-{movie['total_seats']}): "))

    if seat_no < 1 or seat_no > movie["total_seats"]:
        print("Invalid seat number.")
        return

    if seat_no in movie["booked_seats"]:
        print("This seat is already booked!")
        return

    movie["booked_seats"].append(seat_no)
    print(f"Seat {seat_no} booked for '{movie['title']}'!")

while True:
    print("\n--- Movie Ticket Booking ---")
    print("1. View Movies\n2. Book Seat\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        view_movies()
    elif choice == "2":
        book_seat()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
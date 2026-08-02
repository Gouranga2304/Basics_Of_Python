candidates = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0,
}

voted_ids = []

def cast_vote():
    voter_id = input("Enter your voter ID: ")

    if voter_id in voted_ids:
        print("You have already voted!")
        return

    print("\n--- Candidates ---")
    for name in candidates:
        print(name)

    choice = input("\nEnter candidate name to vote: ").title()

    if choice not in candidates:
        print("Invalid candidate.")
        return

    candidates[choice] += 1
    voted_ids.append(voter_id)
    print(f"Vote cast for {choice}!")

def view_results():
    print("\n--- Live Results ---")
    for name, votes in candidates.items():
        print(f"{name}: {votes} votes")

while True:
    print("\n--- Voting System ---")
    print("1. Cast Vote\n2. View Results\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        cast_vote()
    elif choice == "2":
        view_results()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
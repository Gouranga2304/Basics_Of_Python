print("You wake up in a mysterious forest. There are two paths ahead.")
print("1. Go left towards the sound of running water")
print("2. Go right towards a faint light")

choice1 = input("Choose 1 or 2: ")

if choice1 == "1":
    print("\nYou find a river. A boat is tied to the bank.")
    print("1. Take the boat and cross the river")
    print("2. Follow the river on foot")

    choice2 = input("Choose 1 or 2: ")

    if choice2 == "1":
        print("\nThe boat capsizes halfway! You swim to shore, soaked but alive. THE END.")
    elif choice2 == "2":
        print("\nYou walk for hours and find a village. You are welcomed warmly. THE END.")
    else:
        print("Invalid choice. The story ends here.")

elif choice1 == "2":
    print("\nYou find a small cabin with the light coming from inside.")
    print("1. Knock on the door")
    print("2. Peek through the window first")

    choice2 = input("Choose 1 or 2: ")

    if choice2 == "1":
        print("\nAn old wizard opens the door and offers you tea. THE END.")
    elif choice2 == "2":
        print("\nYou see the wizard brewing a potion. He notices you and invites you in. THE END.")
    else:
        print("Invalid choice. The story ends here.")

else:
    print("Invalid choice. The story ends here.")
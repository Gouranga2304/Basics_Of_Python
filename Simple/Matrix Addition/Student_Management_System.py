students = {}

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    
    marks = {}
    subjects = ["Math", "Science", "English"]
    for subject in subjects:
        marks[subject] = int(input(f"Enter marks for {subject}: "))
    
    students[roll] = {"name": name, "marks": marks}
    print(f"Student '{name}' added successfully.")

def view_all():
    if not students:
        print("No students yet.")
        return
    for roll, info in students.items():
        print(f"\nRoll: {roll} | Name: {info['name']}")
        for subject, mark in info["marks"].items():
            print(f"  {subject}: {mark}")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student\n2. View All\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
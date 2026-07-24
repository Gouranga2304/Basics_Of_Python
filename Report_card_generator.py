subjects = ["Math", "Science", "English"]
marks = {}

for subject in subjects:
    m = int(input(f"Enter marks for {subject}: "))
    marks[subject] = m

total = sum(marks.values())
average = total / len(subjects)

print(f"Total: {total}")
print(f"Average: {average}")

# your task: assign a grade based on average using if-elif
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
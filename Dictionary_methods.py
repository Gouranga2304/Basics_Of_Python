#Common Dictionary Methods:
student = {"name": "Alice", "age": 21, "grade": "A"}
print(student.keys())    # dict_keys(['name', 'age', 'grade', 'city'])
print(student.values())  # dict_values(['Alice', 22, 'A', 'New York'])
print(student.items())   # dict_items([('name', 'Alice'), ('age', 22), ...])

student.pop("age")  # Removes "age" key
print(student)

student.clear()  # Empties dictionary
print(student)



squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
#positional argument
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8


 
# default argument
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!

#keyword argument

def student(name , age ):
    print (f''' my name is {name} 
        my age is {age} ''')

student(name="rick", age="20")

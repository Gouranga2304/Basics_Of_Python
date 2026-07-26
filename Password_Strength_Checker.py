password = input("Enter a password: ")

has_upper = False
has_digit = False
has_symbol = False

symbols = "!@#$%^&*()_+"

for char in password:
    if char.isupper():
        has_upper = True
    if char.isdigit():
        has_digit = True
    if char in symbols:
        has_symbol = True

length_ok = len(password) >= 8

print(f"Length OK: {length_ok}")
print(f"Has uppercase: {has_upper}")
print(f"Has digit: {has_digit}")
print(f"Has symbol: {has_symbol}")

if length_ok and has_upper and has_digit and has_symbol:
    print("Strong password!")
elif length_ok and (has_upper or has_digit or has_symbol):
    print("Moderate password")
else:
    print("Weak password")
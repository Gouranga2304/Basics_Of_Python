print("---- Unit Converter ----")
print("1. Length\n2. Weight\n3. Volume")
category = int(input("Choose category: "))

if category == 1:
    print("1. Km to Miles\n2. Miles to Km")
    choice = int(input("Choose conversion: "))
    value = float(input("Enter value: "))

    if choice == 1:
        result = value * 0.621371
        print(f"{value} km = {result} miles")
    elif choice == 2:
        result = value / 0.621371
        print(f"{value} miles = {result} km")

elif category == 2:
    print("1. Kg to Pounds\n2. Pounds to Kg")
    choice = int(input("Choose conversion: "))
    value = float(input("Enter value: "))

    if choice == 1:
        result = value * 2.20462
        print(f"{value} kg = {result} pounds")
    elif choice == 2:
        result = value / 2.20462
        print(f"{value} pounds = {result} kg")

elif category == 3:
    print("1. Liters to Gallons\n2. Gallons to Liters")
    choice = int(input("Choose conversion: "))
    value = float(input("Enter value: "))

    if choice == 1:
        result = value * 0.264172
        print(f"{value} liters = {result} gallons")
    elif choice == 2:
        result = value / 0.264172
        print(f"{value} gallons = {result} liters")

else:
    print("Invalid category")
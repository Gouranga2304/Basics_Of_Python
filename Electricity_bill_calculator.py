# Electricity Bill Calculator - Python Mini Project

def calculate_bill(units):
    if units <= 100:
        bill = units * 3.50
    elif units <= 200:
        bill = (100 * 3.50) + (units - 100) * 4.50
    elif units <= 300:
        bill = (100 * 3.50) + (100 * 4.50) + (units - 200) * 5.50
    else:
        bill = (100 * 3.50) + (100 * 4.50) + (100 * 5.50) + (units - 300) * 6.50

    service_charge = 50
    bill += service_charge

    return bill


# Take input from user
units = float(input("Enter the number of units consumed: "))

if units < 0:
    print("Invalid input. Units cannot be negative.")
else:
    total_bill = calculate_bill(units)
    print(f"Total Electricity Bill = ₹{total_bill:.2f}")
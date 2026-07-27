bill = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter tip percentage (e.g., 15): "))

tip = bill * (tip_percent / 100)
total = bill + tip

print(f"Tip amount: {tip:.2f}")
print(f"Total amount: {total:.2f}")
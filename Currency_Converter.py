print("1. USD to INR")
print("2. INR to USD")
print("3. USD to EUR")
print("4. EUR to USD")

choice = int(input("Choose conversion: "))
amount = float(input("Enter amount: "))

usd_to_inr = 83.0
usd_to_eur = 0.92

if choice == 1:
    result = amount * usd_to_inr
    print(f"{amount} USD = {result:.2f} INR")
elif choice == 2:
    result = amount / usd_to_inr
    print(f"{amount} INR = {result:.2f} USD")
elif choice == 3:
    result = amount * usd_to_eur
    print(f"{amount} USD = {result:.2f} EUR")
elif choice == 4:
    result = amount / usd_to_eur
    print(f"{amount} EUR = {result:.2f} USD")
else:
    print("Invalid choice")
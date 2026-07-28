def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    return interest, total_amount


def compound_interest(principal, rate, time, frequency=1):
    # frequency: 1 = yearly, 2 = half-yearly, 4 = quarterly
    amount = principal * (1 + (rate / (100 * frequency))) ** (frequency * time)
    interest = amount - principal
    return interest, amount


def get_valid_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("=== Interest Calculator ===")
    print("1. Simple Interest")
    print("2. Compound Interest")

    choice = input("Choose an option (1/2): ").strip()

    if choice not in ("1", "2"):
        print("Invalid choice. Please enter 1 or 2.")
        return

    principal = get_valid_number("Enter Principal amount: ")
    rate = get_valid_number("Enter Rate of interest (%): ")
    time = get_valid_number("Enter Time (in years): ")

    if choice == "1":
        interest, total = simple_interest(principal, rate, time)
        print(f"\nSimple Interest: {interest:.2f}")
        print(f"Total Amount: {total:.2f}")

    elif choice == "2":
        print("\nCompounding Frequency:")
        print("1. Yearly")
        print("2. Half-Yearly")
        print("3. Quarterly")
        freq_choice = input("Choose frequency (1/2/3): ").strip()

        frequency_map = {"1": 1, "2": 2, "3": 4}
        frequency = frequency_map.get(freq_choice, 1)  # default yearly if invalid

        interest, total = compound_interest(principal, rate, time, frequency)
        print(f"\nCompound Interest: {interest:.2f}")
        print(f"Total Amount: {total:.2f}")


if __name__ == "__main__":
    main()
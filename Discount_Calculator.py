price = float(input("Enter the original price: "))
discount_percent = float(input("Enter discount percentage: "))

discount = price * (discount_percent / 100)
final_price = price - discount

print(f"Discount amount: {discount:.2f}")
print(f"Final price after discount: {final_price:.2f}")
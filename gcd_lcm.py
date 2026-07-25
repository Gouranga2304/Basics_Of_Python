num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

smaller = min(num1, num2)
gcd = 1

for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD/HCF:", gcd)

# Find LCM using the GCD shortcut
lcm = (num1 * num2) // gcd
print("LCM:", lcm)
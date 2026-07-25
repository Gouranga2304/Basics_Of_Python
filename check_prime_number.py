n = int(input("enter the number: "))

if n <= 1:
    print("the number isn't prime")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime==True:
        print("it is a prime number")
    else:
        print("it is not a prime number")
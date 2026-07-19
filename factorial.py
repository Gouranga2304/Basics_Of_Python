n = int(input("Enter the number for factorial: "))
s = 1
r=n

if n == 0:
    print("The factorial value is 1")
else:
    while n!=0 :
        s *= n
        n-=1
    print("The factorial of", r, "is", s)
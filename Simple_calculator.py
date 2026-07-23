def add(a,b):
    return a+b

def subs(a,b):
    return a-b

def div(a,b):
    return float(a/b)

def mul(a,b):
    return a*b 

n=int(input("enter the first number: "))
m=int(input("enter the second number: "))

menu = "press 1 for addition\npress 2 for subtraction\npress 3 for division\npress 4 for multiplication\nnow enter your choice: "
x = int(input(menu))

if(x==1):
    print("result=",add(n,m))
elif(x==2):
    print("result=",subs(n,m))
elif(x==3):
    print("result=",div(n,m))
elif(x==4):
    print("result=",mul(m,n))
else:
    print("invalid input")

print("---------ATM SYSTEM----------")

print('your Balance=10000')
b=10000
while True:
    print("--------ATM MENU--------")
    print(" Enter 1 for withdraw\n Enter 2 for deposit\n Enter 3 for show balance\n Enter 4 to exit")

    c=int(input("Enter your choice: "))


    if c==1 :
        m=int(input("enterr the amount: "))
        b=b-m

    elif c==2:
        d=int(input("enetr the amount: "))
        b=b+d

    elif c==3:
       print(b)

    elif c==4:
       print("you have exited from the program")
       break

    else:
       print("invalid choice")
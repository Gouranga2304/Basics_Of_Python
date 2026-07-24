print("-------user login-------")
user_name="Gouranga"
passward=1234
attampts=3
for i in range(attampts):
    n=str(input("enter the user_name: "))
    p=int(input("enter the passward:"))
    if  (n==user_name and p==passward) :
        print("login sucessfull")
        break
    else:
        print("login unsuccessfull")
else:
    print("Account locked. Too many failed attempts.")

import random
n=int(input("enetr how many times you want to roll: "))
total=0
for i in  range(n) :
    roll=random.randint(1,6)
    print("roll no:",i+1,'value=',roll)
    total += roll
print("Total=",total)
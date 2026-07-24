import random
c=["rock", "paper","scissor"]
u=str(input("enter your choice: ")).lower()
comp_c=random.choice(c)
print("computer choice is: ",comp_c)
if u==comp_c:
    print("it is a tie") 
elif u=='rock' and comp_c=='paper' :
    print("computer wins")
elif u=='paper' and comp_c=='scissor':
    print('computer wins')
elif u=="scissor" and comp_c=="rock":
    print("computer wins ")
else:
    print("you win")


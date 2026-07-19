'''what is armstrong number 
--->> armstrong number means if you qube of the digits of the number and add them you will get the same number '''


n=int(input("enter the number :"))

m=n
s=0
while m>0 :
 s+=(m%10)**3
 m=m//10

if (s==n) :
 print(n,"is a armstrong number")

else :
 print("this is not a armstrong number")


 
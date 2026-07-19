'''
what is palindrome number ??
--->>> so palindrome number is the number whith is same from the both end it does not matter from which end you are watching the number 
for example 121 , 1221 , 1234321......
'''
n=int(input("enter the number: "))
m=n
s=0
while m!=0 :
    s=(s*10)+(m%10)
    m//=10

print(s)
if (s==n):
    print("this is a palindrome number ")

else :
    print("this is not a palindrome number ")
def fibo(n):

   a=0
   b=1
   for i in range(0,n+1):
       print(a,end=" ")
       a,b=b,a+b

n=int(input("enter how many terms you want: "))
fibo(n)
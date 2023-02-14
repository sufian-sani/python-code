import math
n=int(input("Enter number: "))
temp=n
sum=0
while n>0:
    s=n%10
    sn = math.factorial(s)
    sum=sum+sn
    n=n//10

if sum==temp:
    print('The number is a strong number')
else:
    print('The number is not a strong number')
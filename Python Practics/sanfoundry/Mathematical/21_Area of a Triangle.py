import math

a=int(input("Enter First number: "))
b=int(input("Enter Second number: "))
c=int(input("Enter Second number: "))

s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of the triangle is:',round(area,2))
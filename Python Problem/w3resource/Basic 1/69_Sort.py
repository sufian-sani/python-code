x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1=min(x,y,z)
a2=max(x,y,z)
mid=(x+y+z)-a1-a2

print(a1,mid,a2)
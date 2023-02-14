n=int(input("Enter a number: "))
a=[]
while(n>0):
    dig=n%10
    a.append(dig)
    n=n//10
a.reverse()
print(sum(a))
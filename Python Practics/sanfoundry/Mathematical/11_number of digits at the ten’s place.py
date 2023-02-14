n=int(input("Enter a Intiger number: "))
i=0
s=n%10
while n>0:
    n=n//10
    i+=1

s=str(s)
i=str(i)

res=''.join((i,s))
print('The new number formed:',res)
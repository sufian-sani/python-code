l=int(input('Enter the lower range: '))
u=int(input('Enter the upper range: '))

for i in range(l,u+1):
    if (i%7==0 and i%5==0):
        print(i)
    else:
        pass
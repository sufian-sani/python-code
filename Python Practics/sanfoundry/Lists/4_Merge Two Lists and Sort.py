ls1=[]
ls2=[]
n1=int(input('Enter The Number of Element for list 1:'))
for i in range(0,n1):
    e=int(input('Enter The Element of list 1:'))
    ls1.append(e)

n2=int(input('Enter The Number of Element for list 2:'))
for i in range(0,n2):
    e=int(input('Enter The Element of list 2:'))
    ls1.append(e)

z=ls1+ls2
z.sort()
print(z)
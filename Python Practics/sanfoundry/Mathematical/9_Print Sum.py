n=int(input("Enter the number of elements to be in the list: "))
ls=[]
for i in range(0,n):
    element=int(input('Element: '))
    ls.append(element)

even1=0
odd1=0
negative1=0
for j in ls:
    if j>0:
        if(j%2==0):
            even1=even1+j
        elif(j%2!=0):
            odd1=odd1+j
    else:
        negative1=negative1+j

print('Sum of all positive even numbers:',even1)
print('Sum of all positive odd numbers:',odd1)
print('Sum of all negative numbers:',negative1)
n=int(input("Enter the number of elements to be in the list: "))

ls=[]
for i in range(0,n):
    element=int(input('Element: '))
    ls.append(element)

even1=[]
odd1=[]

for j in ls:
    if j%2==0:
        even1.append(j)
    elif j%2!=0:
        odd1.append(j)
    else:
        pass

print('Largest even number: ',max(even1))
print('Largest odd number: ',max(odd1))
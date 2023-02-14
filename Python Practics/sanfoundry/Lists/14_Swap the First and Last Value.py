a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element:"))
    a.append(element)

a[n-1:],a[:1]=a[:1],a[n-1:]
print(a)

# print(a[n-1:])
# print(a[:1])
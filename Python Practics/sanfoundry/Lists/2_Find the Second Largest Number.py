a=[]
n=int(input('Enter number of elements: '))
for i in range(0,n):
    b=int(input("Enter element:"))
    a.append(b)

# large=max(a)
# print(large)

a.sort()
print(n)
print(a[n-2])
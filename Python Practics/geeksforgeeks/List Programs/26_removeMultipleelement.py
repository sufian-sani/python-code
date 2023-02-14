list=[5,6,-7,4,2,91,-2,10]

n1=6
n2=10

for i in list:
    if i==n1 or i==n2:
        list.remove(i)
    else:
        continue
print(list)

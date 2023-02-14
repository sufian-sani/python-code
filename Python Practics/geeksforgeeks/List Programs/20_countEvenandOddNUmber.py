list=[5,6,7,4,2,91,2,10]

even=0
odd=0

for i in list:
    if i%2==0:
        even+=1
    else:
        odd+=1

print('Even: ',even)
print('Odd: ',odd)
a=[]
n=int(input('Enter The Number of Element:'))
for i in range(0,n):
    e=int(input('Enter The Element:'))
    a.append(e)

even=[]
odd=[]
for j in a:
    if j%2==0:
        even.append(j)
    elif j%2!=0:
        odd.append(j)
    else:
        continue
print('Even list:',even)
print('Odd list:',odd)

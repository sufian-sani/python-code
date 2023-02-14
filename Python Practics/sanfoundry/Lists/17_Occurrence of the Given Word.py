a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element:")
    a.append(element)
c=[]
count=0

r_w=input('Enter word to remove:')
occurence=int(input('Enter the occurence to remove:'))
for i in a:
    if i==r_w:
        count=count+1
        if count!=occurence:
            c.append(i)
    else:
        c.append(i)
if count==0:
    print('It\'s not found')
print('Update list:',c)
print('Old List:',a)

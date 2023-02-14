a=[]
n=int(input('Enter The Number of Element:'))
for i in range(0,n):
    e=int(input('Enter The Element:'))
    a.append(e)
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp


print('Second largest number is:',a[n-2])
a=[]
n=int(input('Enter The Number of Element: '))
for i in range(1,n+1):
    element=int(input('Enter element:'))
    a.append(element)

num=int(input('Enter the number to be counted:'))
k=0
for j in a:
    if(num==j):
        k=k+1
print("Number of times",num,"appears is",k)
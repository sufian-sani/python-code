n=int(input())
d=[]
for i in range(1,n+1):
    print(i,end=" ")
    if i<n:
        print("+",end=" ")
    d.append(i)

print('=',sum(d))

print()

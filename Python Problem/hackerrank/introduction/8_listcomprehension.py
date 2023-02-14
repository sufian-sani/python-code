x=int(input())
y=int(input())
z=int(input())
n=int(input())
ls=[]
for i in range(x+1):
    for j in range(y+1):
        for z in range(z+1):
            if (i+j+z)==n:
                pass
            else:
                ls.append([i,j,z])

print(ls)
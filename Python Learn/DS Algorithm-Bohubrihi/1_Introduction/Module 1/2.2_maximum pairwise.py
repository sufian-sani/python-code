def findlarge_faster(a):
    index1=0
    for i in range(1,len(a)):
        if a[i] > a[index1]:
            index1=i

    index2=0
    for j in range(1,len(a)):
        if a[j]!=a[index1] and a[j] > a[index2]:
            index2 = j

    return a[index1]*a[index2]

f = open("data1.txt", "r")
d=f.read()
var=''.join(d).split(' ')
var1=map(int,var)

ls_var=list(var1)
a=[]
for i in range(len(ls_var)):
    a.append(int(ls_var[i]))

print(findlarge_faster(a))
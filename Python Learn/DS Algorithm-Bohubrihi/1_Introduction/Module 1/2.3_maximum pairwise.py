def findlarge_faster(a):
    index1 = -1
    for i in range(len(a)):
        if index1 == -1 or a[i] > a[index1]:
            index1 = i

    index2 = -1
    for j in range(len(a)):
        if j != index1 and (index2 == -1 or a[j] > a[index2]):
            index2 = j

    return a[index1] * a[index2]



f = open("data5.txt", "r")
d=f.read()
var=''.join(d).split(' ')
var1=map(int,var)

ls_var=list(var1)
a=[]
for i in range(len(ls_var)):
    a.append(int(ls_var[i]))

print(findlarge_faster(a))
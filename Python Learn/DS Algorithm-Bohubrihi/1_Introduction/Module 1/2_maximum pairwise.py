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

x=input().split()
a=[]
for i in range(len(x)):
    a.append(int(x[i]))

print(findlarge_faster(a))

'''
def findlarge(a):
    max_product=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            max_product=max(max_product,a[i]*a[j])

    return max_product

x=input().split()
a=[]
for i in range(len(x)):
    a.append(int(x[i]))

print(findlarge(a))
'''
'''
def findlarge(multi):
    return max(multi)

def pairwise(ls):
    ls_new=[]
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i==j:
                pass
            else:
                res=ls[i]*ls[j]
                ls_new.append(res)
    return ls_new

ls=[5,6,2,7,4]
multi=pairwise(ls)
print(findlarge(multi))
'''
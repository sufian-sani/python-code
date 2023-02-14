def cloning(ls):
    clist=[]
    clist = ls[:]
    return clist

list=[5,6,7,4,1,2,9]
clist=cloning(list)
print(list)
print(clist)
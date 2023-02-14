def swapls(ls,p1,p2):

    ls[p1],ls[p2]=ls[p2],ls[p1]

    print(ls)


list=[23,65,19,90]
swapls(list,0,3)
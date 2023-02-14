def countnumber(ls,n):
    count=0
    for i in ls:
        if i==n:
            count=count+1
    return count

n=4
ls1=[1, 4, 6, 7, 4]
ls2=[1, 4, 6, 4, 7, 4,8,7,4,5,6,9,2,4]
print(countnumber(ls1,n))
print(countnumber(ls2,n))
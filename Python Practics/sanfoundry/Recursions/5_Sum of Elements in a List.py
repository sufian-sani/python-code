def list_sum(ls,size):
    if size == 0:
        return 0
    print(ls,size)
    return ls[size-1]+list_sum(ls,size-1)


ls=[3,56,7]
size=len(ls)
print(list_sum(ls,size))


























'''
def sum(a,n):
    if n==0:
        return 0
    else:
        return a[n-1]+sum(a,n-1)

n=int(input('Take a number:'))
a=[]
for i in range(n):
    e=int(input())
    a.append(e)

print(a)
b=sum(a,n)
print(b)
'''

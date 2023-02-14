# pos=1
def binary_search(ls,k):
    l=0
    u=len(ls)-1

    while l <= u:
        mid = (l+u) // 2
        if ls[mid] == k:
            return True
        else:
            if ls[mid] < k:
                l=mid+1
            else:
                u=mid-1

    return False



ls = list(map(int, input().split()))
k = int(input())

if binary_search(ls,k):
    print('Found')
else:
    print('Not Found')



'''
def binary_search(ls,mid,k,low):
    for low in range(mid):
        if ls[low]==k:
            return low

ls = list(map(int, input().split()))
# ls = [2,4,5,7,8,10,14,9]
low=0
k = int(input())
size = len(ls)
mid = size//2

if ls[mid]==k:
    print(mid)
elif ls[mid]>k:
    print(binary_search(ls,mid+1,k,low))
else:
    print(binary_search(ls,size,k,mid-1))


'''
'''
ls = list(map(int, input().split()))
size = len(ls)

for i in range(1,size):
    p=ls[i]
    j=i-1
    while j >= 0 and p < ls[j]:
        ls[j+1]=ls[j]
        j-=1
    ls[j+1]=p

print(ls)
'''

'''
ls = list(map(int, input().split()))
size = len(ls)
min=ls[0]
for i in range(1,size):
    if min>ls[i]:
        min=ls[i]
    else:
        pass
print(min)
'''

'''
ls = list(map(int, input().split()))
size = len(ls)
max=ls[0]
for i in range(1,size):
    if max<ls[i]:
        max=ls[i]
    else:
        pass
print(max)
'''


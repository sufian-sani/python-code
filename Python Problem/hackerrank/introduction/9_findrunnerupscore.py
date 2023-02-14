n = int(input())
arr = list(map(int, input().split()))

# print(arr)

print(max([x for x in arr if x!=max(arr)]))

'''
n = int(input())
arr = list(map(int, input().split()))
zes = max(arr)
i=0
while(i<n):
    if zes == max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))
'''
'''
i = int(input())
ls = list(map(int, input().strip().split()))[:i]
# for i in range(x):
#     n=int(input())
#     ls.append(n)

size=len(ls)
u_p = max(ls)
for j in ls:
    if u_p in ls:
        ls.remove(u_p)
    else:
        continue

uu_p=max(ls)
print(uu_p)

# n=ls.pop(size-1)
# u_p=max(ls)
#
# print(u_p)
'''
# k,m=map(int,input().split())

from itertools import product
n,m=[int(x) for x in input().split()]
li=list()

for i in range(n):
    l=list(map(int,input().split()))[1:]
    # print(l)
    li.append(l)

# print(li)

# for i in product(*li):
#     print(i)

r=map(lambda x:sum(i*i for i in x)%m,product(*li))

# for j in r:
#     print(j)

print(max(r))
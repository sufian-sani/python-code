from itertools import combinations

a = input().split()

for i in range(1,int(a[1])+1):
    for j in combinations(sorted(a[0]),i):
        print(''.join(j))

'''
from itertools import combinations

a = input().split()

for i in range(1, int(a[1]) + 1):
    for j in combinations(sorted(a[0]), i):
        print(''.join(j))
'''
# ls=combinations(s[-1])

# print(list(combinations('123456',3)))
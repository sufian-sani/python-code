from itertools import combinations_with_replacement

a = input().split()
ls=combinations_with_replacement(sorted(a[0]),int(a[1]))

for i in ls:
    print(''.join(i))
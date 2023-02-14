from itertools import combinations

s='hack'

p=combinations(s,3)

for i in list(p):
    print(''.join(map(str, i)))

from itertools import permutations

str = 'ABCDEFG'

permlist = permutations(str)

for i in list(permlist):
    print(''.join(i))
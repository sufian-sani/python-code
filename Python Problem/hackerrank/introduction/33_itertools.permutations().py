from itertools import permutations


s, k = map(str,input().split())
s=sorted(s)
k=int(k)
# no length entered so default length
# taken as 4(the length of string GeEK)
p = permutations(s,k)


# # Print the obtained permutations
for j in list(p):
	print(''.join(map(str, j)))

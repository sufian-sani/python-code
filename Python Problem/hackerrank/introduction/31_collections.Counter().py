from collections import Counter

x=int(input())
s = Counter(map(int, input().split()))

n=int(input())
sp=0
for i in range(n):
    size, p=map(int, input().split())
    if size in s and s[size]>0:
        s[size] -= 1
        sp+=p
print(sp)

'''
from collections import Counter

X = input()
S = Counter(map(int, input().split()))
print(S)
N = int(input())
earnings = 0
for customer in range(N):
    size, x_i = map(int, input().split())
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i

print(earnings)
'''
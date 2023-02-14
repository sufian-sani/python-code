from collections import Counter

s=sorted(input())

x=Counter(s).most_common(3)

for i,j in x:
    print(i , j)
import re

n=int(input())
ls=[]
for i in range(n):
    str=input()
    ls.append(str)

for j in ls:
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', j)))


# ^[-+]?[0-9]*\.[0-9]+$ floting number check
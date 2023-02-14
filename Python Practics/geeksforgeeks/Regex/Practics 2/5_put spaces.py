import re

# str = 'BruceWayneIsBatman'
str = 'GeeksForGeeks'

finding=re.findall(r'[A-Z][a-z]*',str)
ls=[]
for i in finding:
    ls.append(i)

print(' '.join(ls))
from collections import Counter

str= 'geeksforgeeks'

wc = Counter(str)

d=[]

for key,value in wc.items():
    if value>1:
        d.append(key)
    else:
        pass
print(d)
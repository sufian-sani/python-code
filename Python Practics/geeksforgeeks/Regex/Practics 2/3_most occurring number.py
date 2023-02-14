import re

from collections import Counter

str='abcd1def2high2bnasvd3vjhd44'

occurance=re.findall(r'\d+',str)

c = Counter(occurance)

list_key=list(c.keys())

list_key=list(map(int,list_key))

max=0

max_pro=0

for i in list_key:
    if max<i:
        max_pro=i
        max=max_pro

# print(type(list_key[0]))

print(max)
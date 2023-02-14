import re

str='ankitrai326'

regex=r'[\w]$'

if re.findall(regex,str):
    print('Accept')
else:
    print('Discard')
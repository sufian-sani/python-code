#^[.*geeks.*]+
import re

# str='geeks for geeks makes learning fun'
str=input()

substr=input()

# if re.search('^[.*geeks.*]+',str):
if re.search(f'^[.*{substr}.*]+',str):
    print('Valid')
else:
    print('Invalid')



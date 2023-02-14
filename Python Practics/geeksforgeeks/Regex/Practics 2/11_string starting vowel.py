import re

str='animal'

if re.search('^[aeiouAEIOU]+',str):
    print('Valid')
else:
    print('Invalid')
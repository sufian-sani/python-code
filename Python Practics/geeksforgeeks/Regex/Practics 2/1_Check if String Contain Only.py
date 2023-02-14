import re

str='1234'

pattern=re.compile('^[1234]+$')

if re.search(pattern,str):
    print('Match')
else:
    print('Not Match')
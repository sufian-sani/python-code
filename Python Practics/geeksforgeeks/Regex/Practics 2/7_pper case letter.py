import re

str='Yeeksrtyuu'

# finding=re.search(r'^[A-Z]',str)

if re.search(r'^[A-Z]',str):
    print('True')
else:
    print('False')
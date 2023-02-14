import re

str='abbdfhhkdhskhdfisudyhha'

# check=re.search(r'^(.).*\1$',str)

if re.search(r'^(.).*\1$',str):
    print('True')
else:
    print('False')
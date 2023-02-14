import re

def check(str):
    rex = re.compile('^[1234]+$')
    if re.search(rex, str):
        return 'Valid String'
    else:
        return 'Invalid String'



str_1='2134'
str_2='349'

print(check(str_1))
print(check(str_2))

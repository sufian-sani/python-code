import re

a  = 'My name is Rahim and i am a student'

p = re.search('(.*)and (.*)',a, re.I)

if p:
    print('Found')
    print(p.group())
    print(p.group(1).capitalize())
    print(p.group(2).upper())
else:
    print('Not Found')

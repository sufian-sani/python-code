import re

a  = 'My name is Rahim and i am a student'

# p = re.match('My.*',a)
p = re.match('(My.*)(and) (.*student)',a)

if p:
    print('Match')
    print('Group-1:',p.group(1))
    print('Group-2:',p.group(2))
    print('Group-3:',p.group(3))
else:
    print('Not Match')
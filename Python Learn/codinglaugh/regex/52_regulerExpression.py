import re

a  = 'My name is Rahim and i am a student'
#(.*---.*)

# p = re.search('.*And.*',a, re.I)
p = re.search('.*is.*',a, re.I)

if p:
    print('Found')
else:
    print('Not Found')
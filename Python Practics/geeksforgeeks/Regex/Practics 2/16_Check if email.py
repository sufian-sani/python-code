import re

regex=re.compile('\S+@\S+\.\S+')

mail=input()

if re.search(regex,mail):
    print('Valid')
else:
    print('Invalid')
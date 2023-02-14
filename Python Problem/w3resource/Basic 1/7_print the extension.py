import re

regex=re.compile('.[a-zA-Z0-9]+$')

str=input()

r_output=re.findall(regex,str)

print(''.join(r_output))
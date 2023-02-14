import re

str='ThisIsGeeksforGeeks !, 123'
uppercase=re.findall(r'[A-Z]',str)
lowercase=re.findall('[a-z]',str)
numerical=re.findall('[0-9]',str)
special=re.findall('[, .!?]',str)

print('No. of uppercase characters = ',len(uppercase))
print('No. of lowercase characters = ',len(lowercase))
print('No. of numerical characters = ',len(numerical))
print('No. of special characters = ',len(special))

'''
import re

rex=re.compile('([A-Z]*)([a-z]*)(\d*)(\W*)')

str='ThisIsGeeksforGeeks!, 123'

rex_output=re.search(rex,str)

print('No. of uppercase characters = ',rex_output.group(1))
print('No. of lowercase characters = ',rex_output.group(2))
print('No. of numerical characters = ',rex_output.group(3))
print('No. of special characters = ',rex_output.group(4))
'''

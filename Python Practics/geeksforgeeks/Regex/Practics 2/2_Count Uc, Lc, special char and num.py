import re

'''
digit = \d+
uppercase = [A-Z]+
lowercase = [a-z]+
special charter = \W+
'''
string = "ThisIsGeeksforGeeks !, 123"

digit=re.findall('\d',string)
uppercase=re.findall('[A-Z]',string)
lowercase=re.findall('[a-z]',string)
special_charter=re.findall('\W',string)

print('uppercase: ',len(uppercase))
print('lowercase: ',len(lowercase))
print('Digit: ',len(digit))
print('special charter: ',len(special_charter))
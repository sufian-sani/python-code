import re
date_data = '13/Feb/2022 I will go Canada'
date_pattern=re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')

result=date_pattern.match(date_data)

for x in range(0,4):
    print(result.group(x))

print(result.groups())
day,month,year=result.groups()

print("Today's day is: ",day)


'''
import re
pattern = r'colour'
text='it is a colour, I love it'
match=re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())
'''
'''
import re
pattern = r'it'
print(re.findall(pattern,'it is a colour, I love it'))
'''

'''
import re
pattern = r'colour'
if re.search(pattern,'It is a colour, I love it'):
    print('Match')
else:
    print('Not Match')
'''
'''
import re
pattern = r'colour'
if re.match(pattern,'colour is a color, I love it'):
    print('Match')
else:
    print('Not Match')
'''
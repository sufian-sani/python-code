from collections import Counter

str1 = 'hello'
str2 = 'rteksfoGrdsskGeggehes'

dict1=Counter(str1)
dict2=Counter(str2)

result = dict1 & dict2

if result==dict1:
    print('possible')
else:
    print('Not Possible')


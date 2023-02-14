# searching - gmail
import re

# a = 'marjuk.sma@gmail.com'
# a = 'marjuk.sma@gmail.com'
a = 'marjuk.sma@gmail.in'

# p = re.search('\w+@gmail.com',a)
# p = re.search('\w+\.*\w+@gmail.com',a)
# p = re.search('\w+\.*\w+@\w+.com',a)
p = re.search('\w+\.*\w+@\w+.\w+',a) #universal pattern

if p:
    print('Found')
else:
    print('Not Found')
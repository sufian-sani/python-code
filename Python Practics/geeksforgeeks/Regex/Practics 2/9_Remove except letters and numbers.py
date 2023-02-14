import re

def removing(str):
    regex = r'\b\W*\b'

    return re.sub(regex,'',str)

str='123abcjw:, .@! eiw'

print(removing(str))
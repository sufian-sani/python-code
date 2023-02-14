import re

str='BruceWayneIsBatman'

check=re.compile('[A-Z][a-z]*')

check_str=re.findall(check,str)
result=[]
for word in check_str:
    word=chr(ord(word[0])+32)+word[1:]
    result.append(word)

print(' '.join(result))

# reconfigur=' '.join(check_str)
# print(reconfigur)
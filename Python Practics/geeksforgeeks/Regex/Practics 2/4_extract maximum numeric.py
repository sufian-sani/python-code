import re

str='abchsd0sdhs148'

number_find=re.findall(r'\d+',str)

number_find_ls=list(map(int,number_find))

print(max(number_find_ls))

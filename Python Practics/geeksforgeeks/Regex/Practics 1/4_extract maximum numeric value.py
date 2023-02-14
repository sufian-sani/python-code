import re

n = input()

match=re.findall(r'\d+',n)

int_output=map(int,match)

max_value=max(int_output)

print(max_value)
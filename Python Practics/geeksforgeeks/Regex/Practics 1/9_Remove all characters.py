import re

ini_string = "123abcjw:, .@! eiw"

result=re.sub(r'[\W_]+','',ini_string)

print(result)
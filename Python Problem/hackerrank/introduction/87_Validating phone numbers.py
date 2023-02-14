import re

n=int(input())

regex=re.compile('^[789][0-9]{9}$')

for _ in range(n):
    check=re.match(regex,input())
    print('YES' if bool(check) else 'NO')
import re

n=input()

ls=re.split(r"[,.]",n)

for i in ls:
  print(i)
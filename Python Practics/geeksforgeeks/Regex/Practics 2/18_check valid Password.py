import re

regex=re.compile("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[\w])(?=\\S+$).{8,}$")

str = input()

if re.search(regex,str):
    print("Valid")
else:
    print("Invalid")
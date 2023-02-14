import re

#^(https:\/\/www\.|http:\/\/www.|www.)[a-zA-Z0-9\-\_$]+\.[a-zA-Z]{2,5}$

regex='(https:\/\/www\.|http:\/\/www.|www.)[a-zA-Z0-9\-\_$]+\.[a-zA-Z]{2,5}$'

pattern=re.compile(regex)

str=input()

if re.search(pattern,str):
    print("True")
else:
    print("False")

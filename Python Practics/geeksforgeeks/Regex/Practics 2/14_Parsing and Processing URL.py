import re

str='https://www.geeksforgeeks.org/'

regex1='(\w+)://'

pattran1=re.compile(regex1)

print("Protocol: ",re.findall(pattran1,str))

regex2='\w+\.\w+\.\w+'

pattran2=re.compile(regex2)

print("Domain Name: ",re.findall(pattran2,str))
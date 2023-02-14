def process(str,n):
    str1 = ""
    for i in range(3):
        str1 = str1 + str[:2]
    return str1

str='rtyuiop'
n=3
print(process(str,3))
'''
str='abcdf'
print(str[:2])
str1=""
for i in range(3):
    str1=str1+str[:2]

print(str1)
'''
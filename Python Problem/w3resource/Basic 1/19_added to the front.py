def stringcut(str):
    if str[:2] == 'Is':
        return str
    else:
       return 'Is' + str[2:]

str='am unlucky men'

print(stringcut(str))

'''
str='i am unlucky men'
print(str[2:])
str1='Is '+str[2:]
print(str1)
'''
# str='i am unlucky men'
# print(str[:2])
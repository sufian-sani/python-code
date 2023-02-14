def reverse_str(str):
    if len(str) == 1:
        return str
    else:
        return reverse_str(str[1:])+str[0]

str=input('Take a string: ')
print(reverse_str(str))
























'''
def is_revarse(s):
    if len(s)==0:
        return s
    else:
        return is_revarse(s[1:]) + s[0]

string=input('Take a string: ')
print(is_revarse(string))
'''
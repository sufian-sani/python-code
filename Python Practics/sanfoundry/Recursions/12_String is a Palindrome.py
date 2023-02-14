def c_palindrome(str):
    if len(str) < 1:
        return True
    else:
        if str[0]==str[-1]:
            return c_palindrome(str[1:-1])
        else:
            return False


str=input('Take a string: ')
print(c_palindrome(str))

























'''
def check(s):
    if len(s)<=1:
        return True
    else:
        if s[0] == s[-1]:
            return check(s[1:-1])
        else:
            return False


string=input('Take a string: ')
print(check(string))
'''
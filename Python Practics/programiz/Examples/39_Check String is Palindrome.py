str='moon'
my_str = str.casefold()
# str_rev=str[::-1]
str_rev=reversed(str)

if list(str)==list(str_rev):
    print('The string is a palindrome.')
else:
    print('The string isn\'t a palindrome.')

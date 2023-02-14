def occur_check(str,f_str):
    if f_str not in str:
        return 0
    elif str[0]==f_str:
        print('1st:',str,f_str)
        return 1+occur_check(str[1:],f_str)
    else:
        print('2nd:',str,f_str)
        return occur_check(str[1:], f_str)

str=input('Take a string: ')
f_str=input('Take finding letter: ')
print(occur_check(str,f_str))
























'''
def f_letter(string,f_char):
    if f_char not in string:
        return 0
    elif string[0]==f_char:
        return 1+f_letter(string[1:],f_char)
    else:
        return f_letter(string[1:],f_char)

string=input('Take a string: ')
f_char=input('Take finding letter: ')
print(f_letter(string,f_char))
'''

# def check(string, ch):
#     if not string:
#         return 0
#     elif string[0] == ch:
#         return 1 + check(string[1:], ch)
#     else:
#         return check(string[1:], ch)
#
#
# string = input("Enter string:")
# ch = input("Enter character to check:")
# print("Count is:")
# print(check(string, ch))

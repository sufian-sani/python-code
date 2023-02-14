def str_occur(str):
    char = str[0]
    str=str.replace(char,'$')
    return char+str[1:]

print(str_occur('restart'))

# def str_occur(str):
#     char = str[0]
#     str1=str[1:]
#     length=len(str1)
#     for i in range(length):
#         if char==str1[i]:
#             str1=str1.replace(str1[i],'$')
#     return char+str1
#
#
# print(str_occur('restart'))
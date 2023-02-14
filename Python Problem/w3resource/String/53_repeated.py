def first_repeated_char(str1):
    for index,c in enumerate(str1):
        if str1[:index+1].count(c) > 1:
            return c
    return None

print(first_repeated_char("abcdabcd"))

# def first_repeated_char(str1):
#     count=0
#     length=len(str1)
#     # f_letter=str1[0]
#     for i in range(1,length):
#         j = i
#         f_letter=str1[i-1]
#         while j<length:
#             if f_letter==str1[j]:
#                 count+=1
#             else:
#                 pass
#             j=j+1
#         if count==1:
#             return f_letter
#     return None
#
# print(first_repeated_char("abcdabcd"))
# print(first_repeated_char("abcd"))
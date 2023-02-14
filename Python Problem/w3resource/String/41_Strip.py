def strip_chars(str,req):
    return ''.join(c for c in str if c not in req)

print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))

# def strip_chars(str,req):
#     ls_add=[]
#     for i in str.split():
#         for j in i:
#             if j in req:
#                 pass
#             else:
#                 ls_add.append(j)
#         ls_add.append(' ')
#     return ''.join(ls_add)
#
# print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))
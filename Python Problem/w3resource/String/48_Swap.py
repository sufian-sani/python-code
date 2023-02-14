amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.','.,'))
print(amount)

# amount = "32.054,23"
# str1=''
# f_index=0
# l_index=0
# for i in range(len(amount)):
#     if amount[i]=='.':
#         f_index=i
#     elif amount[i]==',':
#         l_index = i
# for i in range(len(amount)):
#     if i==f_index:
#         str1+=','
#     elif i==l_index:
#         str1 += '.'
#     else:
#         str1+=amount[i]
# print(str1)
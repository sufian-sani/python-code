# ls=[5,8,9]
# n=7
#
# for i in ls:
#     if i > n:
#         print(True)
#     else:
#         print(False)

num = [2,3,4]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()

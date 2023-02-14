def all_repeat(str1):
    ls_all=[]
    str1=list(str1)
    for i in str1:
        for j in str1:
            for k in str1:
                ls_all.append((i,j,k))
    return ls_all

print(all_repeat('xyz'))

# from itertools import product
# def all_repeat(str1, rno):
#     chars=list(str1)
#     result=[]
#     for c in product(chars, repeat=rno):
#         result.append(c)
#     return result
#
# print(all_repeat('xyz', 3))
# print(all_repeat('xyz', 2))
# print(all_repeat('abcd', 4))



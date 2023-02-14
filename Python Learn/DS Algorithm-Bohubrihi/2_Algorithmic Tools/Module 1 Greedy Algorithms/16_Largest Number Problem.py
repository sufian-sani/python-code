# def find_large(ls, max):
#     i = 0
#     while i < len(ls):
#         if max < ls[i]:
#             max = ls[i]
#         i += 1
#     return max

ls=[4,5,8,7,1,2,3,6,9,5]

n_ls=[]

while ls:
    min=ls[0]
    for i in ls:
        if i<min:
            min=i
    n_ls.append(min)
    ls.remove(min)


print(n_ls)
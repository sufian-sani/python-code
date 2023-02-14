n = int(input())

ls = []

for i in range(n):
    n1,n2=map(int,input().split())
    ls_sub = []
    for j in range(n1,n2+1):
        ls_sub.append(j)
        # print(ls_sub)
        # break
        # print(ls_sub)
    ls.append(ls_sub)
    # print(ls_sub)


# print(ls)
# set_ls = set.intersection(*[set(list) for list in ls])
# print(set_ls)
# len_ls = len(ls)

final_ls = []
# for i in range(len_ls-1):
#     # print(i)
#     common = set(ls[i]) & set(ls[i+1])
#     print(common)
#     ls.remove(ls[i])
len_ls = len(ls)
ls_len_initial = 0
while ls_len_initial < len_ls:
    for i in ls[ls_len_initial]:

    ls_len_initial += 1
    # if len(ls) != 0:
    #     ls.pop()
    #     ls_len_initial += 1
    # else:
    #     break

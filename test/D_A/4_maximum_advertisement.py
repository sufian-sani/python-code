# ls1 = [1,3,-5]
# ls2 = [-2,4,1]
# #
# # ls1 = [23]
# # ls2 = [39]
#
# max_add = []
#
# while len(ls1) > 0 and len(ls2) > 0:
#     ls1_max = max(ls1)
#     ls2_max = max(ls2)
#     multification = ls1_max*ls2_max
#     max_add.append(multification)
#     print(ls1_max)
#     print(ls2_max)
#     ls1.remove(ls1_max)
#     ls2.remove(ls2_max)
#
# print(sum(max_add))
# -----main code-----
# for i,j in zip(ls1,ls2):
#     print(i,j)

# print(ls1)
# print(ls2)
# import pdb; pdb.set_trace();

n = int(input())
ls = []
max_add = []

for i in range(2):
    all_list = list(map(int,input().strip().split()))[:n]
    ls.append(all_list)
    # print(oil_station)

# print(ls[0])
# print(ls[1])
while len(ls[0]) > 0 and len(ls[1]) > 0:
    ls1_max = max(ls[0])
    ls2_max = max(ls[1])
    multification = ls1_max*ls2_max
    max_add.append(multification)
    # print(ls1_max)
    # print(ls2_max)
    ls[0].remove(ls1_max)
    ls[1].remove(ls2_max)

print(sum(max_add))








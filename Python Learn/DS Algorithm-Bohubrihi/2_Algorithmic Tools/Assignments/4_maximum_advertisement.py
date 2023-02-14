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
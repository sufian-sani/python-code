# pro_w_r = [[60,20],[100,50],[120,30]]
# pro_w_r = [[7,2],[10,6],[15,6]]
# pro_w_r = [[500, 30],[1,1]]
n,w=map(int,input().split())
it_v=[]
it_w=[]
for i in range(n):
    v,w_p=map(int,input().split())
    it_v.append(v)
    it_w.append(w_p)

pro_w_r = []
pro_w_r.extend([list(a) for a in zip(it_v, it_w)])

max_loot = w
val_ls = []
max_val = 0
max_val_index = 0
max_val_item_index = []
main_value = 0
for i in pro_w_r:
    val1, val2 = i[0], i[1]
    val_res = val1/val2
    val_ls.append(val_res)

while max_loot > 0:
    max_val = max(val_ls)
    max_val_index = val_ls.index(max_val)
    max_val_item_index = pro_w_r[max_val_index]
    # print(val_ls)
    # print(pro_w_r)
    if max_val_item_index[1] <= max_loot:
        main_value+=max_val_item_index[0]
        max_loot-=max_val_item_index[1]
        val_ls.pop(max_val_index)
        pro_w_r.pop(max_val_index)
    else:
        # print(max_val_item_index[0])
        extend_val = max_loot*max_val
        # extend_val = max_loot*max_val_item_index[0]
        # print(max_loot)
        # print(extend_val)
        main_value+=extend_val
        val_ls.pop(max_val_index)
        pro_w_r.pop(max_val_index)
        # print('Extra:',val_ls)
        # max_loot-=1
        break


print("{:.4f}".format(main_value))
# print(main_value)

# print(max_val_item_index[1])
# print(max_val)
# print(max_val_index)
# print(val_ls)

# it_v=[]
# it_w=[]
# for i in range(n):
#     v,w_p=map(int,input().split())
#     it_v.append(v)
#     it_w.append(w_p)

# print(it_v)
# print(it_w)
n,w=map(int,input().split())
it_v=[]
it_w=[]
for i in range(n):
    v,w_p=map(int,input().split())
    it_v.append(v)
    it_w.append(w_p)

main_ls = []
main_ls.extend([list(a) for a in zip(it_v, it_w)])

# print(it_v)
# print(it_w)
#
# print('main list')
# print(main_ls)
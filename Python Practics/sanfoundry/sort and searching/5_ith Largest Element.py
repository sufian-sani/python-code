ls = list(map(int, input().split()))
k = int(input('The ith largest element will be found. Enter i:'))
new_ls=[]
while ls:
    large=ls[0]
    for i in ls:
        if i>large:
            large=i
    new_ls.append(large)
    ls.remove(large)

ith=new_ls[k-1]
print(new_ls)
print(ith)

'''
ls = [2, 3, 4, 7,45,8,88,5,6]
i = 9

ls=sorted(ls)
ls.reverse()


k = ls[i-1]

print(k)
'''
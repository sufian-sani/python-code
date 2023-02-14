

ls = list(map(int, input().split()))
k = int(input('The ith smallest element will be found. Enter i:'))
new_ls=[]
while ls:
    min=ls[0]
    for i in ls:
        if i<min:
            min=i
    new_ls.append(min)
    ls.remove(min)

ith=new_ls[k-1]
print(new_ls)
print(ith)


# def find_smallest(ls,k):
#     return k
    # for i in range(len(ls)):
    #     if ls[i]==k:
    #         return ls[i]
    #     else:
    #         return -1
'''
ls = [2, 3, 4, 7,45,8,88,5,6]
i = 5

ls=sorted(ls)

k = ls[i-1]

print(k)
'''
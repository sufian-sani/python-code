n, m = map(int, input().split())

ls=[]

for i in range(n):
    ls_i=[int(x) for x in input().strip().split(' ')]
    ls.append(ls_i)

k = int(input().strip())

sorted_arr=sorted(ls,key=lambda x:x[k])


for row in sorted_arr:
    print(' '.join(str(y) for y in row))

# [int(x) for x in range(m)]

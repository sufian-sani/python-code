# n=5
# for i in range(n,0,-1):
#     print((n-i)*' '+i*'*')


n=5

for i in range(n,0,-1):
    s=n-i
    for j in range(s):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    print()
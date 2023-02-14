n = int(input("Enter a number: "))

for i in range(n,0,-1):
    print((n-i)*' '+i*'*')
# for i in range(n,0,-1):
#     s =i-1
#     for j in range(0,i):
#         print('*', end="")
#     print()
#     for k in range(0,n-s):
#         print(' ',end='')
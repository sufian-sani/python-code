# n = int(input())
#
# for i in range(2,n):
#     if n%i==0:
#         print(False)
#         break
#     else:
#         print(True)
#         break

# n = int(input())
# m = int(input())
#
# for i in range(n,m):
#     for j in range(2,i):
#         if i % j == 0:
#             print(False)
#             break
#         else:
#             print(i)

n = int(input())
i=2
while n>=2:
    if n % i == 0:
        print(False)
        break
    else:
        print(True)
        break
    i=i+1

# for i in range(2,n):
#     if n%i==0:
#         print(False)
#         break
#     else:
#         print(True)
#         break
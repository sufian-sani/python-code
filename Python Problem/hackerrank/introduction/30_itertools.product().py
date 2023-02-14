from itertools import product

arr1 = tuple(map(int, input().split()))
arr2 = tuple(map(int, input().split()))

# print(arr1)
# arr1 = [1, 2, 3]
# arr2 = [5, 6, 7]
#
print(*product(arr1, arr2))

# res = str(s)[1:-1]

# u=''
# for i in s:
#     u=''.join(i)

# print(s)
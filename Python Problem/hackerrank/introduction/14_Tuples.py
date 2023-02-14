def print_tuple(t):
    t=(t)
    hash(t)
    return t

n = int(input())
integer_list = tuple(map(int, input().split()))

# print(print_tuple(n))
print(hash(integer_list))

# def operation(a):
#
#
#     return 0

# input()
# a=set(map(int, input().split()))
# n=int(input())
# for i in range(n):
#     comment = input().split()
#     operations = comment[0]
#     updateSet = set(map(int, input().split()))
#
#     if operations == 'intersection_update':
#         a.intersection_update(updateSet)
#         print(a)
#     elif operations == 'update':
#         a.union(updateSet)
#         print(a)
#     elif operations == 'symmetric_difference_update':
#         a.symmetric_difference_update(updateSet)
#         print(a)
#     elif operations == 'difference_update':
#         a.difference_update(updateSet)
#         print(sum(a))


length = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    (p, q) = input().split()
    s2 = set(map(int, input().split()))
    if p == 'intersection_update':
        s.intersection_update(s2)
    elif p == 'update':
        s.update(s2)
    elif p == 'symmetric_difference_update':
        s.symmetric_difference_update(s2)
    elif p == 'difference_update':
        s.difference_update(s2)
print(sum(s))
a,b=int(input()),map(int, input().split())
c,d=int(input()),map(int, input().split())

m_ls=set(b)
n_ls=set(d)

symmetric_difference=m_ls.symmetric_difference(n_ls)
symmetric_difference=sorted(symmetric_difference)

for x in symmetric_difference:
    print(x)

'''
m_ls=set(m_ls)
n_ls=set(n_ls)

symmetric_difference=m_ls.symmetric_difference(n_ls)

for x in symmetric_difference:
    print(x)
'''
# m_ls=[set(input().split()) for _ in range(4)]
# n_ls=[set(input().split()) for _ in range(4)]
#
# n = int(input())
# for i in range(n):
#     n_ls=list(map(int, input().split()))

# print(a,[i for i in b])
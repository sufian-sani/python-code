
s = 'AABCAAADA'
k = 3

size=len(s)
factor=size//k

for i in range(factor):
    sq=s[k*i:(i+1)*k]

    sub=''

    for c in sq:
        if c not in sub:
            sub+=c
    print(sub)

'''
s = input()
k = int(input())
num_subsegments = int(len(s) / k)

for index in range(num_subsegments):
    # Subsegment string
    t = s[index * k: (index + 1) * k]

    # Subsequence string having distinct characters
    u = ""

    # If a character is not already in 'u', append
    for c in t:
        if c not in u:
            u += c

    # Print final converted string
    print(u)
'''
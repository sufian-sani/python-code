str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'

s1=set(str1)
s2=set(str2)

# u_set= s1 & s2
u_set= s1.intersection(s2)

count=len(u_set)
print(count)

'''
str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'
c,j=0,0

for i in str1:
    if str2.find(i) >= 0 and j == str1.find(i):
        c += 1
    j += 1
print(c)
'''
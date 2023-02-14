import collections
str1 = 'thequickbrownfoxjumpsoverthelazydog'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d,key=d.get, reverse=True):
    if d[c] > 1:
        print(c, d[c])

# for c in sorted(d, key=d.get):
#     if d[c] > 1:
#         print('%s %d' % (c, d[c]))

# str = 'thequickbrownfoxjumpsoverthelazydog'
# count=0
# ls=list(set(str))
#
# for i in range(len(str)):
#     for j in str:
#         if str[i]==j:
#             count+=1
#         else:
#             pass
#     if str[i] in ls:
#         if count>1:
#             print(str[i],count)
#     count=0


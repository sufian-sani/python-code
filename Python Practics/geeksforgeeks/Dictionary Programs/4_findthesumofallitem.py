d = {'a': 100, 'b':200, 'c':300}
sum=0
for i in d.values():
    sum=sum+i

print(sum)
'''
d = {'a': 100, 'b':200, 'c':300}
sum=0
for i in d:
    sum=sum+d[i]

print(sum)
'''
arr = [ 100, 10, 5, 25, 35, 14 ]
n=11

lens = len(arr)
index=1
for i in arr:
    index=index*i

val = index%n
print(val)
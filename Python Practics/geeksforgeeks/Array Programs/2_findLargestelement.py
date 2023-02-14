arr = [12,3,4,15,266,36]

l=len(arr)

max = arr[0]

for i in range(1,l):
    if arr[i]>max:
        max=arr[i]
print(max)
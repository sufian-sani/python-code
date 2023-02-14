def linear_search(arr,x):
    val=0
    for i in range(len(arr)):
        if arr[i]==x:
            return i

    return -1


arr = [2, 3, 4, 10, 40]
x = 2
result = linear_search(arr,x)

if result != -1:
    print('Element is present at index',str(result))
else:
    print('Element is not present in array')
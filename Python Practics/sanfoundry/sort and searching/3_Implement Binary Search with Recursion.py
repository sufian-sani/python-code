def binary_search(ls,k,low,high):
    if high >= low:
        mid = (low+high) // 2
        if ls[mid]>k:
            return binary_search(ls,k,low,mid-1)
        elif ls[mid]<k:
            return binary_search(ls,k,mid+1,high)
        else:
            return mid
    else:
        return False

ls = list(map(int, input().split()))
k = int(input())
l=0
u=len(ls)-1


if binary_search(ls,k,l,u):
    print('Found')
else:
    print('Not Found')


'''
def binary_search(ls, low, high, k):
    if high>=low:
        mid = (high+low) // 2
        if ls[mid] > k:
            return binary_search(ls, low, mid-1, k)
        elif ls[mid] < k:
            return binary_search(ls, mid+1, high, k)
        else:
            return mid
    else:
        return -1

# ls = list(map(int, input().split()))

ls = [ 2, 3, 4, 10, 40,41,7,60]
# k = int(input())
k = 60
size = len(ls)
high = size-1

result = binary_search(ls, 0, high, k)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
'''


def bin_search(arr,low,high,x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bin_search(arr,low,mid-1,x)
        else:
            return bin_search(arr, mid + 1, high, x)
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 3
low=0
high=len(arr)-1
result = bin_search(arr,low,high,x)

if result != -1:
    print('Element is present at index',str(result))
else:
    print('Element is not present in array')

'''
# Iterative Binary Search Function 
# It returns index of x in given array arr if present, 
# else returns -1 
def binary_search(arr, x): 
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high: 

		mid = (high + low) // 2

		# Check if x is present at mid 
		if arr[mid] < x: 
			low = mid + 1

		# If x is greater, ignore left half 
		elif arr[mid] > x: 
			high = mid - 1

		# If x is smaller, ignore right half 
		else: 
			return mid 

	# If we reach here, then the element was not present 
	return -1


# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binary_search(arr, x) 

if result != -1: 
	print("Element is present at index", str(result)) 
else: 
	print("Element is not present in array") 

'''



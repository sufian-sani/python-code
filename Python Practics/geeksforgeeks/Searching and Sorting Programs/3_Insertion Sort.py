'''
a = [16, 19, 11, 15, 10, 12, 14]

#iterating over a
for i in a:
    j = a.index(i)
    #i is not the first element
    while j>0:
        #not in order
        if a[j-1] > a[j]:
            #swap
            a[j-1],a[j] = a[j],a[j-1]
        else:
            #in order
            break
        j = j-1
print(a)
'''

# Python Learn program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j=j-1
		arr[j+1]=key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])



'''
def find_small(arr,size):
    low=0
    while size>0:
        for

arr = [12, 11, 13, 5, 6]

low=arr[0]
size = len(arr)
print(find_small(arr,size))
'''
'''
def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]
        # print(value_to_sort)
        print(list_a[i-1])

    #     while list_a[i-1] > value_to_sort and i>0:
    #         list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
    #         i = i -1
    #
    # return list_a

arr = [12, 11, 13, 5, 6]

# print(insertion_sort(arr))
insertion_sort(arr)
'''
'''
# Python Learn program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])

# This code is contributed by Mohit Kumra

'''

'''
def find_small(arr):
    for i in range(1,len(arr)):
        value=arr[i]
        low=i-1
        while i>=0:
            if value < arr[low]:
                arr[low+1] = arr[low]
                arr[low] = value
                i=i - 1
            else:
                break
        print(value)

arr = [12, 11, 13, 5, 6]
find_small(arr)
'''
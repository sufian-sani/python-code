# Min and Max in Python Learn - Hacker Rank Solution
# Python Learn 3
# Min and Max in Python Learn - Hacker Rank Solution START
import numpy

N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(storage, axis=1), axis=0))
# Min and Max in Python Learn - Hacker Rank Solution END

'''
import numpy

my_array = numpy.array([[2, 5],
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print(numpy.min(my_array, axis = 0))         #Output : [1 0]
print(numpy.min(my_array, axis = 1))         #Output : [2 3 1 0]
print(numpy.min(my_array, axis = None))      #Output : 0
print(numpy.min(my_array))                   #Output : 0
'''
'''
import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7
'''

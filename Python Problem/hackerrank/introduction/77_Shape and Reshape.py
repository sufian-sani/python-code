import numpy

n=list(map(int,input().split()))
c_array=numpy.array(n)
c_array.shape = (3, 3)

print(c_array)


'''
import numpy

my_array = numpy.array([1,2,3,4,5,6])
print(numpy.reshape(my_array,(3,2)))
'''
'''
import numpy

change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print(change_array)
'''
'''
import numpy

my__1D_array = numpy.array([1, 2, 3, 4, 5])
print(my__1D_array.shape)     #(5,) -> 1 row and 5 columns

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print(my__2D_array.shape)     #(3, 2) -> 3 rows and 2 columns
'''


import numpy
numpy.set_printoptions(sign=" ")
A=list(map(float,input().split()))
my_array = numpy.array(A)

print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))

'''
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.rint(my_array))           #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
'''
'''
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.ceil(my_array))           #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
'''
'''
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.floor(my_array))          #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
'''
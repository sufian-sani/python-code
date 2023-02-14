import numpy

N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],dtype=int)

transpose_arra=storage.transpose()
flatten_arra=storage.flatten()
print(transpose_arra)
print(flatten_arra)

'''
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print(my_array.flatten())
'''
'''
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print(numpy.transpose(my_array))
'''

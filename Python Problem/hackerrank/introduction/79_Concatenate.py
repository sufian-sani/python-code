import numpy

N, M, P = map(int, input().split())
storage1 = numpy.array([input().split() for _ in range(N)],dtype=int)
storage2 = numpy.array([input().split() for _ in range(M)],dtype=int)

print(numpy.concatenate((storage1, storage2)))

'''
import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print(numpy.concatenate((array_1, array_2), axis = 1))
'''
'''
import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print(numpy.concatenate((array_1, array_2, array_3)))
'''
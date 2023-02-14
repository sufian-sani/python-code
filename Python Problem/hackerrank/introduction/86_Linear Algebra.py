import numpy

N = int(input())
A = numpy.array([input().split() for _ in range(N)], float)
print(round(numpy.linalg.det(A),2))   #computes the determinent value of a matrix


#numpy.linalg.eig(array)   --- computes the eigen values of the matrix
#numpy.linalg.inv(array)   --- computes the inverse of a matrix
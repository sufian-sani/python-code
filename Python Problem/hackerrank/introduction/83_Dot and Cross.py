import numpy

N = int(input())
A = numpy.array([input().split() for _ in range(N)],dtype=int)
B = numpy.array([input().split() for _ in range(N)],dtype=int)

print(numpy.dot(A, B))
# print(numpy.cross(A, B))

'''
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2
'''

'''
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11
'''
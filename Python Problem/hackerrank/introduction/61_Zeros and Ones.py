'''
import numpy

# a,b,c=map(int, input().split(' '))
a,b,c= [int(x) for x in input().split()]
zero=numpy.zeros((a,b,c), dtype=numpy.int)
one=numpy.ones((a,b,c), dtype=numpy.int)

print(zero)
print(one)
'''
import numpy
N = tuple(map(int, input().split()))
print(numpy.zeros(N, int))
print(numpy.ones(N, int))
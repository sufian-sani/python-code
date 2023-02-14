'''
import numpy

# print (numpy.identity(3))

# print (numpy.eye(3, 3, k = 0))

print(numpy.identity(3))
'''
'''
import numpy

n,m=map(int, input().split())

result=numpy.eye(n, m, k = 0)

print(result)
'''

import numpy

numpy.set_printoptions(sign=' ') #get alignment correct
print(numpy.eye(*map(int, input().split())))
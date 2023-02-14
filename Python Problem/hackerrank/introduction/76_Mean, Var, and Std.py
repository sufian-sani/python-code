import numpy
# numpy.set_printoptions(sign="")
N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],dtype=int)

print(numpy.mean(storage, axis=1))
print(numpy.var(storage, axis=0))
ls_output=numpy.std(storage)
print(ls_output.round(11))

'''
import numpy

N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],int)

print(numpy.mean(storage, axis=1))
print(numpy.var(storage, axis=0))
print(numpy.std(storage, axis=None))
'''

'''
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.mean(my_array, axis = 0))        #Output : [ 2.  3.]
print(numpy.mean(my_array, axis = 1))         #Output : [ 1.5  3.5]
print(numpy.mean(my_array, axis = None))      #Output : 2.5
print(numpy.mean(my_array))                   #Output : 2.5
'''
import numpy

A = numpy.array([input().split()],dtype=int)
B = numpy.array([input().split()],dtype=int)

# print(numpy.inner(A, B))
# print(str(numpy.inner(A, B))[1:-1])
ra_g=numpy.inner(A, B)
for i in ra_g:
    print(*i,sep=", ")
print(numpy.outer(A, B))

'''
A = numpy.array([0, 1])
B = numpy.array([3, 4])

print(numpy.outer(A, B))      #Output : [[0 0]
                            #          [3 4]]
'''
'''
A = numpy.array([0, 1])
B = numpy.array([3, 4])

print(numpy.inner(A, B))      #Output : 4
'''
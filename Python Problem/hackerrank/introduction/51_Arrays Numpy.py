import numpy

ls=list(map(int,input().strip().split(' ')))
ls.reverse()

numpy_ls=numpy.array(ls,float)

print(numpy_ls)
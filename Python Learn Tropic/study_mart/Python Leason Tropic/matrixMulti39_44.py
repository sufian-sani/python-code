import numpy as np
m1 = ([1,2,3],
      [4,5,6],
      [7,3,5]
      )

m2 = ([3,4,2],
      [7,8,9],
      [3,5,9]
      )

'''
print(m1)
print(m2)
'''

# result = np.add(m1,m2)
# result = np.subtract(m1,m2)
result = np.dot(m1,m2)
print(result)
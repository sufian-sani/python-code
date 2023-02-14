'''
import math

ab=int(input())
bc=int(input())

h = math.sqrt(ab**2+bc**2)

h=h/2.0
adj=bc/2.0

print(str(int(math.degrees(math.acos(adj/h))))+'°')
'''

from math import *

ab = float(input())
bc = float(input())
print(str(int(round(degrees(atan(ab/bc)),0)))+'°')
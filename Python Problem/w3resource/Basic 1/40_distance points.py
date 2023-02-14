import math

def distance(x1,x2,y1,y2):
    x=x2-x1
    y=y2-y1
    d= math.sqrt((pow(x,2))+pow(y,2))
    return round(d,2)

x1=2
y1=2
x2=-2
y2=-3
print(distance(x1,x2,y1,y2))
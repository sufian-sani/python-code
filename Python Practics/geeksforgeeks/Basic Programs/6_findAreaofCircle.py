import math
def cal_area(radius):
    area = math.pi * pow(radius,2)
    return area

n = float(input('Input Radius: '))
m = cal_area(n)
print('Area of circle: %.2f'%m)
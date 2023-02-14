
import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius

r = int(input("Enter radius of circle: "))
obj=circle(r)
print('Area of circle:',round(obj.area(),2))
print('Perimeter of circle:',round(obj.perimeter(),2))


'''
class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def calculator_area(self):
        area=(self.height*self.base)/2
        print(area)

t1=Triangle(10,20)
t1.calculator_area()
t2=Triangle(20,30)
t2.calculator_area()
'''


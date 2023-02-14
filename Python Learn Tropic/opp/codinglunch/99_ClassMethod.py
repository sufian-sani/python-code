#Class Method

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def cal_area(self):
        print(self.width * self.height)

    @classmethod
    def square(cls,no):
        return cls(no,no)

a = Rectangle(4,5)
a.cal_area()
a = Rectangle.square(3)
a.cal_area()

a = Rectangle.square(4)
a.cal_area()
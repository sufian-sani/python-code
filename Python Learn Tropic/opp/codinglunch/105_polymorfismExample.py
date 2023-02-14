# Polymorphic with Inheritance
class A:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def nameshow(self):
        print(self.name)

    def info(self):
        print("good")

class B(A):
    def info(self):
        print('BAD')

C = A('salam','Green')
C.nameshow()
C.info()

D = B('Selim','Red')
D.nameshow()
D.info()

# Polymorphism with function and objects

class Man:
    def leg(self):
        print('has 2 legs')

class Animan:
    def leg(self):
        print('has 4 legs')

def func(obj):
    obj.leg()

a=Man()
b=Animan()

func(a)
func(b)

# Polymorphic Function
def add(x,y,z=0):
    print(x+y+z)
    
add(1,2,3)
add(1,2)
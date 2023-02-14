# method: ---->   1) class Method
#                 2) Instance Method
#                 3) Static Method

class Vehicle:
    hey = "Hello World"
    def __init__(self,name,wheel,drive): #instance method
        self.v_name = name
        self.v_wheel = wheel
        self.v_drive = drive

    def show(self): #instance method
        print( self.v_name,self.v_wheel,self.v_drive)

    @classmethod
    def seen(cls):
        print(cls.hey)

car = Vehicle("Toyota",4,"Solimoddiin")
car.show()
car.seen()
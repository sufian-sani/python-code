#Static Method

class Vehicle:
    hey = "Hello World"
    def __init__(self,name,wheel,driver):
        self.v_name = name
        self.v_wheel = wheel
        self.v_driver = driver

    def show(self):
        print(self.v_name,self.v_driver,self.hey)
    
    @classmethod
    def seen(cls):
        print(cls.hey)

    @staticmethod
    def print(i):
        print("I am static",i)


car = Vehicle("Toyota",4,"Solimoddin")
car.show()
car.seen()
car.print("dragon")

truck = Vehicle("Tata",8,"Kolimoddin")
truck.show()

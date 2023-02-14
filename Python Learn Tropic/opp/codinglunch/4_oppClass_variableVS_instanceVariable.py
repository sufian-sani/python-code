
class Vehicle:
    hey='Hello World'
    def __init__(self,name,wheel,driver):
        self.v_name=name    #instance variable
        self.v_wheel=wheel
        self.v_driver=driver

    def show(self):
        print(self.v_name,self.v_wheel, self.v_driver,self.hey)

car = Vehicle("Toyota",4,'Solimoddin')
# car.set_value()
car.show()
print(Vehicle.hey)
print((car.hey))

truck = Vehicle("Tata",8,'Kolimoddin')
truck.show()
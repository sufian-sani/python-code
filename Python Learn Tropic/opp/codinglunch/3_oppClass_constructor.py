class Vehicle:
    def __init__(self,name,wheel,driver):
        self.v_name=name
        self.v_wheel=wheel
        self.v_driver=driver

    def show(self):
        print(self.v_name,self.v_wheel, self.v_driver)

car = Vehicle("Toyota",4,'Solimoddin')
# car.set_value()
car.show()
# Vehicle.show(car)

truck = Vehicle("Tata",8,'Kolimoddin')
truck.show()
class Vehicle:
    def set_value(self,name,wheel,driver):
        self.v_name=name
        self.v_wheel=wheel
        self.v_driver=driver

    def show(self):
        print(self.v_name,self.v_wheel, self.v_driver)

car = Vehicle()
car.set_value("Toyota",4,'Solimoddin')
car.show()
# Vehicle.show(car)

truck = Vehicle()

truck.set_value("Tata",8,'Kolimoddin')
truck.show()
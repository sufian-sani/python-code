#inheritance

class Vehicle:
    def __init__(self,name):
        self.vehicle_name = name

    def name(self):
        print(self.vehicle_name)

class Car(Vehicle):
    def drive(self):
        print(self.vehicle_name,"is drive")

    # def __init__(self,name):
    #      self.car_name = name

    # def name(self):
    #     print(self.car_name)

class Truck(Vehicle):
    def wheel(self):
        print(self.vehicle_name,"--> has 8 wheel")

a = Car("Toyota")
a.name()
a.drive()

b = Truck("tata")
b.name()
b.wheel()
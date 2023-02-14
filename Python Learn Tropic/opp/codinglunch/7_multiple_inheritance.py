class Vehicle:
    def __init__(self,name):
        self.vehicle_name=name

    def cname(self):
        print(self.vehicle_name)

class Driver():
    def __init__(self,name):
        self.driver_name=name

    def dname(self):
        print(self.driver_name)

class Car(Vehicle, Driver):
    def __init__(self,cname,dname):
        Vehicle.__init__(self,cname)
        Driver.__init__(self,dname)

    def drive(self):
        print(self.vehicle_name,':is drive')

class Truck(Vehicle,Driver):
    def __init__(self,cname,dname):
        Vehicle.__init__(self,cname)
        Driver.__init__(self,dname)

    def wheel(self):
        print(self.vehicle_name,': has 8 wheel')

a=Car('Toyota','Rahim Islam')
a.cname()
a.drive()
a.dname()

b=Truck('TATA','Salam Mia')
b.cname()
b.dname()
b.wheel()
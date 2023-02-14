class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name,self.price

    def __str__(self):
        return self.name


a = Vehicle("Toyota",300)
b = Vehicle("Toyota",300)
c = Vehicle("BMW",100)

print(a.__str__())
print(a.__repr__())

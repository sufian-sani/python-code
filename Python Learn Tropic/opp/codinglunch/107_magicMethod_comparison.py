class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        print(self.name == other.name, self.price == other.price)


a = Vehicle('Toyota',300)
b = Vehicle('Toyota',300)
c = Vehicle('Tata',200)

a.__eq__(b)
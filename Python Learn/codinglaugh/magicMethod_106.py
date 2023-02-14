class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __add__(self, other,bmw):
        print("Total Price: ",self.price + other.price + bmw.price)

    # def total_price(self,obj):
        # print("Total Price: ",self.price + obj.price)

a = Vehicle("Toyota",300)
b = Vehicle("Tata",200)
c = Vehicle("BMW",100)

# a.total_price(b)

a.__add__(b,c)

# c = 10
# d = 10
# print(c.__add__(d))
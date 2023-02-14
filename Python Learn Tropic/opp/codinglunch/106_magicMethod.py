# __word__()
class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __add__(self, other,other1):
        print('Total Price: ', self.price + other.price+other1.price)


a = Vehicle('Toyota',300)
b = Vehicle('Tata',200)
c = Vehicle('Pulsar',100)

a.__add__(b,c)



# c = 10
# d = 10
# print(c.__add__(d))
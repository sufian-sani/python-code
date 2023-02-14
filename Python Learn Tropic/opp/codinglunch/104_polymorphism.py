class Man:
    def leg(self):
        print('has 2 legs')

class Animan:
    def leg(self):
        print('has 4 legs')

a=Man()
b=Animan()

for obj in (a,b):
    obj.leg()
# encapsulation--->
#             1) Pablic
#             2) Protected
#             3) Private

class Vehical:
    def __init__(self,name):
        self.name = name #public
        self._name = name #protected
        self.__name = name #private

a = Vehical("Toyta")
print("public: ",a.name)
print("protected : ",a._name)
print("private : ",a._Vehical__name)
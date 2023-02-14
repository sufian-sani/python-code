class Vehicle:
    def __init__(self,name):
        self.name = name #puplic
        self._name = name #protected
        self.__name = name #privet

a=Vehicle('Solimoddin')
print("public: ",a.name)
print("Protected: ",a._name)
print("Private: ",a._Vehicle__name)

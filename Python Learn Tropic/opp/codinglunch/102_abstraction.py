from abc import ABC,abstractmethod
class Father:
    @abstractmethod
    def do_study(ABC):
        pass

class Son(Father):
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)

    def do_study(self):
        print('Yes. Father')

a = Son('Solimuddin')
a.show()
a.do_study()
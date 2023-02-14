class A:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def nameshow(self):
        print(self.name)

    def info(self):
        print('Good')

class B(A):
    def info(self):
        print('BAD')

C = B("Salim","Red")
C.nameshow()
C.info()
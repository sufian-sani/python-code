class A:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def nameshow(self):
        print(self.name)

    def info(self):
        print("good")

class B(A):
    def info(self):
        print("BAD")

C = A("Selim","Red")
C.nameshow()
C.info()

D = B("Abul","Black")
D.nameshow()
D.info()
class A:
    def first(self):
        print('Method - A')

class B:
    def second(self):
        print('Method - B')

class C(A,B):
    def third(self):
        print('Method - C')
        super().first()
        super().second()

D = C()
D.third()
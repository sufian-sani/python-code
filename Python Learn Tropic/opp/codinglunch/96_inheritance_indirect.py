class A:
    def first(self):
        print('Method - A')

class B(A):
    def second(self):
        print('Method - B')

class C(B):
    def third(self):
        print('Method - C')

D=C()
D.first()
D.second()
D.third()

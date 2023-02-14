class cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b


a=int(input('Enter first number:'))
b=int(input('Enter second number:'))

obj=cal(a,b)
choise=1
while choise!=0:
    print('0. Exit')
    print('1. Add')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    choise=int(input('Enter choice: '))
    if choise==1:
        print('Result: ',obj.add())
    elif choise==2:
        print('Result: ', obj.sub())
    elif choise==3:
        print('Result: ', obj.mul())
    elif choise==4:
        print('Result: ', obj.div())
    elif choise==0:
        print('Exiting!')
    else:
        print("Invalid choice!!")

print()



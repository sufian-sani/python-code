def addition():
    x = float(input('Enter first number:'))
    y = float(input('Enter second number:'))
    print('Result:', round(x + y, 3))

def subtract():
    x = float(input('Enter first number:'))
    y = float(input('Enter second number:'))
    print('Result:', round(x - y, 3))

def multiply():
    x = float(input('Enter first number:'))
    y = float(input('Enter second number:'))
    print('Result:', round(x * y, 3))

def divide():
    x = float(input('Enter first number:'))
    y = float(input('Enter second number:'))
    print('Result:',round(x / y,3))

print('Select operation.')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
print('Enter choice(1/2/3/4):')
c_num=int(input('Take your choice: '))

if c_num==1:
    addition()
elif c_num==2:
    subtract()
elif c_num==3:
    multiply()
elif c_num==4:
    divide()
else:
    print('Somthing Worng')
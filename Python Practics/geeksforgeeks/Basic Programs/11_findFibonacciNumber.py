x = int(input('Enter a Number: '))
a=0
b=1
if x<0:
    print('Error')
elif x == 0:
    print(0)
elif x>0:
    for i in range(1,x):
        c=a+b
        a=b
        b=c
        if b==x:
            print('It\'s a Fibonacci Number')
            break
        elif b>x:
            print('It\'s not a Fibonacci Number')
            break



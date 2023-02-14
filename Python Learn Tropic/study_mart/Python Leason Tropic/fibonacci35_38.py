def fibo(x):
    a=0
    b=1
    for i in range(2,x):
        c=a+b
        a=b
        b=c
        print(c)

x = int(input('Enter value: '))
fibo(x)
def fibo_serise(n):
    a = 0
    b = 1
    ls = []
    if n<0:
        print('Invalid Number')
    elif n==0:
        ls.append(0)
    elif n==1:
        ls.append(0)
        ls.append(1)
    elif n==2:
        ls.append(0)
        ls.append(1)
        ls.append(1)
    else:
        ls.append(0)
        ls.append(1)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            ls.append(b)
    return ls

x = int(input('Enter Value: '))
print(fibo_serise(x))
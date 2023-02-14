def fibonacci_num(n):
    if n<0:
        print('Invalid Number')
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fibonacci_num(n-1)+fibonacci_num(n-2)

print(fibonacci_num(6))
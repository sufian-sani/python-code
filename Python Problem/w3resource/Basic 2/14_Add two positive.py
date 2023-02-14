def add_without_plus_operator(a, b):
    while b != 0:
        print('b:',b)
        data = a & b
        print('data:',data)
        a = a ^ b
        print('a',a)
        b = data << 1
    return a

a,b=map(int,input().split())
print('Result of addition:',add_without_plus_operator(a,b))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        # print(n)
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input('Take a number: '))
print(fibonacci(n))

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibonacci(n-1)+fibonacci(n-2))
#
# n=int(input('Take a number: '))
# for i in range(n):
#     print(fibonacci(i))























'''
def fibon(n):
    if n<=1:
        return n
    else:
        return fibon(n-1)+fibon(n-2)

n=int(input('Take a number:'))
for i in range(0,n+1):
    print(fibon(i),end=' ')
'''


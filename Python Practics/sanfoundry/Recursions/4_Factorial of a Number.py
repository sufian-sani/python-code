def factorial(n):
    if n <= 1:
        return n
    else:
        return n*factorial(n-1)


n=int(input('Take a number: '))
print(factorial(n))
























'''
def factorial(n):
    if n<=1:
        return 1
    else:
        return n * factorial(n - 1)


n=int(input('Take a number:'))
print(factorial(n))
'''
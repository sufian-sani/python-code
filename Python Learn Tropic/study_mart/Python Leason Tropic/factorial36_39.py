'''def factorial(x):
    initial = 1
    for i in range(1,x+1):
        initial = initial * i
    return initial

result = factorial(5)
print(result)'''

'''import math
n=5
r = math.factorial(n)
print(r)'''

def factorial(x):
    initial = 1
    while x>0:
        initial = initial * x
        print(initial)
        x=x-1
    return initial

result = factorial(5)
print(result)
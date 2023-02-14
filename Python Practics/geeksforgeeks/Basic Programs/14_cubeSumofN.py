import math

def squerMal(x):
    n=0
    for i in range(1,x+1):
        n = n+math.pow(i,3)
    print(n)

x = int(input('Enter a Number: '))
squerMal(x)
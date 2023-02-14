import math

def squerMal(x):
    n=0
    for i in range(1,x+1):
        n = n+pow(i,2)
    print(n)

x = int(input('Enter a Number: '))
squerMal(x)
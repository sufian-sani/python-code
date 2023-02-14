def collatz(n):
    while n>1:
        print(n, end=' ')
        if (n%2):
            n=3*n+1
        else:
            n=n//2
    print(1, end='')

n=int(input('Take a Number: '))
print('Sequence: ',end='')
collatz(n)
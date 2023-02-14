# Python3 program to calculate
# Last Digit of the sum of the
# Fibonacci numbers from M to N

# Calculate the sum of the first
# N Fibonacci numbers using Pisano
# period
def fib(n):
    # The first two Fibonacci numbers
    f0 = 0
    f1 = 1

    # Base case
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    else:

        # Pisano Period for % 10 is 60
        rem = n % 60

        # Checking the remainder
        if (rem == 0):
            return 0

        # The loop will range from 2 to
        # two terms after the remainder
        for i in range(2, rem + 3):
            f = (f0 + f1) % 60
            f0 = f1
            f1 = f

        s = f1 - 1
        return (s)


# Driver code
if __name__ == '__main__':
    m,n=map(int,input().split())

    final = fib(n) - fib(m - 1)

    print(final % 10)

'''
# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
'''
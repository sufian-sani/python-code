def c_prime(n,div=None):
    if div is None:
        div=n-1
    while div >= 2:
        if n%div==0:
            print('Number not prime')
            return False
        else:
            return c_prime(n,div-1)
    else:
        print('It\'s prime')
        return True

n=int(input('Take a Number: '))
c_prime(n)





























'''
def check(n,div=None):
    if div is None:
        div=n-1
    while div >= 2:
        if n%div==0:
            print('Number not prime')
            return False
        else:
            return check(n,div-1)
    else:
        print('Number is prime')
        return True

n = int(input("Enter a number: "))
check(n)
'''
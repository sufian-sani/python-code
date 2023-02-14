def gcd(n1,n2):
    if n2==0:
        print('if part',n1,n2)
        return n1
    else:
        print('else part: ',n1,n2)
        return gcd(n2,n1%n2)

n1=int(input('Take a Number1: '))
n2=int(input('Take a Number2: '))
out=gcd(n1,n2)
print(out)
























'''
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print(GCD)
'''
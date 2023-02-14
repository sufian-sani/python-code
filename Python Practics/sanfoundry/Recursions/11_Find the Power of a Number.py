def f_power(n1,n2):
    if n1==0 or n2==0:
        return 1
    return n1*f_power(n1,n2-1)

n1=int(input('Take a Number 1: '))
n2=int(input('Take a Number 2: '))
r=f_power(n1,n2)
print(r)



























'''
def process(b,e):
    if e==0:
        return b
    else:
        return b**e

b=int(input("Enter the base: "))
e=int(input("Enter the exponential: "))
print('Result:', process(b,e))
'''
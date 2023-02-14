def multi(n1,n2):
    if n1<n2:
        print('if condition:',n1,n2)
        return multi(n2,n1)
    elif n2!=0:
        print('elif condition:', n1, n2)
        return n1+multi(n1,n2-1)
    else:
        return 0

n1=int(input('Take a Number 1: '))
n2=int(input('Take a Number 2: '))
r=multi(n1,n2)
print(r)
























'''
def product(a,b):
    if(a<b):
        return product(b,a)
    elif(b!=0):
        return(a+product(a,b-1))
    else:
        return 0
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Product is: ",product(a,b))
'''
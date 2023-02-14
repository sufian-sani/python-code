def add_check(n1,n2):
    if not (isinstance(n1,int) and isinstance(n2,int)):
        raise TypeError("Inputs must be integers")
    return n1+n2

n1=8
n2=9
print(add_check(n1,n2))
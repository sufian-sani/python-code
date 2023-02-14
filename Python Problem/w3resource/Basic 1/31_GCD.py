def gcd(n1,n2):
    gdc=1
    if n1%n2==0:
        return n2
    for i in range(int(n1/2),0,-1):
        if n1%i==0 and n2%i==0:
            gdc=i
            break
    return gdc

n1=336
n2=360
print(gcd(n1,n2))


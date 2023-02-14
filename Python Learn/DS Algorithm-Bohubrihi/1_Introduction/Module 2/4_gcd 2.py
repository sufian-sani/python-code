def gcd(a,b):
    if b==0:
        return a
    r=a%b
    return gcd(b,r)


a,b=map(int,input().split())
print(gcd(a,b))
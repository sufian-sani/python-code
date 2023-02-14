lower=int(input('lower: '))
upper=int(input('upper: '))
r=0
for i in range(lower,upper+1):
    r = 0
    temp=i
    order = len(str(temp))
    while temp > 0:
        dig = temp%10
        r+=dig**order
        temp=temp//10

    if i==r:
        print(r)

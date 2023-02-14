p = float(input('Enter Main Amount: '))
t = int(input('Give your time periode: '))
r = float(input('Rate: '))

if p>0 and t>0 and r>0:
    x = p*t*r
    n=x/100
    print(n)
else:
    print('Error! Please input correct value')

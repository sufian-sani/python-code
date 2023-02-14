def compound_int(pri,time,rate):
    if p > 0 and t > 0 and r > 0:
        a = p * (pow((1 + r / 100), t))
        ci=a-p
        return ci
    else:
        print('Error! Please input correct value')

p = float(input('Enter Principle Amount: '))
t = int(input('Give your time periode: '))
r = float(input('Rate: '))

x = compound_int(p,t,r)
print('%.3f'%x)


# Amount = principle * (pow((1 + rate / 100), time))
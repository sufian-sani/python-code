lower=int(input("Upper Range: "))
upper=int(input("Lower Range: "))
divition_number=int(input("The number to be divided by: "))

for i in range(lower,upper+1):
    if i%divition_number==0:
        print(i)
    else:
        pass
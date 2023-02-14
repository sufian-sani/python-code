a = int(input("Enter Value: "))
b=a-1

for row in range(0,a):
    for col in range(0,a):
        if ((row==col) or (col==0 and row!=0) or (row==b and col!=0)):
            print("* ",end="")
        else:
            print("  ",end="")
    print()


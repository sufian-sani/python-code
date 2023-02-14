a = int(input("Enter value: "))
b=a-1
for row in range(0,a):
    for col in range(0,a):
        if (col==0 or col==b or ((row==0 or row==b) and (col>0 and col<b))):
            print("1 ",end="")
        else:
            print("0 ",end="")
    print()
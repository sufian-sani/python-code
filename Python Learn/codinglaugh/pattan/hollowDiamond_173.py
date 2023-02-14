for row in range(0,9):
    for col in range(0,9):
        if((col+row==4) or (col-row==4 and row!=0) or (row-col==4 and row!=4) or (row+col==12 and row!=4)):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
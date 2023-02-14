for row in range(0,5):
    for col in range(0,9):
        if((row+col==4) or (col-row==4 and row!=0)):
            print(row+1," ",end="")
        else:
            print("  ",end="")
    print()
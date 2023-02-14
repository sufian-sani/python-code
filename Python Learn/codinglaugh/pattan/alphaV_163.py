for row in range(0,4):
    for col in range(0,7):
        if ((col==row) or (col==4 and row==2) or (col==5 and row==1) or (col==6 and row==0)):
            print("* ",end=" ")
        else:
            print(" ",end=" ")
    print()
for row in range(0,7):
    for col in range(0,7):
        if ((col==0) or (row==0 and (col>0 and col<5)) or (row==3 and (col>0 and col<5)) or ((col==6) and (row==1 or row==2))):
            print("* ",end=" ")
        else:
            print(" ",end=" ")
    print()
# for row in range(0,5):
#     for col in range(0,13):
#         if ((row==col) or (row==3 and col==5) or (row==2 and col==6) or (row==3 and col==7) or (row==4 and col==8) or (row==3 and col==9) or (row==2 and col==10) or (row==1 and col==11) or (row==0 and col==12)):
#             print("* ",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

i=0
j=12
for row in range(0,5):
    for col in range(0,13):
        if ((row==col) or (row==3 and col==5) or (row==2 and col==6) or (row==3 and col==7)):
            print("* ",end=" ")
        elif (row==i and col==j):
            print("* ",end=" ")
            i = i+1
            j = j-1
        else:
            print(" ",end=" ")
    print()
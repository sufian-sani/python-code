# n=input("Take your height: ")
n=input("Take height: ")

ls=list(map(str,n.strip().split(".")))
ls=list(map(int,ls))

cm_feet=ls[0]*30.48
cm_inch=ls[1]*2.54

total_height=cm_feet+cm_inch

print(round(total_height,6))
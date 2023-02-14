a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element:"))
    a.append(element)

List_without_duplicate = set (a)
print(List_without_duplicate)
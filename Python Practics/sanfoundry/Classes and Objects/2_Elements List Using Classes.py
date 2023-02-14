class check():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def delete(self,b):
        return self.n.remove(b)
    def dis(self):
        return self.n

obj=check()

choise=1
while choise!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    choise=int(input("Enter choice: "))
    if choise==1:
        n=int(input("Enter number to append: "))
        obj.add(n)
        print("List: ",obj.dis())
    elif choise==2:
        n = int(input("Enter number to remove: "))
        obj.delete(n)
        print("List: ",obj.dis())
    elif choise==3:
        print("List: ",obj.dis())
    elif choise==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()



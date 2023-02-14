# f = open("codee.txt","r")
# print("1st =",f.read(10))
# # print("2st =",f.read())
# f.close()

# f = open("codee.txt","r")
# # print("1st =",f.read(10))
# print("2st =",f.read())
# f.close()

with open("codee.txt","r") as f:
    print("1st =",f.read(10))

with open("codee.txt","r") as f:
    print("2st =",f.read())

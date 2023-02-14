# + --> write and read
# f = open("codee.txt","r+")
# print(f.writable())
# print(f.readable())
# f.close()
# t -> text
# f = open("codeee.png","rb")
f = open("codee.txt","rb+")
print(f.writable())
print(f.readable())
f.close()
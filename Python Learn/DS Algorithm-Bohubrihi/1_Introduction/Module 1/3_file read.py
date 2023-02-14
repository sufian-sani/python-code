f = open("data5.txt", "r")
d=f.read()

# print(d)

var=''.join(d).split(' ')
var1=map(int,var)

ls_var=list(var1)

print(ls_var)

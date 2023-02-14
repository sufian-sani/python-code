list=[5,6,7,4,2,91,2,10]

e_ls=[]
for i in list:
    if i%2!=0:
        e_ls.append(i)
    else:
        continue

print(e_ls)
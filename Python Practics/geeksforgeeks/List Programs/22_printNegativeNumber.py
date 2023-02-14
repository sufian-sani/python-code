list=[5,6,-7,4,2,91,-2,10]

e_list=[]

for i in list:
    if i>0:
        continue
    else:
        e_list.append(i)

print(e_list)
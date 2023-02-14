name=input().split()
name_ls=[]
len_str=len(name)

for i in range(len_str,0,-1):
    name_ls.append(name[i-1])

print(' '.join(name_ls))
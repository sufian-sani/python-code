n=int(input())
ls=[]
add=0
multi=1
for i in range(1,4,1):
    ls.append([n] * i)

ls_new=[]

for i in ls:
    str1=list(map(str,i))
    str2=''.join(str1)
    ls_new.append(str2)

int_str1=list(map(int,ls_new))

for i in int_str1:
    add+=i

print(add)

# for index,i in enumerate(ls):

# ls=[8,7,9,6,4,2,3,5]
# ls=list(map(str,ls))
#
# print(''.join(ls))
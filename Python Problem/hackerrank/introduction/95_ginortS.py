str=input()

ls_lc=[]
ls_up=[]
ls_d_odd=[]
ls_other=[]

for i in str:
    if 97<=ord(i)<=123:
        ls_lc.append(i)

    elif 65<=ord(i)<=91:
        ls_up.append(i)

    elif ord(i)%2!=0:
        ls_d_odd.append(i)

    else:
        ls_other.append(i)

ls_lc=sorted(ls_lc)
ls_up=sorted(ls_up)
ls_d_odd=sorted(ls_d_odd)
ls_other=sorted(ls_other)

ls_main=ls_lc+ls_up+ls_d_odd+ls_other

# for row in ls_main:
print(''.join(y for y in ls_main))
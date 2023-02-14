def swap_case(s):
    str1=''
    str=[]
    for i in s:
        if i.islower():
            j=i.upper()
            str.append(j)
            str1=''.join(str)
        else:
            j = i.lower()
            str.append(j)
            str1 = ''.join(str)

    return str1


s = input()
print(swap_case(s))
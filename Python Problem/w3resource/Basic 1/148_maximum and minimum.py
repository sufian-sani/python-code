def max_min(ls):
    l=ls[0]
    s=ls[0]
    for num in ls:
        if num>l:
            l = num
        elif num<s:
            s = num
    return l,s

ls=[0, 10, 15, 40, -5, 42, 17, 28, 75]
print(max_min(ls))
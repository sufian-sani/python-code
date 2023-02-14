def vowel(str):
    vow='aeiou'
    count=0
    vow_ls=[]
    str=str.lower()
    for i in str:
        if i in vow:
            count+=1
            vow_ls.append(i)
    print(count)
    print(vow_ls)

vowel('w3resource')
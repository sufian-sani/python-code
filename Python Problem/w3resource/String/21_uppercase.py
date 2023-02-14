def to_uppercase(str):
    c_check=len(str[:4])
    count=0
    for i in range(c_check):
        if str[i]>='A' and str[i]<='Z':
            count+=1
    if count>=2:
        str=str.upper()
    return str


print(to_uppercase('Python'))
print(to_uppercase('PyThon'))
def odd_values_string(str):
    str1=""
    for i in range(len(str)):
        if i%2!=0:
            pass
        else:
            str1+=str[i]
    return str1


print(odd_values_string('abcdef'))
print(odd_values_string('python'))
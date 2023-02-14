def sum_digits_string(str1):
    int_ls=[]
    for i in str1:
        if i.isdigit() == True:
            int_ls.append(int(i))

    return sum(int_ls)

print(sum_digits_string("123abcd45"))
print(sum_digits_string("abcd1234"))
def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]


print(capitalize_first_last_letters("python exercises practice solution"))
print(capitalize_first_last_letters("w3resource"))

'''
def capitalize_first_last_letters(str1):
    ls_str1=list(str1.split())
    up_ls_list=[]
    for i in ls_str1:
        first_char=i[0].upper()
        last_char=i[-1].upper()
        rest_char=i[1:-1]
        final_char=first_char+rest_char+last_char
        up_ls_list.append(final_char)

    return ' '.join(up_ls_list)

print(capitalize_first_last_letters("python exercises practice solution"))
print(capitalize_first_last_letters("w3resource"))
'''
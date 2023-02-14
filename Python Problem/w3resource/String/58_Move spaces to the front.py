def move_Spaces_front(str1):
    noSpaces_char=[ch for ch in str1 if ch!=' ']
    modified_str=''.join(noSpaces_char)
    len_defer=len(str1)-len(modified_str)
    str_space=' '*len_defer
    result=''.join(str_space+modified_str)
    return result


print(move_Spaces_front("w3resource .  com  "))
print(move_Spaces_front("   w3resource.com  "))
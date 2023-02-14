def chars_mix_up(str1,str2):
    c_str1=str1[:2]
    c_str2=str2[:2]
    str1=c_str2+str1[2:]
    str2=c_str1+str2[2:]
    return str1+' '+str2


print(chars_mix_up('abc', 'xyz'))
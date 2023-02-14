def insert_sting_middle(str1,str2):
    gap=len(str1)//2
    return str1[:gap]+str2+str1[gap:]


print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))
'''
person_name = ['shakin', 'abu','tamin']
person_age = [23,22,21]

# compind_twolist = list(zip(person_name,person_age))
compind_twolist = list(zip('123',person_name,person_age))
print(compind_twolist)
'''

all_info = [('1', 'shakin', 23), ('2', 'abu', 22), ('3', 'tamin', 21)]
unzip_all_info=list(zip(*all_info))
print(unzip_all_info)

serial = unzip_all_info[0]
name = unzip_all_info[1]
age = unzip_all_info[2]

print(serial)
print(name)
print(age)
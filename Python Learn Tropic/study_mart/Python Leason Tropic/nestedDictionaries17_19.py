student={1:{'Name': 'Abu', 'Age':25, 'sex': 'Male'},
        2:{'Name': 'noman', 'Age':26, 'sex': 'Male'},
        # 3:{'Name': 'siddik', 'Age':23, 'sex': 'Male'},
        4:{'Name': 'mani', 'Age':22, 'sex': 'Female'}
         }
print(student[1])
# print(student[1]['sex'])

student[3]={}
student[3]['name'] = 'sohan khan'
student[3]['age']=26
student[3]['sex']='Male'
print(student[3])
print(student)

# del student[3]['sex']
del student[3]
print(student)
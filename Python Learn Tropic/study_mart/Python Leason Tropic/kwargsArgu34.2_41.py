'''def myself(age,**other):
    print(age)
    print(other)
myself(23,name='Abu',versity='UAP',country='BD')'''

def myself(**other):
    print(other)
myself(age=23,name='Abu',versity='UAP',country='BD')
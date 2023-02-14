'''def my_rul(*num):
    result = 1
    for i in num:
        result=result*i
    print('Result is: ',result)
my_rul(2,5,6,9,5,6,9,8,7,4,55,2,1)'''

def my_rul(num1,*num):
    result = 1
    for i in num:
        result=result*i
    print('Result is: ',result)
my_rul(2,5,6,9)
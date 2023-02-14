import functools
def add_two_value(num1,num2):
    return num1+num2

list = [12,4,5,8]

result = functools.reduce(add_two_value,list)
print(result)
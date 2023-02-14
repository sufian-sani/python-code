key=[]
value=[]
element=int(input('Enter the element of: '))
print('For key')
for x in range(0,element):
    key_element=input('Enter element '+str(x+1)+':')
    key.append(key_element)
print('For value')
for x in range(0,element):
    value_element=input('Enter element '+str(x+1)+':')
    value.append(value_element)

combind=dict(zip(key,value))
print('The dictionary is:',combind)


test_str = "GeeksForGeeks"

print('The orginal string: ' +test_str)

new_str=test_str[:2]+test_str[3:]
print(new_str)
'''
test_str = "GeeksForGeeks"

print('The orginal string: ' +test_str)
new_str=''
for i in range(len(test_str)):
    if i!=2:
        new_str=new_str+test_str[i]
print('New String: ' +new_str)
'''
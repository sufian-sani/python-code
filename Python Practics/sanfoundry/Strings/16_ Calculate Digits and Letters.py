string=input('Take a String: ')
count_disit=0
for i in string:
    if i.isdigit():
        count_disit+=1
print('The number of digits is:',count_disit)
print('The number of characters is:',len(string))
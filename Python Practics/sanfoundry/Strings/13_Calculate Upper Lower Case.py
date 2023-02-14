string=input('Take a String: ')
count_upper=0
count_lower=0

for i in string:
    if i.isupper():
        count_upper+=1
    elif i.islower():
        count_lower+=1
print('The number of lowercase characters is:',count_lower)
print('The number of uppercase characters is:',count_upper)
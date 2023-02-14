string=input('Take a String: ')
count=0

for i in string:
    if i.islower():
        count+=1
print(count)
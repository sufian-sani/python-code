string=input('Take a String: ')
count=''
for i in range(len(string)):
    if i%2==0:
        count=count+string[i]

print(count)
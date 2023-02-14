string=input('Take String: ')
vowels='aeiouAEIOU'
count=0
for i in string:
    for j in vowels:
        if i==j:
            count=count+1
        else:
            continue
print(count)
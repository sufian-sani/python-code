str = "01100001"
size=len(str)
count = 0

for i in str:
    if i=='0' or i=='1':
        count+=1
    else:
        continue
if count==size:
    print('yes')
else:
    print('No')

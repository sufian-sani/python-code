str='GeeksforGeeks'

v_set=('aeiouAEIOU')
count=0
for i in str:
    if i in v_set:
       count+=1
print(count)
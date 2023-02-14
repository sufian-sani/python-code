str = "Geeks For Geeks"
k=3

str_size=len(str)

str_word=str.split(' ')

for i in str_word:
    if len(i)>k:
        print(i,end=" ")

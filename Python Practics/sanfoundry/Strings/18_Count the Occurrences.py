string=input('Take a String: ')
word=input("Enter word:")
a=[]
a=string.split(' ')
# word=word.split(' ')
count=0

for i in range(0,len(a)):
    if word==a[i]:
        count+=1

print('Count of the word is:',count)





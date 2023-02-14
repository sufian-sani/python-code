string=input('Take a String: ')
word=input("Enter word:")

if string.find(word)==-1:
    print('Substring not found in string!')
else:
    print('Substring in string!')
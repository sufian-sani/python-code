my_str = "Hello this Is an Example With cased letters"

word=[word.lower() for word in my_str.split()]

word.sort()

for i in word:
    print(i)
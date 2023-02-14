import random
import string

print('Generate a random alphabetical character: ')
print(random.choice(string.ascii_letters))

print('Generate a random alphabetical string:')
max_length = 255
str=''

for i in range(random.randint(1,max_length)):
    str+=random.choice(string.ascii_letters)
print(str)
print()
str=''
for i in range(1,10):
    str += random.choice(string.ascii_letters)

print(str)
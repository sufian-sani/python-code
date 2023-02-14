# word subtitutde
import re

a = 'This is a number 1234 5678'

p=re.sub('\d+','$',a)

print(p)
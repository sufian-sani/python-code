punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, he said ---and went."

no_pun=''

for i in my_str:
    if i not in punctuations:
        no_pun=no_pun+i
print(no_pun)
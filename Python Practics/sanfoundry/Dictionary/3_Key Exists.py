d={'A':1,'B':2,'C':3}
key=input('Enter the key:')

if key in d.keys():
    print('Key is present and value of the key is:',d[key])
else:
    print('Key isn\'t present!')

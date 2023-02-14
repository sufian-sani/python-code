d={'a': 1, 'c': 3, 'b': 2, 'd': 4}
print('Initial dictionary:',d)
key=input('Enter the key to delete:')

if key in d.keys():
    del d[key]
    print('Updated dictionary',d)
else:
    print('Key not found!')
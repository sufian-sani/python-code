str = 'a123'
# str = '123'
try:
    i = float(str)
    print('numeric')
except (ValueError, TypeError):
    print('\nNot numeric')
print()

from string import ascii_lowercase as asc_lower
string=input('Take a String: ')

if (set(asc_lower)-set(string))==set([]):
    print('The string is a pangram')
else:
    print('The string isn\'t a pangram')

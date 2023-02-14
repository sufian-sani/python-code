
string=input('Take String: ')
n=len(string)
ex=string[n-1:]+string[n-(n-1):n-1]+string[:1]
print(ex)
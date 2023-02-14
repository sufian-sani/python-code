def re_char(string,n):
    first=string[:n]
    second=string[n+1:]
    return first+second

string=input('Take String: ')
n=int(input('Enter the remove char:'))
print(re_char(string,n))

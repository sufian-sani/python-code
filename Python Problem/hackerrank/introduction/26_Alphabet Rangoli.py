'''
n = int(input())
ascii_code=ord(str(n))
char_convert=chr(ascii_code+48)
print(char_convert)
'''

'''
import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))
'''
'''
n = int(input())
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))
'''
'''
n = int(input())
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3,'-'))
for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))
'''
def print_rangoli(n):
    for i in range(n):
        s = "-".join(chr(ord('a') + n - j - 1) for j in range(i + 1))
        print((s + s[::-1][1:]).center(n * 4 - 3, '-'))
    for i in range(n - 1):
        s = "-".join(chr(ord('a') + n - j - 1) for j in range(n - i - 1))
        print((s + s[::-1][1:]).center(n * 4 - 3, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

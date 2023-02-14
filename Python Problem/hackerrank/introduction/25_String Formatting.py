'''
n = int(input())
width = len("{0:b}".format(n))
for i in range(1,n+1):
  print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
'''
'''
# String Formatting in Python Learn - Hacker Rank Solution
def print_formatted(number):
    # your code goes here
    # String Formatting in Python Learn - Hacker Rank Solution START
    l1 = len(bin(number)[2:])

    for i in range(1,number+1):
        print(str(i).rjust(l1,' '),end=" ")
        print(oct(i)[2:].rjust(l1,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1,' '),end=" ")
        print(bin(i)[2:].rjust(l1,' '),end=" ")
        print("")
    # String Formatting in Python Learn - Hacker Rank Solution END

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
'''

'''
# String Formatting in Python Learn - Hacker Rank Solution
def print_formatted(number):
    # your code goes here
    # String Formatting in Python Learn - Hacker Rank Solution START
    for i in range(1, number + 1):
        binlen = len(str(bin(number)))
        octf = oct(i).split('o')
        hexf = hex(i).split('x')
        binf = bin(i).split('b')
        print(i, octf[1], hexf[1].upper(), binf[1])
    # String Formatting in Python Learn - Hacker Rank Solution END


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
'''

# String Formatting in Python Learn - Hacker Rank Solution
# def print_formatted(number):
#     # your code goes here
#     # String Formatting in Python Learn - Hacker Rank Solution START
#     l1 = len(bin(number)[2:])
#
#     for i in range(1,number+1):
#         print(str(i).rjust(l1,' '),end=" ")
#         print(oct(i)[2:].rjust(l1,' '),end=" ")
#         print(((hex(i)[2:]).upper()).rjust(l1,' '),end=" ")
#         print(bin(i)[2:].rjust(l1,' '),end=" ")
#         print("")
    # String Formatting in Python Learn - Hacker Rank Solution END


n = int(input())
l1 = len(bin(n)[2:])
# print(bin(n)[2:])
for i in range(1,n+1):
    print(str(i).rjust(l1,' '),end=" ")
    print(oct(i)[2:].rjust(l1,' '),end=" ")
    print((hex(i)[2:].upper()).rjust(l1,' '),end=" ")
    print(bin(i)[2:].rjust(l1,' '),end=" ")
    print("")

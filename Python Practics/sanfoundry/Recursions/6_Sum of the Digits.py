ls=[]
def sum_d(n):
    if n==0:
        return 1
    dig=n%10
    ls.append(dig)
    sum_d(n//10)

n=int(input('Take a Number: '))
sum_d(n)
print(sum(ls))

# n=int(input())
# n1=n//10
# print(n1)























'''
l=[]
def sum_digit(b):
    if b==0:
        return 1
    dig=b%10
    l.append(dig)
    sum_digit(b//10)

n = int(input("Enter a number: "))
sum_digit(n)
print(sum(l))
'''
def check_num(n):
    if n < 2:
        return (n%2==0)
    return  check_num(n-2)

n=int(input('Take a number: '))
if check_num(n)==True:
    print(True)
else:
    print(False)






















'''
def check(n):
    if 0<n:
        return n%2==0
    return 0

n=int(input("Enter number:"))
if check(n)==True:
    print("Number is even!")
else:
    print('Number is odd!')
'''
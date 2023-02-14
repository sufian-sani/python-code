n=int(input('Enter a number: '))
dig=0
r=0
m_r=0
real_n=n
len=len(str(n))
# if n < 9:
#     print('you take unnecessary number')
while n > 0:
    dig=n%10
    r=dig**len
    m_r+=r
    n=n//10

if real_n==m_r:
    print('it\'s Armstrong Number')
else:
    print('it isn\'t Armstrong Number')

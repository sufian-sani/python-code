sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))

avg = (sub1+sub2+sub3+sub4+sub5)/5

if avg>=80:
    print('A+')
elif avg>=75:
    print('A')
elif avg>=70:
    print('A-')
elif avg>=65:
    print('B+')
elif avg>=60:
    print('B')
elif avg>=55:
    print('B-')
elif avg>=50:
    print('C+')
elif avg>=45:
    print('C')
elif avg>=40:
    print('D')
else:
    print('Fall')
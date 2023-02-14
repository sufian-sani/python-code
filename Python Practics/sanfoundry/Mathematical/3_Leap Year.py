year=int(input("Give The Year: "))

if(year%4==0 and year%100!=0 or year%400==0):
    print('The year is Leap')
else:
    print('The year isn\'t Leap')
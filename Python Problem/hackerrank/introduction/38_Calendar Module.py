import calendar

m, d, y=map(int,input().split())

print(calendar.day_name[calendar.weekday(y, m, d)].upper())

'''
# Python Learn code to demonstrate the working of
# calendar() function to print calendar

# importing calendar module
# for calendar operations
import calendar

# using calender to print calendar of year
# prints calendar of 2018
print("The calender of year 2018 is : ")
print(calendar.calendar(2018))
'''

'''
import calendar
yy = 2017
mm = 11

# display the calendar
print(calendar.month(yy, mm))
'''
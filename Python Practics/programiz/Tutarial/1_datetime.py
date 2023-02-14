import time

while True:
    localtime = time.localtime()
    result = time.strftime('%I:%M:%S %p',localtime)
    print(result)
    time.sleep(1)


# '''
# from datetime import datetime
# import pytz
#
# local = datetime.now()
# print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))
#
# tz_NY = pytz.timezone('America/New_York')
# datetime_NY = datetime.now(tz_NY)
#
# print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
#
# tz_London = pytz.timezone('Europe/London')
# datetime_London = datetime.now(tz_London)
# print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
# '''

'''
# Python Learn strptime() - string to datetime
from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
'''

'''
#Time duration in seconds
from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("total seconds =", t.total_seconds())
'''
'''
#Printing negative timedelta object
from datetime import timedelta

t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2

print("t3 =", t3)
print("t3 =", abs(t3))
'''
'''
#Difference between two timedelta objects
from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)
'''
'''
from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3))
print("type of t6 =", type(t6))
'''
'''
from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())
'''
'''
from datetime import datetime

#datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)
'''
'''
from datetime import time

a=time(11,40,56,569845)
print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)
'''
'''
from datetime import date

today=date.today()
print('current year',today.year)
print('current month',today.month)
print('current day',today.day)
'''
'''
#Get date from a timestamp
from datetime import date
time_stamp=date.fromtimestamp(1326244364)
print(time_stamp)
'''
'''
import datetime

d=datetime.date(2012,4,13)
print(d)
'''
'''
#We can use dir() function to get a list containing all attributes of a module.
import datetime
print(dir(datetime))
'''
'''
#current date
import datetime
date_get=datetime.date.today()
print(date_get)
'''
'''
#current date and time
import datetime

date_time=datetime.datetime.now()

print(date_time)
'''
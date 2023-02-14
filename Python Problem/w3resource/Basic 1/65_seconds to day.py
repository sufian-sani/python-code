second=int(input("Input time in seconds: "))
day=second//(24*3600)
time=second%(24*3600)
hour=time//3600
time=second%3600
minutes=time//60
time=second%60

print(f'd:h:m:s-> {day}:{hour}:{minutes}:{time} ')
# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
from datetime import datetime,timedelta

presendtdate=datetime.now()
yesterday=presendtdate-timedelta(1)
tomorrow=presendtdate+timedelta(1)

print('yesterday=',yesterday.strftime('%d-%m-%Y'))
print('Today=',presendtdate.strftime('%d-%m-%Y'))
print('Tomorrow=',tomorrow.strftime('%d-%m-%Y'))

'''
from datetime import datetime, timedelta 
  
  
# Get today's date 
presentday = datetime.now() # or presentday = datetime.today() 
  
# Get Yesterday 
yesterday = presentday - timedelta(1) 
  
# Get Tomorrow 
tomorrow = presentday + timedelta(1) 
  
  
# strftime() is to format date according to 
# the need by converting them to string 
print("Yesterday = ", yesterday.strftime('%d-%m-%Y')) 
print("Today = ", presentday.strftime('%d-%m-%Y')) 
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y')) 
'''
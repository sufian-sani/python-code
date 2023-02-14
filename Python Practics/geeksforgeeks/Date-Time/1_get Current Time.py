from datetime import*
import pytz
tz_INDIA=pytz.timezone('Asia/Dhaka')
datetime_INDIA=datetime.now(tz_INDIA)
print(datetime_INDIA.strftime('%H:%M:%S'))
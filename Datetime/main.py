import datetime
import pytz

now = datetime.datetime.now(tz=pytz.timezone("Asia/Kolkata"))

formattedtime = now.strftime("%A , %d %B")

print(formattedtime)

newdate = datetime.datetime.strptime(formattedtime, "%A , %d %B")
print(newdate)

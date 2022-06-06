import pytz
from datetime import datetime
from tzlocal import get_localzone

timeformat = "%Y-%m-%d %H:%M"
present = datetime.now().strftime(timeformat)
print("\nCurrent Time : " + present)

'''
# Shows current time in all common timezones

print("\n Converted Time\n")
for zone in pytz.common_timezones:
    dt = datetime.now(timezone(zone)).strftime(timeformat)
    print (zone+ ":" + dt)
'''
tz1 = get_localzone()
print("Current Zone : ", tz1)
dt = input("\nEnter the time you want to convert in YYYY-MM-DD HH:MM ")
dt = datetime.strptime(dt, timeformat)
print("Convert {} Time: {} ".format(tz1, dt))
print("\n Converted Time\n")

# Coverts entered local date and time to all common timezones
for zone in pytz.common_timezones:
    tz2 = pytz.timezone(zone)
    dt = dt.astimezone(tz2)
    print("{} : {}" .format(zone, dt))
import pytz
from datetime import datetime
print(len(pytz.all_timezones))
print(len(pytz.common_timezones))
t=[]
for i in pytz.all_timezones:
    for j in pytz.common_timezones:
        if i == j:
            t.append(i)

print(len(t))
print(pytz.country_names["IT"])
for i in pytz.country_names.items():
    print(i)

print(pytz.country_timezones["RU"])
t=pytz.timezone("Asia/Tomsk")
print(datetime.now(t))


print(t)

import calendar
for i in calendar.day_name:
    print(i)

print(calendar.day_name[3])
for j in calendar.month_name:
    print(j)


print(calendar.month(2022,1))
print(calendar.weekday(2022,1,4))
print(calendar.leapdays(2020,2030))
cal= calendar.Calendar(firstweekday=3)
for ij in cal.itermonthdates(2021,12):
    print(ij)
import calendar
wdl = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(calendar.TextCalendar(firstweekday=6).formatyear(2015))
w = calendar.weekday(2015,8,5)
print(wdl[w])


# 08 05 2015

# import calendar
# tc= calendar.TextCalendar(firstweekday=0)
# print(tc.formatyear(2016, 3))
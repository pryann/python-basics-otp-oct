from datetime import date, datetime, time, timezone

print(datetime.now(timezone.utc))
print(datetime(2020, 11, 11, 11, 11, 11, 11, timezone.utc))
# https://docs.python.org/3.14/library/datetime.html
print(date(2020, 11, 11).strftime("%Y %B %d."))
print(date(2020, 11, 11).isoformat())
print(date(2020, 11, 11) - date(2020, 10, 10))

d = date(2020, 10, 10)
t = time(11, 11, 11, 111111)
print(datetime.combine(d, t))

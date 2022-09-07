from datetime import date

bm = int(input("You : Enter month born(1-12) : "))
bd = int(input("You : Enter day born(1-31) : "))
by = int(input("You : Enter year born(4-digit) : "))

m = int(input("Today : Enter month (1-12) : "))
d = int(input("Today : Enter day (1-31) : "))
y = int(input("Today : Enter year (4-digit) : "))

x = date(by,bm,bd)
y = date(y,m,d)
result = (y-x).days

print("Number of days you lived : ",result)


# 오늘 날짜 자동인식하게 만들면?

from datetime import datetime
from datetime import date

bm = int(input("You : Enter month born(1-12) : "))
bd = int(input("You : Enter day born(1-31) : "))
by = int(input("You : Enter year born(4-digit) : "))

now = datetime.now()
m = now.month
d = now.day
y = now.year

x = date(by,bm,bd)
y = date(y,m,d)
result = (y-x).days

print("Number of days you lived : ",result)

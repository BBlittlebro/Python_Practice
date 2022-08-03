# Datetime - date
from datetime import date
halloween = date(2022, 10, 31)
print(halloween)
print(halloween.year)
print(halloween.month)
print(halloween.day)
print(halloween.isoformat())
print(date.today())

#####################################
# timedelta (y/m/d)
print()
from datetime import timedelta
one_day = timedelta(days=1)
now = date.today()
tomorrow = now + one_day
print(tomorrow)
print(now - 5*one_day)      	    # 範圍從 1\1\1 ~ 9999\12\31

#####################################
# Datetime - time (h/m/s/ms)
print()
from datetime import time
noon = time(12, 0, 0)
print(noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)

#####################################
# Datetime - datetime (y/m/d/h/m/s/ms)
print()
from datetime import datetime
some_day = datetime(2022, 1, 2, 3, 4, 5, 6)
print(some_day)
print(some_day.isoformat())         # T 來分隔日期與小時
print(datetime.now())

#####################################
# 把 date, time 物件合併成 datetime
print()
from datetime import date, time, datetime
play_time = time(19, 30)
this_day = date.today()
play_time_today = datetime.combine(this_day, play_time)
print(play_time_today)

# 也可以用函式取得 date / time
print(play_time_today.date())
print(play_time_today.time())

#####################################
# time
import time
now = time.time()       # 1970/1/1
print(now)
print(time.ctime(now))

# localtime() => 系統時區, gmtime() => UTC
print(time.localtime(now))
print(time.gmtime(now))

now = time.localtime()
print(now)          # 省略引數，使用目前時間
print(list(now[x] for x in range(9)))

tm = time.mktime(now)   # 轉換回 epoch
print(tm)           # 毫秒在 localtime() 沒有被保存
#####################################

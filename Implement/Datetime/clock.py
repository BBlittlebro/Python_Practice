# Datetime - date
from datetime import date
from threading import local
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
# strftime() 轉成字串
# strptime() 轉回tuple
print()
import time
fmt = "It's %A, %Y, %B %d, local time %I:%M:%S %p"
t = time.localtime()
print(time.strftime(fmt, t))

#####################################
# 根據語言環境改變
print()
import locale
from datetime import date
halloween = date(2022, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is']:
    locale.setlocale(locale.LC_TIME, lang_country)
    print(halloween.strftime('%A, %B %d'))

# 查看 lang_country
names = locale.locale_alias.keys()
good_names = [name for name in names if len(name) == 5 and name[2] == '_']
print(good_names[:10])

#####################################
# 13.1
print()
from datetime import date
now = date.today()
print(now, type(now))
print(now.isoformat(), type(now.isoformat()))

# 13.3
print()
now_str = now.isoformat()
fmt = "%Y-%m-%d"                    # 要跟 str 格式一模一樣
print(datetime.strptime(now_str, fmt))

# 13.4
print()
my_birthday = date(1999, 10, 1)
print(my_birthday)

# 13.5
print()
print(my_birthday.weekday())        # Monday == 0
print(my_birthday.isoweekday())     # Monday == 1

# 13.6
print()
from datetime import timedelta
party_day = my_birthday + timedelta(days=10000)
print(party_day)
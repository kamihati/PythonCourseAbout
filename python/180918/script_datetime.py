# coding=utf8

import datetime

# 获取当前时间
now = datetime.datetime.now()
print(now)
print(type(now))
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

# "2018-3-3 20:33:33"

# 格式化时间。使用datetime.datetime
# 传入的参数依次为年。月。日。时。分。秒。微秒
# 日期缺少的部分会被设为为0
# 传入的参数必须为正整数 int
# 年:必须为大于0的整数.且小于10000
# 月:必须1到12之内的整数
# 日:必须为1到31之内的整数。闰年2月最多为29天。平年2月最多为28天。其它每月按照每月规则为30天或31天
# 时:必须为0到23之内的整数
# 分:必须为0到59之内的整数
# 秒:必须为0到59之内的整数
dt = datetime.datetime(2018, 9, 8, 18, 59, 59, 333)
print(dt)

dt = datetime.datetime(2018, 9, 8, 18)
print(dt)

dt = datetime.datetime(2018, 9, 8, 18)
print(dt)

dt = datetime.datetime(1, 1, 2, 22, 0, 59)
print(dt)

dt = datetime.datetime(2000, 4, 30, 8, 8, 8)
print(dt)

# 基础事件格式化方式演示
def format_date(*args):
    if len(args) == 3:
        return datetime.datetime(args[0], args[1], args[2])

print(format_date(2018, 9, 28))


"""
日期格式化为指定格式的字符串
使用datetime.strftime方法
日期格式化占位符定义如下
年: %Y 代表四位的年份, %y代表年份后两位
月: %m 代表月份
日: %d 代表日。  %D代表时间的日期部分
时: %H 代表 日期中的小时数
分: %M 代表 分钟
秒：%S 代表秒部分
"""
from datetime import datetime
str_now = "2018-9-18 14:22:33"
print(datetime.now())
now = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
print(type(now))
print(now)
now = datetime.strftime(datetime.now(), "%Y年%m月%日 %H:%M:%S")
print(now)
print(datetime.strftime(datetime.now(), '%D'))
print(datetime.strftime(datetime.now(), "%y年%m月%d日 %H:%M:%S"))

print(datetime.strftime(datetime.now(), "%y年%m月%d日 %H:%M:%S"))
print(datetime.strftime(datetime.now(), "%Y_%m_%d %H_%M_%S"))



"""
字符串转为日期
使用datetime.strptime方法吧字符串转为日期
第一个参数为日期字符串。第二个参数为与日期字符串对应的格式描述
"""
from datetime import datetime
str_now = "2018-9-18 14:22:33"
now = datetime.strptime(str_now, "%Y-%m-%d %H:%M:%S")
print(now)
print(type(now))

str_now = "2018_9_18 14_22_33"
now = datetime.strptime(str_now, "%Y_%m_%d %H_%M_%S")
print(now)
print(type(now))


"""
日期的计算
"""
from datetime import datetime, timedelta
now = datetime.now()
print(now)
# 时间增加10小时
new_date = now + timedelta(hours=10)
print(new_date)
# 时间减少10小时
new_date = now + timedelta(hours=-10)
print(new_date)
new_date = now - timedelta(hours=10)
print(new_date)

# 时间减少一天
new_date = now - timedelta(hours=24)
print(new_date)
new_date = now - timedelta(days=1)
print(new_date)

# 时间增加2天。12小时
new_date = now + timedelta(hours=60)
print(new_date)
new_date = now + timedelta(days=2, hours=12)
print(new_date)
new_date = now + timedelta(days=2.5)
print(new_date)



"""
时间戳（unix时间戳)
把时间转为时间戳需要使用到time.mktime方法
python时间戳会忽略毫秒微妙部分
"""

print(48 * 365 * 24 * 60 * 60 + 9 * 30 * 24 * 60 * 60)

import datetime
import time
now = datetime.datetime.now()
print(now)
print(now.timetuple())
# 时间转为时间戳
timestamp = time.mktime(now.timetuple())
print(timestamp)
print(type(timestamp))

# 时间戳转为时间
dt = datetime.datetime.fromtimestamp(timestamp)
print(type(dt))
print(dt)




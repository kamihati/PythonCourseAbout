# coding=utf8

"""
枚举
一组固定的值。不可被修改。但是python中并不对此做强制要求
"""

class Week(object):
    """
    简单的模仿枚举的类
    """
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7



"""
Enum
枚举类型默认对成员赋值为有序的数字。从1开始赋值
"""

from enum import Enum

week = Enum('week', ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'))
# 调用枚举值
print(week.MON.value)
print(week.SUN.value)


class L1(list):
    pass

l = L1()


"""
继承Enum的子类
建议使用unique装饰器。装饰Enum的子类。定义时会检测此类的值是否重复。若重复则会抛出异常
"""
from enum import unique

@unique
class Week(Enum):
    sun = 0
    mon = 1
    tue = 2
    wed = 3
    thu = 4
    fri = 5
    sat = 6

# 继承Enum的子类。此类变量的访问与Enum相同
print(Week.sun.value)
print(Week['sun'].value)
print(Week.wed.value)

# 对Enum的遍历
for k, v in Week.__members__.items():
    print("k=%s,v=%s" % (k, v.value))




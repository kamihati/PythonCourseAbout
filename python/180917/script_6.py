# coding=utf8

"""
metaclass
"""

list_1 = list()

print(list_1)
print(type(list_1))

class LikeList(list):
    pass

list_2 = LikeList()
print(list_2)
print(type(list_2))

# 原生的list没有find方法。index查找不存在的元素会抛出异常
list_3 = [1, 2, 3, 4]
print(list_3.index(3))


# 定义函数解决list无find方法的问题
def list_find(list_base, value):
    # if value in list_base:
    #     return list_base.index(value)
    # return -1
    return list_base.index(value) if value in list_base else -1


print(list_find(list_3, 3))
print(list_find(list_3, 10))

# AttributeError: 'list' object has no attribute 'find'
# list_3.find(3)


# metaclass（元类）是类的模板,必须继承type这个类
class ListMetaclass(type):
    # 初始化的时候除了__init__也会调用__new__这个方法
    # cls: 类对象
    # name: 类名称
    # bases: 类继承的父类集合
    # attrs: 类成员列表
    def __new__(cls, name, bases, attrs):
        # 把定义好的方法。绑定到类的属性中
        attrs['find'] = list_find
        return type.__new__(cls, name, bases, attrs)


class LikeList(list, metaclass=ListMetaclass):
    pass

list_4 = LikeList()
list_4.append(1)
list_4.append(2)
list_4.append(3)
list_4.append(4)
print(list_4)
print(list_4.index(3))
print(list_4.find(3))
print(list_4.find(10))



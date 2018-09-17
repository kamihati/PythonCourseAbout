# coding=utf8

"""
修改类实例的描述
__str__是类内的魔法方法之一。返回值为字符串。代表类实例化之后的对象被转为字符串的结果
__str__方法只能返回字符串。其它类型会导致异常
__doc__会获取类定义时写的第一个注释。在help获取类的描述时显示

# 类的其它魔法方法还有以下这些并不仅有这些
__init__
__del__
__repr__
__setitem__
__getitem__
__len__
"""

class Human(object):
    pass

print(Human)
print(Human())

class Human(object):
    """
    人类的类
    """
    # 实例被转化为字符串时。所显示的文字
    def __str__(self):
        return "我是人啊"


print("--------")
print(Human)
print('-------')
print(Human())
print(Human.__doc__)
# print(help(Human))




"""
让类可以被序列化
普通的类不可被序列化
实现了__iter__和__next__魔法方法的类。才可被用于for...in..
但不能被索引访问
"""

for i in range(3):
    print(i)

class Animal(object):
    pass


class Fib(object):
    def __init__(self, max=3):
        print("__init__ max=%s" % max)
        self.max = max
        self.a, self.b = 0, 1

    # __iter__方法会在初始化后被调用。应返回self。也就是实例本身
    def __iter__(self):
        print("__iter__  a=%s,b=%s" % (self.a, self.b))
        return self

    # __next__方法会在被遍历的时候调用。每次遍历会调用一次。
    # 直到raise StopIteration
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b

        print("__next__  a=%s, b = %s" % (self.a, self.b))
        if self.a > self.max:
            raise StopIteration
        return self.a

#
# f = Fib()
# print(f.a)
# print(f.b)

print("遍历实现了__iter__和__next__方法的类")
for x in Fib(7):
    print(x)

import collections
print(isinstance(Fib(7), collections.Iterable))

l1 = [1,2 ,3]
print(l1[0], l1[2])

fib_result = Fib(7)


"""
让可序列化的类。能被索引访问
实现了__getitem__方法的逻辑。可以让类支持按索引访问
"""

class Fib(object):
    def __init__(self, max=3):
        print("__init__ max=%s" % max)
        self.max = max
        self.a, self.b = 0, 1

    # __iter__方法会在初始化后被调用。应返回self。也就是实例本身
    def __iter__(self):
        print("__iter__  a=%s,b=%s" % (self.a, self.b))
        return self

    # __next__方法会在被遍历的时候调用。每次遍历会调用一次。
    # 直到raise StopIteration
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b

        print("__next__  a=%s, b = %s" % (self.a, self.b))
        if self.a > self.max:
            raise StopIteration
        return self.a

    def __getitem__(self, max):
        print("__getitem__  max=%s" % max)
        a, b = 1, 1
        for x in range(max):
            a, b = b, a + b
        return a

result = Fib(10)
print(list(result))
print(result[0])
print(result[3])
print(result[4])


"""
让可被序列化的类能够使用切片
"""

print(result[:3])



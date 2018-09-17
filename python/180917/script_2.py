# coding=utf8

# @property的使用

# 普通的类
class Human(object):
    pass

Human.height = 180
print(Human.height)
human = Human()
human.height = 181
print(human.height)


class Human(object):
    score = 0


Human.score = 0
Human.score = 100
Human.score = 1000

score = input("请输入分数:")
if score.isdigit():
    score = int(score)
    if score >=0 and score <= 100:

        Human = score
    else:
        print("输入的分数有误。只能为数字并且在0与100之间的范围内")


"""
通过类方法对变量赋值进行限制
"""

class Human(object):
    # 声明一个受保护的变量
    _score = 0

    def get_score(self):
        return self._score

    def set_score(self, score):
        if not type(score) == int:
            return
        if score >= 0 and score <= 100:
            self._score = score


human_1 = Human()
human_1.set_score(99)
print(human_1.get_score())
human_1.set_score(101)
print(human_1.get_score())


"""
使用属性设置与读取变量
"""

class Human(object):

    _score = 0

    # @property 装饰器可以让被装饰的实例方法可被当做变量（属性)访问
    @property
    def score(self):
        return self._score

    # @[property_name].setter 装饰器可以让实例方法变为属性的设置器。可以属性加上有效性校验等
    # [property_name] 为使用@property装饰器装饰的方法名
    @score.setter
    def score(self, value):
        if not type(value) == int:
            # raise 会抛出指定的异常和异常信息。并中断执行
            # 一般在确定异常类型的时候。主动抛出异常
            raise ValueError("您输入的值不是int")
        if value < 0 or value > 100:
            raise ValueError("您输入的分数不能小于0.不能大于100")
        self._score = value


human_1 = Human()
human_1.score = 100
print(human_1.score)
# human_1.score = 1001
# print(human_1.score)


"""
只读属性
"""
class Human(object):
    def __init__(self, age):
        self._age = age
    # 只使用@property会让属性成为只读属性
    @property
    def age(self):
        return self._age


human_1 = Human(33)
print(human_1.age)
# 此时设置这个属性会抛出异常
# human_1.age = 33


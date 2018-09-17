# coding=utf8

# 单一继承

# superclass
class A(object):
    def show(self):
        print("A has show")


# subclass
class A_1(A):
    def show(self):
        print("A_1 has show")


a = A_1()
a.show()


"""
多重继承
多重继承的成员查找规则
"""

class A(object):
    def show(self):
        print("A has show")

    def dance(self):
        print(" A  has dance")

class B(object):
    def dance(self):
        print("B has dance")


class Cc(A, B):
    def dance(self):
        print("Cc has dance")

c = Cc()
c.show()
c.dance()

# python3中。继承的顺序。可以使用子类的__mro__属性查看到。尽量不要依赖代码取判断
print(Cc.__mro__)


"""
super
# 使用super 可以在子类重写了父类的方法后调用父类的方法
"""

class A(object):
    def __init__(self):
        print("A has init")

class B(object):
    def __init__(self):
        print("B has init")


class C(A, B):
    def __init__(self):
        print("C has init")
        # 调用父类的方法
        super(C, self).__init__()
        B.__init__(self)

c = C()






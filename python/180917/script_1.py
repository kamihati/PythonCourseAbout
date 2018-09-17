# coding=utf8


"""
 动态语言可以较为自由的给类或实例绑定属性或方法
"""


# 类中没有任何变量或方法
class Book(object):
    pass

book_1 = Book()

# 类增加了一个page_num变量
Book.page_num = 0
# 类增加的变量也可被实例访问到。
# 因为实例里找不到的时候会继续到类中找
print(book_1.page_num)

book_2 = Book()

# 实例变量的改变不会影响到其他实例
book_1.page_num = 100
print(book_1.page_num, book_2.page_num)

# 实例动态增加变量不会影响到类和其他实例
book_1.current_num = 9

# 一下两句会抛出异常
# print(book_2.current_num)
# print(Book.current_num)

# 实例变量不影响类变量的定义和值
print(Book.page_num)




"""
__slots__限制动态绑定的属性名
"""

class Fish(object):
    # 类的__slots__ 变量为一个元素为字符串的元祖。
    # 在此元祖的字符串可作为动态绑定的变量名或方法名
    __slots__ = ('fresh', 'sea')

# 初始化一个实例
fish_1 = Fish()
# 实例可以动态绑定__slots__中的属性
fish_1.fresh = True
print(fish_1.fresh)
# 实例可以修改动态绑定的属性
fish_1.fresh = False
print(fish_1.fresh)
print('------------')

# 类动态绑定__slot__内的变量
Fish.sea = False
# 实例可以访问类动态绑定的变量
print(fish_1.sea)
# 实例不可以修改类动态绑定的变量。即使是__slots__内的。此时类变量为只读。下一行会报错
# fish_1.sea = True
print("-------------")

# 类可以动态绑定__slot__之外的变量
Fish.count = 100
print(Fish.count)
# 实例会在找不到属性时继续到所属类寻找
print(fish_1.count)
# 实例不可以更改类动态绑定的在__slots__之外的变量，此时变量为只读。下一行异常
# fish_1.count = 99


# 实例不能动态绑定除__slots__外的属性。提示属性不存在。下一行会报错
# fish_1.length = 10

print("---------------")


"""
__slot__仅对当前实例起作用。子类不能继承
"""


class Fish(object):
    __slots__ = ('mouth')


class Shark(Fish):
    pass

# 子类的实例可以动态绑定父类__slots__之外的变量
big_fish = Shark()
big_fish.has_leg = False
print(big_fish.has_leg)
big_fish.has_leg = True
# 类的动态绑定限制
Shark.has_eye = True
print(Shark.has_eye)
# 实例对类动态绑定变量的修改不再受__slot__限制
big_fish.has_eye = False
print(big_fish.has_eye)




"""
练习:动态绑定方法是否与动态绑定属性的表现一致
"""
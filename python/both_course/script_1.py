# coding=utf-8

# python是一门弱类型语言，变量的类型随着赋值的变化而变化，不用指定变量的类型
# 数据类型
# 字符串(str), 整数(int),浮点数(float),布尔值(bool),空值(None)


"""
字符串
1。字符串是用单引号或双引号扩起来的任意文本，
2。若字符串中有与引号相同的字符，需要使用转义符反斜杠\进行转义
3。\n表示换行，
4。字符串前加小写字母r,可以让字符串不转义
5。多行字符串可以使用三引号
6。字符串是不可变数据类型
"""
# 字符串输出
print("show me the money")
print("i'm a teacher")
# 字符串内的引号与外层引号相同需要转义
print('i\'m a teacher')
# 使用转义符和制表符
print('111\n222\n333\n444')

# 使用转义符显示反斜杠
print("aabcc\\111")
# 使用小写字母r前缀让字符串转义符不生效
print(r"aabcc\111")

# 三引号字符串输出
print("""
abc
ddd
eeeee
""")


# 字符串运算

# 字符串相加
print("abc" + "bcd")

# 重复输出
print("abc" * 2)

# 索引访问
print("abc"[1])

# 切片
print("abcdefg"[2: 4])

# 是否存在
print("a" in "abcedf")

# 查找
print("abcde".find("bc"))
print("abcde".index("bc"))


#  替换
print("abcde".replace("bc", "8888"))

# 分割
print("a,b,c,d,e".split(","))


# 字符串格式化
print("abc%szxvcsav" % 1111)
# 多个参数格式化
print("abc%s234234%s" % (1111, 2222))

# format方法
# 使用位置
print("abc{0}-{1}-{2}".format(111, 222, 333))
print("abc{0}-{1}-{0}".format(111, 222))

# 使用关键字
print("hello,{name},go to {place},ok?{name}".format(name='god', place='hell'))


# 字符编码
# 计算机只能处理二进制的01，如果要让计算机处理文本，就必须先把文本转为数字01，这种转换方式成为字符编码
# 常见字符编码
# ASCII编码：早起专门为英语系创造的编码，只有255个字符，每个字符占用内存 8位也就是1个字节。不兼容汉字
# Unicode编码：国际组织为容纳世界所有文字和符号所制定的字符编码方案，用2个字节来表示汉字；
# UTF-8编码：在Unicode基础上进行优化的编码。用1个字节表示英文字符，3个字符表示汉字。兼容ASCII编码。目前最为流行。
# GB2312: 我国早期为简体中文制定的编码，使用范围比较小；
# GBK：兼容GB2312，使用范围较小




# 字符串颜色控制(选讲)
# 仅在命令行模式下有用。
# 格式： \033[显示方式;前景色;背景色m正文\033[0m
"""
前景色 背景色 颜色
30   40   黑色
31   41   红色
32   42   绿色
33   43   黄色
34   44   蓝色
35   45   紫红色
36   46   青蓝色
37   47   白色
显示方式  意义
0        终端默认显示
1         高亮
4         下划线
5         闪烁
7         反白
8         不可见
"""

# 例子
# 开始设置[高亮;前景色黄;背景色黑;
print("\033[1;33;40m")

# 正文
print("人生如梦。一樽还酹江月")

# 取消显示设置
print("\033[0m")


"""
整数 （int)
1。python3除法结果都为浮点数
2。整数与浮点数互相运算结果为浮点数
"""

print(1 * 2)
print(2 * 3)
print(7 / 3)
# 整除
print(7 // 3)
# 取模
print(7 % 3)
# 乘方
print(2 ** 3)

# 绝对值
print(abs(-10))


"""
浮点数(float)
"""

# 四舍五入
print(round(3.12345))
# 四舍五入指定小数位
print(round(3.12345, 4))

# 舍入
import math
print(math.ceil(3.1111))
# 舍去
print(math.floor(3.555))

# 求平方根
print(math.sqrt(9))

# 圆周率 pi
print(math.pi)


"""
布尔值 bool
1. 只有True,False
2. True == 1,  False == 0
3. 大部分数据类型的空值都可转为False
"""

x = 16
print(x > 15)
# 数据对比
print(True == 1)
print(False == 0)

# 常见数据转为布尔型
print(bool(1), bool(0), bool(-1))
print(bool([]))
print(bool(()))
print(bool({}))

"""
空值 None
"""

a = None
print(a is None)
b = 1
print(b is not None)

print(a is None and b is not None)


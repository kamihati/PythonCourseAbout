# coding=utf8


"""
print
在控制台输出指定的值
"""

# 输出单个值
print("aaa")
print(1)
print(True)
print(3.32)
# 输出表达式
print(3 * 3)
print(5 % 3)
print(5 // 2)
print("abc_" * 3)


# 输出多个值
print("abc", 1, [3, 4, 5])


"""
output
接收用户输入的值。输入的所有内容都会被转为字符串(python3)
"""

# 接收输入的值
str_1 = input()
print(type(str_1))
print(str_1)

# 显示提示语，在提示语后输入值
name = input("请输入您的姓名:")
print(type(name))
print("你好，", name)




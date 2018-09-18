# coding=utf8


import pdb

"""
pdb。可以单步调试代码中的异常
"""

# 使用pdb的命令格式为
# python3 -m pdb xxx.py
# 基础命令有
# n 回车，进入下一行。执行当前行代码
# p 变量名    会显示变量当前的值
# q 退出

a = '0'
b = int(a)
pdb.set_trace()
print(10 / b)


"""
pdb.set_trace()
使用pdb.set_trace()可以加入断点。执行到指定行
执行时不需要输入 -m pdb
例如：python3 xxx.py  即会直接执行到调用pdb.set_trace之后的一行代码
"""


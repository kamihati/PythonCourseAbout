# coding=utf8

# 正则表达式在Python中的应用
# re模块

import re

"""
关于反斜杠 \
字符串中可作为转义符使用。让不能直接在字符串中出现的字符可以出现     
一般正则表达式的字符串前要跟一个r。避免字符串中对特殊字符过多的转义引起阅读障碍
"""

# 使用转义符让单引号可以出现在字符串中
a = 'abce\'eeee'
print(a)

# 反斜杠也是字符串的一部分时，需要使用转义符把反斜杠转义为正常字符
a = 'abbcc\\ddddd'
print(a)

a = r'abce\aeeee'
print(a)

print("-------------")
"""
re.compile 
用来编译正则表达式。使之后的正则匹配更有效率
只需要第一次调用时传入正则表达式。一般用于同一个正则表达式。需要大量多次匹配字符串的时候
"""
import re
p = re.compile(r'abc')

# match方法会从待匹配的字符串开始部分匹配。若开始部分匹配不上。则返回None。否则返回match对象
m = p.match("abc123")
print(type(m))
# 返回被正则匹配的字符串
print(m.string)
# 返回匹配到的内容
print(m.group())

m = p.match("abb123abc")
print(type(m))
print(m)


print('------------')
"""
re.match 
从字符串开始部分匹配。若开始部分与正则表达式不匹配。则返回None，匹配到则返回match对象
"""
import re
match_1 = re.match(r'abc', 'abc123123123132')
print(match_1)
print(match_1.group())

match_2 = re.match(r'abc', 'abdddddwerwerabc')
print(match_2)


print("------------")

"""
re.search
会在字符串中查找与正则表达式匹配的字符串，查找不到。返回None，查找到了返回match对象,
与match方法不同的地方在于search可以查找字符串中的字符
"""
import re
search_1 = re.search(r'abc', 'abc123123123223')
print(search_1)
print(search_1.group())

search_2 = re.search(r'abc', 'abasddfsdfda234234abc234234')
print(search_2)
# 返回匹配到的字符串的起始于结束索引
print(search_2.span())
print(search_2.group())
a = 'abasddfsdfda234234abc234234'
print(a)
print(a[18:21])


# 返回None的情况
search_3 = re.search(r'aasdf', 'asdasdffsdfdsdfsfd')
print(search_3)


"""
re.findall
正则表达式对大小写敏感
课后作业：查找如何让正则表达式关闭大小写敏感
"""
import re
r = re.findall(r'abc', 'abc1111abc222abc333')
print(type(r))
print(r)

r = re.findall(r'abc', 'abc1111aBc222abc333')
print(type(r))
print(r)

print('-------------')

"""
使用split分割字符串
"""

str_0 = '1,2,3,4,5'
print(str_0.split(','))

str_1 = 'a b c d      e   f  '
# 字符串的split方法可以根据指定的间隔字符分割字符串。返回一个列表
result = str_1.split(' ')
print(type(result))
print(result)

# re.split方法用于分割字符会比字符串本身split方法更为有效
result = re.split(r'\s+', str_1)
print(type(result))
print(result)



"""
re.sub
根据正则表达式替换匹配到的内容
会把待处理的字符串中匹配到的所有内容替换掉
"""
str_3 = 'abc123456abc'
# 字符串原生的replace方法会把字符串中匹配到的所有字符串替换掉
result = str_3.replace('abc', '谢瑞阳')
print(type(result))
print(str_3)
print(result)

import re
r = re.sub(r'abc', 'JJJ', '123abc456abc789abc')
print(type(r))
print(r)


"""
匹配规则组
每个正则表达式使用小括号包起来
"""
# 0371-123123123
r_str = r'^(\d{4})-(\d+)$'
wait_str = '0371-12312312321'

match_0 = re.match(r_str, wait_str)
print(match_0)
# group方法会把匹配到的部分输出出来
# group方法接收参数为索引。代表匹配到的每个部分
print(match_0.group())
print(match_0.group(0))
print(match_0.group(1))
print(match_0.group(2))


"""
贪婪匹配
python的re模块。默认为贪婪匹配。
贪婪匹配是让前面的正则表达式尽可能多的匹配字符串
"""
print('--------')
import re
r_str = r'^(\d+)(0*)'
wait_str = '102300'
result = re.match(r_str, wait_str)
print(result)
print("all=", result.group())
print("first=", result.group(1))
print("second=", result.group(2))

# 在正则表达式后增加?号会改为非贪婪匹配
# 非贪婪匹配会在保证后面的正则表达式也能匹配到值得情况下，才会匹配
r_str = r'^(\d+?)(102300)'
wait_str = '102300'
result = re.match(r_str, wait_str)
print(result)
print("all=", result.group())
print("first=", result.group(1))
print("second=", result.group(2))

# 常用正则表达式以及基础语法
# http://www.liujiangblog.com/course/python/73


# 作业呢
# 把上面网页中的常用正则表达式都测试一遍









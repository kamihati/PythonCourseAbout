# coding=utf8

"""
使用hashlib模块进行md5加密
加密流程如下
1.初始化一个md5实例
2.把要加密的字符串编码为bytes
3.使用md5实例调用实例方法update，参数为要加密的字符串编码为bytes的结果
4.md5实例的hexdigest()方法会返回加密结果
"""

import hashlib
md5 = hashlib.md5()

str_base = '谢文豪和谢瑞阳是同一姓'
md5.update(str_base.encode('utf8'))
result = md5.hexdigest()
print(type(result))
print(result)

str_base  = '123123123123123' \
            '2342342343244,23423' \
            '443234234'

# md5对过长的字符串可以分次执行update方法。结果与单次加密一个完整的字符串一致
md5 = hashlib.md5()
md5.update("aaaaaa".encode('utf8'))
md5.update('bbbbb'.encode("utf8"))
md5.update("cccc".encode('utf8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update("aaaaaabbbbbcccc".encode("utf8"))
print(md5.hexdigest())



"""
md5与salt结合使用增强密码破解难度
"""
str_base = "123456"
salt = "!@#!@#!ASDd_FAS*****234324*DF@#$@#$@#$"

md5 = hashlib.md5()
md5.update(str_base.encode('utf8'))
md5.update(salt.encode('utf8'))
result = md5.hexdigest()

# 简单的密码校验
pwd = input("请输入与您的密码:")
md5 = hashlib.md5()
md5.update((pwd + salt).encode('utf8'))
input_result = md5.hexdigest()
if input_result == result:
    print("密码正确")
else:
    print("密码错误")


"""
sha1
sha1的使用与md5接近.不做赘述
"""
import hashlib
sha1 = hashlib.sha1()
sha1.update("什么什么大冒险".encode('utf8'))
print(sha1.hexdigest())



"""
使用hmac模块进行加密时的加盐操作
"""
import hmac
wait_md5 = '谢瑞阳很开心'
salt = '谢瑞阳也就还算开心吧'
h = hmac.new(salt.encode('utf8'), wait_md5.encode('utf8'), digestmod='MD5')
print(h.hexdigest())
md5 = hashlib.md5()
md5.update(wait_md5.encode('utf8'))
print(md5.hexdigest())

h = hmac.new(salt.encode('utf8'), wait_md5.encode('utf8'), digestmod='sha1')
print(h.hexdigest())




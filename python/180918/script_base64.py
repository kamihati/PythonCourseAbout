# coding=utf-8

s = "谢瑞阳"
b = s.encode("utf8")
print(b)
b = s.encode("utf-8")
print(b)
print(b.decode("utf8"))


"""
base64
base64编码后长度会增加大概%33. 好处是编码后的内容可以在邮件正文和网页正常显示
base64加密的参数是bytes。解密的结果也是bytes
"""

s = '谢瑞阳偷吃了0个月饼'

bb = s.encode("utf-8")
print(type(bb))
print(bb)

import base64
# base64基础加密
bs64_str = base64.b64encode(bb)
print(type(bs64_str))
print(bs64_str)

# base64解密
base_str = base64.b64decode(bs64_str)
print(type(base_str))
print(base_str)

print(base_str.decode('utf8'))



"""
base64在网络中传输可能会遇到的坑
+ /
"""

bb = b'i\xb7\x1d\xfb\xef\xff'
print(bb)
print(type(bb))

print(base64.b64encode(bb))

us_str = base64.urlsafe_b64encode(bb)
print(us_str)
us_str_base = base64.urlsafe_b64decode(us_str)
print(us_str_base)


"""
关于==号。base64加密结果可能在尾部用=号补位。这时候在url中使用处理后的字符串就可能引起歧义
一般在url使用中会把尾部的等号去掉。在解密前使用=号进行补位
"""

s = '谢瑞阳偷吃了0个月饼'

bb = s.encode("utf-8")
print(type(bb))
print(bb)

import base64
# base64基础加密
bs64_str = base64.b64encode(bb)
print(type(bs64_str))
print(bs64_str)







bs_index = str(bs64_str).rfind("==")
print(str(bs64_str)[:bs_index])
print(str(bs64_str[:-2]))



















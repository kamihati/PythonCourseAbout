# codingt=uf8

"""
stringIO
主要用于在内存中存储数据与读取数据
"""

from io import StringIO

sio = StringIO()

sio.write("xxxx")
list_1 =['1,1111', '23423424343', '234234234\n', '234234']
sio.writelines(list_1)

print(sio.getvalue())

print('---------------------------')
sio = StringIO("xxxxxxxx\nyyyyyy\nzzzzzz")
while True:
    s = sio.readline()
    if not s:
        break
    print(s)

"""
BytesIO
"""
print("=====================")
from io import BytesIO

wait_save = "谢文豪喜欢喜欢学习\n但是有点不真实\n所以他还是有点喜欢学习的"

b_wait_save = wait_save.encode("utf8")

bio = BytesIO()
bio.write(b_wait_save)
b_text = bio.getvalue()
print(b_text)
print(b_text.decode("utf8"))

bio = BytesIO()
bio.write(b_wait_save)

print("==============")
# bytesIO的内容需要使用read()读出后转码为原文使用
# 下方代码无输出
while True:
    s = bio.readline()
    if not s:
        break
    print(s)
print("=========")



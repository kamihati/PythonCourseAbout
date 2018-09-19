# coding=utf8


"""
路径
1.绝对路径
/Users/shusheng/study/0918/xxx.xx
是根目录到当前目录或文件的完整路径。可以直接用来读取文件或文件夹内容

2.相对路径
是相对于当前所在目录的路径。一般不能直接使用相对路径读取文件
"""



"""
文本文件读写
open方法打开指定路径的文件。路径尽量为绝对路径，避免因为切换执行目录导致的路径错误
读取模式:
r: 只读

打开文件后(open) 。读取文件完毕之后都要执行文件实例的close()方法关闭文件。否则可能出现不可预料的异常
"""
f_1 = open("/Users/shusheng/study/0919/readme.txt", 'r')
# read()方法能读取出文件中所有的内容
print(f_1.read())
f_1.close()

f_1 = open("/Users/shusheng/study/0919/readme.txt", 'r')
# readline()方法能读取出文件中一行的内容。每次调用读取出下一行内容
print(f_1.readline())
print(f_1.readline())
print(f_1.readline())
print(f_1.readline())
print(f_1.readline())
print(f_1.readline())
print(f_1.readline())
print(f_1.readline())
print(f_1.readline())
print(f_1.readline())
print(f_1.readline())
print(f_1.readline())

f_1.close()


print("----------------------")
# readlines()可以读取到文件所有的行。并把每一行作为一个字符串。写入到列表中。
f_1 = open("/Users/shusheng/study/0919/readme.txt", 'r')
line_list = f_1.readlines()

for line in line_list:
    print(line)
f_1.close()
print(type(line_list))
print(line_list)
print("----------------------")


"""
with命令的使用
with代码块声明的变量在with代码块执行完毕后会自动销毁，打开的文件会自动关闭。打开的数据库连接也会
"""

with open("/Users/shusheng/study/0919/readme.txt", 'r') as f_1:
    line_list = f_1.readlines()
    for line in line_list:
        print(line)


"""
文件非常大的情况
循环调用read或readline读取部分内容
"""
print("xxxxxxxxxxxxxxxxxxxx")
with open("/Users/shusheng/study/0919/readme.txt", 'r') as f_1:
    str_1 = f_1.read(6)

    while str_1:
        print("iiiiiiiiiiiiiii")
        print(str_1)
        str_1 = f_1.read(6)

print("yyyyyyyyyyyyyyy")



"""
读取文件时指定编码，默认会使用utf8。但是文件编码确认的情况下。要指定编码。否则容易出错，
建议读取可能有非英文字符的文件时都指定编码
"""
print("sssssssssssssssss")
with open("/Users/shusheng/study/0919/readme.txt", 'r', encoding='utf8') as f_1:
    str_1 = f_1.read(6)
    print(str_1)
print("sssssssssssssss")


"""
编辑并保存指定编码的文件
使用open方法指定路径并把模式写为 w
"""
print("写文件并读取")
with open("/Users/shusheng/study/0919/test_write_file.txt", 'w', encoding='gbk') as f_1:
    # write方法可以不断的向文件里追加
    f_1.write("谢瑞阳在说话")
    f_1.write("是真的么？")
    # \n 可用来换行
    # writelines会读取一个字符串列表逐个追加到文件内容中
    list_1 = ['也许真的是真的', '也许并不是真的', '那究竟是不是真的', '是']
    for txt in list_1:
        f_1.writelines("\n" + txt)


with open("/Users/shusheng/study/0919/test_write_file.txt", 'r', encoding='gbk') as f_1:
    print(f_1.read())


"""
读取二进制文件（非文本文件)
与读取文本文件基本一样。读取模式需要改为  rb
"""
with open("/Users/shusheng/study/demo.jpg", 'rb') as img:
    str_1 = img.read()
    print(str_1)
    print("图片的长度为：", len(str_1))




"""
文件读取模式大全
r: 只读，莫名人模式，如果文件不存在就报错，存在就正常读取；
w: 只写，如果文件不存在，新建文件并写入；如果存在则先清空文件内容再写入；
a: 追加，如果文件不存在，新建文件，然后写入；如果存在，则在文件的最后追加写入；
x: 新建模式, 如果文件存在则报错，如果不存在就新建文件然后写入内容，比w模式安全；
b: 二进制模式, 例如： rb、wb、ab，以bytes类型操作文件
+: 读写模式，例如:  r+、w+、a+
"""


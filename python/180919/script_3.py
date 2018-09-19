# coding=utf8

# 对文件与目录的操作

import os

# 获取当前执行时的文件夹
base_dir = os.getcwd()

print(base_dir)

print(base_dir + "/readme.txt")

readme_path = os.path.join(base_dir, 'readme.txt')
print(readme_path)

# /shusheng/study/0919/readme.txt
# os.path.join 用于拼接合法的路径。除了根目录需要指定外。其他目录和文件名的间隔都会有系统补全
print(os.path.join('/Users', 'shusheng', 'study', '0919', 'readme.txt'))


# 创建文件夹
# linux中可能需要给python文件赋予权限
# 当目录已经存在时。创建目录的命令会抛出异常
# FileExistsError
os.mkdir(os.path.join(base_dir, "test_mkdir"))

# 删除文件夹
# 当文件夹不存在时。删除文件夹的命令会抛出异常
# FileNotFoundError
os.rmdir(os.path.join(base_dir, 'test_mkdir'))


# 文件的完整路径拆分为目录部分和文件名部分
readme_path = "/Users/xxxx/yyy/zzz/readme.txt"
result = os.path.split(readme_path)
print(result)

# 文件夹的路径拆分。会分为目录部分和最后一级目录部分
print(base_dir)
result = os.path.split(base_dir)
print(result)

# 拆分文件路径的扩展名部分与其他部分
# 会把文件扩展名作为结果的第二部分。其他路径为第一部分
result = os.path.splitext(readme_path)
print(result)
result = os.path.splitext("readme.txt")
print(result)

# 使用splitext拆分文件夹路径不会拆分出扩展名部分
result = os.path.splitext(base_dir)
print(result)


"""
扩展练习。查找os.path的相关资料进行练习
"""


# coding=utf8

import sys
import os


if __name__ == "__main__":
    print("sys模块常用方法如下：")
    # sys.argv是一个list，第0个元素为执行的脚本路径,其他元素为传入的参数
    print(u"脚本路径：", sys.argv[0])
    print("第一个参数为:", (sys.argv[1] if len(sys.argv) > 1 else '无'))
    print("第二个参数为:", (sys.argv[2] if len(sys.argv) > 2 else '无'))
    
    # 获取系统当前编码
    print("系统当前编码为：", sys.getdefaultencoding())
    
    # 获取文件系统使用编码方式，Windows下返回'mbcs'，mac下返回'utf-8'.
    print("当前文件系统编码为:", sys.getfilesystemencoding())
    
    # sys.modules.keys()可以列出所有已导入的模块。包含自动导入的模块。依环境不同结果也会不同
    print("已导入的模块有：")
    print(sys.modules.keys())
    
    # sys.hexversion 获取python解释器的版本
    print("当前python解释器版本值为：", sys.hexversion)
    
    # sys.version 获取当前python解释器的版本信息
    print("当前python解释器版本为：", sys.version)
    
    # sys.maxsize 当前环境下int类型的最大值
    print("int类型最大值为：", sys.maxsize)
    
    # sys.path 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值。
    # 注：并非系统环境变量
    print("python模块搜索路径列表:", sys.path)
    
    # sys.platform 返回操作系统平台名称
    print("当前操作系统名称：", sys.platform)
    
    # sys.exec_prefix。返回当前python解释器安装目录
    print("当前python安装目录：", sys.exec_prefix)
    
    print("os模块常用方法如下：")
    # 判断当前使用的系统。windows返回nt,linux返回posix
    print("当前系统为：", os.name)
    
    # 获取当前工作目录
    print("当前工作目录为：", os.getcwd())
    
    # 获取指定目录下的文件和文件夹名称列表
    print("指定目录下的文件和文件夹有：", os.listdir("."))
    
    # os.remove('xxxx.txt') 删除指定文件
    # os.rmdir("xxx") 删除指定目录
    
    # 判断指定路径是否为文件
    print("判断指定目录是否文件:", os.path.isfile("sysos.py"))
    
    # 判断指定路径是否为目录
    os.path.isdir("folder_name")
    
    # 判断指定路径是否存在
    os.path.exists("path")
    
    # 分割路径的目录和文件名部分返回列表
    # os.path.split("/kamihati/xxx/bbb/c.py")
    
    # 执行shell命令
    os.system("ls")
    
    # 获取文件大小。传入目录返回0
    # os.path.getsize("xxxxx.py")
    
    # 获取指定路径的绝对路径
    print("获取到的绝对路径：", os.path.abspath("."))

    # 拼接传入的路径为一个路径
    print("拼接路径的结果为：", os.path.join("/aaa/", "bbb", "c.py"))
    
    # 获取指定路径的文件名
    print("获取到的文件名是：", os.path.basename("/aaa/bbb/c.py"))
    
    # 获取指定路径的目录
    print("获取到的目录为：", os.path.dirname("/aaa/bbb/c.py"))

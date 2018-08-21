# coding=utf8

import sys


if __name__ == "__main__":
    # 位置0为执行时输入的文件路径
    print('input file path :', sys.argv[0])
    # 输入的第一个参数
    print('first:', sys.argv[1])
    # 第二个参数，更多的参数以此类推
    print('second:', sys.argv[2])

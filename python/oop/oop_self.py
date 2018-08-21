# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self):
        print("当前对象的地址是:%s" % self)


if __name__ == '__main__':
    student1 = Student()
    student2 = Student()

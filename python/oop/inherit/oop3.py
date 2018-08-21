# -*- coding:utf-8 -*-


class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tell()

    def tell(self):
        print("%s---%s" % (self.name, self.age))


class Student(People):
    def tell(self):
        print("呵呵!")


if __name__ == '__main__':
    student = Student("alex", 20)
    # 查看Student所有的父类
    print(Student.__bases__)
    
    # 查看最近的父类
    print(Student.__base__)
    
    # student既是Student类,又是People类
    print(isinstance(student, Student))
    print(isinstance(student, People))

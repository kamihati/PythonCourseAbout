# -*- coding:utf-8 -*-


class People:
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

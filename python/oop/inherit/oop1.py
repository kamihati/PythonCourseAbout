# -*- coding:utf-8 -*-


class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        print("%s-%s-%s" % (self.name, self.age, self.sex))


class Student(People):
    def __init__(self, name, age, sex, salary):
        # self.name = name
        # self.age = age
        # self.sex = sex
        People.__init__(self, name, age, sex)
        self.salary = salary

    def tell(self):
        print("%s是最棒的!" % self.name)


if __name__ == '__main__':
    student = Student("alex", 20, "man", 2000)
    student.tell()

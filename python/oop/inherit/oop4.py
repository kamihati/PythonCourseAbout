# coding=utf8
import abc


class File(object):
    
    # 标记为抽象方法。子类必须重写此方法。
    @abc.abstractmethod
    def read(self):
        print('i am base abstract method')
    
    # 抽象类中可以有普通方法，子类不需重写此方法
    def write(self):
        print("i am base normal method")


class B(File):
    # 重写父类的抽象方法。如果写pass,也是可以的,此时子类将会覆盖掉父类
    def read(self):
        print('i am override son method')


if __name__ == '__main__':
    bb = B()
    bb.read()
    bb.write()

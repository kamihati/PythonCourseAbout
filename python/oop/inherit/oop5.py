#!/usr/bin/python
# -*- coding:utf-8 -*-


class A(object):
    def fun(self):
        print("aaaa")


class B(A):
    def fun(self):
        print("bbbb")


class C(object):
    def fun(self):
        print("cccc")


class D(C):
    def fun(self):
        print("dddd")


class F(B, D):
    def fun(self):
        print("ffff")


if __name__ == '__main__':
    print(F.mro())
    # F==>B==>A==>D==>C===>Object
    ff = F()
    ff.fun()

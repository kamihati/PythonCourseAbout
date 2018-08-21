#!/usr/bin/python
# -*- coding:utf-8 -*-


class Foo(object):
    def test(self):
        print("from foo")


class Bar(Foo):
    def test(self):
        # Foo.test(self)
        super().test()
        print("bar")


if __name__ == '__main__':
    bb = Bar()
    bb.test()

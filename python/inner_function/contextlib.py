# coding=utf8

from datetime import datetime


class TestWith(object):
    def __init__(self, now):
        self.time = now

    def __enter__(self):
        print("start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("error")
        else:
            print('end')

    def go(self):
        print('go go.fire in the hole,', self.time)


if __name__ == "__main__":
    with TestWith(datetime.now()) as tw:
        tw.go()

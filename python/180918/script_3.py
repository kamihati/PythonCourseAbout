# coding=utf8

class Fish(object):
    def __init__(self, name):
        self.name = name
        self.length = 0

    def get_name(self):
        return "fish name is %s" % self.name

    def set_length(self, length):
        if type(length) != int:
            self.length = 0
        else:
            self.length = length

    def get_length(self):
        return self.length * 1000




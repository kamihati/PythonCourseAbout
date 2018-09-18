# coding=utf8

import unittest
import time
from script_3 import Fish


# 测试类必须继承unittest.TestCase
class TestFish(unittest.TestCase):

    def setUp(self):
        """
        在每个测试方法前会自动执行。一般用于测试数据的初始化
        :return:
        """
        self.fish = Fish("shark")

    def tearDown(self):
        """
        在每隔测试方法后自动执行。一般用于清理测试数据
        :return:
        """
        pass


    # 测试方法必须以test_开头。否则不会被测试程序执行
    def test_init(self):
        """
        测试Fish类的__init__方法
        :return:
        """
        print("test_init_ begin")
        fish = Fish("shark")
        assert fish.name == "shark"
        assert fish.length == 0

        fish = Fish("")
        assert fish.name == ""
        assert fish.length == 0
        print("test_init_finish")

    def test_get_name(self):
        """
        测试Fish类的get_name方法
        :return:
        """
        print("test_get_name begin")
        # fish = Fish("shark")
        fish_name = self.fish.get_name()
        assert type(fish_name) == str
        assert fish_name.find(self.fish.name) != -1
        assert fish_name == "fish name is %s" % self.fish.name
        print("test_get_name finish")

    def test_set_length(self):
        """
        测试Fish类的set_length方法
        :return:
        """
        fish = Fish("shark")
        fish.set_length(10)
        assert type(fish.length) == int
        assert fish.length == 10

        fish.set_length("333")
        assert type(fish.length) == int
        assert fish.length == 0

    def test_get_length(self):
        fish = Fish("shark")
        fish.set_length(30)
        length = fish.get_length()
        assert length == fish.length * 1000
        assert length == 30 * 1000


if __name__ == '__main__':
    unittest.main()

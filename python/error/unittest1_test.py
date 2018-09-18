# coding=utf8

# 单元测试需要导入unittest模块
import unittest

from unittest1 import Dict


# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
class TestDict(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    def test_init(self):
        d = Dict(a=1, b='test')
        # 断言结果与1相等
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        # 断言结果为True
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        # 断言会抛出异常KeyError
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        # 断言会抛出AttributeError
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == "__main__":
    unittest.main()


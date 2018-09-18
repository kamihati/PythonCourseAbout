# coding=utf8

"""
使用print调试时最简单也最直接的方式。但是当代码非常多的时候使用print会导致非常繁琐
"""

def TestPrint(num):
    print(num)
    num += 1
    print(num)
    num *= 2
    print(num)
    num **= 3
    print(num)
    num -= 1
    return num

print(TestPrint(99))


"""
断言 assert
"""
# 断言异常 AssertionError

def TestPrint(num):
    # 断言条件为True时。不会触发断言异常。否则抛出断言异常与描述
    # assert num != 0, "你扯淡呢"
    print(10 / num)


TestPrint(3)
TestPrint(5)
TestPrint(-1)
TestPrint(0)




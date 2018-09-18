# coding=utf8

"""
错误处理
"""

# 0除的异常
# ZeroDivisionError: division by zero
def read_int(num):
    try:
        print("1111111111")
        print(10 / num)
        print("2222222222")
        print("success")
        print("3333333333")
    except Exception as e:
        # 捕获到异常后。执行的语句
        print("000000000")
        print(e)
        print("fail, error_value=%s" % num)
        print("44444444444")
    finally:
        # finally语句块之内的代码总是会在异常捕获结束后执行。无论是否捕获到异常
        print("fffffffffffff")

read_int(10)
read_int(5)
read_int(3)
read_int(0)



"""
异常捕获中的else
else 语句块跟着except语句块 。当except未捕获到异常的时候生效
"""
a = 10
b = 3
try:
    print("111111")
    print(a / b)
    print('222222')
except Exception as e:
    print("333333")
    print(e)
else:
    print('44444')
    print("not error")
finally:
    print("ffffffff")


list_1 = [1 ,2, 3]
# list_1[5]

"""
捕获多个指定异常
抛出的异常会逐个判断是否与指定的异常相同。相同则触发特定的异常捕获语句
"""
try:
    print(a / 10)
    print(list_1[1])

except IndexError as index_error:
    print("索引异常:", index_error)
except ZeroDivisionError as zero_error:
    print("0除异常：", zero_error)
else:
    print("程序很ok嘛")
finally:
    print("over.......")


"""
异常抛出  raise 结合异常捕获使用。味道更佳
也有主动抛出异常中断程序的情况
"""
a = 10
b = 0

try:
    if b == 0:
        raise ZeroDivisionError("0除异常。代码有bug")
    print(a / b)
except Exception as e:
    print('error:', e)


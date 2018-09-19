# coding=utf8

"""
序列化和反序列化
"""

dict_1 = dict(a=1, b=2, c=[1, 2, 3], d=dict(x='a', y='b'))
# 使用字符串转换。结果并不可靠
print(str(dict_1))

# pickle
# 使用pickle模块可以在python内进行序列化与反序列化
import pickle
result = pickle.dumps(dict_1)
print(result)
dict_2 = pickle.loads(result)
print(dict_2)
print(type(dict_2))


# json
import json

students = []
students.append(dict(name='谢瑞阳', detail=dict(age=18, height=160, weight=200, books=['语文书', '数学书', '小人书', '英语书'])))
students.append(dict(name='杨勇浩', detail=dict(age=19, height=180, weight=130, books=['语文书', '数学书', '黄皮书', '英语书'])))

# 把students序列化为json字符串,
# json字符串可被其它语言所读取并反序列化。所以通用性非常强
json_result = json.dumps(students)
print(json_result)
print(type(json_result))

# 把json字符串反序列化为原数据
student_new = json.loads(json_result)
print(type(student_new))
print(student_new)
print(type(student_new[0]))
print(student_new[0])



"""
对复杂数据类型进行序列化和反序列化
"""

class Student(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


stu_1 = Student('谢瑞阳', 18, 160, 100)
# 如果没有实现类的序列化方法。那么类的实例不可被序列化为json字符串。
# 下面的语句会抛出异常。故注释
# print(json.dumps(stu_1))
# 对类实例的序列化需要实现一个中转方法。一般中转方法要把类的实例转为一个字典

def student2dict(stu):
    """
    把类实例转为字典。
    :param stu: 必须为Student类的实例
    :return:
    """
    return dict(name=stu.name, age=stu.age, height=stu.height, weight=stu.weight)


result = json.dumps(stu_1, default=student2dict)
print(type(result))
print(result)

# 直接使用json.loads只会反序列化为一个字典。不能成为实例
# 想要反序列化为一个实例。需要实现一个字典到实例的中转函数
"""
result = json.loads(result)
print(type(result))
print(result)
"""
def dict2student(dic):
    """
    把字典转为Student类实例
    :param dic:
    :return:
    """
    return Student(dic['name'], dic['age'], dic['height'], dic['weight'])


result = json.loads(result, object_hook=dict2student)
print(type(result))
print(result)
print(result.name)
print(result.age)


"""
特例
"""
students = []
students.append(dict(name='谢瑞阳', detail=dict(age=18, height=160, weight=200, books=['语文书', '数学书', '小人书', '英语书'])))
students.append(dict(name='杨勇浩', detail=dict(age=19, height=180, weight=130, books=['语文书', '数学书', '黄皮书', '英语书'])))

# json.dumps默认ensure_ascii为True。打印的汉字会被转码。但并不影响反序列化结果
s1 = json.dumps(students, ensure_ascii=True)
s2 = json.dumps(students, ensure_ascii=False)
print(s1)
print(s2)

s1_result = json.loads(s1)
s2_result = json.loads(s2)
print(s1_result)
print(s2_result)











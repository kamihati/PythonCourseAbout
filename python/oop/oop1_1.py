# -*- coding:utf-8 -*-

"""
1、什么叫做抽象方法?含有@abc.abstractmethod标识符的就是？
2、原样抄下来也是重写？
"""


# 定义盖伦类和瑞文类,并进行互相残血
# 对象之间的交互问题(面向对象之间互相交互)
class Garen:
    camp = "Demacia"
    
    # 定义一个对象的时候,指定了这个对象的生命值和杀伤力
    def __init__(self, nickname, life_value=200, aggre_value=100):
        self.nickname = nickname
        self.life_value = life_value
        self.aggre_value = aggre_value
        
    def attack(self, enemy):
        print('%s攻击了%s,造成了%s点伤害' % (self.nickname, enemy.nickname, self.aggre_value))
        enemy.life_value = enemy.life_value - self.aggre_value


class Riven:
    camp = "Demacia"
    
    # 定义一个对象的时候,指定了这个对象的生命值和杀伤力
    def __init__(self, nickname, life_value=100, aggre_value=200):
        self.nickname = nickname
        self.life_value = life_value
        self.aggre_value = aggre_value
        
    def attack(self, enemy):
        # python为弱类型语言
        print('%s攻击了%s,造成了%s点伤害' % (self.nickname, enemy.nickname, self.aggre_value))
        enemy.life_value = enemy.life_value - self.aggre_value


g = Garen("盖伦")
r = Riven("瑞文")
print("盖伦的生命值是%s" % g.life_value)
print("瑞文的生命值是%s" % r.life_value)

g.attack(r)
print("瑞文的生命值是%s" % r.life_value)
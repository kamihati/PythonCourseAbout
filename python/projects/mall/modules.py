# coding=utf8
import copy
import datetime
import time
import json
from config import USER_DATA_PATH, COMMODITY_TYPE
from common import write_file, read_file, make_commodity_no


class User(object):
    """
    用户类
    """
    
    # 已注册用户列表。元素为User 类的实例
    user_list = []
    
    def __init__(self, user_id, password, *, user_name, question, answer, balance=0, id=0, reg_time=None):
        """
        初始化用户
        :param user_id:  用户账号
        :param password: 密码，加密
        :param user_name: 用户姓名
        :param question: 提示问题
        :param answer:   提示问题的答案
        :param balance:  注册时不需传入
        :param id: 用户编号。注册时不需传入
        :param reg_time: 注册时间，注册时不需传入
        """
        self.user_id = user_id
        self.password = password
        self.question = question
        self.answer = answer
        
        if type(balance) != int and type(balance) != float:
            raise TypeError("User类__init__方法的balance参数类型错误。必须为int或float, 传入的是%s" % type(balance))
        if balance < 0:
            raise ValueError("User类__init__方法的balance参数必须大于或者等于0")
        
        self.balance = balance if not self.balance else (self.balance + balance)
        
        if id > 0:
            self.id = id
        else:
            # 初始化id
            pass
        if reg_time is not None:
            self.reg_time = reg_time
        else:
            self.reg_time = datetime.datetime.now()
    
    def money_in(self, money):
        """
        充值
        :param money: 充值金额。float 或int 。大于0。至少为0.01。最大为100000
        :return: 无返回
        """
        if type(money) != float and type(money) != int:
            raise TypeError("User类的实例方法 money_in的money参数类型错误。应为float或int,传入了%s" % type(money))
        if money < 0.01 or money > 100000:
            raise ValueError("User类的实例方法 money_in的money参数值错误。最小为0.01,最大为100000")
        self.balance = self.balance + money if self.balance else money
    
    def show_detail(self):
        """
        显示当前实例的用户信息
        :return:
        """
        print("账号:%s,姓名:%s,余额:%s" % (self.user_id, self.user_name, self.balance))
        
    @staticmethod
    def show_user(users, user_id=None):
        """
        print用户信息
        :param users: 用户列表，元素为用户实例
        :param user_id: 默认为None 则查看所有已注册用户。否则查看此user_id对应的用户
        :return: 无返回
        """
        local_users = copy.deepcopy(users)
        if user_id is not None:
            if type(user_id) != str:
                raise TypeError("User类的静态方法show_user的参数user_id类型有误，应为str,传入的是%s" % type(user_id))
            local_users = [item for item in local_users if item.user_id == user_id]
        for item in local_users:
            print("账号:%s,姓名:%s,余额:%s" % (item.user_id, item.user_name, item.balance))
            
            
    @staticmethod
    def get_user(users, user_id):
        """
        从指定的用户列表中查找指定账号的用户实例返回
        :param users:已注册的用户列表
        :param user_id:指定的用户id
        :return:查找到则返回该用户实例。未查到则返回None
        """
        result = [user for user in users if user.user_id == user_id]
        return result[0] if result else None
    
    @staticmethod
    def save(users):
        """
        保存序列化后的注册用户列表到文件
        :param users: 用户列表。元素为用户实例
        :return:
        """
        def user_to_dict(u):
            """
            用户实例转为字典
            :param u:
            :return:
            """
            return dict(id=u.id,
                        user_id=u.user_id,
                        password=u.password,
                        user_name=u.username,
                        question=u.question,
                        answer=u.answer,
                        balance=u.balance,
                        reg_time=time.mktime(u.reg_time.timetuple()))
        json_users = json.dump(users, default=user_to_dict)
        write_file(USER_DATA_PATH, json_users)
    
    
    @staticmethod
    def read_user_from_file():
        """
        从用户数据文件中读取到已注册的用户列表并返回
        :return: list,元素为 User类的实例
        """
        users_data = read_file(USER_DATA_PATH)
        if not users_data.strip():
            return []
        
        def dict_to_user(d):
            """
            字典转为User类实例返回
            :param d:
            :return:
            """
            return User(d['user_id'], d['password'],
                        user_name=d['user_name'],
                        question=d['question'],
                        answer=d['answer'],
                        balance=d['balance'],
                        id=d['id'],
                        reg_time=datetime.datetime.fromtimestamp(d['reg_time'])
                        )
        return json.loads(users_data, default=dict_to_user)


class Commodity(object):
    """
    商品类
    """
    
    # 所有已发布商品
    commodity_list = []
    
    def __init__(self, id, commodity_name, price, stock, commodity_type, user_id, detail, *, add_time=None, edit_time=None,
                 edit_log=None, commodity_no=""):
        """
        初始化商品类
        :param id: 唯一标识
        :param commodity_name: 商品名称
        :param price: 商品单价
        :param stock: 商品库存,int ，0-9999
        :param commodity_type: 商品类型，对应商品类型的编号
        :param user_id: str,发布人的user_id
        :param detail: str,商品描述 。不能为空
        :param addtime:  为None则为新增。自动赋值
        :param edit_time: 为None则为新增。自动赋值
        :param edit_log: 为None则为新增。赋值为空列表
        :param commodity_no: 为空字符则重新生成
        """
        self.id = id
        self.commodity_name = commodity_name
        self.price = price
        self.stock = stock
        self.commodity_type = commodity_type
        self.user_id = user_id
        self.detail = detail
        self.add_time = datetime.datetime.now if add_time is None else add_time
        self.edit_time = datetime.datetime.now if edit_time is None else edit_time
        self.edit_log = [] if edit_log is None else edit_log
        self.commodity_no = commodity_no if commodity_no else make_commodity_no(self.commodity_type)
    
    def edit(self, *, commodity_name=None, price=None, stock=None, commodity_type=None, detail=None):
        """
        编辑当前商品实例
        :param commodity_name: 商品名称
        :param price: int or float,商品单价。不能小于0.01
        :param stock:  库存，int, 0-9999
        :param commodity_type:str, 商品类型。参考config。py定义
        :param detail: str,商品详情
        :return:
        """
        log_detail = "【编辑商品】操作时间：%s" % datetime.datetime.now()
        
        if commodity_name:
            if type(commodity_name) != str:
                raise TypeError("编辑商品时传入的商品名称类型错误。应为str,传入的是%s" % type(commodity_name))
            

            log_detail += ",修改商品标题。从【%s】修改为【%s】" % (self.commodity_name, commodity_name)
            self.commodity_name = commodity_name
        
        if price:
            if type(price) != float and type(price) != int:
                raise TypeError("编辑商品时传入的价格类型有误。")
            if price < 0.01:
                raise ValueError("编辑商品时价格不能小于 0.01")
            log_detail += ",修改商品单价，从【%s】修改为【%s】" % (self.price, price)
            self.price = round(price, 2)
        
        if stock:
            if stock < 0:
                raise ValueError("编辑商品时库存不能小于0")
            log_detail += ",修改商品库存，从【%s】修改为【%s】" % (self.stock, stock)
            self.stock = int(stock)
            
        if commodity_type:
            commodity_type = commodity_type.upper()
            if commodity_type not in COMMODITY_TYPE:
                raise ValueError("编辑商品时传入的商品类型不正确。允许范围为：%s" % COMMODITY_TYPE)
            log_detail += ",修改商品类型，从【%s】修改为【%s】" % (self.commodity_type, commodity_type)
            self.commodity_type = commodity_type
        
        if detail:
            if type(detail) != str:
                raise ValueError("编辑商品时传入的商品详情类型不正确。应为str,传入的是%s" % type(detail))
            log_detail += ",修改商品详情，从【%s】修改为【%s】" % (self.detail, detail)
            self.detail = detail
            
        self.edit_log.append(log_detail)
        self.edit_time = datetime.datetime.now()
    
    
    def show_log(self):
        """
        显示当前实例的修改记录
        :return:
        """
        for log in self.edit_log:
            print(log)
        
    
    def show_detail(self):
        """
        显示当前实例的详细信息
        :return:
        """
        print("""
            商品id:%s,
            商品编号:%s,
            商品名称:%s,
            商品单价:%s元,
            商品库存:%s件,
            商品分类:%s,
            商品描述:%s,
            添加日期:%s,
            最后修改日期:%s
            """ % (
            self.id,
            self.commodity_no,
            self.commodity_name,
            self.price,
            self.stock,
            self.commodity_type,
            self.detail,
            self.add_time,
            self.edit_time
        ))
    
    @staticmethod
    def get_user_commodity(commodity_list, user_id):
        """
        在指定的商品列表中筛选出指定用户发布的商品
        :param commodity_list: list,元素为商品实例，要筛选的商品列表
        :param user_id: str,发布人user_id
        :return: list,商品实例的列表
        """
        pass
    
    @staticmethod
    def get_commodity(commodity_list, commodity_id):
        """
        在指定列表中查找到指定商品
        :param commodity_list: list, 元素为商品
        :param commodity_id: int,商品id
        :return: 查找到则返回商品实例，找不到则返回None
        """
        pass
    
    @staticmethod
    def save(commoditys):
        """
        保存商品列表到商品文件
        :return:
        """
        pass
    
    @staticmethod
    def read_commodity_from_file():
        """
        从commodity.txt文件中读取商品列表反序列化为商品实例的列表并返回
        :return: list
        """
        pass
    
        
# coding=utf8

import os
import hmac
import random
import datetime
import time
from config import COMMODITY_TYPE


def read_file(path):
    """
    读取指定路径文件的所有内容并返回
    :param path: file path
    :return:
    """
    if not os.path.isfile(path) or not os.path.exists(path):
        print("读取文件失败，指定的路径不正确或文件不存在")
        return
    
    with open(path, 'r') as f:
        return f.read()


def write_file(path, content):
    """
    向指定路径写入指定的文本内容
    :param path: 文件路径
    :param content: str,要写入文件的文本内容
    :return:
    """
    with open(path, 'w') as f:
        f.write(content)


def md5_encry(base_str, salt="&*(*123123&(*"):
    """
    使用md5加密指定的字符串
    :param base_str: 待加密的字符串
    :param salt: 盐。不传此参数则使用默认salt加密
    :return: str, 返回加密结果
    """
    md5 = hmac.new(salt.encode('utf8'), base_str.encode("utf8"), digestmod='MD5')
    return md5.hexdigest()


def make_commodity_no(commodity_type):
    """
    生成商品编号
    :param commodity_type:str, 商品类型编号
    :return: str, 返回生成的商品编号
    """
    if commodity_type.upper() not in COMMODITY_TYPE:
        raise ValueError("商品类型不合法。合法的商品类型有:%s" % str(COMMODITY_TYPE))
    
    return "%s%s%s" % (commodity_type.upper(),
                       int(time.mktime(datetime.datetime.now().timetuple())),
                       random.randint(100000, 999999))

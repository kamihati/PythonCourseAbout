# coding=utf8

import os

BASE_DIR = os.getcwd()

# 用户数据文件路径
USER_DATA_PATH = os.path.join(BASE_DIR, 'user_data.txt')
# 商品数据文件路径
COMMODITY_DATA_PATH = os.path.join(BASE_DIR, 'commodity_data.txt')

# 商品类型编号列表
COMMODITY_TYPE = ['BOK', 'FOD', 'CTH']
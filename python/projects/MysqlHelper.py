# coding=utf8
# author: kamihati 2018-8-18 16:32


import pymysql


class MysqlHelper(object):
    # 初始化mysql连接
    def __init__(self, host, port, uid, pwd, dbname):
        self.__conn = pymysql.connect(host=host, port=port, user=uid, passwd=pwd, db=dbname,
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor)

    # 返回查询结果
    def exec_query(self, sql, params=None):
        if params is None:
            params = []
        with self.__conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()

    # 执行sql不返回结果
    def exec_no_query(self, sql, params):
        if params is None:
            params = []
        with self.__conn.cursor() as cursor:
            cursor.execute(sql, params)

    def close(self):
        self.__conn.close()


if __name__ == "__main__":
    mysql = MysqlHelper('127.0.0.1', 3306,  'root', '123456', 'study')
    try:
        result = mysql.exec_query("select * from tb_course where cid=%s", 5)
        print(result)
        mysql.exec_no_query('update tb_course set cname=%s where cid=%s', ('面向对象的分析与设计', 5))
        result = mysql.exec_query("select cid,cname from tb_course where cid=%s", 5)
        print(result)
    finally:
        mysql.close()

# sqlite3 数据库文件名
sqliteDbPath = 'jd.db'
import os
import sqlite3
import config
def safe_input(val):
    return val.replace('\'', '＇')
class SqliteHelper:
    def __init__(self):
        self.dbPath = os.path.join(os.getcwd(), config.sqliteDbPath)
    def __get_connect(self):
        if not self.dbPath:
            raise (NameError, "not set dbPath")
        self.conn = sqlite3.connect(self.dbPath)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "connect db fail")
        return cur
    def exec_query(self, sql, parm=None):
        cur = self.__get_connect()
        if parm is None:
            cur.execute(sql)
        else:
            cur.execute(sql, parm)
        res_list = cur.fetchall()
        self.conn.close()
        return res_list
    def exec_no_query(self, sql, parm=None):
        cur = self.__get_connect()
        if parm is None:
            cur.execute(sql)
        else:
            cur.execute(sql, parm)
        self.conn.commit()
        self.conn.close()
    def exec_many_no_query(self, sql, parm):
        cur = self.__get_connect()
        cur.executemany(sql, parm)
        self.conn.commit()
        self.conn.close()
    def exists_table(self, table_name):
        data = self.exec_query("SELECT * FROM sqlite_master WHERE type='table' AND name='%s'" % table_name)
        return len(data) > 0
if __name__ == '__main__':
    # init sqlite connection
    conn = SqliteHelper()
    tb_name = "demo"
    if conn.exists_table(tb_name):
        conn.exec_no_query("drop table %s" % tb_name)
    # create table
    conn.exec_no_query(
        "CREATE TABLE %s(cid integer primary key not null," % tb_name +
        "root_name varchar(50),second_name varchar(50), cname varchar(50),curl varchar(500))")
    # query
    cate_list = conn.exec_query("SELECT * FROM %s" % tb_name)
    print("create table success.")
    # insert
    conn.exec_no_query("INSERT INTO %s(cid,root_name,second_name,cname,curl) VALUES(?, ?, ?, ?, ?)" % tb_name,
                         (100001, '手机', '手机通讯', '对讲机', 'http://test.html'))
    # m insert
    data_list = [{"cid": 1, "root_name": "手机", "second_name": "手机通讯", "cname": "手机1", "curl": "http://test2.html"},
                {"cid": 2, "root_name": "手机", "second_name": "手机通讯", "cname": "手机2", "curl": "http://test3.html"}]
    conn.exec_many_no_query("INSERT INTO %s(cid,root_name,second_name,cname,curl) " % tb_name +
                              "VALUES(:cid, :root_name, :second_name, :cname, :curl)",
                              data_list)
    # query
    cate_list = conn.exec_query("SELECT * FROM %s " % tb_name)
    print("insert success cate_list length=%s" % len(cate_list))
    print(cate_list)
    # delete
    conn.exec_no_query("DELETE FROM %s WHERE cid=100001" % tb_name)
    # query
    cate_list = conn.exec_query("SELECT * FROM %s " % tb_name)
    print("delete success. cate_list length=", len(cate_list))
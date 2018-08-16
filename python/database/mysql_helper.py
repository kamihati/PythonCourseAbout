
# -*- coding:utf-8 -*-
# author: kamihati 2018-08-16 10:39

import pymysql


DB_NAME = 'study'
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_UID = 'root'
DB_PWD = '123456'


if __name__ == "__main__":
    conn = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_UID, passwd=DB_PWD, db=DB_NAME, charset='utf8mb4')
    
    # 创建游标
    cursor = conn.cursor()

    # 执行SQL，并返回收影响行数
    effect_row = cursor.execute("select * from tb_course")
    
    # 获取数据列表并遍历输出
    print("print full list: ")
    full_list = cursor.fetchall()
    for item in full_list:
        print(item)
    
    # 写入一行数据
    print('insert one data')
    cursor.execute("INSERT INTO tb_course(cname,detail) VALUES('新增课程1', '课程1描述')")
    conn.commit()
    
    # 查询刚刚写入的数据
    print('query new data')
    cursor.execute("SELECT cid,cname,addtime,detail FROM tb_course WHERE cname='新增课程1'")
    # 这次只获取查到的第一条数据
    first_item = cursor.fetchone()
    print(first_item)
    
    # 更新刚刚写入的数据
    print('update new data 新增课程1 to 测试课程1')
    cursor.execute("UPDATE tb_course SET cname='测试课程1' WHERE cname='新增课程1'")
    conn.commit()
    # 查询刚刚更新的数据
    print('query new modify data')
    cursor.execute("SELECT cid,cname,addtime,detail FROM tb_course WHERE cname='测试课程1'")
    # 这次只获取查到的第一条数据
    first_item = cursor.fetchone()
    print(first_item)
    
    # 删除刚刚写入的数据并返回影响行数
    print('delete new data')
    del_row_count = cursor.execute("DELETE FROM tb_course WHERE cname='测试课程1'")
    conn.commit()
    print('del row count=', del_row_count)

    # 查询刚刚删除的数据
    print('query deleted data')
    cursor.execute("SELECT cid,cname,addtime,detail FROM tb_course WHERE cname='测试课程1'")
    # 这次只获取查到的第一条数据
    first_item = cursor.fetchone()
    print('data is None:', first_item is None)
    
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


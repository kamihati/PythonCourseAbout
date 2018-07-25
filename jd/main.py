# coding=utf8

import sys
import os
from SqlHelper import Sqlite, SafeInput
from config import *
from bs4 import BeautifulSoup as bs
import requests
import time
import random
import json

rootPath = os.getcwd()

def read_cate_to_db():
    """
    读取京东类别并保存到数据库
    :return:
    """
    cate_url = "https://www.jd.com/allSort.aspx"
    cate_response = requests.get(cate_url)
    if cate_response.status_code == 200:
        print('success')
    print("cate read error,code=", cate_response.status_code)


def read_jd_item_list(cateid, url, page=1):
    """读取京东商品列表页面数据项"""
    if page > 1:
        url += '&page=%s' % page
    url = "http:" + url
    # 抓取京东商品列表网页html
    response = requests.get(url)

    # 商品数据项列表
    items = []
    if response.status_code == 200:
        print('url=', response.url)
        # 格式化html代码
        bsObj = bs(response.text, 'html.parser')
        bsItemList = bsObj.select_one("#plist").select("li.gl-item")
        print('page item count=', len(bsItemList))
        jdidList = []
        for bsItem in bsItemList:
            shopId = bsItem.select_one("div.j-sku-item").attrs["data-sku"]
            shopName = bsItem.select_one("div.p-name").text.strip()
            if not shopName or not shopId:
                continue
            shopIsJdZy = -1
            if bsItem.text.find("自营") != -1:
                shopIsJdZy = 1
            jdidList.append(shopId)
            items.append({"cateid": cateid, "name": shopName, "jdid": shopId, "isJdzy": shopIsJdZy, "price": 0})
        if len(jdidList) > 0:
            priceDict = read_sku_price(url, jdidList)
            print(priceDict)
            for item in items:
                if item['jdid'] in priceDict:
                    item['price'] = priceDict[item['jdid']]
        print(items)
    return items


def read_sku_price(prev_url, jdid_list):
    """
	读取指定京东sku的当前售价
	"""
    jdid_param = ""
    for jdid in jdid_list:
        jdid_param += ",J_%s" % jdid
    if jdid_param:
        jdid_param = jdid_param[1:]
    sku_url = "https://p.3.cn/prices/mgets?callback=jQuery3156835&type=1&area=7_412_46822_51756&skuIds=%s&pdbp=0" \
              "&pdtk=&pdpin=376466-177329&pduid=1299962097&source=list_pc_front" % jdid_param
    # url = "http://p.3.cn/prices/mgets?skuIds=J_%s" % jd_sku_id:

    try:
        price_dict = dict()
        time.sleep(random.randint(1, 5))
        headers = {
		    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/44.0.2403.157 Safari/537.36',
		    "Referer": prev_url
		}
        # 构造头部
        response = requests.get(sku_url, headers=headers)
        if response.status_code == 200:
            jsonStr = response.text[response.text.find("["): response.text.rfind("]") + 1]
            jsonObj = json.loads(jsonStr)
            for obj in jsonObj:
                price_dict[obj['id'].replace("J_", "")] = float(obj['p'])
    except:
        print('read_sku_price error:', sku_url, sys.exc_info()[0])
    return price_dict


def save_jd_item_list(itemList):
	"""
	保存商品列表
	"""
	if not itemList:
		return
	print("wait insert data=", len(itemList))
	try:
		sql = u""
		for item in itemList:
			sql += (u'if not exists (select 1 from ' + item_tb_name + ' where jdid=%s) INSERT INTO ' + item_tb_name + '(cateid, jdid, price, name, isJdzy, isJDexpress, comment, imgs, channel_price, tax_rate, tax_price, diff_price) VALUES') % (item["jdid"])
			sql += "(%s, %s, %s, '%s', %s, %s, 0, '', 0, 0, 0, 0);" % (item["cateid"], item["jdid"], float(item["price"]), SafeInput(str(item["name"])), item["isJdzy"], item["isJdzy"])
			sql += "ELSE BEGIN "
			sql += " UPDATE %s SET price=%s WHERE jdid=%s;" % (item_tb_name, float(item["price"]), item['jdid'])
			sql += " UPDATE bma_products SET shopprice=%s WHERE jdid=%s;" % (float(item['price']), item['jdid'])
			sql += " END"
		mssqlconn = Sqlite()
		mssqlconn.ExecNonQuery(sql)
	except Exception, ex:
		print("insert error:")
		print(ex)
	print("save_jd_item_list over. num=", len(itemList))


def read_cate_for_down_list(cateid, page):
	"""
	读取该分类商品列表并存储数据库
	cateid: 分类
	page: 从该分类下第一页开始。默认1
	"""
	print("lastCateId=", cateid)
	sql = "SELECT * FROM %s WHERE cateid>%d AND url is not null and url<>''" % (cate_tb_name, cateid)
	sqlConn = Sqlite()
	cateList = sqlConn.ExecQuery(sql)
	print("cate count=", len(cateList))
	for cate in cateList:
		print("cate=", cate)
		baseUrl = str(cate[-2])
		cateId = cate[0]
		# dirPath = os.path.join(rootPath, "pages", str(cateId))
		# if not os.path.isdir(dirPath):
		# 	os.makedirs(dirPath)
		itemList = []
		
		# 取该类别前20页商品列表
		for i in range(page, 21):
			# 抓取商品列表存储并存
			items = read_jd_item_list(cateId, baseUrl, i)
			# 存储本页数据
			save_jd_item_list(items)
			# 休眠一段时间开始读取下页数据
			sleepSecond = random.randint(1, 5)
			print('sleep second=', sleepSecond)
			time.sleep(sleepSecond)


def read_no_images_item():
	"""
	读取无图片的商品从商品详情页抓取图片以及规格信息并保存
	"""
	print("begin get not images item data")
	lastId = 0
	while True:
		
		mssqlconn = Sqlite()
		if lastId > 0:
			sql = "SELECT TOP 80 id,jdid FROM " + item_tb_name + " WHERE imgs='' AND id<" + str(lastId) + " ORDER BY id DESC"
		else:
			sql = "SELECT TOP 10 id,jdid FROM " + item_tb_name + " WHERE imgs='' ORDER BY id DESC"
		itemList = mssqlconn.ExecQuery(sql)
		# 逐个商品处理
		sql = ""
		for item in itemList:
			item_id = int(item[0])
			last_id = item_id
			jdid = int(item[1])

			url = "http://item.jd.com/%s.html" % jdid

			response = requests.get(url)
			if response.status_code == 200:
				bsObj = bs(response.text, 'html.parser')
				# 图片
                imgs = []
				for imgLi in bsObj.select_one("ul.lh").select("li"):
					img = imgLi.find("img")
					if not img:
						continue
					imgSrc = img.attrs["src"]
					imgSrc = imgSrc[imgSrc.find("n5") + 3:]
					imgs.append(imgSrc)

				parameter = str(bsObj.select_one("div.p-parameter"))
				detail = str(bsObj.select_one("div.detail-content"))
				ptable = str(bsObj.select_one("div.Ptable"))
				sql += 'UPDATE ' + item_tb_name +\
                       " SET imgs='%s',parameter='%s',ptable='%s',detail='%s' WHERE id=%d AND imgs=''" % \
                       (','.join(imgs), SafeInput(parameter), SafeInput(ptable), SafeInput(detail), item_id)
			print(jdid)
		mssqlconn.ExecNonQuery(sql)
		print("save count=", len(itemList))
	print("read_no_images_item over")


if __name__ == '__main__':
	read_cate_to_db()
    """
    cateid = sys.argv[1] if len(sys.argv) > 1 else 7
    page = sys.argv[2] if len(sys.argv) > 2 else 1
    try:
        read_cate_for_down_list(cateid, page)
    except Exception, ex:
        print(ex)

	try:
		read_no_images_item()
	except Exception as ex:
	    print(ex)
    """

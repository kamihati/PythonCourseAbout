# coding=utf8

import sys
import time
import json
import random
from bs4 import BeautifulSoup as bs
from SqlHelper import SqliteHelper
from HttpHelper import get_http_response
from config import cate_tb_name, item_tb_name


def read_jd_item(max_page=0):
	conn = SqliteHelper()

	cate_list = conn.exec_query("select cid,curl from %s" % cate_tb_name)
	read_page_count = 0
	for cate in cate_list:
		cate_id = cate[0]
		cate_url = cate[1]
		print(cate_id)
		print(cate_url)
		res = get_http_response(cate_url)
		bs_obj = bs(res.text, 'html.parser')
		item_list = bs_obj.select_one("#plist").select("li.gl-item")
		print("page item length:", len(item_list))
		values = []
		for item in item_list:
			sku_id = item.select_one("div.j-sku-item").attrs["data-sku"]
			title = item.select_one("div.p-name").text.strip()
			item_url = "https://item.jd.com/%s.html" % sku_id
			# price = item.select_one("div.p-price").select_one("strong.J_price").text
			list_pic = item.select_one("div.p-img").select_one("img")
			if "src" in list_pic.attrs:
				list_pic_url = list_pic.attrs['src']

			values.append({"sku_id": sku_id, "title": title, "cate_id": cate_id, "item_url": item_url, "list_pic_url": list_pic_url})
		read_page_count += 1
		conn.exec_many_no_query("INSERT INTO %s(sku_id,cate_id,title,list_pic_url,item_url) " % item_tb_name +
	                        "VALUES(:sku_id,:cate_id,:title,:list_pic_url,:item_url)", values)
		if max_page > 0 and read_page_count >= max_page:
			break


def read_jd_item_price(jdid_list):
	jdid_param = ""
	for jdid in jdid_list:
		jdid_param += ",J_%s" % jdid
	if jdid_param:
		jdid_param = jdid_param[1:]
	sku_url = "https://p.3.cn/prices/mgets?callback=jQuery3156835&type=1&area=7_412_46822_51756&skuIds=%s&pdbp=0" \
	          "&pdtk=&pdpin=376466-177329&pduid=1299962097&source=list_pc_front" % jdid_param
	print(sku_url)
	try:
		price_dict = dict()
		time.sleep(random.randint(1, 5))

		response = get_http_response(sku_url)
		if response.status_code == 200:
			print(response.text)
			json_str = response.text[response.text.find("["): response.text.rfind("]") + 1]
			print(json_str)
			json_obj = json.loads(json_str)
			for obj in json_obj:
				print(obj)
				price_dict[obj['id']] = float(obj['p'])

	except:
		print('read_sku_price error:', sku_url, sys.exc_info()[0])
	return price_dict


if __name__ == "__main__":
	if False:
		read_jd_item_price(["7224901"])
	else:
		demo_conn = SqliteHelper()
		if demo_conn.exists_table(item_tb_name):
			demo_conn.exec_no_query("drop table %s" % item_tb_name)

		demo_conn.exec_no_query(
			"CREATE TABLE %s(" % item_tb_name +
			"sku_id int,"
			"cate_id int,"
			"list_pic_url text,"
			"title text,"
			"price real,"
			"item_url text)")
		read_jd_item(3)
		data_list = demo_conn.exec_query("select * from %s" % item_tb_name)
		if len(data_list) > 0:
			print(data_list[0])
		print("data length:", len(data_list))

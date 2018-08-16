# -*- coding:utf-8 -*-
# author: kamihati 2018-08-16 14:33


import requests
from bs4 import BeautifulSoup as bs

DEFAULT_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) " \
                     "Chrome/67.0.3396.99 Safari/537.36"


def get_http_response(url, params=None):
    if params is None:
        params = {}
    headers = {'user-agent': DEFAULT_USER_AGENT}
    response = requests.get(url, headers=headers, params=params)
    return response


def read_html(url):
    """
    使用BeautifulSoup4解析网页的html代码
    :param url:
    :return:
    """
    # 声明list变量用于保存解析到的数据
    result = []
    res = get_http_response(url)
    # html.parser必填。建议使用的python的html解析器。
    bs_obj = bs(res.text, 'html.parser')
    # 找到列表容器plist。并查询旗下的class包含有gl-item的li列表
    item_list = bs_obj.select_one("#plist").select("li.gl-item")
    print("page item length:", len(item_list))
    # 遍历li列表
    for item in item_list:
        # 根据class查找到其中的sku元素值
        sku_id = item.select_one("div.j-sku-item").attrs["data-sku"]
        # 根据class查找商品标题
        title = item.select_one("div.p-name").text.strip()
        
        # 根据class读取img元素的src属性来获取列表商品图片地址
        list_pic = item.select_one("div.p-img").select_one("img")
        list_pic_url = ""
        if "src" in list_pic.attrs:
            list_pic_url = list_pic.attrs['src']
        # 写入list
        result.append(dict(skuid=sku_id, title=title, pic_url=list_pic_url ))
    return result


if __name__ == "__main__":
    items = read_html("https://list.jd.com/list.html?cat=9987,653,655")
    print(items)

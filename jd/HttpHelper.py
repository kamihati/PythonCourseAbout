# coding=utf8

import requests
from bs4 import BeautifulSoup as bs

DEFAULT_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"


def get_http_response(url, params=None):
	if params is None:
		params = {}
	headers = {'user-agent': DEFAULT_USER_AGENT}
	response = requests.get(url, headers=headers, params=params)
	return response


if __name__ == "__main__":
	res = get_http_response("https://ip.cn")
	if res.status_code == 200:
		bs_obj = bs(res.text, "html.parser")
		code_list = bs_obj.select("code")
		for code in code_list:
			print(code.text)
	else:
		print("response status_code:", res.status_code)

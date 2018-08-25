# coding=utf8

import os
import logging

# 配置输出日志格式.
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
# 配置输出时间的格式，注意月份和天数不要搞乱了
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '

# 有了filename参数就不会直接输出显示到控制台，而是直接写入文件
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    filename=os.path.join(os.getcwd(), 'test.log')
                    )

try:
    a = 10 / 0
except Exception as e:
    logging.debug(e)

logging.debug("msg1")
logging.info("msg2")
logging.warning("msg3")
logging.error("msg4")
logging.critical("msg5")

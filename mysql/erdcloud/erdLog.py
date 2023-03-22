# -*- coding: utf-8 -*-
# @Time  : 2021/5/19 17:23
# @File  : erdLog.py
# @Author: guo

import logging


def Log():
    # 创建日志器
    logger = logging.getLogger()
    # 默认级别warning
    logger.setLevel(logging.INFO)
    # logger显示控制台
    s_handler = logging.StreamHandler()
    # 日志信息放在控制台
    logger.addHandler(s_handler)
    # 设置格式
    formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s')
    # 格式给控制台
    s_handler.setFormatter(formatter)
    # # logger显示文本FileHandler
    # f_handler = logging.FileHandler('../erdcloud/log.log', encoding='utf-8')
    # # 日志信息放在文本FileHandler
    # logger.addHandler(f_handler)
    # # 格式给文本FileHandler
    # f_handler.setFormatter(formatter)
    logger.handlers.pop()
    return logger

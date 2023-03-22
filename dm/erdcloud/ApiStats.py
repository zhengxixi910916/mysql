# -*- coding: utf-8 -*-
from erdcloud.Store import *


def add(api, info=""):
    """ 定义一个全局变量 """
    instance = Store.instance()
    apis = instance.get_value("apis")
    if apis is None:
        apis = {}
    apis[api] = info
    instance.set_value("apis", apis)


def stats():
    instance = Store.instance()
    apis = instance.get_value("apis") or {}
    all_apis = sorted(list(apis.values()), key=lambda info: info["api"])

    result = {
        "count": len(all_apis),
        "apis": all_apis
    }
    return result

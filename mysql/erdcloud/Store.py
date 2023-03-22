# -*- coding: utf-8 -*-

import threading


class Store(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        self._global_dict = dict()

    @classmethod
    def instance(cls, *args, **kwargs):
        with cls._instance_lock:
            if not hasattr(Store, "_instance"):
                Store._instance = Store()
                return Store._instance
            return Store._instance

    def set_value(self, key, value):
        """ 定义一个全局变量 """
        self._global_dict[key] = value

    def get_value(self, key, def_value=None):
        """ 获得一个全局变量,不存在则返回默认值 """
        try:
            return self._global_dict[key]
        except KeyError:
            return def_value

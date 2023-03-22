# -*- coding: utf-8 -*-
import configparser as parser
import nacos
import threading

from erdcloud import Utils


class NacosClient(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        self.client = None
        self.dbs = dict()

    @classmethod
    def instance(cls, *args, **kwargs):
        with cls._instance_lock:
            if not hasattr(NacosClient, "_instance"):
                NacosClient._instance = NacosClient()
                return NacosClient._instance
            return NacosClient._instance

    def get_nacos_client(self):
        if self.client is None:
            print("获取新的nacos client实例")
            server_addresses = Utils.Config.get_env_value("env.nacos.server.ip",
                                                          "127.0.0.1") + ":" + Utils.Config.get_env_value(
                "env.nacos.server.port", "8848")
            namespace = Utils.Config.get_env_value("env.nacos.server.config.namespace",
                                                   "ceb2fa99-0989-47f9-80c8-ec6375d806c4")

            # no auth mode
            self.client = nacos.NacosClient(server_addresses, namespace=namespace)

        return self.client

    def get_config_str(self, data_id=None, group=None):
        if data_id is None:
            # data_id = Utils.Config.get_env_value("erd.test.db.dataid", "erdcloud-test-db.ini")
            data_id = Utils.Config.get_env_value("erd.test.path.db.config", "db.ini")

        if group is None:
            group = Utils.Config.get_env_value("env.nacos.server.config.group", "eCloud")
        if data_id is None or group is None:
            return ""
        return self.get_nacos_client().get_config(data_id, group)

    def get_ini_config(self, data_id=None, group=None):
        config_str = self.get_config_str(data_id, group)
        if config_str == "":
            return dict()
        rcp = parser.RawConfigParser()
        rcp.read_string(config_str)
        print(rcp.sections())
        return rcp

    def get_db_config(self, data_id=None, group=None):
        config = self.get_ini_config(data_id, group)
        return config


if __name__ == '__main__':
    print(Utils.Config.get_env_value("env.nacos.server.ip"))
    NacosClient.instance().get_db_config()

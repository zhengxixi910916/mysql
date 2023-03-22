# -*- coding: utf-8 -*-

import os
import base64
import random

from erdcloud.Nacos import NacosClient


class Config:
    @staticmethod
    def project_root_path(project_name=None):
        """
        获取当前项目根路径
        :param project_name:
        :return: 根路径
        """
        PROJECT_NAME = 'erdcloud-test-py' if project_name is None else project_name
        project_path = os.path.abspath(os.path.dirname(__file__))
        root_path = project_path[:project_path.find("{}\\".format(PROJECT_NAME)) + len("{}\\".format(PROJECT_NAME))]
        print('当前项目名称：{}\r\n当前项目根路径：{}'.format(PROJECT_NAME, root_path))
        return root_path

    @staticmethod
    def get_env_value(env_key="", default_value=""):
        env_value = os.getenv(env_key, '')
        if env_value == '':
            env_value = os.getenv(env_key.replace(".", "_"), default_value)

        return env_value

    @staticmethod
    def get_config_txt(env_key="", file=""):
        env_path = Config.get_env_value(env_key, "")
        if env_path == '':
            return Config.read_file_text(os.path.abspath(os.path.join(os.path.dirname(__file__), file)))
        else:
            if env_path.startswith('local:'):
                filepath = os.path.abspath(env_path[len('local:'):len(env_path)])
                return Config.read_file_text(filepath)
            elif env_path.startswith('nacos:'):
                dataid = env_path[len('nacos:'):len(env_path)]
                group = Config.get_env_value("env.nacos.server.config.group", "eCloud")
                return NacosClient.instance().get_config_str(dataid, group)
            else:
                return ""

    @staticmethod
    def api_mapping():
        """
        获取api_mapping.json路径
        :return: 路径
        """
        return Config.get_config_txt("erd.test.path.apimapping", 'config' + os.path.sep + 'api_mapping.json')

    @staticmethod
    def env_config():
        """
        获取env.ini路径
        :return: 路径
        """
        return Config.get_config_txt("erd.test.path.env.config", 'config' + os.path.sep + 'env.ini')

    @staticmethod
    def db_config():
        """
        获取env.ini路径
        :return: 路径
        """
        return Config.get_config_txt("erd.test.path.db.config", 'config' + os.path.sep + 'db.ini')

    @staticmethod
    def read_file_text(filepath):
        f = open(filepath, 'r', encoding="utf-8")
        txt = f.read()
        f.close()
        return txt

    @staticmethod
    def random(prefix, start=100, end=999, suffix=""):
        return prefix + str(random.randint(start, end)) + suffix

    @staticmethod
    def dele_file(path):
        if os.path.exists(path):
            os.remove(path)

    @staticmethod
    def down_check(path, name):
        if os.path.exists(path):
            s = os.listdir(path)
            if name in s:
                print(f'文件{name}存在')
                return True
            else:
                print(f"文件{name}不存在")
                return False
        else:
            print('路径不存在')

    @staticmethod
    def base_convert(path):
        f = open(path, 'rb')  # 二进制方式打开文件
        ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()
        return str(ls_f, 'utf-8')


if __name__ == '__main__':
    # print(Config().api_mapping_path())
    print('local:c:/123'.startswith('local:'))
    print('local:c:/123'[len('local:'):len('local:c:/123')])

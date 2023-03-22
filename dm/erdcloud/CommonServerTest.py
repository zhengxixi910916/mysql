import configparser as cparser

import requests

from erdcloud import Utils


# 公共类，获取当前用户信息、当前用户所属组织、当前站点、请求Headers-带token

class CommonServer(object):
    def __init__(self):
        self.token = ''
        self.myOrgId = ''
        self.user_id = ''
        self.siteId = ''
        self.organization = {}
        self.site = {}
        self.currUser = {}
        # base_dir = path.dirname(path.dirname(path.abspath(__file__)))
        # base_dir = base_dir.replace('\\', '/')
        # file_path = base_dir + "/config/env.ini"

        cf = cparser.ConfigParser()
        # cf.read(path.abspath(path.join('config' + path.sep + 'env.ini')))
        # cf.read(path.abspath(Utils.Config.env_config()))
        cf.read_string(Utils.Config.env_config())
        self.host = cf.get("envConf", "host")
        self.env = cf.get("envConf", "env")
        self.user = cf.get("envConf", "user")
        self.password = cf.get("envConf", "password")
        self.context = cf.get("envConf", "context")
        self.Authorization = cf.get("envConf", "Authorization")
        self.Headers = {}

    def get_host(self):
        return self.host

    def get_context(self):
        return self.context

    # 获取token
    def get_token(self):
        if self.token == '':
            url = self.host + '/oauth/erdp-token'
            params = {'rememberMe': 'true',
                      'password': self.password,
                      'username': self.user}
            payload = {"username": self.user, "password": self.password}
            header = {"Authorization": self.Authorization}
            r = requests.post(url, data=payload, params=params, headers=header)

            self.token = r.json()['res']['data']['access_token']
            self.Headers = {"Content-Type": "application/json;charset=utf-8",
                            "Authorization": "Bearer " + self.token}
        return self.token

    def get_headers(self, custom=None):
        if self.token == '':
            self.get_token()
        result = dict.copy(self.Headers)
        if custom is not None:
            for k in custom:
                result[k] = custom[k]
        return result

    def get_currUser(self):
        if self.user_id == '':
            url = self.host + '/sys/v1/user/me'
            r = requests.get(url, headers=self.get_headers())
            self.currUser = r.json()["res"]["user"]
            self.user_id = self.currUser['id']
        return self.currUser

    def get_curr_userId(self):
        if self.user_id == '':
            self.get_currUser()
        return self.user_id

    def get_MyOrgOid(self):
        if self.myOrgId == '':
            url = self.host + '/pdm/container/getCurrentContainerInfo'
            r = requests.get(url, headers=self.get_headers())
            result = r.json()
            self.organization = result["data"]["organization"]
            self.myOrgId = self.organization["oid"]
            self.site = result["data"]["site"]
            self.siteId = self.site["oid"]
        return self.myOrgId

    def get_siteOid(self):
        if self.siteId == '':
            self.get_MyOrgOid()
        return self.siteId

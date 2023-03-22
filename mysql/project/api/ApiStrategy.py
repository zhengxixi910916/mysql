import os
import time
from contextlib import closing

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
战略目标管理
'''
dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dir_document = dir_path + r'/document'
times = time.strftime("%Y-%m-%d %H %M %S", time.localtime(time.time()))
file_name = "strategy_" + times + ".xlsx"

apis = Api({
    "download_template": "/decision/$VERSION$/strategies/export/template",  # 模板下载
    "import_strategy": "/decision/$VERSION$/strategies/import/excel",  # 导入战略或战略目标
    "query_strategy_tree": "/decision/$VERSION$/strategies/tree",  # 查询战略树
    "delete_strategy": "/decision/$VERSION$/strategies/%s",  # 删除战略或战略目标
    "add_strategy": "/decision/$VERSION$/strategy",  # 新增战略或战略目标
    "update_strategy": "/decision/$VERSION$/strategy",  # 修改战略或战略目标
    "isrepeat_strategy": "/decision/$VERSION$/strategy/exist",  # 判断名称是否重复
    "query_strategy_map": "/decision/$VERSION$/strategy/map",  # 查询战略键值对
    "query_one_strategy": "/decision/$VERSION$/strategy/%s",  # 查询战略或战略目标
})


def download_template(self, checker=None):
    """
    接口名称：模板下载
    接口地址：/decision/$VERSION$/strategies/export/template
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("download_template"), None
                                                  )) as response:
        with open(dir_document + r"\export_strategy_tem_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def import_strategy(self, checker=None):
    """
    接口名称：导入战略或战略目标
    接口地址：/decision/$VERSION$/strategies/import/excel
    """
    r = RequestService.call_post(apis.get("import_strategy"), data={
        "file": ""  # file - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def query_strategy_tree(self, checker=None):
    """
    接口名称：查询战略树
    接口地址：/decision/$VERSION$/strategies/tree
    """
    r = RequestService.call_get(apis.get("query_strategy_tree"), params={
        "name": ""  # name - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delete_strategy(self, strategyid, checker=None):
    """
    接口名称：删除战略或战略目标
    接口地址：/decision/$VERSION$/strategies/{ids}
    """
    r = RequestService.call_delete(apis.get("delete_strategy", strategyid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_strategy(self, name, description, checker=None):
    """
    接口名称：新增战略或战略目标
    接口地址：/decision/$VERSION$/strategy
    """
    r = RequestService.call_post(apis.get("add_strategy"), json={"strategies": [
        {"name": name, "description": description, "evaluateAlgorithm": "", "evaluateMethod": "math", "type": 1},
        {"id": "", "name": name, "description": description, "type": 2}]}
                                 )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_strategy(self, strategy_id, strategy_name,name, strategy_description, description, checker=None):
    """
    接口名称：修改战略或战略目标
    接口地址：/decision/$VERSION$/strategy
    """
    r = RequestService.call_put(apis.get("update_strategy"), json={
        "strategies": [{"id": strategy_id, "name": strategy_name, "description": strategy_description,
                         "evaluateAlgorithm": "", "evaluateMethod": "math", "type": 1},
                        {"id": "", "name": name, "description": description, "type": 2}]
        }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def isrepeat_strategy(self, name, flag, strategyid=None, checker=None):
    """
    接口名称：判断名称是否重复
    接口地址：/decision/$VERSION$/strategy/exist
    """
    r = RequestService.call_get(apis.get("isrepeat_strategy"), params={
        "flag": flag,  # 1新增2修改 - required: True
        "id": strategyid,  # 修改必传id - required: False
        "name": name,  # name - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def query_strategy_map(self, flag, checker=None):
    """
    接口名称：查询战略键值对
    接口地址：/decision/$VERSION$/strategy/map
    """
    r = RequestService.call_get(apis.get("query_strategy_map"), params={
        "flag": flag  # 0战略1战略目标 - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def query_one_strategy(self, strategyid, checker=None):
    """
    接口名称：查询战略或战略目标
    接口地址：/decision/$VERSION$/strategy/{id}
    """
    r = RequestService.call_get(apis.get("query_one_strategy", strategyid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

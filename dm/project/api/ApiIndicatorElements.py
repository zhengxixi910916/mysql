from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
import uuid
import time
'''
指标要素定义
'''
apis = Api({
    "addUsingPOST": "/decision/$VERSION$/indelemdef",  # 新增指标要素定义
    "updateUsingPUT": "/decision/$VERSION$/indelemdef",  # 修改指标要素定义
    "queryTreeUsingGET": "/decision/$VERSION$/indelemdef/tree",  # 查询指标要素定义树
    "deleteUsingDELETE_1": "/decision/$VERSION$/indelemdef/%s",  # 批量删除指标要素定义
    "queryOneUsingGET": "/decision/$VERSION$/indelemdef/%s",  # 查询指标要素定义
    "isRepeatUsingGET": "/decision/$VERSION$/indicatorelem/exist",  # 判断名称是否重复
    "downloadtemplateUsingGET": "/decision/$VERSION$/indicatorelem/export/template",  # 模板下载
    "importExcelUsingPOST": "/decision/$VERSION$/indicatorelem/import/excel",  # 导入组合决策指标要素
})


def addUsingPOST(self, checker=None):
    """
    接口名称：新增指标要素定义
    接口地址：/decision/$VERSION$/indelemdef
    """
    r = RequestService.call_post(apis.get("addUsingPOST", None), json={"indicatorElementDef": [
        {"name": "接口测试指标库"+time.strftime('%Y%m%d%H%M%S', time.localtime()), "description": "123", "evaluateAlgorithm": "",
         "evaluateMethod": "math", "type": 1},
        {"id": "", "name": "接口测试指标要素"+time.strftime('%Y%m%d%H%M%S', time.localtime()), "description": "111", "type": 2}]}, )

    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateUsingPUT(self, elIndElemDef, checker=None):
    """
    接口名称：修改指标要素定义
    接口地址：/decision/$VERSION$/indelemdef
    """
    r = RequestService.call_put(apis.get("updateUsingPUT", None), json=elIndElemDef)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def queryTreeUsingGET(self, name, checker=None):
    """
    接口名称：查询指标要素定义树
    接口地址：/decision/$VERSION$/indelemdef/tree
    """
    r = RequestService.call_get(apis.get("queryTreeUsingGET", None), params={
        "name": name  # name - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteUsingDELETE_1(self, ids, checker=None):
    """
    接口名称：批量删除指标要素定义
    接口地址：/decision/$VERSION$/indelemdef/{ids}
    """
    r = RequestService.call_delete(apis.get("deleteUsingDELETE_1", ids), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def queryOneUsingGET(self, IndicatorId, checker=None):
    """
    接口名称：查询指标要素定义
    接口地址：/decision/$VERSION$/indelemdef/{id}
    """
    r = RequestService.call_get(apis.get("queryOneUsingGET", IndicatorId), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def isRepeatUsingGET(self, name, flag, checker=None):
    """
    接口名称：判断名称是否重复
    接口地址：/decision/$VERSION$/indicatorelem/exist
    """
    r = RequestService.call_get(apis.get("isRepeatUsingGET", None), params={
        "flag": flag,  # 1新增2修改 - required: True
        "id": "",  # 修改必传id - required: False
        "name": name,  # name - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def downloadtemplateUsingGET(self, checker):
    """
    接口名称：模板下载
    接口地址：/decision/$VERSION$/indicatorelem/export/template
    """
    r = RequestService.call_get(apis.get("downloadtemplateUsingGET", None), None)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def importExcelUsingPOST(self, checker):
    """
    接口名称：导入组合决策指标要素
    接口地址：/decision/$VERSION$/indicatorelem/import/excel
    """
    r = RequestService.call_post(apis.get("importExcelUsingPOST", None), data={
        "file": ""  # file - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "selectAvlbFieldListUsingGET_4": "/proj/$VERSION$/extfields",  # 查询可用的扩展列名称
    "addExtfieldsUsingPOST_3": "/proj/$VERSION$/extfields",  # 添加可扩展列
    "selectFilterListUsingPOST_4": "/proj/$VERSION$/project/filterlist",  # 过滤业务数据
    "businessTableUsingPOST_3": "/proj/$VERSION$/%s/businessTable",  # 查询业务表格列
})


def selectAvlbFieldListUsingGET_4(self, active, checker=None):
    """
    接口名称：查询可用的扩展列名称
    接口地址：/proj/$VERSION$/extfields
    """
    r = RequestService.call_get(apis.get("selectAvlbFieldListUsingGET_4", None), params={
        "active": active
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def addExtfieldsUsingPOST_3(self, attrName, attrKey, attrType, typeLength, defaultValue, checker=None):
    """
    接口名称：添加可扩展列
    接口地址：/proj/$VERSION$/extfields
    """
    r = RequestService.call_post(apis.get("addExtfieldsUsingPOST_3", None), params={
        "entityAttrs[0].attrName": attrName,
        "entityAttrs[0].attrKey": attrKey,
        "entityAttrs[0].attrType": attrType,
        "entityAttrs[0].typeLength": typeLength,
        "entityAttrs[0].defaultValue": defaultValue
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def select_filter_list_using_post_4(self, el_condition_list, checker=None):
    """
    接口名称：过滤业务数据
    接口地址：/proj/$VERSION$/project/filterlist
    """
    r = RequestService.call_post(apis.get("selectFilterListUsingPOST_4", None), json={
        "elConditionList": el_condition_list,
        "pageindex": 1,
        "pagesize": 20
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def businessTableUsingPOST_3(self, viewid, checker=None):
    """
    接口名称：查询业务表格列
    接口地址：/proj/$VERSION$/{viewid}/businessTable
    """
    r = RequestService.call_post(apis.get("businessTableUsingPOST_3", viewid), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

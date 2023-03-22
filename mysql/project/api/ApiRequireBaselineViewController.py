from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "searchBusinessUsingPOST_2": "/req/$VERSION$/baseline/api/list",  # 通用查询逻辑
    "selectBusinessExportUsingGET_2": "/req/$VERSION$/baseline/export",  # 导出业务数据
    "selectAvlbFieldListUsingGET_5": "/req/$VERSION$/baseline/extfields",  # 查询可用的扩展列名称
    "addExtfieldsUsingPOST_4": "/req/$VERSION$/baseline/extfields",  # 添加可扩展列
    "importBusinessUsingPOST_2": "/req/$VERSION$/baseline/import",  # 导入业务数据
    "selectBusinessTemplateExportUsingGET_2": "/req/$VERSION$/baseline/template/export",  # 导出业务数据模板
    "businessTableUsingPOST_4": "/req/$VERSION$/baseline/%s/businessTable",  # 查询业务表格列
    "selectBusinessListUsingPOST_2": "/req/$VERSION$/baseline/%s/businesslist",  # 查询业务数据
    "selectFilterListUsingPOST_2": "/req/$VERSION$/baseline/%s/filterlist",  # 过滤业务数据
    "releasePlanComfirmUsingPOST_2": "/req/$VERSION$/baseline/%s/releasePlanComfirm",  # 发布计划前判断是否可以发布
})


def searchBusinessUsingPOST_2(self, checker=None):
    """
    接口名称：通用查询逻辑
    接口地址：/req/$VERSION$/baseline/api/list
    """
    r = RequestService.call_post(apis.get("searchBusinessUsingPOST_2", None), json={
        "elViewDto": ""  # 条件列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectBusinessExportUsingGET_2(self, checker=None):
    """
    接口名称：导出业务数据
    接口地址：/req/$VERSION$/baseline/export
    """
    r = RequestService.call_get(apis.get("selectBusinessExportUsingGET_2", None), params={
        "businessType": "",  # 业务对象 - required: True
        "elConditionList": "",  # 条件 - required: False
        "exportIdList": "",  # 导出数据的id - required: False
        "exprotList": "",  # 导出字段 - required: True
        "isFilter": "",  # 是否过滤查询 - required: False
        "isMyCare": "",  # 是否查询我的收藏 - required: False
        "mgReqFlag": "",  # 是否需求管理 - required: False
        "nameOrcode": "",  # 首页高级查询 - required: False
        "projectId": "",  # 项目ID - required: False
        "relationship": "",  # 过滤关系and-or - required: False
        "viewid": "",  # 视图ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectAvlbFieldListUsingGET_5(self, active, checker=None):
    """
    接口名称：查询可用的扩展列名称
    接口地址：/req/$VERSION$/baseline/extfields
    """
    r = RequestService.call_get(apis.get("selectAvlbFieldListUsingGET_5", None), params={
        "active": active  # 列状态1已使用0未使用，空所有 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def addExtfieldsUsingPOST_4(self, attrName, attrKey, attrType, typeLength, defaultValue, checker=None):
    """
    接口名称：添加可扩展列
    接口地址：/req/$VERSION$/baseline/extfields
    """
    r = RequestService.call_post(apis.get("addExtfieldsUsingPOST_4", None), params={
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


def importBusinessUsingPOST_2(self, checker=None):
    """
    接口名称：导入业务数据
    接口地址：/req/$VERSION$/baseline/import
    """
    r = RequestService.call_post(apis.get("importBusinessUsingPOST_2", None), data={
        "file": ""  # file - required: True
    }, params={
        "businessType": "",  # 业务对象 - required: True
        "projectId": "",  # 项目ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectBusinessTemplateExportUsingGET_2(self, checker=None):
    """
    接口名称：导出业务数据模板
    接口地址：/req/$VERSION$/baseline/template/export
    """
    r = RequestService.call_get(apis.get("selectBusinessTemplateExportUsingGET_2", None), params={
        "businessType": "",  # 业务对象 - required: True
        "exprotList": "",  # 导出字段 - required: True
        "projectId": "",  # 项目ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def businessTableUsingPOST_4(self, viewid, checker=None):
    """
    接口名称：查询业务表格列
    接口地址：/req/$VERSION$/baseline/{viewid}/businessTable
    """
    r = RequestService.call_post(apis.get("businessTableUsingPOST_4", viewid), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectBusinessListUsingPOST_2(self, viewid, viewDto, checker=None):
    """
    接口名称：查询业务数据
    接口地址：/req/$VERSION$/baseline/{viewid}/businesslist
    """
    r = RequestService.call_post(apis.get("selectBusinessListUsingPOST_2", viewid), json=viewDto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectFilterListUsingPOST_2(self, viewid, viewDto, checker=None):
    """
    接口名称：过滤业务数据
    接口地址：/req/$VERSION$/baseline/{viewid}/filterlist
    """
    r = RequestService.call_post(apis.get("selectFilterListUsingPOST_2", viewid), json=viewDto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def releasePlanComfirmUsingPOST_2(self, checker=None):
    """
    接口名称：发布计划前判断是否可以发布
    接口地址：/req/$VERSION$/baseline/{viewid}/releasePlanComfirm
    """
    r = RequestService.call_post(apis.get("releasePlanComfirmUsingPOST_2", None), json={
        "viewDto": ""  # 条件列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

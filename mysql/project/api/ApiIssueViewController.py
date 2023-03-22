from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "searchBusinessUsingPOST_1": "/issue/$VERSION$/api/list",  # 通用查询逻辑
    "selectBusinessExportUsingGET_1": "/issue/$VERSION$/export",  # 导出业务数据
    "selectAvlbFieldListUsingGET_1": "/issue/$VERSION$/extfields",  # 查询可用的扩展列名称
    "addExtfieldsUsingPOST_1": "/issue/$VERSION$/extfields",  # 添加可扩展列
    "importBusinessUsingPOST_1": "/issue/$VERSION$/import",  # 导入业务数据
    "selectBusinessTemplateExportUsingGET_1": "/issue/$VERSION$/template/export",  # 导出业务数据模板
    "businessTableUsingPOST_1": "/issue/$VERSION$/%s/businessTable",  # 查询业务表格列
    "selectBusinessListUsingPOST_1": "/issue/$VERSION$/%s/businesslist",  # 查询业务数据
    "selectFilterListUsingPOST_1": "/issue/$VERSION$/%s/filterlist",  # 过滤业务数据
    "releasePlanComfirmUsingPOST_1": "/issue/$VERSION$/%s/releasePlanComfirm",  # 发布计划前判断是否可以发布
})


def searchBusinessUsingPOST_1(self, checker=None):
    """
    接口名称：通用查询逻辑
    接口地址：/issue/$VERSION$/api/list
    """
    r = RequestService.call_post(apis.get("searchBusinessUsingPOST_1", None), json={
        "elViewDto": ""  # 条件列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectBusinessExportUsingGET_1(self, checker=None):
    """
    接口名称：导出业务数据
    接口地址：/issue/$VERSION$/export
    """
    r = RequestService.call_get(apis.get("selectBusinessExportUsingGET_1", None), params={
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


def selectAvlbFieldListUsingGET_1(self, active, checker=None):
    """
    接口名称：查询可用的扩展列名称
    接口地址：/issue/$VERSION$/extfields
    """
    r = RequestService.call_get(apis.get("selectAvlbFieldListUsingGET_1", None), params={
        "active": active  # 列状态1已使用0未使用，空所有 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def addExtfieldsUsingPOST_1(self, attrName, attrKey, attrType, typeLength, defaultValue, checker=None):
    """
    接口名称：添加可扩展列
    接口地址：/issue/$VERSION$/extfields
    """
    r = RequestService.call_post(apis.get("addExtfieldsUsingPOST_1", None), params={
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


def importBusinessUsingPOST_1(self, checker=None):
    """
    接口名称：导入业务数据
    接口地址：/issue/$VERSION$/import
    """
    r = RequestService.call_post(apis.get("importBusinessUsingPOST_1", None), data={
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


def selectBusinessTemplateExportUsingGET_1(self, checker=None):
    """
    接口名称：导出业务数据模板
    接口地址：/issue/$VERSION$/template/export
    """
    r = RequestService.call_get(apis.get("selectBusinessTemplateExportUsingGET_1", None), params={
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


def businessTableUsingPOST_1(self, viewid, checker=None):
    """
    接口名称：查询业务表格列
    接口地址：/issue/$VERSION$/{viewid}/businessTable
    """
    r = RequestService.call_post(apis.get("businessTableUsingPOST_1", viewid), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectBusinessListUsingPOST_1(self, viewDto, viewid, checker=None):
    """
    接口名称：查询业务数据
    接口地址：/issue/$VERSION$/{viewid}/businesslist
    """
    r = RequestService.call_post(apis.get("selectBusinessListUsingPOST_1", viewid), json=viewDto, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectFilterListUsingPOST_1(self, checker=None):
    """
    接口名称：过滤业务数据
    接口地址：/issue/$VERSION$/{viewid}/filterlist
    """
    r = RequestService.call_post(apis.get("selectFilterListUsingPOST_1", None), json={
        "viewDto": ""  # 条件列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def releasePlanComfirmUsingPOST_1(self, checker=None):
    """
    接口名称：发布计划前判断是否可以发布
    接口地址：/issue/$VERSION$/{viewid}/releasePlanComfirm
    """
    r = RequestService.call_post(apis.get("releasePlanComfirmUsingPOST_1", None), json={
        "viewDto": ""  # 条件列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

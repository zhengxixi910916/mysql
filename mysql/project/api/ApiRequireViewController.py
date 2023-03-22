from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "searchBusinessUsingPOST_3": "/req/$VERSION$/api/list",  # 通用查询逻辑
    "selectBusinessExportUsingGET_3": "/req/$VERSION$/export",  # 导出业务数据
    "selectAvlbFieldListUsingGET_6": "/req/$VERSION$/extfields",  # 查询可用的扩展列名称
    "addExtfieldsUsingPOST_5": "/req/$VERSION$/extfields",  # 添加可扩展列
    "importBusinessUsingPOST_3": "/req/$VERSION$/import",  # 导入业务数据
    "selectBusinessTemplateExportUsingGET_3": "/req/$VERSION$/template/export",  # 导出业务数据模板
    "businessTableUsingPOST_5": "/req/$VERSION$/%s/businessTable",  # 查询业务表格列
    "selectBusinessListUsingPOST_3": "/req/$VERSION$/%s/businesslist",  # 查询业务数据
    "selectFilterListUsingPOST_3": "/req/$VERSION$/%s/filterlist",  # 过滤业务数据
    "releasePlanComfirmUsingPOST_3": "/req/$VERSION$/%s/releasePlanComfirm",  # 发布计划前判断是否可以发布
})


def searchBusinessUsingPOST_3(self, checker=None):
    """
    接口名称：通用查询逻辑
    接口地址：/req/$VERSION$/api/list
    """
    r = RequestService.call_post(apis.get("searchBusinessUsingPOST_3", None), json={
        "elViewDto": ""  # 条件列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectBusinessExportUsingGET_3(self, checker=None):
    """
    接口名称：导出业务数据
    接口地址：/req/$VERSION$/export
    """
    r = RequestService.call_get(apis.get("selectBusinessExportUsingGET_3", None), params={
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


def selectAvlbFieldListUsingGET_6(self, active, checker=None):
    """
    接口名称：查询可用的扩展列名称
    接口地址：/req/$VERSION$/extfields
    """
    r = RequestService.call_get(apis.get("selectAvlbFieldListUsingGET_6", None), params={
        "active": active
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def addExtfieldsUsingPOST_5(self, attrName, attrKey, attrType, typeLength, defaultValue, checker=None):
    """
    接口名称：添加可扩展列
    接口地址：/req/$VERSION$/extfields
    """
    r = RequestService.call_post(apis.get("addExtfieldsUsingPOST_5", None), params={
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


def importBusinessUsingPOST_3(self, checker=None):
    """
    接口名称：导入业务数据
    接口地址：/req/$VERSION$/import
    """
    r = RequestService.call_post(apis.get("importBusinessUsingPOST_3", None), data={
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


def selectBusinessTemplateExportUsingGET_3(self, checker=None):
    """
    接口名称：导出业务数据模板
    接口地址：/req/$VERSION$/template/export
    """
    r = RequestService.call_get(apis.get("selectBusinessTemplateExportUsingGET_3", None), params={
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


def businessTableUsingPOST_5(self, viewid, checker=None):
    """
    接口名称：查询业务表格列
    接口地址：/req/$VERSION$/{viewid}/businessTable
    """
    r = RequestService.call_post(apis.get("businessTableUsingPOST_5", viewid), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectBusinessListUsingPOST_3(self, viewid, viewDto, checker=None):
    """
    接口名称：查询业务数据
    接口地址：/req/$VERSION$/{viewid}/businesslist
    """
    r = RequestService.call_post(apis.get("selectBusinessListUsingPOST_3", viewid), json=viewDto, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectFilterListUsingPOST_3(self, viewid, viewDto, checker=None):
    """
    接口名称：过滤业务数据
    接口地址：/req/$VERSION$/{viewid}/filterlist
    """
    r = RequestService.call_post(apis.get("selectFilterListUsingPOST_3", viewid), json=viewDto,
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def releasePlanComfirmUsingPOST_3(self, checker=None):
    """
    接口名称：发布计划前判断是否可以发布
    接口地址：/req/$VERSION$/{viewid}/releasePlanComfirm
    """
    r = RequestService.call_post(apis.get("releasePlanComfirmUsingPOST_3", None), json={
        "viewDto": ""  # 条件列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

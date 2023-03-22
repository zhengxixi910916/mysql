from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "createUsingPOST_1": "/proj/$VERSION$/dictionary",  # 新增字典定义
    "deleteUsingDELETE_4": "/proj/$VERSION$/dictionary",  # 删除多个字典定义
    "importDictionaryUsingPOST": "/proj/$VERSION$/dictionary/import",  # 导入项目数据字典
    "queryTypeListUsingGET": "/proj/$VERSION$/dictionary/types",  # 获取字典类型列表数据
    "getUsingGET": "/proj/$VERSION$/dictionary/%s",  # 获取字典详情
    "updateUsingPUT_3": "/proj/$VERSION$/dictionary/%s",  # 更新字典定义
    "deleteUsingDELETE_3": "/proj/$VERSION$/dictionary/%s",  # 删除字典定义
    "queryListUsingGET": "/proj/$VERSION$/dictionarys",  # 获取字典列表数据-分页
    "selectListUsingGET": "/proj/$VERSION$/dictionarys/context",  # 获取字典列表数据,根据context相关参数规则获取
})


def createUsingPOST_1(self, typeName, attribute, contextType, contextId, displayCn, displayEn, description, parentId, name, sort, value, checker=None):
    """
    接口名称：新增字典定义
    接口地址：/proj/$VERSION$/dictionary
    """
    r = RequestService.call_post(apis.get("createUsingPOST_1", None), params={
        "attribute": attribute,  # 附加属性 - required: False
        "contextId": contextId,  # 上下文Id，具体某个上下文 - required: False
        "contextType": contextType,  # 上下文类型，System、Organization、Project - required: False
        "description": description,  # 描述 - required: False
        "displayCn": displayCn,  # 中文显示名 - required: False
        "displayEn": displayEn,  # 英文显示名 - required: False
        "name": name,  # 字典名称，唯一 - required: False
        "parentId": parentId,  # 父Id - required: False
        "sort": sort,  # 排序 - required: False
        "typeName": typeName,  # 类型名称 - required: False
        "value": value,  # 数据枚举值，key - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def deleteUsingDELETE_4(self, listIds, checker=None):
    """
    接口名称：删除多个字典定义
    接口地址：/proj/$VERSION$/dictionary
    """
    r = RequestService.call_delete(apis.get("deleteUsingDELETE_4", None), json=listIds, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def importDictionaryUsingPOST(self, contextType, contextId, typeName, attribute, checker=None):
    """
    接口名称：导入项目数据字典
    接口地址：/proj/$VERSION$/dictionary/import
    """
    r = RequestService.call_post(apis.get("importDictionaryUsingPOST", None), params={
        "contextType": contextType,
        "contextId": contextId,
        "typeName": typeName,
        "attribute": attribute
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def queryTypeListUsingGET(self, contextId, checker=None):
    """
    接口名称：获取字典类型列表数据
    接口地址：/proj/$VERSION$/dictionary/types
    """
    r = RequestService.call_get(apis.get("queryTypeListUsingGET", None), params={
        "contextId": contextId  # 上下文id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getUsingGET(self, id, checker=None):
    """
    接口名称：获取字典详情
    接口地址：/proj/$VERSION$/dictionary/{id}
    """
    r = RequestService.call_get(apis.get("getUsingGET", id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def updateUsingPUT_3(self, id, dict, checker=None):
    """
    接口名称：更新字典定义
    接口地址：/proj/$VERSION$/dictionary/{id}
    """
    r = RequestService.call_put(apis.get("updateUsingPUT_3", id), json=dict)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def deleteUsingDELETE_3(self, id, checker=None):
    """
    接口名称：删除字典定义
    接口地址：/proj/$VERSION$/dictionary/{id}
    """
    r = RequestService.call_delete(apis.get("deleteUsingDELETE_3", id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def queryListUsingGET(self, contextType, contextId, displayCn=None, typeName=None, attribute=None, active=None,
                      sortBy=None, orderBy=None, page_size=20, page_index=1, checker=None):
    """
    接口名称：获取字典列表数据-分页
    接口地址：/proj/$VERSION$/dictionarys
    """
    r = RequestService.call_get(apis.get("queryListUsingGET", None), params={
        "contextType": contextType,
        "contextId": contextId,
        "displayCn": displayCn,
        "typeName": typeName,
        "attribute": attribute,
        "active": active,
        "sortBy": sortBy,
        "orderBy": orderBy,
        "pagesize": page_size,
        "pageindex": page_index,
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def selectListUsingGET(self, contextType, contextId, checker=None):
    """
    接口名称：获取字典列表数据,根据context相关参数规则获取
    接口地址：/proj/$VERSION$/dictionarys/context
    """
    r = RequestService.call_get(apis.get("selectListUsingGET", None), params={
        "contextType": contextType,
        "contextId": contextId
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

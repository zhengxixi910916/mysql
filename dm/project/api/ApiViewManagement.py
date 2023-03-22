# -*- coding: utf-8 -*-#
# Author:zhihuimin
# Date:2022/7/6
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "insertViewListUsingPOST": "/proj/basis/$VERSION$/view/",  # 新增视图
    "viewConfigUsingPUT": "/proj/basis/$VERSION$/view/config",  # 个人配置是否禁用-是否默认
    "selectViewByIdUsingGET": "/proj/basis/$VERSION$/view/detail",  # 查询视图详情
    "selectExportFieldUsingGET": "/proj/basis/$VERSION$/view/exportfield",  # 查询导出字段
    "selectViewNameListUsingGET": "/proj/basis/$VERSION$/view/list",  # 查询视图管理列表
    "viewProjectConfigUsingPUT": "/proj/basis/$VERSION$/view/projectconfig",  # 项目配置是否禁用-是否默认
    "selectBusinessListUsingPOST_7": "/proj/basis/$VERSION$/view/query/{viewId}",  # 查询视图ID查询视图信息
    "viewRememberUsingPUT": "/proj/basis/$VERSION$/view/remember",  # 开启关闭是否记住-记住视图
    "viewRememberStateUsingPUT": "/proj/basis/$VERSION$/view/rememberstate",  # 检查是否记住状态
    "selectViewListUsingGET": "/proj/basis/$VERSION$/view/selectlist",  # 获取视图下拉列表
    "updateSortUsingPUT": "/proj/basis/$VERSION$/view/updateSort",  # 排序
    "updateViewUserUsingPUT": "/proj/basis/$VERSION$/view/updateViewUser",  # 配置是否禁用，是否默认，是否公共
    "updateViewListUsingPUT_1": "/proj/basis/$VERSION$/view/%s",  # 更新视图
    "delViewByViewIdUsingDELETE": "/proj/basis/$VERSION$/view/%s",  # 删除视图
    "updateViewSortUsingPUT": "/proj/basis/$VERSION$/view/{id}/sort",  # 更新视图排序
    "updateViewListUsingPUT": "/proj/basis/$VERSION$/view/{id}/viewstate",  # 更新视图是否禁用-是否默认
    "selectAdvancedSearchUsingGET": "/proj/basis/$VERSION$/view/%s/advancedsearch",  # 高级查询字段列表
    "selectViewFieldUsingGET": "/proj/basis/$VERSION$/view/%s/field",  # 查询视图可显示字段
})


def insert_view(self, view_name, checker=None):
    """
    接口名称：新增视图
    接口地址：/proj/basis/$VERSION$/view/
    """
    r = RequestService.call_post(apis.get("insertViewListUsingPOST", None), params={
        "elView.businessType": "erd.cloud.plan.dto.EtTask",
        "elView.conditionRef": "and",
        "elView.name": view_name,
        "elView.projectId": "",
        "elView.selectedFields": "903,59,60,41,30,37,36,503,905,d24b5ba8afc411ec8f810242ac120002,505",
        "elView.contextType": 1,
        "elView.enabled": 0,
        "elView.viewDefault": 0,
        "elView.affiliation": "define",
        "elConditionList[0].fieldId": 30,
        "elConditionList[0].fieldType": "text-static-lifecycle",
        "elConditionList[0].oper": "in",
        "elConditionList[0].value": ",PENDING",
        "elConditionList[0].name": "state",
        "viewUserDto.isDefault": 1,
        "viewUserDto.isPub": 0,
        "viewUserDto.isUse": 0,
        "viewUserDto.businessType": "erd.cloud.plan.dto.EtTask",
        "viewUserDto.type": 2,
        "viewUserDto.contextId": ""
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r['res']['data']
    else:
        apis.check_success(self, r)
        return r['res']['data']


def view_config(self, checker=None):
    """
    接口名称：个人配置是否禁用-是否默认
    接口地址：/proj/basis/$VERSION$/view/config
    """
    r = RequestService.call_put(apis.get("viewConfigUsingPUT", None), params={
        "businesstype": "",  # 业务类型 - required: True
        "contextid": "",  # 项目ID - required: False
        "contexttype": "",  # 1工作台2项目 - required: True
        "state": "",  # 状态yes是no否 - required: True
        "type": "",  # 类型2禁用3默认 - required: True
        "viewid": "",  # 视图ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def select_view(self, view_id, object_id, checker=None):
    """
    接口名称：查询视图详情
    接口地址：/proj/basis/$VERSION$/view/detail
    """
    r = RequestService.call_get(apis.get("selectViewByIdUsingGET", None), params={
        "viewId": view_id,  # 视图Id - required: True
        "viewUserId": object_id,  # 视图用户Id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def select_export_field(self, checker=None):
    """
    接口名称：查询导出字段
    接口地址：/proj/basis/$VERSION$/view/exportfield
    """
    r = RequestService.call_get(apis.get("selectExportFieldUsingGET", None), params={
        "businesstype": ""  # 业务类型 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def select_view_name_list(self, checker=None):
    """
    接口名称：查询视图管理列表
    接口地址：/proj/basis/$VERSION$/view/list
    """
    r = RequestService.call_get(apis.get("selectViewNameListUsingGET", None), params={
        "affiliation": "define",  # 所属人：个人define系统system项目project - required: True
        "businesstype": "erd.cloud.plan.dto.EtTask",  # 业务类型 - required: True
        "contexttype": 1,  # 1工作台2项目 - required: True
        "projectid": "",  # 项目ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r['res']['data']
    else:
        apis.check_success(self, r)
        return r['res']['data']


def view_project_config(self, checker=None):
    """
    接口名称：项目配置是否禁用-是否默认
    接口地址：/proj/basis/$VERSION$/view/projectconfig
    """
    r = RequestService.call_put(apis.get("viewProjectConfigUsingPUT", None), params={
        "businesstype": "",  # 业务类型 - required: True
        "contextid": "",  # 项目ID - required: True
        "state": "",  # 状态yes是no否 - required: True
        "type": "",  # 类型2禁用3默认 - required: True
        "viewid": "",  # 视图ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def select_business_list(self, checker=None):
    """
    接口名称：查询视图ID查询视图信息
    接口地址：/proj/basis/$VERSION$/view/query/{viewId}
    """
    r = RequestService.call_post(apis.get("selectBusinessListUsingPOST_7", None))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def view_remember(self, checker=None):
    """
    接口名称：开启关闭是否记住-记住视图
    接口地址：/proj/basis/$VERSION$/view/remember
    """
    r = RequestService.call_put(apis.get("viewRememberUsingPUT", None), params={
        "businesstype": "erd.cloud.plan.dto.EtTask",  # 业务类型 - required: True
        "contextid": "",  # 项目ID - required: False
        "contexttype": 1,  # 1工作台2项目 - required: True
        "state": "yes",  # 状态yes是no否 - required: True
        "viewid": "",  # 视图ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def view_remember_state(self, checker=None):
    """
    接口名称：检查是否记住状态
    接口地址：/proj/basis/$VERSION$/view/rememberstate
    """
    r = RequestService.call_put(apis.get("viewRememberStateUsingPUT", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def select_view_list(self, checker=None):
    """
    接口名称：获取视图下拉列表
    接口地址：/proj/basis/$VERSION$/view/selectlist
    """
    r = RequestService.call_get(apis.get("selectViewListUsingGET", None), params={
        "businesstype": "erd.cloud.plan.dto.EtTask",  # 业务类型 - required: True
        "contexttype": 1,  # 1工作台2项目 - required: True
        "projectid": "",  # 项目ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def update_sort(self, object_id_list, checker=None):
    """
    接口名称：排序
    接口地址：/proj/basis/$VERSION$/view/updateSort
    """
    r = RequestService.call_put(apis.get("updateSortUsingPUT", None), json=object_id_list, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def update_view_user(self, object_id, checker=None):
    """
    接口名称：配置是否禁用，是否默认，是否公共
    接口地址：/proj/basis/$VERSION$/view/updateViewUser
    """
    r = RequestService.call_put(apis.get("updateViewUserUsingPUT", None),
                                params={
                                    "id": object_id,  # 视图用户关联id - required: True
                                    "type": "0",  # 类型 - required: True
                                    "value": "0",  # 修改值 - required: True
                                    "contextid": ""
                                }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def update_view(self, view_id, view_name, object_id, checker=None):
    """
    接口名称：更新视图
    接口地址：/proj/basis/$VERSION$/view/{id}
    """
    r = RequestService.call_put(apis.get("updateViewListUsingPUT_1", view_id), json={
        "elConditionList": [{
            "fieldId": "30",
            "fieldType": "text-static-lifecycle",
            "oper": "in",
            "value": ",PENDING",
            "name": "state"
        }],
        "elView": {
            "affiliation": "system",
            "businessType": "erd.cloud.plan.dto.EtTask",
            "conditionRef": "and",
            "enabled": "0",
            "name": view_name,
            "projectId": "",
            "selectedFields": "903,59,60,41,30,37,36,503,905,d24b5ba8afc411ec8f810242ac120002,505",
            "viewDefault": "0"
        },
        "viewUserDto": {
            "businessType": "erd.cloud.plan.dto.EtTask",
            "contextId": "",
            "id": object_id,
            "isDefault": 1,
            "isPub": 1,
            "isUse": 0,
            "type": 0
        }
        # 视图信息 - required: False
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def del_view(self, object_id, checker=None):
    """
    接口名称：删除视图
    接口地址：/proj/basis/$VERSION$/view/{id}
    """
    r = RequestService.call_delete(apis.get("delViewByViewIdUsingDELETE", object_id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def update_view_sort(self, checker=None):
    """
    接口名称：更新视图排序
    接口地址：/proj/basis/$VERSION$/view/{id}/sort
    """
    r = RequestService.call_put(apis.get("updateViewSortUsingPUT", None), params={
        "selectedFields": ""  # 排序结果 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def update_view_list(self, checker=None):
    """
    接口名称：更新视图是否禁用-是否默认
    接口地址：/proj/basis/$VERSION$/view/{id}/viewstate
    """
    r = RequestService.call_put(apis.get("updateViewListUsingPUT", None), json={
        "etView": ""  # 视图 - required: False
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def select_advanced_search(self, view_type, checker=None):
    """
    接口名称：高级查询字段列表
    接口地址：/proj/basis/$VERSION$/view/{type}/advancedsearch
    """
    r = RequestService.call_get(apis.get("selectAdvancedSearchUsingGET", view_type))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def select_view_field(self, view_type, checker=None):
    """
    接口名称：查询视图可显示字段
    接口地址：/proj/basis/$VERSION$/view/{type}/field
    """
    r = RequestService.call_get(apis.get("selectViewFieldUsingGET", view_type))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

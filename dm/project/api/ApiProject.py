import datetime
import os
import time
from contextlib import closing

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目信息
'''

# 获取上一级目录
dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dir_document = dir_path + r'/document'
times = time.strftime("%Y-%m-%d %H %M %S", time.localtime(time.time()))
file_name = "project_" + times + ".xlsx"
finish_time = datetime.datetime.now().replace(year=datetime.datetime.now().year+1).strftime("%Y-%m-%d")
apis = Api({
    "getUserAclUsingGET": "/proj/$VERSION$/acl/sys/%s",  # 获取用户项目权限
    "careMyProjectUsingPOST_1": "/proj/$VERSION$/addMyCareProject",  # 收藏项目/取消收藏
    "addProjectMyOpenUsingPOST": "/proj/$VERSION$/addProjectMyOpen/%s",  # 添加项目查看记录（用于导航栏查看项目）
    "searchBusinessUsingPOST_2": "/proj/$VERSION$/api/list",  # 通用查询逻辑
    "selectAvlbFieldListUsingGET_2": "/proj/$VERSION$/avlbfields",  # 查询可用的扩展列名称
    "closeUsingPOST": "/proj/$VERSION$/close",  # 关闭项目
    "selectBusinessExportUsingGET_2": "/proj/$VERSION$/export",  # 导出业务数据
    "selectAvlbFieldListUsingGET_3": "/proj/$VERSION$/extfields",  # 查询可用的扩展列名称
    "addExtfieldsUsingPOST_2": "/proj/$VERSION$/extfields",  # 添加可扩展列
    "getMyAdministrationProjectUsingGET": "/proj/$VERSION$/getMyAdministrationProject",  # 获取我最近打开的项目
    "getMyCareProjectUsingGET": "/proj/$VERSION$/getMyCareProject",  # 获取我收藏的项目
    "importBusinessUsingPOST_2": "/proj/$VERSION$/import",  # 导入业务数据
    "getMemberByNameUsingGET": "/proj/$VERSION$/members",  # 查询成员
    "pageProjectUsingGET": "/proj/$VERSION$/pageProject",  # 根据条件查询项目信息列表（不权限控制）
    "addProjectUsingPOST_1": "/proj/$VERSION$/project",  # 保存项目基本信息
    "updateProjectUsingPUT": "/proj/$VERSION$/project",  # 更新项目信息
    "getBascDataByTypeUsingGET": "/proj/$VERSION$/project/dict",  # 获取数据字典
    "exportProjectListUsingGET": "/proj/$VERSION$/project/export",  # 导出项目列表数据
    "exportTemplateUsingGET": "/proj/$VERSION$/project/export/template",  # 导出数据模板
    "importProjectUsingPOST": "/proj/$VERSION$/project/import/excel",  # 导入项目基础数据
    "getProjecByIdUsingGET": "/proj/$VERSION$/project/%s",  # 根据项目ID查询项目基本信息
    "updateProjectFileUsingPUT": "/proj/$VERSION$/project/%s/archived",  # 项目归档
    "getChildrenByIdUsingGET": "/proj/$VERSION$/project/%s/children",  # 根据项目ID获取下一层子项目
    "getDelayTaskByproject_idUsingGET": "/proj/$VERSION$/project/%s/delay",  # 延误率(延误率=延误任务数/计划完成任务数)
    "getProjectByNameOrCodeUsingGET": "/proj/$VERSION$/project/%s/keyword",  # 根据项目名称或编码查询项目详情列表
    "deleteParentLinkUsingPUT": "/proj/$VERSION$/project/%s/link",  # 根据子项目ID解除父子关系
    "getProjectProgressByIdUsingGET": "/proj/$VERSION$/project/%s/progress",  # 项目进度(已完成任务/总任务数)
    "getPorjectInfoByProcessInstanceIdUsingGET": "/proj/$VERSION$/project/%s",  # 根据流程的id查询实体对象的详情
    "getProjectListUsingGET": "/proj/$VERSION$/projects",  # 根据当前用户查询项目信息列表
    "getAllProjectListUsingGET": "/proj/$VERSION$/projects/all",  # 获取所有项目详细信息列表
    "getIsFileProjectUsingGET": "/proj/$VERSION$/projects/archived",  # 获取归档项目
    "getProjectListByExtUsingPOST": "/proj/$VERSION$/projects/ext",  # 根据当前用户查询项目信息列表支持扩展字段
    "addChildrenUsingPOST": "/proj/$VERSION$/projects/%s/children",  # 批量添加子项目
    "updateChildrenLinkUsingPUT": "/proj/$VERSION$/projects/%s/children",  # 根据项目ID、子项目ID串更新项目父子关系
    "getProjectTreeUsingGET": "/proj/$VERSION$/projects/%s/tree",  # 根据项目id获取树形子孙项目详情数据
    "projectPublishUsingPOST": "/proj/$VERSION$/publish",  # 发布项目计划
    "searchProjectListUsingGET": "/proj/$VERSION$/searchProjects",  # 根据当前用户高级查询项目信息列表
    "updateStateFlowMembersUsingPUT_1": "/proj/$VERSION$/stateflow/members",  # 修改状态流程成员
    "selectBusinessTemplateExportUsingGET_2": "/proj/$VERSION$/template/export",  # 导出业务数据模板
    "updateProjectCompatibleWorkflowUsingPUT": "/proj/$VERSION$/workflow/project",  # 更新项目信息(兼容流程处理人可修改)
    "deleteProjectUsingDELETE": "/proj/$VERSION$/%s",  # 删除项目
    "getProjectCloseAccessUsingGET": "/proj/$VERSION$/%s/close/validate",  # 根据项目ID判断项目是否支持关闭
    "getTempFirstNodeStateByIdUsingGET": "/proj/$VERSION$/%s/state/firststate",  # 根据模板ID获取项目模板的第一个节点状态
    "businessTableUsingPOST_2": "/proj/$VERSION$/%s/businessTable",  # 查询业务表格列
    "selectBusinessListUsingPOST_2": "/proj/$VERSION$/%s/businesslist",  # 查询业务数据
    "selectFilterListUsingPOST_2": "/proj/$VERSION$/%s/filterlist",  # 过滤业务数据
    "releasePlanComfirmUsingPOST_2": "/proj/$VERSION$/%s/releasePlanComfirm",  # 发布计划前判断是否可以发布
    "projAppBasicConfigUsingGET": "/proj/$VERSION$/basic/config/one",  # 查询单个系统应用基础配置
    "pageProjAppBasicConfigUsingGET": "/proj/$VERSION$/basic/config/page",  # 分页查询系统应用基础配置
    "getChangeMemberLogConfigUsingGET": "/proj/$VERSION$/changeMemberLogConfig/%s",  # 根据项目ID查询更换成员的配置
    "getProjectByNameOrCodePageUsingGET": "/proj/$VERSION$/project/%s/keyword/page",  # 根据项目名称或编码查询项目详情列表(分页展示)
    "updateApplicationConfigUsingPUT": "/proj/$VERSION$/basic/config/%s/update",  # 修改系统应用配置

})


def updateApplicationConfigUsingPUT(self, project_id, basicConfig, checker=None):
    """
    接口名称：修改系统应用配置
    接口地址：/proj/$VERSION$/basic/config/{project_id}/update
    """
    r = RequestService.call_put(apis.get("updateApplicationConfigUsingPUT", project_id), json=basicConfig
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getProjectByNameOrCodePageUsingGET(self, project_id, hasParent, keyword, page_index, page_size, checker=None):
    """
    接口名称：根据项目名称或编码查询项目详情列表(分页展示)
    接口地址：/proj/$VERSION$/project/{id}/keyword/page
    """
    r = RequestService.call_get(apis.get("getProjectByNameOrCodePageUsingGET", project_id), params={
        "hasParent": hasParent,  # 有无父项目（0：无父项目，1：有父项目，2：不限，其它：非法） - required: True
        "keyword": keyword,  # 查询关键字 - required: False
        "pageindex": page_index,  # page_index - required: False
        "pagesize": page_size,  # page_size - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getChangeMemberLogConfigUsingGET(self, project_id, checker=None):
    """
    接口名称：根据项目ID查询更换成员的配置
    接口地址：/proj/$VERSION$/changeMemberLogConfig/{project_id}
    """
    r = RequestService.call_get(apis.get("getChangeMemberLogConfigUsingGET", project_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def pageProjAppBasicConfigUsingGET(self, page_index=1, page_size=10, checker=None):
    """
    接口名称：分页查询系统应用基础配置
    接口地址：/proj/$VERSION$/basic/config/page
    """
    r = RequestService.call_get(apis.get("pageProjAppBasicConfigUsingGET", None), params={
        "pageindex": page_index,  # 页码 - required: True
        "pagesize": page_size,  # 每页数量 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def projAppBasicConfigUsingGET(self, project_id, checker=None):
    """
    接口名称：查询单个系统应用基础配置
    接口地址：/proj/$VERSION$/basic/config/one
    """
    r = RequestService.call_get(apis.get("projAppBasicConfigUsingGET", None), params={
        "projectId": project_id  # 项目id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getUserAclUsingGET(self, userId, project_id, checker=None):
    """
    接口名称：获取用户项目权限
    接口地址：/proj/$VERSION$/acl/sys/{userId}
    """
    r = RequestService.call_get(apis.get("getUserAclUsingGET", userId), params={
        "projectId": project_id  # 项目ID - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def careMyProjectUsingPOST_1(self, project_id, project_name, checker=None):
    """
    接口名称：收藏项目/取消收藏
    接口地址：/proj/$VERSION$/addMyCareProject
    """
    r = RequestService.call_post(apis.get("careMyProjectUsingPOST_1"), params={
        "projectId": project_id,  # 项目id - required: True
        "projectName": project_name,  # 项目名称 - required: True
        "typeId": 1,  # 收藏类型(3:最近打开的;2:我关注的; 1:我收藏的 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r['res']["data"]
    else:
        apis.check_success(self, r)
        return r['res']["data"]


def addProjectMyOpenUsingPOST(self, project_id, checker=None):
    """
    接口名称：添加项目查看记录（用于导航栏查看项目）
    接口地址：/proj/$VERSION$/addProjectMyOpen/{project_id}
    """
    r = RequestService.call_post(apis.get("addProjectMyOpenUsingPOST", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def searchBusinessUsingPOST_2(self, checker=None):
    """
    接口名称：通用查询逻辑
    接口地址：/proj/$VERSION$/api/list
    """
    r = RequestService.call_post(apis.get("searchBusinessUsingPOST_2"), json={
        "elViewDto": ""  # 条件列表 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def selectAvlbFieldListUsingGET_2(self, checker=None):
    """
    接口名称：查询可用的扩展列名称
    接口地址：/proj/$VERSION$/avlbfields
    """
    r = RequestService.call_get(apis.get("selectAvlbFieldListUsingGET_2"), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def closeUsingPOST(self, checker=None):
    """
    接口名称：关闭项目
    接口地址：/proj/$VERSION$/close
    """
    r = RequestService.call_post(apis.get("closeUsingPOST"), json={
        "params": ""  # params - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def selectBusinessExportUsingGET_2(self, checker=None):
    """
    接口名称：导出业务数据
    接口地址：/proj/$VERSION$/export
    """
    r = RequestService.call_get(apis.get("selectBusinessExportUsingGET_2"), params={
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
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def selectAvlbFieldListUsingGET_3(self, active, checker=None):
    """
    接口名称：查询可用的扩展列名称
    接口地址：/proj/$VERSION$/extfields
    """
    r = RequestService.call_get(apis.get("selectAvlbFieldListUsingGET_3"), params={
        "active": active  # 列状态1已使用0未使用，空所有 - required: False
    },
                                )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def addExtfieldsUsingPOST_2(self, checker=None):
    """
    接口名称：添加可扩展列
    接口地址：/proj/$VERSION$/extfields
    """
    r = RequestService.call_post(apis.get("addExtfieldsUsingPOST_2"), params={
        "asc": "",  # None - required: False
        "ascs": "",  # None - required: False
        "current": "",  # 当前分页，默认1 - required: False
        "deployState": "",  # None - required: False
        "description": "",  # None - required: False
        "descs": "",  # None - required: False
        "entityAlias": "",  # None - required: False
        "entityAttrs[0].attrKey": "",  # None - required: False
        "entityAttrs[0].attrName": "",  # None - required: False
        "entityAttrs[0].attrType": "",  # None - required: False
        "entityAttrs[0].available": "",  # None - required: False
        "entityAttrs[0].createBy": "",  # 创建者 - required: False
        "entityAttrs[0].createTime": "",  # 创建时间 - required: False
        "entityAttrs[0].dataFormat": "",  # None - required: False
        "entityAttrs[0].defaultValue": "",  # None - required: False
        "entityAttrs[0].delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "entityAttrs[0].entityId": "",  # None - required: False
        "entityAttrs[0].id": "",  # 对象Id - required: False
        "entityAttrs[0].required": "",  # None - required: False
        "entityAttrs[0].typeLength": "",  # None - required: False
        "entityAttrs[0].updateBy": "",  # 更新者 - required: False
        "entityAttrs[0].updateTime": "",  # 更新 - required: False
        "entityTable": "",  # None - required: False
        "entityTitle": "",  # None - required: False
        "limit": "",  # None - required: False
        "newColumnDtoList[0].attrKey": "",  # None - required: False
        "newColumnDtoList[0].attrName": "",  # None - required: False
        "newColumnDtoList[0].attrType": "",  # None - required: False
        "newColumnDtoList[0].available": "",  # None - required: False
        "newColumnDtoList[0].createBy": "",  # 创建者 - required: False
        "newColumnDtoList[0].createTime": "",  # 创建时间 - required: False
        "newColumnDtoList[0].dataFormat": "",  # None - required: False
        "newColumnDtoList[0].defaultValue": "",  # None - required: False
        "newColumnDtoList[0].delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "newColumnDtoList[0].entityId": "",  # None - required: False
        "newColumnDtoList[0].id": "",  # 对象Id - required: False
        "newColumnDtoList[0].required": "",  # None - required: False
        "newColumnDtoList[0].typeLength": "",  # None - required: False
        "newColumnDtoList[0].updateBy": "",  # 更新者 - required: False
        "newColumnDtoList[0].updateTime": "",  # 更新 - required: False
        "offset": "",  # None - required: False
        "oldColumnDtoList[0].attrKey": "",  # None - required: False
        "oldColumnDtoList[0].attrName": "",  # None - required: False
        "oldColumnDtoList[0].attrType": "",  # None - required: False
        "oldColumnDtoList[0].available": "",  # None - required: False
        "oldColumnDtoList[0].createBy": "",  # 创建者 - required: False
        "oldColumnDtoList[0].createTime": "",  # 创建时间 - required: False
        "oldColumnDtoList[0].dataFormat": "",  # None - required: False
        "oldColumnDtoList[0].defaultValue": "",  # None - required: False
        "oldColumnDtoList[0].delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "oldColumnDtoList[0].entityId": "",  # None - required: False
        "oldColumnDtoList[0].id": "",  # 对象Id - required: False
        "oldColumnDtoList[0].required": "",  # None - required: False
        "oldColumnDtoList[0].typeLength": "",  # None - required: False
        "oldColumnDtoList[0].updateBy": "",  # 更新者 - required: False
        "oldColumnDtoList[0].updateTime": "",  # 更新 - required: False
        "openSort": "",  # None - required: False
        "optimizeCountSql": "",  # None - required: False
        "orderByField": "",  # None - required: False
        "pages": "",  # 总数 - required: False
        "records": "",  # None - required: False
        "searchCount": "",  # None - required: False
        "size": "",  # 分页数量，默认10 - required: False
        "tableCharacterSet": "",  # None - required: False
        "total": "",  # None - required: False
        "tplJson": "",  # None - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getMyAdministrationProjectUsingGET(self, checker=None):
    """
    接口名称：获取我最近打开的项目
    接口地址：/proj/$VERSION$/getMyAdministrationProject
    """
    r = RequestService.call_get(apis.get("getMyAdministrationProjectUsingGET"), params={
        "name": "",  # 项目名称 - required: False
        "pageNo": "",  # pageNo - required: False
        "pagesize": "",  # page_size - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getMyCareProjectUsingGET(self, project_name, checker=None):
    """
    接口名称：获取我收藏的项目
    接口地址：/proj/$VERSION$/getMyCareProject
    """
    r = RequestService.call_get(apis.get("getMyCareProjectUsingGET"), params={
        "name": project_name  # 项目名称 - required: False
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
    接口地址：/proj/$VERSION$/import
    """
    r = RequestService.call_post(apis.get("importBusinessUsingPOST_2"), data={
        "file": ""  # file - required: True
    }, params={
        "businessType": "",  # 业务对象 - required: True
        "projectId": "",  # 项目ID - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getMemberByNameUsingGET(self, condition):
    """
    接口名称：查询成员
    接口地址：/proj/$VERSION$/members
    """
    r = RequestService.call_get(apis.get("getMemberByNameUsingGET"), params={
        "condition": condition,
    })


def pageProjectUsingGET(self, name, project_ids, state, type, checker=None):
    """
    接口名称：根据条件查询项目信息列表（不权限控制）
    接口地址：/proj/$VERSION$/pageProject
    """
    r = RequestService.call_get(apis.get("pageProjectUsingGET"), params={
        "createBy": "SYS_E39B20EA11E7A81AC85B767C89C1",  # 创建人（多个状态以逗号分隔） - required: False
        "name": name,  # 项目名称 - required: False
        "order_by": 'create_time',  # 排序字段，默认修改时间 - required: False
        "pageindex": 1,  # 页码 - required: False
        "pagesize": 10,  # 每页条数 - required: False
        "pmId": "SYS_E39B20EA11E7A81AC85B767C89C1",  # 项目经理（多个状态以逗号分隔） - required: False
        "project_ids": project_ids,  # 项目ids（多个状态以逗号分隔） - required: False
        "sort_by": 'DESC',  # 排序方式，默认倒序 - required: False
        "state": state,  # 项目状态（多个状态以逗号分隔） - required: False
        "type": type,  # 类型（多个状态以逗号分隔） - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def addProjectUsingPOST_1(self, name, checker=None):
    """
    接口名称：保存项目基本信息
    接口地址：/proj/$VERSION$/project
    """
    r = RequestService.call_post(apis.get("addProjectUsingPOST_1"), params={
        "type": "ITProject",
        "templateId": "",
        "name": name,
        "state": "PLANNING",
        "projCategory": "category",
        "startTime": time.strftime('%Y-%m-%d', time.localtime()),
        "finishTime": finish_time,
        "pmId": 'SYS_E39B20EA11E7A81AC85B767C89C1',
        "extStringValue15": '0',
        "flexAttrs[extStringValue15]": "0",
        "description": "description_" + time.strftime('%Y-%m-%d', time.localtime()),
        "productId": "0094d641626eb400e57d78583f5e5018",

    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateProjectUsingPUT(self, project_code, project_id, project_name, checker=None):
    """
    接口名称：更新项目信息
    接口地址：/proj/$VERSION$/project
    """
    r = RequestService.call_put(apis.get("updateProjectUsingPUT"),
                                json={"type": "STANDARD", "templateId": "", "code": project_code, "name": project_name,
                                      "projCategory": "category",
                                      "state": "PLANNING", "startTime": time.strftime('%Y-%m-%d', time.localtime()), "finishTime":"2031-01-01",
                                      "pmId": "SYS_E39B20EA11E7A81AC85B767C89C1", "topProjectSN": "0",
                                      "productId": "0094d641626eb400e57d78583f5e5018", "phase": "0",
                                      "description": "description_" + time.strftime('%Y-%m-%d', time.localtime()),
                                      "closeReason": "23131321", "flexAttrs": {}, "contextType": "Project",
                                      "id": project_id,
                                      "parentId": "-1"},
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getBascDataByTypeUsingGET(self, attribute, type, checker=None):
    """
    接口名称：获取数据字典
    接口地址：/proj/$VERSION$/project/dict
    """
    r = RequestService.call_get(apis.get("getBascDataByTypeUsingGET"), params={
        "attribute": attribute,  # 附加属性 - required: False
        "type": type,  # 类型 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def exportProjectListUsingGET(self, exprotList, exportIdList=None):
    """
    接口名称：导出项目列表数据
    接口地址：/proj/$VERSION$/project/export
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("exportProjectListUsingGET"), params={
        "exprotList": exprotList,
        "exportIdList": exportIdList
    })) as response:
        with open(dir_document + r"\export_project_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def exportTemplateUsingGET(self, checker=None):
    """
    接口名称：导出数据模板
    接口地址：/proj/$VERSION$/project/export/template
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("exportTemplateUsingGET"))) as response:
        with open(dir_document + r"\export_proj_tem_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def importProjectUsingPOST(self, checker=None):
    """
    接口名称：导入项目基础数据
    接口地址：/proj/$VERSION$/project/import/excel
    """
    r = RequestService.call_post(apis.get("importProjectUsingPOST"), data={
        "file": ""  # file - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getProjecByIdUsingGET(self, project_id, checker=None):
    """
    接口名称： 根据项目ID查询项目基本信息
    接口地址：/proj/$VERSION$/project/{id}
    """
    r = RequestService.call_get(apis.get("getProjecByIdUsingGET", project_id),
                                # json= {
                                #                    "procInstId": ""  # 流程实例Id - required: False
                                # },
                                params={
                                    "isTemplate": ""  # 是否项目模板 - required: False
                                })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateProjectFileUsingPUT(self, project_id, checker=None):
    """
    接口名称：项目归档
    接口地址：/proj/$VERSION$/project/{id}/archived
    """
    r = RequestService.call_put(apis.get("updateProjectFileUsingPUT", project_id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getChildrenByIdUsingGET(self, project_id, checker=None):
    """
    接口名称：根据项目ID获取下一层子项目
    接口地址：/proj/$VERSION$/project/{id}/children
    """
    r = RequestService.call_get(apis.get("getChildrenByIdUsingGET", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getDelayTaskByproject_idUsingGET(self, project_id, checker=None):
    """
    接口名称：延误率(延误率=延误任务数/计划完成任务数)
    接口地址：/proj/$VERSION$/project/{id}/delay
    """
    r = RequestService.call_get(apis.get("getDelayTaskByproject_idUsingGET", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getProjectByNameOrCodeUsingGET(self, project_id, hasParent, keyword, checker=None):
    """
    接口名称：根据项目名称或编码查询项目详情列表
    接口地址：/proj/$VERSION$/project/{id}/keyword
    """
    r = RequestService.call_get(apis.get("getProjectByNameOrCodeUsingGET", project_id), params={
        "hasParent": hasParent,  # 有无父项目（0：无父项目，1：有父项目，2：不限，其它：非法） - required: True
        "keyword": keyword,  # 查询关键字 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteParentLinkUsingPUT(self, children_ids, checker=None):
    """
    接口名称：根据子项目ID解除父子关系
    接口地址：/proj/$VERSION$/project/{id}/link
    """
    r = RequestService.call_put(apis.get("deleteParentLinkUsingPUT", children_ids))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getProjectProgressByIdUsingGET(self, project_id, checker=None):
    """
    接口名称：项目进度(已完成任务/总任务数)
    接口地址：/proj/$VERSION$/project/{id}/progress
    """
    r = RequestService.call_get(apis.get("getProjectProgressByIdUsingGET", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getPorjectInfoByProcessInstanceIdUsingGET(self, processInstanceId, checker=None):
    """
    接口名称：根据流程的id查询实体对象的详情
    接口地址：/proj/$VERSION$/project_id/{processInstanceId}
    """
    r = RequestService.call_get(apis.get("getPorjectInfoByProcessInstanceIdUsingGET", processInstanceId))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']


def getProjectListUsingGET(self, checker=None):
    """
    接口名称：根据当前用户查询项目信息列表
    接口地址：/proj/$VERSION$/projects
    """
    r = RequestService.call_get(apis.get("getProjectListUsingGET"),
                                #                 json= {
                                #     "viewDto": ""  # 扩展属性条件列表 - required: False
                                # }
                                params={
                                    "archivedFlag": "",  # 是否归档【空或者0，全部（默认）；1.归档；2.未归档】 - required: False
                                    "code": "",  # 项目编码 - required: False
                                    "contextType": 0,  # 项目/项目机会 【1】项目;【2】项目机会 - required: False
                                    "createBy": "",  # 创建人（多个状态以逗号分隔） - required: False
                                    "name": "",  # 项目名称 - required: False
                                    "order_by": "",  # 排序字段，默认修改时间 - required: False
                                    "pageindex": 1,  # 页码 - required: False
                                    "pagesize": 10000,  # 每页条数 - required: False
                                    "pmId": "",  # 项目经理（多个状态以逗号分隔） - required: False
                                    "sort_by": "",  # 排序方式，默认倒序 - required: False
                                    "state": "",  # 项目状态 - required: False
                                    "type": "",  # 类型（多个状态以逗号分隔） - required: False
                                })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getAllProjectListUsingGET(self, checker=None):
    """
    接口名称：获取所有项目详细信息列表
    接口地址：/proj/$VERSION$/projects/all
    """
    r = RequestService.call_get(apis.get("getAllProjectListUsingGET"), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getIsFileProjectUsingGET(self, name=None, checker=None):
    """
    接口名称：获取归档项目
    接口地址：/proj/$VERSION$/projects/archived
    """
    r = RequestService.call_get(apis.get("getIsFileProjectUsingGET"), params={
        "name": name  # 项目名称 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getProjectListByExtUsingPOST(self, viewDto, page_index=1, page_size=10, archivedFlag=None, code=None,
                                 contextType=None,
                                 createBy=None, name=None, order_by=None, pmId=None, sort_by=None, state=None,
                                 type=None, checker=None):
    """
    接口名称：根据当前用户查询项目信息列表支持扩展字段
    接口地址：/proj/$VERSION$/projects/ext
    """
    r = RequestService.call_post(apis.get("getProjectListByExtUsingPOST"), json={
        "viewDto": viewDto  # 扩展属性条件列表 - required: False
    }, params={
        "archivedFlag": archivedFlag,  # 是否归档【空或者0，全部（默认）；1.归档；2.未归档】 - required: False
        "code": code,  # 项目编码 - required: False
        "contextType": contextType,  # 项目/项目机会 【1】项目;【2】项目机会 - required: False
        "createBy": createBy,  # 创建人（多个状态以逗号分隔） - required: False
        "name": name,  # 项目名称 - required: False
        "order_by": order_by,  # 排序字段，默认修改时间 - required: False
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
        "pmId": pmId,  # 项目经理（多个状态以逗号分隔） - required: False
        "sort_by": sort_by,  # 排序方式，默认倒序 - required: False
        "state": state,  # 项目状态 - required: False
        "type": type,  # 类型（多个状态以逗号分隔） - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def addChildrenUsingPOST(self, project_id, children_ids, checker=None):
    """
    接口名称：批量添加子项目
    接口地址：/proj/$VERSION$/projects/{id}/children
    """
    r = RequestService.call_post(apis.get("addChildrenUsingPOST", project_id), params={
        "childrenIds": children_ids  # 子项目id字符串（多个子项目id以分号分隔） - required: True
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def updateChildrenLinkUsingPUT(self, projectsId, childrenIds, checker=None):
    """
    接口名称：根据项目ID、子项目ID串更新项目父子关系
    接口地址：/proj/$VERSION$/projects/{id}/children
    """
    r = RequestService.call_put(apis.get("updateChildrenLinkUsingPUT", projectsId), params={
        "childrenIds": childrenIds  # 子项目id串，以分号分隔 - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getProjectTreeUsingGET(self, project_id, checker=None):
    """
    接口名称：根据项目id获取树形子孙项目详情数据
    接口地址：/proj/$VERSION$/projects/{id}/tree
    """
    r = RequestService.call_get(apis.get("getProjectTreeUsingGET", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def projectPublishUsingPOST(self, checker=None):
    """
    接口名称：发布项目计划
    接口地址：/proj/$VERSION$/publish
    """
    r = RequestService.call_post(apis.get("projectPublishUsingPOST"), json={
        "params": ""  # params - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def searchProjectListUsingGET(self, condition, conditionRef, order_by, page_index, page_size, sort_by, checker=None):
    """
    接口名称：根据当前用户高级查询项目信息列表
    接口地址：/proj/$VERSION$/searchProjects
    """
    r = RequestService.call_get(apis.get("searchProjectListUsingGET"), params={
        "condition": condition,  # 搜索条件 - required: False
        "conditionRef": conditionRef,  # 搜索条件之间关系 - required: False
        "order_by": order_by,  # 排序字段，默认修改时间 - required: False
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
        "sort_by": sort_by,  # 排序方式，默认倒序 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateStateFlowMembersUsingPUT_1(self, checker=None):
    """
    接口名称：修改状态流程成员
    接口地址：/proj/$VERSION$/stateflow/members
    """
    r = RequestService.call_put(apis.get("updateStateFlowMembersUsingPUT_1"), json={
        "members": ""  # members - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def selectBusinessTemplateExportUsingGET_2(self, checker=None):
    """
    接口名称：导出业务数据模板
    接口地址：/proj/$VERSION$/template/export
    """
    r = RequestService.call_get(apis.get("selectBusinessTemplateExportUsingGET_2"), params={
        "businessType": "",  # 业务对象 - required: True
        "exprotList": "",  # 导出字段 - required: True
        "projectId": "",  # 项目ID - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateProjectCompatibleWorkflowUsingPUT(self, checker=None):
    """
    接口名称：更新项目信息(兼容流程处理人可修改)
    接口地址：/proj/$VERSION$/workflow/project
    """
    r = RequestService.call_put(apis.get("updateProjectCompatibleWorkflowUsingPUT"), json={
        "procInstId": "",  # 流程实例Id - required: False
        "project": "",  # 项目信息 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteProjectUsingDELETE(self, project_id, checker=None):
    """
    接口名称：删除项目
    接口地址：/proj/$VERSION$/{id}
    """
    r = RequestService.call_delete(apis.get("deleteProjectUsingDELETE", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getProjectCloseAccessUsingGET(self, project_id, checker=None):
    """
    接口名称： 根据项目ID判断项目是否支持关闭
    接口地址：/proj/$VERSION$/{id}/close/validate
    """
    r = RequestService.call_get(apis.get("getProjectCloseAccessUsingGET", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getTempFirstNodeStateByIdUsingGET(self, type, checker=None):
    """
    接口名称：根据模板ID获取项目模板的第一个节点状态
    接口地址：/proj/$VERSION$/{type}/state/firststate
    """
    r = RequestService.call_get(apis.get("getTempFirstNodeStateByIdUsingGET", type))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def businessTableUsingPOST_2(self, viewid, checker=None):
    """
    接口名称：查询业务表格列
    接口地址：/proj/$VERSION$/{viewid}/businessTable
    """
    r = RequestService.call_post(apis.get("businessTableUsingPOST_2", viewid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']


def selectBusinessListUsingPOST_2(self, checker=None):
    """
    接口名称：查询业务数据
    接口地址：/proj/$VERSION$/{viewid}/businesslist
    """
    r = RequestService.call_post(apis.get("selectBusinessListUsingPOST_2"), json={
        "viewDto": ""  # 条件列表 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def selectFilterListUsingPOST_2(self, checker=None):
    """
    接口名称：过滤业务数据
    接口地址：/proj/$VERSION$/{viewid}/filterlist
    """
    r = RequestService.call_post(apis.get("selectFilterListUsingPOST_2"), json={
        "viewDto": ""  # 条件列表 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def releasePlanComfirmUsingPOST_2(self, checker=None):
    """
    接口名称：发布计划前判断是否可以发布
    接口地址：/proj/$VERSION$/{viewid}/releasePlanComfirm
    """
    r = RequestService.call_post(apis.get("releasePlanComfirmUsingPOST_2"), json={
        "viewDto": ""  # 条件列表 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

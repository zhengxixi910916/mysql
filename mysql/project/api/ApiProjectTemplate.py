from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目模板
'''
apis = Api({
    "allTemplatesUsingGET": "/proj/$VERSION$/alltemplates",  # 查询所有的模板
    "mytemplatesUsingGET": "/proj/$VERSION$/mytemplates",  # 查询所有我创建的模板
    "getAllProjecTemplatetListUsingGET": "/proj/$VERSION$/projects/all/template",  # 获取所有项目模板详细信息列表
    "addProjectTemplateUsingPOST": "/proj/$VERSION$/template",  # 保存项目模板基本信息并根据配置表和项目类型生成相应计划类型
    "replaceProjectTemplateUsingPOST": "/proj/$VERSION$/template/information/%s",  # 替换项目模板内容
    "getProjectTemplateListUsingGET": "/proj/$VERSION$/template/list",  # 项目模板列表接口
    "deleteTemplateUsingDELETE": "/proj/$VERSION$/template/%s",  # 删除项目模板
    "updateDefaultTemplateUsingPUT": "/proj/$VERSION$/project/defaultTemplate",  # 更新项目默认模板

})


def updateDefaultTemplateUsingPUT(self, project, checker=None):
    """
    接口名称：更新项目默认模板
    接口地址：/proj/$VERSION$/project/defaultTemplate
    """
    r = RequestService.call_put(apis.get("updateDefaultTemplateUsingPUT", None), json={
        "project": project  # 项目信息 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def allTemplatesUsingGET(self, checker=None):
    """
    接口名称：查询所有的模板
    接口地址：/proj/$VERSION$/alltemplates
    """
    r = RequestService.call_get(apis.get("allTemplatesUsingGET"), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def mytemplatesUsingGET(self, checker):
    """
    接口名称：查询所有我创建的模板
    接口地址：/proj/$VERSION$/mytemplates
    """
    r = RequestService.call_get(apis.get("mytemplatesUsingGET"), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getAllProjecTemplatetListUsingGET(self, project_id, type, checker=None):
    """
    接口名称：获取所有项目模板详细信息列表
    接口地址：/proj/$VERSION$/projects/all/template
    """
    r = RequestService.call_get(apis.get("getAllProjecTemplatetListUsingGET"), params={
        "projectId": project_id,  # 项目ID - required: False
        "type": type,  # 类型 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def addProjectTemplateUsingPOST(self, description, project_id, name, checker=None):
    """
    接口名称：保存项目模板基本信息并根据配置表和项目类型生成相应计划类型
    接口地址：/proj/$VERSION$/template
    """
    r = RequestService.call_post(apis.get("addProjectTemplateUsingPOST"), params={
        "description": description,  # 项目模板详细描述 - required: False
        "id": project_id,  # 项目id - required: False
        "items": "plan,projectRole,risk,folder",  # 项目模板设置模板项 - required: False
        "name": name,  # 模板名称 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def replaceProjectTemplateUsingPOST(self, description, project_id, items, checker=None):
    """
    接口名称：替换项目模板内容
    接口地址：/proj/$VERSION$/template/information/{project_id}
    """
    r = RequestService.call_post(apis.get("replaceProjectTemplateUsingPOST", project_id), params={
        "description": description,  # 项目模板详细描述 - required: False
        "id": project_id,  # 项目id - required: False
        "items": items,  # 项目模板设置模板项 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getProjectTemplateListUsingGET(self, createBy, name, order_by, page_index, page_size, pmId,
                                   sort_by, type, checker=None):
    """
    接口名称：项目模板列表接口
    接口地址：/proj/$VERSION$/template/list
    """
    r = RequestService.call_get(apis.get("getProjectTemplateListUsingGET"), params={
        "createBy": createBy,  # 创建人（多个状态以逗号分隔） - required: False
        "name": name,  # 项目名称 - required: False
        "order_by": order_by,  # 排序字段，默认修改时间 - required: False
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
        "pmId": pmId,  # 项目经理（多个状态以逗号分隔） - required: False
        "sort_by": sort_by,  # 排序方式，默认倒序 - required: False
        "type": type,  # 类型（多个状态以逗号分隔） - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteTemplateUsingDELETE(self, id, checker=None):
    """
    接口名称：删除项目模板
    接口地址：/proj/$VERSION$/template/{id}
    """
    r = RequestService.call_delete(apis.get("deleteTemplateUsingDELETE", id), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r

import time

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api




'''
任务/需求/问题/风险对象关联(可关联需求、问题、风险、文档)
计划添加/删除关联需求、问题、风险
'''
apis = Api({
    "add_task": "/plan/$VERSION$/task",  # 创建任务
    "add_require": "/req/$VERSION$/require",  # 新增需求接口
    "add_issue": "/issue/$VERSION$/issue",  # 新建问题
    "add_risk": "/risk/v1",  # 添加风险

    "search_task_business_linked": "/plan/$VERSION$/%s/businesslink",  # 查询已经做关联的需求、任务、问题、风险列表
    "plan_search_add_remove_association": "/plan/$VERSION$/%s/businesslink/%s",  # 搜索可以做关联的需求、问题、风险；添加业务对象关联；删除关联
    "search_task_business": "/plan/$VERSION$/task/%s/businesses",  # 查询关联的需求、问题、风险列表
    "search_task_business_1": "/plan/$VERSION$/task/%s/candidatebusinesses",  # 搜索可以关联的需求、问题、风险

    "search_req_business_linked": "/req/$VERSION$/%s/businesslink",  # 查询已经做关联的需求、任务、问题、风险列表
    "req_search_add_remove_association": "/req/$VERSION$/%s/businesslink/%s",  # 搜索可以做关联的任务、问题、风险;添加业务对象关联;删除关联

    "search_risk_business_linked": "/risk/$VERSION$/%s/businesslink",  # 查询已经做关联的需求、任务、问题列表
    "risk_search_add_remove_association": "/risk/$VERSION$/%s/businesslink/%s",  # 搜索可以做关联的需求、问题、任务;添加业务对象关联;删除关联

    "search_issue_business_linked": "/issue/$VERSION$/%s/businesslink",  # 查询已经做关联的需求、任务、问题、风险列表
    "issue_search_add_remove_association": "/issue/$VERSION$/%s/businesslink/%s",  # 搜索可以做关联的需求、任务、风险、问题;添加业务对象关联;删除关联
})


def add_task(self, data, checker=None):
    """
    接口名称：创建任务
    接口地址：/plan/$VERSION$/task
    """
    r = RequestService.call_post(apis.get("add_task"), params=data)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_require(self, data, file_ids=None, checker=None):
    """
    接口名称：新增需求接口
    接口地址：/req/$VERSION$/require
    """
    r = RequestService.call_post(apis.get("add_require"), json={
        "fileIds": file_ids  # 表单关联文件Id - required: False
    }, params=data, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_issue(self, data, file_ids=None, checker=None):
    """
    接口名称：新建问题
    接口地址：/issue/$VERSION$/issue
    """
    r = RequestService.call_post(apis.get("add_issue"), json={
        "fileIds": file_ids  # 字段，多个 - required: False
    }, params=data)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_risk(self, project_id, name="risk_" + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()), grade="3", state="DRAFT", type_="1", file_ids=None,
             description=None, phase=None, plan_close_time=None,
             label_link_ids=None, checker=None):
    """
    接口名称：添加风险
    接口地址：/risk/v1
    """
    r = RequestService.call_post(apis.get("add_risk"), json={
        "fileIds": file_ids  # 字段Id,支持多值,逗号分割 - required: False
    }, params={
        "description": description,  # 描述 - required: False
        "grade": grade,  # 风险等级 - required: False
        "labelLinkIds": label_link_ids,  # 标签 - required: False
        "name": name,  # 名称 - required: False
        "phase": phase,  # 阶段 - required: False
        "planCloseTime": plan_close_time,  # 计划关闭时间 - required: False
        "projectId": project_id,  # 项目id - required: False
        "state": state,  # 风险状态 - required: False
        "type": type_,  # 风险类别 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def search_task_business_linked(self, task_id, name=None, checker=None):
    """
    接口名称：查询已经做关联的需求、任务、问题、风险列表
    接口地址：/plan/$VERSION$/{id}/businesslink
    """
    r = RequestService.call_get(apis.get("search_task_business_linked", task_id), params={
        "name": name  # 名称模糊查询 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def search_task_avl_business_link(self, task_id, project_id, type_, current=1, size=20, name=" ", checker=None):
    """
    接口名称：搜索可以做关联的需求、问题、风险
    接口地址：/plan/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_get(apis.get("plan_search_add_remove_association", task_id, type_), params={
        "current": current,  # 当前页 - required: False
        "name": name,  # 名称模糊查询 - required: False
        "projectId": project_id,  # 项目ID - required: True
        "size": size,  # 每页数量 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_task_business_link(self, role_a_id, type_, role_b_id, checker=None):
    """
    接口名称：添加业务对象关联
    接口地址：/plan/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_put(apis.get("plan_search_add_remove_association", role_a_id, type_), json=[{
        "roleAId": role_a_id,
        "roleBId": role_b_id
    }])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delete_task_business_link(self, task_id, type_, business_id, checker=None):
    """
    接口名称：删除关联
    接口地址：/plan/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_delete(apis.get("plan_search_add_remove_association", task_id, type_), params={
        "businessId": business_id  # 关联业务对象ID - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def search_task_business(self, task_id, checker=None):
    """
    接口名称：查询关联的需求、问题、风险列表
    接口地址：/plan/$VERSION$/task/{id}/businesses
    """
    r = RequestService.call_get(apis.get("search_task_business", task_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def search_task_business_1(self, task_id, type_, name=" ", checker=None):
    """
    接口名称：搜索可以关联的需求、问题、风险
    接口地址：/plan/$VERSION$/task/{id}/candidatebusinesses
    """
    r = RequestService.call_get(apis.get("search_task_business_1", task_id), params={
        "name": name,  # name - required: False
        "type": type_,  # type,取值：requirement/issue/risk - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def search_req_business_linked(self, requireid, name=None, checker=None):
    """
    接口名称：查询已经做关联的需求、任务、问题、风险列表
    接口地址：/req/$VERSION$/{id}/businesslink
    """
    r = RequestService.call_get(apis.get("search_req_business_linked", requireid), params={
        "name": name  # 名称模糊查询 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def search_req_avl_business_link(self, require_id, project_id, type_, current=1, size=20, name=" ", checker=None):
    """
    接口名称：搜索可以做关联的任务、问题、风险
    接口地址：/req/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_get(apis.get("req_search_add_remove_association", require_id, type_), params={
        "current": current,  # 当前页 - required: False
        "name": name,  # 名称模糊查询 - required: False
        "projectId": project_id,  # 项目ID - required: True
        "size": size,  # 每页数量 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_req_business_link(self, role_a_id, type_, role_b_id, checker=None):
    """
    接口名称：添加业务对象关联
    接口地址：/req/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_put(apis.get("req_search_add_remove_association", role_a_id, type_), json=[{
        "roleAId": role_b_id,
        "roleBId": role_b_id
    }])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delete_req_business_link(self, require_id, type_, business_id, checker=None):
    """
    接口名称：删除关联
    接口地址：/req/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_delete(apis.get("req_search_add_remove_association", require_id, type_), params={
        "businessId": business_id  # 关联业务对象ID - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def search_risk_business_linked(self, risk_id, name=None, checker=None):
    """
    接口名称：查询已经做关联的需求、任务、问题列表
    接口地址：/risk/$VERSION$/{id}/businesslink
    """
    r = RequestService.call_get(apis.get("search_risk_business_linked", risk_id), params={
        "name": name  # 名称模糊查询 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def search_risk_avl_business_link(self, risk_id, project_id, type_, current=1, size=20, name=" ", checker=None):
    """
    接口名称：搜索可以做关联的需求、问题、任务
    接口地址：/risk/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_get(apis.get("risk_search_add_remove_association", risk_id, type_), params={
        "current": current,  # 当前页 - required: False
        "name": name,  # 名称模糊查询 - required: False
        "projectId": project_id,  # 项目ID - required: True
        "size": size,  # 每页数量 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_risk_business_link(self, role_a_id, type_, role_b_id, checker=None):
    """
    接口名称：添加业务对象关联
    接口地址：/risk/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_put(apis.get("risk_search_add_remove_association", role_a_id, type_), json=[{
        "roleAId": role_a_id,
        "roleBId": role_b_id
    }])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delete_risk_business_link(self, risk_id, type_, business_id, checker=None):
    """
    接口名称：删除关联
    接口地址：/risk/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_delete(apis.get("risk_search_add_remove_association", risk_id, type_), params={
        "businessId": business_id  # 关联业务对象ID - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def search_issue_business_linked(self, issue_id, name=None, checker=None):
    """
    接口名称：查询已经做关联的需求、任务、问题、风险列表
    接口地址：/issue/$VERSION$/{id}/businesslink
    """
    r = RequestService.call_get(apis.get("search_issue_business_linked", issue_id), params={
        "name": name  # 名称模糊查询 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def search_issue_avl_business_link(self, issue_id, project_id, type_, current=1, size=20, name=" ", checker=None):
    """
    接口名称：搜索可以做关联的需求、任务、风险、问题
    接口地址：/issue/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_get(apis.get("issue_search_add_remove_association", issue_id, type_), params={
        "current": current,  # 当前页 - required: False
        "name": name,  # 名称模糊查询 - required: False
        "projectId": project_id,  # 项目ID - required: True
        "size": size,  # 每页数量 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_issue_business_link(self, role_a_id, type_, role_b_id, checker=None):
    """
    接口名称：添加业务对象关联
    接口地址：/issue/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_put(apis.get("issue_search_add_remove_association", role_a_id, type_), json=[{
        "roleAId": role_a_id,
        "roleBId": role_b_id
    }])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delete_issue_business_link(self, issue_id, type_, business_id, checker=None):
    """
    接口名称：删除关联
    接口地址：/issue/$VERSION$/{id}/businesslink/{type}
    """
    r = RequestService.call_delete(apis.get("issue_search_add_remove_association", issue_id, type_), params={
        "businessId": business_id  # 关联业务对象ID - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r

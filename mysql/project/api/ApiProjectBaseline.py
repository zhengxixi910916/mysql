from erdcloud import CommonServer
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

com = CommonServer()
headers = com.get_headers()
headers["Content-Type"] = 'application/x-www-form-urlencoded; charset=UTF-8'

'''
项目基线、基线任务
'''
apis = Api({
    "baseline_add": "/proj/$VERSION$/baseline/add",  # 添加基线
    "baseline_compare": "/proj/$VERSION$/baseline/compare",  # 基线对比
    "baseline_delete": "/proj/$VERSION$/baseline/delete",  # 清除基线
    "baseline_page_list": "/proj/$VERSION$/baseline/list/page",  # 基线分页列表
    "baseline_list": "/proj/$VERSION$/baseline/snapshot/list",  # 基线列表
    "baseline_type_list": "/proj/$VERSION$/baselinetype/list",  # 基线类型列表
    "snapshot_using_get_1": "/plan/$VERSION$/baseline/snapshot/%s",  # 快照任务对象基本信息详情查询
    "get_tasks_using_get": "/plan/$VERSION$/baseline/tasks",  # 通过基线获取任务列表（项目下）
    "get_first_level_children_tasks_by_task_id_using_get": "/plan/$VERSION$/baseline/tasks/%s/children",
    # 根据任务id获取第一层子基线任务列表
    "get_task_baseline_by_baseline_ids_using_get": "/plan/$VERSION$/baseline/tasksattrs",  # 获取基线任务列表-包括扩展字段
    "get_project_by_baseline_id_using_get": "/proj/$VERSION$/baseline/project/%s",  # 根据基线ID查询项目基本信息
    "select_business_list_using_post_5": "/plan/$VERSION$/baseline/%s/businesslist",  # 查询业务数据
    "select_filter_list_using_post_6": "/plan/$VERSION$/baseline/%s/filterlist",  # 过滤业务数据
})


def select_business_list_using_post_5(self, view_id, view_dto, checker=None):
    """
    接口名称：查询业务数据
    接口地址：/plan/$VERSION$/baseline/{viewid}/businesslist
    """
    r = RequestService.call_post(apis.get("select_business_list_using_post_5", view_id), json=view_dto
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def select_filter_list_using_post_6(self, view_id, view_dto, checker=None):
    """
    接口名称：过滤业务数据
    接口地址：/plan/$VERSION$/baseline/{viewid}/filterlist
    """
    r = RequestService.call_post(apis.get("select_filter_list_using_post_6", view_id), json=view_dto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def baseline_add(self, name, baseline_type, baseline_date, description, project_id, checker=None):
    """
    接口名称：添加基线
    接口地址：/proj/$VERSION$/baseline/add
    """
    r = RequestService.call_post(apis.get("baseline_add"),
                                 data={
                                     "name": name,
                                     "baselineType": baseline_type,
                                     "baselineDate": baseline_date,
                                     "description": description,
                                     "projectId": project_id,

                                 },
                                 headers=headers
                                 )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r["res"]["data"]


def baseline_compare(self, baseline_id1, baseline_id2, project_id, fields, checker=None):
    """
    接口名称：基线对比
    接口地址：/proj/$VERSION$/baseline/compare
    """
    r = RequestService.call_get(apis.get("baseline_compare"), params={
        "baselineId1": baseline_id1,
        "baselineId2": baseline_id2,
        "projectId": project_id,
        "fields": fields,
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def baseline_delete(self, baseline_id, checker=None):
    """
    接口名称：清除基线
    接口地址：/proj/$VERSION$/baseline/delete
    """
    r = RequestService.call_delete(apis.get("baseline_delete"), params={
        "baselineId": baseline_id
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def baseline_page_list(self, name, baseline_type, pager_name, sort_by, order_by, page_size, page_index,
                       project_id, checker=None):
    """
    接口名称：基线分页列表
    接口地址：/proj/$VERSION$/baseline/list/page
    """
    r = RequestService.call_get(apis.get("baseline_page_list"), params={
        "name": name,
        "baseline_type": baseline_type,
        "pager_name": pager_name,
        "sort_by": sort_by,
        "order_by": order_by,
        "pagesize": page_size,
        "pageindex": page_index,
        "projectId": project_id
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def baseline_list(self, project_id, baseline_type, checker=None):
    """
    接口名称：基线列表
    接口地址：/proj/$VERSION$/baseline/snapshot/list
    """
    r = RequestService.call_get(apis.get("baseline_list"), params={
        "projectId": project_id,
        "baseline_type": baseline_type
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r["res"]["data"]


def baseline_type_list(self, checker=None):
    """
    接口名称：基线类型列表
    接口地址：/proj/$VERSION$/baselinetype/list
    """
    r = RequestService.call_get(apis.get("baseline_type_list"), params={
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def snapshot_using_get_1(self,task_id1, checker=None):
    """
    接口名称：快照任务对象基本信息详情查询
    接口地址：/plan/$VERSION$/baseline/snapshot/{id}
    """
    r = RequestService.call_get(apis.get("snapshot_using_get_1", task_id1), params={
        "type": "task"
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_tasks_using_get(self, project_id, baseline_id, checker=None):
    """
    接口名称：通过基线获取任务列表（项目下）
    接口地址：/plan/$VERSION$/baseline/tasks
    """
    r = RequestService.call_get(apis.get("get_tasks_using_get", ), params={
        "projectId": project_id,
        "baseline_id": baseline_id
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def get_first_level_children_tasks_by_task_id_using_get(self, task_id, baseline_id, checker=None):
    """
    接口名称：根据任务id获取第一层子基线任务列表
    接口地址：/plan/$VERSION$/baseline/tasks/{id}/children
    """
    r = RequestService.call_get(apis.get("get_first_level_children_tasks_by_task_id_using_get", task_id), params={
        "baseline_id": baseline_id,  # 基线ID - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_task_baseline_by_baseline_ids_using_get(self, checker):
    """
    接口名称：获取基线任务列表-包括扩展字段
    接口地址：/plan/$VERSION$/baseline/tasksattrs
    """
    r = RequestService.call_get(apis.get("get_task_baseline_by_baseline_ids_using_get", None), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_project_by_baseline_id_using_get(self, baseline_id, checker=None):
    """
    接口名称： 根据基线ID查询项目基本信息
    接口地址：/proj/$VERSION$/baseline/project/{id}
    """
    r = RequestService.call_get(apis.get("get_project_by_baseline_id_using_get", baseline_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

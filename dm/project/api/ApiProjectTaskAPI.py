from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目任务API
'''
apis = Api({
    "editUpdateTaskUsingPUT": "/plan/$VERSION$/api/task/batch",  # 批量修改接口（无逻辑）
    "insertUpdateTaskUsingPUT": "/plan/$VERSION$/api/task/insert/batch",  # 批量新增接口（无逻辑）
    "copyTaskUsingPOST_1": "/plan/$VERSION$/api/task/%s/copy",  # 复制|移动
    "deleteTaskMembersUsingPUT": "/plan/$VERSION$/api/taskmember/delete/batch",  # 根据任务ID批量删除计划成员接口（无逻辑）
    "insertTaskMembersUsingPUT": "/plan/$VERSION$/api/taskmember/insert/batch",  # 批量新增计划成员接口（无逻辑）
    "addTaskUsingPOST": "/plan/$VERSION$/api/%s/task",  # 创建任务,如果创建后需要直接与其他对象进行关联，需要传TaskLinkDto
})


def editUpdateTaskUsingPUT(self, checker):
    """
    接口名称：批量修改接口（无逻辑）
    接口地址：/plan/$VERSION$/api/task/batch
    """
    r = RequestService.call_put(apis.get("editUpdateTaskUsingPUT", None), json={
        "taskList": ""  # 任务列表 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def insertUpdateTaskUsingPUT(self, checker):
    """
    接口名称：批量新增接口（无逻辑）
    接口地址：/plan/$VERSION$/api/task/insert/batch
    """
    r = RequestService.call_put(apis.get("insertUpdateTaskUsingPUT", None), json={
        "taskList": ""  # 任务列表 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def copyTaskUsingPOST_1(self, checker):
    """
    接口名称：复制|移动
    接口地址：/plan/$VERSION$/api/task/{project_id}/copy
    """
    r = RequestService.call_post(apis.get("copyTaskUsingPOST_1", None), json={
        "params": ""  # params - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteTaskMembersUsingPUT(self, checker):
    """
    接口名称：根据任务ID批量删除计划成员接口（无逻辑）
    接口地址：/plan/$VERSION$/api/taskmember/delete/batch
    """
    r = RequestService.call_put(apis.get("deleteTaskMembersUsingPUT", None), json={
        "task_ids": ""  # 任务Id列表 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def insertTaskMembersUsingPUT(self, checker):
    """
    接口名称：批量新增计划成员接口（无逻辑）
    接口地址：/plan/$VERSION$/api/taskmember/insert/batch
    """
    r = RequestService.call_put(apis.get("insertTaskMembersUsingPUT", None), json={
        "taskMemberList": ""  # 任务成员列表 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def addTaskUsingPOST(self, project_id, params, checker=None):
    """
    接口名称：创建任务,如果创建后需要直接与其他对象进行关联，需要传TaskLinkDto
    接口地址：/plan/$VERSION$/api/{project_id}/task
    """
    r = RequestService.call_post(apis.get("addTaskUsingPOST", project_id), json={
        "params": params  # params - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

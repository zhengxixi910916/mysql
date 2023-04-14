from workflow.api import ApiTools as ApiTools
import time
from erdcloud.erdApi import Api

apis = Api({
    "enums_EtActivityLifecycleEnum": "/workflow/$VERSION$/dynamic/api/status/enums/TaskTypeEnum",  # 获取任务类型
    "tasks_grouped_zids": "/workflow/$VERSION$/dynamic/api/task/tasks/grouped",  # 批量审批任务查询接口
    "todoList_pagesize_pageindex": "/workflow/$VERSION$/dynamic/api/common/pageQuery/todoList/20/1",  # 查询待我处理列表
})


def launchRecord_pagesize_pageindex():
    # 查询我发起的列表
    data = {"pageSize": 20, "currentPage": 1, "dynamicCondition": [], "orders": [], "keyword": ""}
    api = '/workflow/v1/dynamic/api/common/pageQuery/launchRecord/20/1'
    return ApiTools.call(method='POST', api=api, json=data)


def todoList_pagesize_pageindex():
    # 查询待我处理列表
    tmp = apis.get('todoList_pagesize_pageindex', None)
    print('***', tmp, '***')
    data = {"pageSize": 20, "currentPage": 1, "dynamicCondition": [], "orders": [], "keyword": ""}
    api = '/workflow/v1/dynamic/api/common/pageQuery/todoList/20/1'
    return ApiTools.call(method='POST', api=api, json=data)


def tasks_grouped(taskids):
    # 接口名称：批量审批任务查询接口;
    # 接口地址：/workflow/v1/dynamic/api/task/tasks/grouped;
    print('----------------------')
    tmp = apis.get("tasks_grouped_zids", None)
    print("****", tmp, "****")
    api = "/workflow/v1/dynamic/api/task/tasks/grouped"
    data = {"taskIds": taskids}
    return ApiTools.call(method="POST", api=api, json=data)


def enums_EtActivityLifecycleEnum():
    """
    获取任务类型
    """
    apis.get('enums_EtActivityLifecycleEnum', None)
    api = "/workflow/v1/dynamic/api/status/enums/TaskTypeEnum"
    r = ApiTools.call(method="GET", api=api, params={'_': int(time.time())})
    return r

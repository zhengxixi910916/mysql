from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "task_custom_condition": "/workflow/$VERSION$/process/home/custom",  # 根据appId，role, userId, priority自定义查询条件代办任务
    "task_processing_rate": "/workflow/$VERSION$/process/home/deal/rate",  # 统计一天内、一月以来、一年依赖的任务处理率
    "task_priority_using": "/workflow/$VERSION$/process/home/priority",  # 根据优先级统计
    "query_todo_task": "/workflow/$VERSION$/process/home/todo",  # 统计待我处理任务的数量
    "process_info2me_using": "/workflow/$VERSION$/process/home/transfer/me",  # 统计别人转给我的流程任务
})


def task_custom_condition(self, flag="personal", type_="role", checker=None):
    """
    接口名称：根据appId，role, userId, priority自定义查询条件代办任务;    接口地址：/workflow/$VERSION$/process/home/custom；
    """
    r = RequestService.call_get(apis.get("task_custom_condition", None), params={
        "flag": flag,  # 区分工作台和流程管理：（personal：工作台；system：流程管理） - required: False
        "type": type_,  # X轴(appId，role, userId, priority) - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def task_processing_rate(self, flag="personal", format_="day", checker=None):
    """
    接口名称：统计一天内、一月以来、一年依赖的任务处理率;    接口地址：/workflow/$VERSION$/process/home/deal/rate；
    """
    r = RequestService.call_get(apis.get("task_processing_rate", None), params={
        "flag": flag,  # 区分工作台和流程管理：（personal：工作台；system：流程管理） - required: False
        "format": format_,  # 时间格式：(day:天；month：月：year:年) - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def task_priority_using(self,flag="personal", checker=None):
    """
    接口名称：根据优先级统计;    接口地址：/workflow/$VERSION$/process/home/priority；
    """
    r = RequestService.call_get(apis.get("task_priority_using", None), params={
        "flag": flag  # 区分工作台和流程管理：（personal：工作台；system：流程管理） - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_todo_task(self, checker=None):
    """
    接口名称：统计待我处理任务的数量;    接口地址：/workflow/$VERSION$/process/home/todo；
    """
    r = RequestService.call_get(apis.get("query_todo_task", None), params={
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def process_info2me_using(self, flag="personal",checker=None):
    """
    接口名称：统计别人转给我的流程任务;    接口地址：/workflow/$VERSION$/process/home/transfer/me；
    """
    r = RequestService.call_get(apis.get("process_info2me_using", None), params={
        "flag": flag  # 区分工作台和流程管理：（personal：工作台；system：流程管理） - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

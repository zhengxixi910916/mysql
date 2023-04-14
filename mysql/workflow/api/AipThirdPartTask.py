from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "create_history_task": "/workflow/thirdparty/createHistoryTask",  # 创建第三方历史任务
    "create_task_using": "/workflow/thirdparty/createTask",  # 创建第三方任务
    "delete_process_using": "/workflow/thirdparty/process/{processInstanceIds}/{source}",  # 第三方任务删除根据流程ids
    "delete_task_using": "/workflow/thirdparty/task/{taskIds}/{source}",  # 第三方任务删除根据任务IDs
})
def create_history_task(self,is_End,pro_InstId,sourc_e,task_Id, checker=None):
    """
    接口名称：创建第三方历史任务;    接口地址：/workflow/thirdparty/createHistoryTask；	
    """
    r = RequestService.call_post(apis.get("create_history_task", None),params= {
                    "isEnd": is_End,  # 流程是否结束 - required: False
                    "procInstId":pro_InstId,  # 流程实例id - required: True
                    "source": sourc_e,  # 来源 - required: True
                    "taskId": task_Id,  # 完成的任务id - required: True
                },)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def create_task_using(self, task_json,checker=None):
    """
    接口名称：创建第三方任务;    接口地址：/workflow/thirdparty/createTask；	
    """
    r = RequestService.call_post(apis.get("create_task_using", None),params= {
                    "taskjson": str(task_json)  # 任务json - required: True
                },)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_process_using(self, checker=None):
    """
    接口名称：第三方任务删除根据流程ids;    接口地址：/workflow/thirdparty/process/{processInstanceIds}/{source}；	
    """
    r = RequestService.call_delete(apis.get("delete_process_using", None),)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_task_using(self, checker=None):
    """
    接口名称：第三方任务删除根据任务IDs;    接口地址：/workflow/thirdparty/task/{taskIds}/{source}；	
    """
    r = RequestService.call_delete(apis.get("delete_task_using", None),)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


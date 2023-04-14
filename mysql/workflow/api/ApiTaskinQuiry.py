from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "add_task_inquiry": "/workflow/$VERSION$/taskinquiry/add",  # 任务询问
    "cancle_task_inquiry": "/workflow/$VERSION$/taskinquiry/cancle/%s",  # 任务询问取消
    "detail_by_task": "/workflow/$VERSION$/taskinquiry/detail/%s",  # 查询详情
    "query_page_using": "/workflow/$VERSION$/taskinquiry/page",  # 查询当前用户的询问记录
    "reply_list_using": "/workflow/$VERSION$/taskinquiry/reply/%s",  # 查询询问的回复记录
    "reply_task_inquiry": "/workflow/$VERSION$/taskinquiry/reply/%s",  # 任务询问回复
})


def add_task_inquiry(self, task_inquiry, checker=None):
    """
    接口名称：任务询问;    接口地址：/workflow/$VERSION$/taskinquiry/add；	
    """
    r = RequestService.call_post(apis.get("add_task_inquiry", None), json=task_inquiry)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def cancle_task_inquiry(self, inquiry_id, checker=None):
    """
    接口名称：任务询问取消;    接口地址：/workflow/$VERSION$/taskinquiry/cancle/{inquiryId}；	
    """
    r = RequestService.call_post(apis.get("cancle_task_inquiry", inquiry_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def detail_by_task(self, task_id, checker=None):
    """
    接口名称：查询详情;    接口地址：/workflow/$VERSION$/taskinquiry/detail/{taskId}；	
    """
    r = RequestService.call_get(apis.get("detail_by_task", task_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_page_using(self, user_id, checker=None):
    """
    接口名称：查询当前用户的询问记录;    接口地址：/workflow/$VERSION$/taskinquiry/page；	
    """
    r = RequestService.call_get(apis.get("query_page_using", None), params={
        "inquiryUserId": user_id
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def reply_list_using(self, inquiry_id, checker=None):
    """
    接口名称：查询询问的回复记录;    接口地址：/workflow/$VERSION$/taskinquiry/reply/{inquiryId}；	
    """
    r = RequestService.call_get(apis.get("reply_list_using", inquiry_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def reply_task_inquiry(self, inquiry_id, task_inquiry, checker=None):
    """
    接口名称：任务询问回复;    接口地址：/workflow/$VERSION$/taskinquiry/reply/{inquiryId}；	
    """
    r = RequestService.call_put(apis.get("reply_task_inquiry", inquiry_id), json=task_inquiry)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

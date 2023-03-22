from erdcloud.CommonServerTest import CommonServer
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
甘特图
'''
apis = Api({
    "updateTasksUsingPOST": "/plan/$VERSION$/gantt/tasks",  # 更新甘特图数据
    "getTaskListUsingGET_1": "/plan/$VERSION$/gantt/tasks/tree",  # 根据项目获取任务，用户甘特图显示
})


def updateTasksUsingPOST(self, taskJson, checker=None):
    """
    接口名称：更新甘特图数据
    接口地址：/plan/$VERSION$/gantt/tasks
    """
    com = CommonServer()
    token = com.get_token()

    r = RequestService.call_post(apis.get("updateTasksUsingPOST"), data=taskJson,
                                 headers={
                                     'Authorization': "Bearer " + token,
                                     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                 }
                                 )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getTaskListUsingGET_1(self, project_id, checker=None):
    """
    接口名称：根据项目获取任务，用户甘特图显示
    接口地址：/plan/$VERSION$/gantt/tasks/tree
    """
    r = RequestService.call_get(apis.get("getTaskListUsingGET_1"), params={
        "projectId": project_id  # 项目ID - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r

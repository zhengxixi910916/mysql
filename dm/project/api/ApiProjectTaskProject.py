from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目任务project
'''
apis = Api({
    "importTaskFromProjectUsingPOST": "/plan/$VERSION$/project/tasks/import",  # 导入任务
})


def importTaskFromProjectUsingPOST(self, checker):
    """
    接口名称：导入任务
    接口地址：/plan/$VERSION$/project/tasks/import
    """
    r = RequestService.call_post(apis.get("importTaskFromProjectUsingPOST", None), data={
        "file": ""  # file - required: True
    }, params={
        "projectId": ""  # 项目id - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

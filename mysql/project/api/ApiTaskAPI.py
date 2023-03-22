from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
任务API
'''
apis = Api({
    "getCheckListByIdUsingGET": "/plan/$VERSION$/api/checklist/%s",  # 检查项ID查询检查项对象
    "getAllChecklistUsingGET": "/plan/$VERSION$/api/tasks/doc/list/%s",  # getAllChecklist
})


def getCheckListByIdUsingGET(self, id, checker=None):
    """
    接口名称：检查项ID查询检查项对象
    接口地址：/plan/$VERSION$/api/checklist/{id}
    """
    r = RequestService.call_get(apis.get("getCheckListByIdUsingGET", id), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getAllChecklistUsingGET(self, checker):
    """
    接口名称：getAllChecklist
    接口地址：/plan/$VERSION$/api/tasks/doc/list/{project_id}
    """
    r = RequestService.call_get(apis.get("getAllChecklistUsingGET", None), params={
        "orderBy": "",  # 排序字段(默认名称) - required: False
        "pageindex": "",  # 页码 - required: False
        "pagesize": "",  # 页大小 - required: False
        "phase": "",  # 阶段ID - required: False
        "sortBy": "",  # 排序(默认升序) - required: False
        "state": "",  # 交附件状态 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

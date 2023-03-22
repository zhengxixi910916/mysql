from erdcloud import CommonServer
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "downloadFileUsingGET": "/rpt/$VERSION$/export/excel",  # 导出周报timesheet
    "getDurationTasksUsingGET": "/rpt/$VERSION$/tasks",  # 获取任务列表
    "queryPageUsingGET_1": "/rpt/$VERSION$/weeklies",  # 获取周报分页数据
    "addWeeklyUsingPOST_1": "/rpt/$VERSION$/weekly",  # 添加周报数据
    "updateDraftUsingPUT": "/rpt/$VERSION$/weekly/draft",  # 修改周报草稿数据
    "queryWeeklyUsingGET": "/rpt/$VERSION$/weekly/%s",  # 根据id获取周报数据
    "deleteDraftUsingDELETE": "/rpt/$VERSION$/weekly/%s",  # 删除周报草稿
    "updateStatusUsingPUT": "/rpt/$VERSION$/weekly/{id}/{statekey}",  # 修改周报状态
    "queryByYearAndWeekUsingGET": "/rpt/$VERSION$/weekly/{year}/{week}",  # 根据年月获取周报
})


def downloadFileUsingGET(self, checker):
    """
    接口名称：导出周报timesheet
    接口地址：/rpt/$VERSION$/export/excel
    """
    r = RequestService.call_get(apis.get("downloadFileUsingGET", None), params={
        "ids": "",  # 周报ids - required: False
        "people": "",  # 人员id - required: False
        "queryType": "",  # 所有:1发送:2接收 - required: False
        "status": "",  # 状态0草稿1待审阅2已审阅 - required: False
        "weekOfYear": "",  # 第几周 - required: False
        "year": "",  # 年 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def getDurationTasksUsingGET(self, startDate, endDate, checker=None):
    """
    接口名称：获取任务列表
    接口地址：/rpt/$VERSION$/tasks
    """
    r = RequestService.call_get(apis.get("getDurationTasksUsingGET", None), params={
        "userId": "SYS_E39B20EA11E7A81AC85B767C89C1",
        "startDate": startDate,
        "endDate": endDate
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def queryPageUsingGET_1(self, checker=None):
    """
    接口名称：获取周报分页数据
    接口地址：/rpt/$VERSION$/weeklies
    """
    r = RequestService.call_get(apis.get("queryPageUsingGET_1", None), params={
        "queryType": '',
        "status": '',
        "year": '',
        "weekOfYear": '',
        "people": '',
        "pageSize": 20,
        "pageNo": 1
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def addWeeklyUsingPOST_1(self, checker, data, ):
    """
    接口名称：添加周报数据
    接口地址：/rpt/$VERSION$/weekly
    """

    r = RequestService.call_post(apis.get("addWeeklyUsingPOST_1", None),
                                 json=data,
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def updateDraftUsingPUT(self, checker, data):
    """
    接口名称：修改周报草稿数据
    接口地址：/rpt/$VERSION$/weekly/draft
    """
    r = RequestService.call_put(apis.get("updateDraftUsingPUT", None), json=data
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def queryWeeklyUsingGET(self, checker, week_id):
    """
    接口名称：根据id获取周报数据
    接口地址：/rpt/$VERSION$/weekly/{id}
    """
    r = RequestService.call_get(apis.get("queryWeeklyUsingGET", week_id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def deleteDraftUsingDELETE(self, checker, id):
    """
    接口名称：删除周报草稿
    接口地址：/rpt/$VERSION$/weekly/{id}
    """
    r = RequestService.call_delete(apis.get("deleteDraftUsingDELETE", id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def updateStatusUsingPUT(self, checker):
    """
    接口名称：修改周报状态
    接口地址：/rpt/$VERSION$/weekly/{id}/{statekey}
    """
    r = RequestService.call_put(apis.get("updateStatusUsingPUT", None), path={
        "id": "",  # id - required: True
        "statekey": "",  # statekey - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def queryByYearAndWeekUsingGET(self, checker, year, weekOfYear):
    """
    接口名称：根据年月获取周报
    接口地址：/rpt/$VERSION$/weekly/{year}/{week}
    """
    r = RequestService.call_get(apis.get("queryByYearAndWeekUsingGET", None), params={
        "queryType": '',
        "status": '',
        "year": year,
        "weekOfYear": weekOfYear,
        "people": '',
        "pager_name": 20,
        "pagesize": 20,
        "pageNo": 1
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
问题统计报表
'''
apis = Api({
    "getIssueChartUsingGET": "/issue/$VERSION$/chart/%s",  # 问题统计报表
    "exportIssueChartUsingGET": "/issue/$VERSION$/chartexport/%s",  # 导出项目问题报表
})


def getIssueChartUsingGET(self, project_id, ymonth, checker=None):
    """
    接口名称：问题统计报表
    接口地址：/issue/$VERSION$/chart/{project_id}
    """

    r = RequestService.call_get(apis.get("getIssueChartUsingGET", project_id), params={
        "ymonth": ymonth  # 年-月（yyyy-MM格式） - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def exportIssueChartUsingGET(self, checker):
    """
    接口名称：导出项目问题报表
    接口地址：/issue/$VERSION$/chartexport/{project_id}
    """
    r = RequestService.call_get(apis.get("exportIssueChartUsingGET", None), params={
        "month": ""  # 月份(yyyy-MM) - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

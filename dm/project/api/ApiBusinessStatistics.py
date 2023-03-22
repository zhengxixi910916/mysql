from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
业务统计
'''
apis = Api({
    "queryBusinessCountUsingGET": "/proj/business/statistics/count",  # 业务数据统计未创建流程的、未完成的数量
    "queryBusinessDataUsingGET": "/proj/business/statistics/data",  # 业务数据统计未创建流程的、未完成的数据
    "uploadUsingPOST": "/proj/business/statistics/eChartUpload",  # 上传eChart统计图
    "exportUsingGET": "/proj/business/statistics/export",  # 导出数据
})


def queryBusinessCountUsingGET(self, project, type, startDate, endDate, assignee,
                               expiredNdaysUnfinished, createNdaysUnStartProcess,
                               page_index, page_size, checker=None):
    """
    接口名称：业务数据统计未创建流程的、未完成的数量
    接口地址：/proj/business/statistics/count
    """
    r = RequestService.call_get(apis.get("queryBusinessCountUsingGET", None), params={
        "project": project,
        "assignee": assignee,  # 人员 - required: False
        "createNdaysUnStartProcess": createNdaysUnStartProcess,  # 创建未发起流程的天数 - required: False
        "endDate": endDate,  # 结束时间 - required: False
        "expiredNdaysUnfinished": expiredNdaysUnfinished,  # 未完成过期天数 - required: False
        "pageindex": page_index,  # 第几页 - required: False
        "pagesize": page_size,  # 一页大小 - required: False
        "startDate": startDate,  # 开始时间 - required: False
        "type": type,  # 类型,全部/需求、任务、问题、风险 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def queryBusinessDataUsingGET(self, project, type, startDate, endDate, assignee,
                              expiredNdaysUnfinished, createNdaysUnStartProcess,
                              page_index, page_size, condition, checker=None):
    """
    接口名称：业务数据统计未创建流程的、未完成的数据
    接口地址：/proj/business/statistics/data
    """
    r = RequestService.call_get(apis.get("queryBusinessDataUsingGET", None), params={
        "project": project,
        "assignee": assignee,  # 人员 - required: False
        "createNdaysUnStartProcess": createNdaysUnStartProcess,  # 创建未发起流程的天数 - required: False
        "endDate": endDate,  # 结束时间 - required: False
        "expiredNdaysUnfinished": expiredNdaysUnfinished,  # 未完成过期天数 - required: False
        "pageindex": page_index,  # 第几页 - required: False
        "pagesize": page_size,  # 一页大小 - required: False
        "startDate": startDate,  # 开始时间 - required: False
        "type": type,  # 类型,全部/需求、任务、问题、风险 - required: False
        "condition": condition
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def uploadUsingPOST(self, checker):
    """
    接口名称：上传eChart统计图
    接口地址：/proj/business/statistics/eChartUpload
    """
    r = RequestService.call_post(apis.get("uploadUsingPOST", None), json={
        "notifyHistoryDto": ""  # notifyHistoryDto - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def exportUsingGET(self, checker):
    """
    接口名称：导出数据
    接口地址：/proj/business/statistics/export
    """
    r = RequestService.call_get(apis.get("exportUsingGET", None), params={
        "assignee": "",  # 人员 - required: False
        "chartPath": "",  # eChart路径 - required: False
        "chartcode": "",  # eChart统计图 - required: False
        "condition": "",  # 过期N天未完成条件 - required: False
        "createNdaysUnStartProcess": "",  # 创建未发起流程的天数 - required: False
        "endDate": "",  # 结束时间 - required: False
        "expiredNdaysUnfinished": "",  # 未完成过期天数 - required: False
        "pageindex": "",  # 第几页 - required: False
        "pagesize": "",  # 一页大小 - required: False
        "project": "",  # 项目，单个或多个 - required: False
        "project": "",  # 项目，单个或多个 - required: False
        "projectList": "",  # 项目列表，用于mybatis查询 - required: False
        "startDate": "",  # 开始时间 - required: False
        "type": "",  # 类型,全部/需求、任务、问题、风险 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

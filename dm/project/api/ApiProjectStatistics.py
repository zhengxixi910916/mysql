from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目、项目群统计信息
'''
apis = Api({
    "Statistics": "/proj/$VERSION$/project/%s",  # 项目管理-统计
    "Overview": "/plan/$VERSION$/mchart/%s",  # 项目管理-统计-概况
    "PlanReport": "/plan/$VERSION$/chart/%s",  # 项目管理-统计-计划报表
    "MilestoneReport": "/plan/$VERSION$/task/milestone/%s",  # 项目管理-统计-里程碑情况
    "ProblemReport": "/issue/$VERSION$/chart/%s",  # 项目管理-统计-问题报表
    "RiskReport": "/risk/$VERSION$/chart/%s",  # 项目管理-统计-风险报表
    "CustomReport": "/proj/$VERSION$/project/report/all",  # 项目管理-统计-自定义报表
    "Hrview": "/proj/$VERSION$/statistic/hrview",  # 项目管理-统计-人力视图报表
    "ProjectReport": "/rpt/$VERSION$/reports",  # 项目管理-统计-项目报告
    "TaskCompletionStatistics": "/plan/$VERSION$/getMemberCompletionStatus",  # 项目管理-统计-任务完成统计情况
    "getManpowerViewUsingGET": "/portfolio/$VERSION$/program/statistic/hrview",  # 人力视图
    "getManpowerViewUsingGET_1": "/proj/$VERSION$/statistic/hrview",  # 人力Loading视图
    "getManpowerViewPageUsingGET": "/proj/$VERSION$/statistic/hrview/page",  # 分页查询人力Loading视图
    "getManpowerViewdepartUsingGET": "/proj/$VERSION$/statistic/hrviewdepart",  # 人力视图报表
    "getMonthlyReportsUsingGET": "/proj/$VERSION$/statistic/monthlyreports",  # 研发工作月度统计报表
    "pageProjectUsingGET_1": "/proj/$VERSION$/statistic/page/projects",  # 根据项目id查询项目分页列表
    "getManpowerViewUsingGET_2": "/proj/$VERSION$/statistic/status/report",  # 项目状态统计
    "getTopProjectUsingGET": "/proj/$VERSION$/statistic/topProject",  # TOP项目清单报表
    "getProjectProcessUsingGET": "/proj/$VERSION$/statistic/progress",  # 项目进展统计报表
})


def Statistics(self, project_id, checker=None):
    """
    接口名称：项目管理-统计
    接口地址：/proj/$VERSION$/project/%s
    """
    r = RequestService.call_get(apis.get("Statistics", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r["res"]["data"]


def Overview(self, project_id, month, checker=None):
    """
    接口名称：项目管理-统计-概况
    接口地址：/plan/$VERSION$/mchart/%s
    """
    r = RequestService.call_get(apis.get("Overview", project_id), params={
        "month": month,  # None - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def PlanReport(self, project_id, ymonth, checker=None):
    """
    接口名称：项目管理-统计-计划报表
    接口地址：/plan/$VERSION$/chart/%s
    """
    r = RequestService.call_get(apis.get("PlanReport", project_id), params={
        "ymonth": ymonth
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def MilestoneReport(self, Id, project_id, checker=None):
    """
    接口名称：项目管理-统计-里程碑情况
    接口地址：/plan/$VERSION$/task/milestone/%s
    """
    r = RequestService.call_get(apis.get("MilestoneReport", Id), params={
        "projectId": project_id
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def ProblemReport(self, project_id, ymonth, checker=None):
    """
    接口名称：项目管理-统计-问题报表
    接口地址：/issue/$VERSION$/chart/%s
    """
    r = RequestService.call_get(apis.get("ProblemReport", project_id), params={
        "ymonth": ymonth
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def RiskReport(self, project_id, ymonth, checker=None):
    """
    接口名称：项目管理-统计-风险报表
    接口地址：/risk/$VERSION$/chart/%s
    """
    r = RequestService.call_get(apis.get("RiskReport", project_id), params={
        "ymonth": ymonth
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def CustomReport(self, project_id, checker=None):
    """
    接口名称：项目管理-统计-自定义报表
    接口地址：/proj/$VERSION$/project/report/all
    """
    r = RequestService.call_get(apis.get("CustomReport"), params={
        "projectId": project_id
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def Hrview(self, project_id, memberIds, startDate, endDate, dimension, checker=None):
    """
    接口名称：项目管理-统计-人力视图报表
    接口地址：/proj/$VERSION$/statistic/hrview
    """
    r = RequestService.call_get(apis.get("Hrview"), params={
        "projectId": project_id,
        "memberIds": memberIds,
        "startDate": startDate,
        "endDate": endDate,
        "dimension": dimension
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def ProjectReport(self, name, type, status, createBy, dateFor, startTime, endTime, page_size, page_index, updateBy,
                  project_id, orderBy, sortBy, checker=None):
    """
    接口名称：项目管理-统计-项目报告
    接口地址：/rpt/$VERSION$/reports
    """
    r = RequestService.call_get(apis.get("ProjectReport"), params={
        "name": name,
        "type": type,
        "status": status,
        "createBy": createBy,
        "dateFor": dateFor,
        "startTime": startTime,
        "endTime": endTime,
        "pagesize": page_size,
        "pageindex": page_index,
        "updateBy": updateBy,
        "projectId": project_id,
        "orderBy": orderBy,
        "sortBy": sortBy
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def TaskCompletionStatistics(self, userId, project_ids, taskName, orgId, startDate, endDate, orgid, checker=None):
    """
    接口名称：项目管理-统计-任务完成统计情况
    接口地址：/plan/$VERSION$/getMemberCompletionStatus
    """
    r = RequestService.call_get(apis.get("TaskCompletionStatistics"), params={
        "userId": userId,
        "project_ids": project_ids,
        "taskName": taskName,
        "orgId": orgId,
        "startDate": startDate,
        "endDate": endDate,
        "orgid": orgid
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getManpowerViewUsingGET(self, checker):
    """
    接口名称：人力视图
    接口地址：/portfolio/$VERSION$/program/statistic/hrview
    """
    r = RequestService.call_get(apis.get("getManpowerViewUsingGET", None), params={
        "dimension": "",  # 维度(monthly/weekly/daily) - required: True
        "endDate": "",  # 结束日期，年/月/日（yyyy/MM/dd格式） - required: True
        "memberIds": "",  # 成员ID,多个以逗号隔开 - required: False
        "programId": "",  # 项目群ID - required: False
        "projectId": "",  # 项目ID - required: False
        "startDate": "",  # 开始日期，年/月/日（yyyy/MM/dd格式） - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getManpowerViewUsingGET_1(self, checker):
    """
    接口名称：人力Loading视图
    接口地址：/proj/$VERSION$/statistic/hrview
    """
    r = RequestService.call_get(apis.get("getManpowerViewUsingGET_1", None), params={
        "dimension": "",  # 维度(monthly/weekly/daily) - required: True
        "endDate": "",  # 结束日期，年/月/日（yyyy/MM/dd格式） - required: True
        "memberIds": "",  # 成员ID,多个以逗号隔开 - required: False
        "projectId": "",  # 项目ID - required: True
        "startDate": "",  # 开始日期，年/月/日（yyyy/MM/dd格式） - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getManpowerViewPageUsingGET(self, project_id, memberIds, startDate, endDate, dimension,
                                page_index, page_size, checker=None):
    """
    接口名称：分页查询人力Loading视图
    接口地址：/proj/$VERSION$/statistic/hrview/page
    """
    r = RequestService.call_get(apis.get("getManpowerViewPageUsingGET", None), params={
        "dimension": dimension,  # 维度(monthly/weekly/daily) - required: True
        "endDate": endDate,  # 结束日期，年/月/日（yyyy/MM/dd格式） - required: True
        "memberIds": memberIds,  # 成员ID,多个以逗号隔开 - required: False
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
        "projectId": project_id,  # 项目ID - required: True
        "startDate": startDate,  # 开始日期，年/月/日（yyyy/MM/dd格式） - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getManpowerViewdepartUsingGET(self, project_id, memberIds, departmentId, startDate, endDate,
                                  dimension, page_index, page_size, checker=None):
    """
    接口名称：人力视图报表
    接口地址：/proj/$VERSION$/statistic/hrviewdepart
    """
    r = RequestService.call_get(apis.get("getManpowerViewdepartUsingGET", None), params={
        "projectId": project_id,
        "departmentId": departmentId,  # 部门ID - required: True
        "dimension": dimension,  # 维度(monthly/weekly/daily) - required: True
        "endDate": endDate,  # 结束日期，年/月/日（yyyy/MM/dd格式） - required: True
        "memberIds": memberIds,  # 成员ID,多个以逗号隔开 - required: False
        "pageindex": page_index,  # 页码 - required: True
        "pagesize": page_size,  # 每页条数 - required: True
        "startDate": startDate,  # 开始日期，年/月/日（yyyy/MM/dd格式） - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getMonthlyReportsUsingGET(self, date, checker=None):
    """
    接口名称：研发工作月度统计报表
    接口地址：/proj/$VERSION$/statistic/monthlyreports
    """
    r = RequestService.call_get(apis.get("getMonthlyReportsUsingGET", None), params={
        "date": date  # 日期,格式：yyyy-mm - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def pageProjectUsingGET_1(self, page_index, page_size, project_ids, checker=None):
    """
    接口名称：根据项目id查询项目分页列表
    接口地址：/proj/$VERSION$/statistic/page/projects
    """
    r = RequestService.call_get(apis.get("pageProjectUsingGET_1", None), params={
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
        "project_ids": project_ids,  # 项目ids（多个状态以逗号分隔） - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getManpowerViewUsingGET_2(self, departmentId, pmId, starDateB, startDateA, checker=None):
    """
    接口名称：项目状态统计
    接口地址：/proj/$VERSION$/statistic/status/report
    """
    r = RequestService.call_get(apis.get("getManpowerViewUsingGET_2", None), params={
        "departmentId": departmentId,  # 部门ID - required: False
        "pmId": pmId,  # PMID - required: False
        "starDateB": starDateB,  # 日期B，年-月-日（yyyy-MM-dd格式） - required: True
        "startDateA": startDateA,  # 日期A，年-月-日（yyyy-MM-dd格式） - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']


def getTopProjectUsingGET(self, departmentId, page_index, page_size, checker=None):
    """
    接口名称：TOP项目清单报表
    接口地址：/proj/$VERSION$/statistic/topProject
    """
    r = RequestService.call_get(apis.get("getTopProjectUsingGET", None), params={
        "departmentId": departmentId,  # 虚拟部门Id - required: False
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def get_project_process(self, checker=None):
    """
    接口名称：项目进展统计报表
    接口地址：/proj/$VERSION$/statistic/progress
    """
    r = RequestService.call_get(apis.get("getProjectProcessUsingGET", None), params={
        "pageIndex": 1,
        "pagesize": 10
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

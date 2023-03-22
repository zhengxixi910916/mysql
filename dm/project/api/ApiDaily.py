
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
'''
日报
'''
apis = Api({
    "approveDeptReportUsingPOST": "/rpt/$VERSION$/daily/approve/dept",  # 部门主管审批日报
    "approveProjReportUsingPOST": "/rpt/$VERSION$/daily/approve/proj",  # 项目经理审批日报
    "submitReportUsingPOST": "/rpt/$VERSION$/daily/batch/submit",  # 提交审批日报
    "postDailyReportUsingPOST": "/rpt/$VERSION$/daily/save",  # 添加日报
    "searchDepartmentDailyReportUsingGET": "/rpt/$VERSION$/daily/search/depart",  # 查询部门日报
    "searchPersonDailyReportUsingGET": "/rpt/$VERSION$/daily/search/my",  # 当前用户查询日报
    "searchProjectDailyReportUsingGET": "/rpt/$VERSION$/daily/search/project",  # 查询项目日报
    "postAndSubmitDailyReportUsingPOST": "/rpt/$VERSION$/daily/submit",  # 添加日报并提交审批
    "deleteDailyReportUsingDELETE": "/rpt/$VERSION$/daily/%s",  # 删除日报
    "getDailyReportUsingGET": "/rpt/$VERSION$/daily/%s",  # 按id查询日报
    "editDailyReportUsingPUT": "/rpt/$VERSION$/daily/%s",  # 修改日报
})
def approveDeptReportUsingPOST(self, checker):
    """
    接口名称：部门主管审批日报
    接口地址：/rpt/$VERSION$/daily/approve/dept
    """
    r = RequestService.call_post(apis.get("approveDeptReportUsingPOST", None),json= {
                    "dto": ""  # 工时审批对象 - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def approveProjReportUsingPOST(self, checker):
    """
    接口名称：项目经理审批日报
    接口地址：/rpt/$VERSION$/daily/approve/proj
    """
    r = RequestService.call_post(apis.get("approveProjReportUsingPOST", None),json= {
                    "dto": ""  # 工时审批对象 - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def submitReportUsingPOST(self, checker):
    """
    接口名称：提交审批日报
    接口地址：/rpt/$VERSION$/daily/batch/submit
    """
    r = RequestService.call_post(apis.get("submitReportUsingPOST", None),json= {
                    "ids": ""  # 工时Id,支持多值,逗号分割 - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def postDailyReportUsingPOST(self, timeSheet, checker=None):
    """
    接口名称：添加日报
    接口地址：/rpt/$VERSION$/daily/save
    """
    r = RequestService.call_post(apis.get("postDailyReportUsingPOST", None),json= {
                    "timeSheet": timeSheet  # 工时信息 - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def searchDepartmentDailyReportUsingGET(self, checker):
    """
    接口名称：查询部门日报
    接口地址：/rpt/$VERSION$/daily/search/depart
    """
    r = RequestService.call_get(apis.get("searchDepartmentDailyReportUsingGET", None),params= {
                    "createBys": "",  # 创建人ID集合 - required: False
                    "deptStatus": "",  # 部门审批状态：0待提交，1待审核，2审核通过，3审核不通过 - required: False
                    "endDate": "",  # 结束时间 - required: False
                    "orgId": "",  # 部门主管职能查看当前部门，及当前部门成员的日报 - required: False
                    "pageindex": "",  # 第几页 - required: False
                    "pagesize": "",  # 一页条数 - required: False
                    "projStatus": "",  # 项目审批状态：0待提交，1待审核，2审核通过，3审核不通过 - required: False
                    "projectId": "",  # 项目经理可以查询负责项目中成员的日报 - required: False
                    "reportId": "",  # 周报ID - required: False
                    "reportIds": "",  # 周报ID集合 - required: False
                    "startDate": "",  # 开始时间 - required: False
                    "type": "",  # 考勤类型，数据字典值,-1、空或不传代表全部 - required: False
                    "userIds": "",  # 待查用户id列表 - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def searchPersonDailyReportUsingGET(self, checker):
    """
    接口名称：当前用户查询日报
    接口地址：/rpt/$VERSION$/daily/search/my
    """
    r = RequestService.call_get(apis.get("searchPersonDailyReportUsingGET", None),params= {
                    "createBys": "",  # 创建人ID集合 - required: False
                    "deptStatus": "",  # 部门审批状态：0待提交，1待审核，2审核通过，3审核不通过 - required: False
                    "endDate": "",  # 结束时间 - required: False
                    "orgId": "",  # 部门主管职能查看当前部门，及当前部门成员的日报 - required: False
                    "pageindex": "",  # 第几页 - required: False
                    "pagesize": "",  # 一页条数 - required: False
                    "projStatus": "",  # 项目审批状态：0待提交，1待审核，2审核通过，3审核不通过 - required: False
                    "projectId": "",  # 项目经理可以查询负责项目中成员的日报 - required: False
                    "reportId": "",  # 周报ID - required: False
                    "reportIds": "",  # 周报ID集合 - required: False
                    "startDate": "",  # 开始时间 - required: False
                    "type": "",  # 考勤类型，数据字典值,-1、空或不传代表全部 - required: False
                    "userIds": "",  # 待查用户id列表 - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def searchProjectDailyReportUsingGET(self, checker):
    """
    接口名称：查询项目日报
    接口地址：/rpt/$VERSION$/daily/search/project
    """
    r = RequestService.call_get(apis.get("searchProjectDailyReportUsingGET", None),params= {
                    "createBys": "",  # 创建人ID集合 - required: False
                    "deptStatus": "",  # 部门审批状态：0待提交，1待审核，2审核通过，3审核不通过 - required: False
                    "endDate": "",  # 结束时间 - required: False
                    "orgId": "",  # 部门主管职能查看当前部门，及当前部门成员的日报 - required: False
                    "pageindex": "",  # 第几页 - required: False
                    "pagesize": "",  # 一页条数 - required: False
                    "projStatus": "",  # 项目审批状态：0待提交，1待审核，2审核通过，3审核不通过 - required: False
                    "projectId": "",  # 项目经理可以查询负责项目中成员的日报 - required: False
                    "reportId": "",  # 周报ID - required: False
                    "reportIds": "",  # 周报ID集合 - required: False
                    "startDate": "",  # 开始时间 - required: False
                    "type": "",  # 考勤类型，数据字典值,-1、空或不传代表全部 - required: False
                    "userIds": "",  # 待查用户id列表 - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def postAndSubmitDailyReportUsingPOST(self, checker):
    """
    接口名称：添加日报并提交审批
    接口地址：/rpt/$VERSION$/daily/submit
    """
    r = RequestService.call_post(apis.get("postAndSubmitDailyReportUsingPOST", None),json= {
                    "timeSheet": ""  # 工时信息 - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteDailyReportUsingDELETE(self, checker):
    """
    接口名称：删除日报
    接口地址：/rpt/$VERSION$/daily/{ids}
    """
    r = RequestService.call_delete(apis.get("deleteDailyReportUsingDELETE", None),path= {
                    "ids": ""  # 待删除的id列表，用逗号分隔 - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getDailyReportUsingGET(self, checker):
    """
    接口名称：按id查询日报
    接口地址：/rpt/$VERSION$/daily/{id}
    """
    r = RequestService.call_get(apis.get("getDailyReportUsingGET", None),path= {
                    "id": ""  # 工时Id - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def editDailyReportUsingPUT(self, checker):
    """
    接口名称：修改日报
    接口地址：/rpt/$VERSION$/daily/{id}
    """
    r = RequestService.call_put(apis.get("editDailyReportUsingPUT", None),json= {
                    "timeSheet": ""  # 工时信息 - required: False
                },path= {
                    "id": ""  # 工时Id - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


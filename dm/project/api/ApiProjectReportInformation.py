
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
'''
项目报表信息 
'''
apis = Api({
    "showReportUsingGET": "/proj/$VERSION$/project/report/all",  # 查看项目自定义报表
    "addProjectReportUsingPOST": "/proj/$VERSION$/project/report",  # 保存项目报表基本信息
    "getProjectReportsUsingGET": "/proj/$VERSION$/project/report/all",  # 查询所有项目报表
    "getReportConfigUsingGET": "/proj/$VERSION$/project/report/config",  # 获取报表配置数据
    "getSingleProjectReportUsingGET": "/proj/$VERSION$/project/report/%s",  # 根据ID查询单个项目报表
    "updateProjectReportUsingPUT": "/proj/$VERSION$/project/report/%s",  # 修改项目报表
    "deleteProjectReportUsingDELETE": "/proj/$VERSION$/project/report/%s",  # 删除项目报表
})
def showReportUsingGET(self, project_id, checker=None):
    """
    接口名称：查看项目自定义报表
    接口地址：/proj/$VERSION$/project/report/all
    """
    r = RequestService.call_get(apis.get("showReportUsingGET"), params={
        "projectId": project_id
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def addProjectReportUsingPOST(self, checker):
    """
    接口名称：保存项目报表基本信息
    接口地址：/proj/$VERSION$/project/report
    """
    r = RequestService.call_post(apis.get("addProjectReportUsingPOST"),params= {
                    "createBy": "",  # None - required: False
                    "dimension": "",  # 维度值（纵轴） - required: False
                    "endTime": "",  # None - required: False
                    "filterJson": "",  # 过滤条件（json）） - required: False
                    "finishTime": "",  # None - required: False
                    "id": "",  # None - required: False
                    "milestones[0].actualFinishDate": "",  # None - required: False
                    "milestones[0].finishDate": "",  # None - required: False
                    "milestones[0].name": "",  # None - required: False
                    "name": "",  # None - required: False
                    "objectType": "",  # 对象类型（risk、issue、plan、req） - required: False
                    "orderType": "",  # 排序类型（1：由高到低；2：由低到高） - required: False
                    "projectId": "",  # 项目id - required: False
                    "quota": "",  # 指标值（横轴） - required: False
                    "sender": "",  # None - required: False
                    "startTime": "",  # None - required: False
                    "status": "",  # None - required: False
                    "updateTime": "",  # None - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getProjectReportsUsingGET(self, checker=None):
    """
    接口名称：查询所有项目报表
    接口地址：/proj/$VERSION$/project/report/all
    """
    r = RequestService.call_get(apis.get("getProjectReportsUsingGET"),params= {
                    "projectId": "",  # 项目id - required: False
                    "reportType": "",  # 报表类型（issue:问题；risk：风险；req：需求；task：任务） - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


# def getReportConfigUsingGET(self, checker):
#     """
#     接口名称：获取报表配置数据
#     接口地址：/proj/$VERSION$/project/report/config
#     """
#     r = RequestService.call_get(apis.get("getReportConfigUsingGET"),params= {
#                     "reportType": ""  # 报表类型（issue:问题；risk：风险；req：需求；task：任务） - required: False
#                 },)
#     apis.check_success(self, r)
#     if checker is not None:
#         self.assertEqual(checker, r["res"]["data"])
#     return r['res']["data"]


def getSingleProjectReportUsingGET(self, checker):
    """
    接口名称：根据ID查询单个项目报表
    接口地址：/proj/$VERSION$/project/report/{id}
    """
    r = RequestService.call_get(apis.get("getSingleProjectReportUsingGET"))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateProjectReportUsingPUT(self, checker):
    """
    接口名称：修改项目报表
    接口地址：/proj/$VERSION$/project/report/{id}
    """
    r = RequestService.call_put(apis.get("updateProjectReportUsingPUT"),json= {
                    "projectReport": ""  # 项目报表对象 - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteProjectReportUsingDELETE(self, checker):
    """
    接口名称：删除项目报表
    接口地址：/proj/$VERSION$/project/report/{id}
    """
    r = RequestService.call_delete(apis.get("deleteProjectReportUsingDELETE"))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


import os
import time
from contextlib import closing

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
任务统计报表
'''

# 获取上一级目录
dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dir_document = dir_path + r'/document'
times = time.strftime("%Y-%m-%d %H %M %S", time.localtime(time.time()))
file_name = "project_" + times + ".xlsx"

apis = Api({
    "ChartMilestone": "/plan/$VERSION$/chart/milestone/%s",  # 里程碑报表
    "ChartMilestoneExport": "/plan/$VERSION$/chart/milestoneexport/%s",  # 导出项目里程碑报表
    "ChartTask": "/plan/$VERSION$/chart/%s",  # 计划报表
    "ChartProjectExport": "/plan/$VERSION$/chartexport/%s",  # 导出项目计划报表
    "ChartReportMilestone": "/plan/$VERSION$/report/milestone",  # 按里程碑查询多项目里程碑变更报表API
    "ChartReportMilestoneDept": "/plan/$VERSION$/report/milestone/dept",  # 按部门查询多项目里程碑变更报表API
    "ChartMileStoneReport": "/plan/$VERSION$/task/getSingleMileStoneReport",  # 单个里程碑变更报表API
})


def ChartMilestone(self, project_id, ymonth, checker=None):
    """
    接口名称：里程碑报表
    接口地址：/plan/$VERSION$/chart/milestone/{project_id}
    """
    r = RequestService.call_get(apis.get("ChartMilestone", project_id), params={
        "ymonth": ymonth,
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def Chart_Milestoneexport(self, month):
    """
    接口名称：导出项目里程碑报表
    接口地址：/plan/$VERSION$/chart/milestoneexport/{project_id}
    """
    r = RequestService.call_get(apis.get("Chart_Milestoneexport"), params={
        "month": month  # 月份(yyyy-MM) - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def ChartTask(self, project_id, ymonth, checker=None):
    """
    接口名称：计划报表
    接口地址：/plan/$VERSION$/chart/{project_id}
    """
    r = RequestService.call_get(apis.get("ChartTask", project_id), params={
        "ymonth": ymonth,  # 年-月（yyyy-MM格式） - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def ChartProjectExport(self, month, project_id, exportIdList=None):
    """
    接口名称：导出项目计划报表
    接口地址：/plan/$VERSION$/chartexport/{project_id}
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("ChartProjectExport", project_id), params={
        "month": month,
        "exportIdList": exportIdList
    })) as response:
        with open(dir_document + r"\export_project_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def ChartReportMilestone(self, type, endTime, pm, startTime, checker=None):
    """
    接口名称：按里程碑查询多项目里程碑变更报表API
    接口地址：/plan/$VERSION$/report/milestone
    """
    r = RequestService.call_get(apis.get("ChartReportMilestone"), params={
        "type": type,  # departmentId - required: False
        "endTime": endTime,  # endTime - required: False
        "pm": pm,  # pm - required: False
        "startTime": startTime,  # startTime - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']


def ChartReportMilestoneDept(self, dataType, departmentId, endTime, pm, startTime, type, checker=None):
    """
    接口名称：按部门查询多项目里程碑变更报表API
    接口地址：/plan/$VERSION$/report/milestone/dept
    """
    r = RequestService.call_get(apis.get("ChartReportMilestoneDept"), params={
        "dataType": dataType,  # dataType - required: False
        "departmentId": departmentId,  # departmentId - required: False
        "endTime": endTime,  # endTime - required: False
        "pm": pm,  # pm - required: False
        "startTime": startTime,  # startTime - required: False
        "type": type
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']


def ChartMileStoneReport(self, projId, checker=None):
    """
    接口名称：单个里程碑变更报表API
    接口地址：/plan/$VERSION$/task/getSingleMileStoneReport
    """
    r = RequestService.call_get(apis.get("ChartMileStoneReport"), params={
        "projId": projId  # projId - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r

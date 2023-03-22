from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "showReportUsingGET": "/proj/$VERSION$/project/report",  # 查看项目自定义报表
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
    接口地址：/proj/$VERSION$/project/report
    """
    r = RequestService.call_get(apis.get("showReportUsingGET", None), params={
        "conditionJson": '[{"fieldDesc": "", "fieldName": "createTime", "fieldType": "datetime", "filedValue1": "1", "filedValue2": "month", "queryType": "din", "dicType": "", "linkUrl": ""}]',
        # 查询条件 - required: False
        "dimensionName": "priority",  # 纵坐标 - required: False
        "orderType": 1,  # 排序类型 - required: False
        "projectID": project_id,  # 项目id - required: False
        "quotaName": "priority",  # 横坐标 - required: False
        "reportType": "req",  # 报表类型（issue:问题；risk：风险；req：需求；task：任务） - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def addProjectReportUsingPOST(self, project_id, checker=None):
    """
    接口名称：保存项目报表基本信息
    接口地址：/proj/$VERSION$/project/report
    """
    r = RequestService.call_post(apis.get("addProjectReportUsingPOST", None), params={
        "createBy": "",  # 创建人 - required: False
        "dimension": "priority",  # 维度值（纵轴） - required: False
        "endTime": "",  # 报告结束时间 - required: False
        "filterJson": '[{"fieldDesc":"","fieldName":"createTime","fieldType":"datetime","filedValue1":"1","filedValue2":"month","queryType":"din","dicType":"","linkUrl":""}]',
        # 过滤条件（json）） - required: False
        "finishTime": "",  # 计划完成时间 - required: False
        "id": "",  # ID - required: False
        "milestones[0].actualFinishDate": "",  # None - required: False
        "milestones[0].finishDate": "",  # None - required: False
        "milestones[0].name": "",  # None - required: False
        "name": "需求状态分布图",  # 名称 - required: False
        "objectType": "req",  # 对象类型（risk、issue、plan、req） - required: False
        "orderType": 0,  # 排序类型（1：由高到低；2：由低到高） - required: False
        "projectId": project_id,  # 项目id - required: False
        "quota": "priority",  # 指标值（横轴） - required: False
        "sender": "",  # 发送人 - required: False
        "startTime": "",  # 报告开始时间 - required: False
        "status": "",  # 报告状态：1草稿，2已发送 - required: False
        "updateTime": "",  # 报告更新时间 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r["res"]["data"]


def getProjectReportsUsingGET(self, project_id, checker=None):
    """
    接口名称：查询所有项目报表
    接口地址：/proj/$VERSION$/project/report/all
    """
    r = RequestService.call_get(apis.get("getProjectReportsUsingGET", None), params={
        "projectId": project_id,  # 项目id - required: False
        "reportType": "",  # 报表类型（issue:问题；risk：风险；req：需求；task：任务） - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getReportConfigUsingGET(self, checker=None):
    """
    接口名称：获取报表配置数据
    接口地址：/proj/$VERSION$/project/report/config
    """
    r = RequestService.call_get(apis.get("getReportConfigUsingGET", None), params={
        "reportType": "req"  # 报表类型（issue:问题；risk：风险；req：需求；task：任务） - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getSingleProjectReportUsingGET(self, projectreport_id, checker=None):
    """
    接口名称：根据ID查询单个项目报表
    接口地址：/proj/$VERSION$/project/report/{id}
    """
    r = RequestService.call_get(apis.get("getSingleProjectReportUsingGET", projectreport_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def updateProjectReportUsingPUT(self, projectreport_id, project_id, checker=None):
    """
    接口名称：修改项目报表
    接口地址：/proj/$VERSION$/project/report/{id}
    """
    r = RequestService.call_put(apis.put("updateProjectReportUsingPUT", projectreport_id), json={
        "description": "",
        "dimension": "priority",
        "filterJson": "[{\"fieldDesc\":\"\",\"fieldName\":\"createTime\",\"fieldType\":\"datetime\",\"filedValue1\":\"1\",\"filedValue2\":\"month\",\"queryType\":\"din\",\"dicType\":\"\",\"linkUrl\":\"\"}]",
        "id": projectreport_id,
        "name": "需求状态分布图",
        "objectType": "req",
        "orderType": 0,
        "projectId": project_id,
        "quota": "priority"
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def deleteProjectReportUsingDELETE(self, projectreport_id, checker=None):
    """
    接口名称：删除项目报表
    接口地址：/proj/$VERSION$/project/report/{id}
    """
    r = RequestService.call_delete(apis.get("deleteProjectReportUsingDELETE", projectreport_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

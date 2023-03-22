from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目报告
'''
apis = Api({
    "downloadReportFileUsingGET": "/rpt/$VERSION$/export/report/excel",  # 导出项目报告
    "addReportUsingPOST": "/rpt/$VERSION$/report",  # 创建项目报告
    "delReportUsingDELETE": "/rpt/$VERSION$/report",  # 删除项目报告,支持多个删除
    "getReportUsingGET": "/rpt/$VERSION$/report/%s",  # 获取项目报告信息
    "updateReportUsingPUT": "/rpt/$VERSION$/report/%s",  # 修改项目报告
    "getReportsUsingGET": "/rpt/$VERSION$/reports",  # 获取项目报告分页列表
})


def downloadReportFileUsingGET(self, checker=None):
    """
    接口名称：导出项目报告
    接口地址：/rpt/$VERSION$/export/report/excel
    """
    r = RequestService.call_get(apis.get("downloadReportFileUsingGET", None), params={
        "ids": "",  # ids - required: False
        "projectId": "",  # 项目id - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def addReportUsingPOST(self, project_id, user_id, checker=None):
    """
    接口名称：创建项目报告
    接口地址：/rpt/$VERSION$/report
    """
    r = RequestService.call_post(apis.get("addReportUsingPOST", None), json={"id": "", "templateId": "", "name": "嘻嘻212",
         "type": 1, "projectId": project_id, "startTime": "2023-03-08", "endTime": "2023-03-09",
         "status": 2, "sender": ["SYS_E39B20EA11E7A81AC85B767C89C1"], "ccList": [],
         "receiver": [user_id], "items": [],
         "content": "<div style=\"padding: 5px 15px 0 15px;color:#aaa;\"><span data-lang=\"project_project-receiv_from\">您收到来自</span>【project_20230308】<span data-lang=\"project_project-project_report\">的项目报告</span>，<a href=\"http://ppm-uat.apps.okd4.ddns.e-lead.cn/index.html#jump.html?spm=m-2-0&md=dashboard:paper&pid=9e54012f0368ddc26770d2b2253c0604&tid=79f296ad2075e1b0d040b02c0b523e0f&isPaper=1\"><span data-lang=\"click_to_view\">点击查看</span></a></div><div class=\"preview-container\"><div style=\"padding-left: 10px;background-color: #f8f8f8;border-top: 1px solid #e7e7e7;border-bottom: 1px solid #e7e7e7;\"><h4>计划概览(计划列表)</h4></div><div style=\"padding-left: 10px;background-color: #f8f8f8;border-top: 1px solid #e7e7e7;border-bottom: 1px solid #e7e7e7;\"><h4>需要实现进度(需求列表)</h4></div><div style=\"padding-left: 10px;background-color: #f8f8f8;border-top: 1px solid #e7e7e7;border-bottom: 1px solid #e7e7e7;\"><h4>问题跟踪(问题列表)</h4></div></div>"
                                                                             })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delReportUsingDELETE(self, ids, checker=None):
    """
    接口名称：删除项目报告,支持多个删除
    接口地址：/rpt/$VERSION$/report
    """
    r = RequestService.call_delete(apis.get("delReportUsingDELETE", None), json=ids)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getReportUsingGET(self, reportId, checker=None):
    """
    接口名称：获取项目报告信息
    接口地址：/rpt/$VERSION$/report/{id}
    """
    r = RequestService.call_get(apis.get("getReportUsingGET", reportId), )

    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateReportUsingPUT(self, reportId, report, checker=None):
    """
    接口名称：修改项目报告
    接口地址：/rpt/$VERSION$/report/{id}
    """
    r = RequestService.call_put(apis.get("updateReportUsingPUT", reportId), json=report)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getReportsUsingGET(self,project_id, checker=None):
    """
    接口名称：获取项目报告分页列表
    接口地址：/rpt/$VERSION$/reports
    """
    r = RequestService.call_get(apis.get("getReportsUsingGET", None), params={
        "name": "",
        "type": "0",
        "status": "",
        "createBy": "",
        "dateFor": "",
        "startTime": "",
        "endTime": "",
        "pageSize": 20,
        "pageIndex": 1,
        "updateBy": "",
        "projectId": project_id,
        "orderBy":"createTime",
        "sortBy": "DESC"
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

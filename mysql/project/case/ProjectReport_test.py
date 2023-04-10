# -*- coding: utf-8 -*-
# @Time    : 2022/2/22
# @Author  : Chen

import unittest
import uuid
import time
from project.api import ApiProjectReport, ApiProject
from project.case.file.runSql import db

class ProjectReport(unittest.TestCase):
    """项目报告"""
    user_id = db.user_id
    project_id = ""
    org_id = db.org_id
    report_id = db.project_report_id

    def test_0100_addReportUsingPOST(self):
        """
        接口名称：创建项目报告
        接口地址：/rpt/$VERSION$/report
        """
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        addProjectUsingPOST_1 = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        print(addProjectUsingPOST_1)
        ProjectReport.project_id = addProjectUsingPOST_1.get('id')
        r2 = ApiProjectReport.addReportUsingPOST(self,
                                            project_id=ProjectReport.project_id,
                                            user_id=ProjectReport.user_id)
        print(r2)

    def test_0200_getReportsUsingGET(self):
        """
        接口名称：获取项目报告分页列表
        接口地址：/rpt/$VERSION$/reports
        """


        r = ApiProjectReport.getReportsUsingGET(self,project_id=ProjectReport.project_id)
        print(r)

    def test_0300_getReportUsingGET(self):
        """
        接口名称：获取项目报告信息
        接口地址：/rpt/$VERSION$/report/{id}
        """
        print(db.project_report_id)
        ApiProjectReport.getReportUsingGET(self,
                                           reportId="73be9a73bebfea8742d5a77893eecf46"
                                           )

    # def test_0400_updateReportUsingPUT(self):
    #     """
    #     接口名称：修改项目报告
    #     接口地址：/rpt/$VERSION$/report/{id}
    #     """
    #     ApiProjectReport.updateReportUsingPUT(self,
    #                                           reportId="73be9a73bebfea8742d5a77893eecf46",
    #                                           report=''
    #                                           )

    # def test_0500_downloadReportFileUsingGET(self):
    #     """
    #     接口名称：导出项目报告
    #     接口地址：/rpt/$VERSION$/export/report/excel
    #     """
    #     ApiProjectReport.downloadReportFileUsingGET(self,)

    def test_0600_delReportUsingDELETE(self):
        """
        接口名称：删除项目报告,支持多个删除
        接口地址：/rpt/$VERSION$/report
        """
        ApiProjectReport.delReportUsingDELETE(self,
                                              ids=[db.project_report_id]
                                              )
        # 删除项目
        deleteProjectUsingDELETE = ApiProject.deleteProjectUsingDELETE(self, project_id=ProjectReport.project_id)
        print(deleteProjectUsingDELETE)


if __name__ == "__main__":
    unittest.main()

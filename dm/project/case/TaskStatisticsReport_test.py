# -*- coding: utf-8 -*-
# @Time    : 2022/02/23
# @Author  : Chen

import unittest, time
from project.api import ApiTaskStatisticsReport
from project.case.file.runSql import db


class TaskStatisticsRport(unittest.TestCase):
    """任务统计报表"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_ChartMilestone(self):
        """
        接口名称：里程碑报表
        接口地址：/plan/$VERSION$/chart/milestone/{project_id}
        """
        ApiTaskStatisticsReport.ChartMilestone(self,
                                               project_id=db.project_id,
                                               ymonth=time.strftime('%Y-%m', time.localtime())
                                               )

    def test_0200_ChartTask(self):
        """
        接口名称：计划报表
        接口地址：/plan/$VERSION$/chart/{project_id}
        """
        ApiTaskStatisticsReport.ChartTask(self,
                                          project_id=db.project_id,
                                          ymonth=time.strftime('%Y-%m', time.localtime()),
                                          )

    def test_0300_ChartReportMilestone(self):
        """
        接口名称：按里程碑查询多项目里程碑变更报表API
        接口地址：/plan/$VERSION$/report/milestone
        """
        ApiTaskStatisticsReport.ChartReportMilestone(self,
                                                     type="milestone",
                                                     endTime=time.strftime('%Y-%m-d', time.localtime()),
                                                     pm=db.user_id,
                                                     startTime="2001-01-01"
                                                     )

    def test_0400_ChartReportMilestoneDept(self):
        """
        接口名称：按部门查询多项目里程碑变更报表API
        接口地址：/plan/$VERSION$/report/milestone/dept
        """
        ApiTaskStatisticsReport.ChartReportMilestoneDept(self,
                                                         dataType="1",
                                                         departmentId=db.org_id,
                                                         endTime=time.strftime('%Y-%m-d', time.localtime()),
                                                         pm=db.user_id,
                                                         startTime="2001-01-01",
                                                         type="department"
                                                         )

    def test_0500_ChartMileStoneReport(self):
        """
        接口名称：单个里程碑变更报表API
        接口地址：/plan/$VERSION$/task/getSingleMileStoneReport
        """
        ApiTaskStatisticsReport.ChartMileStoneReport(self,
                                                     projId=db.project_id
                                                     )


if __name__ == '__main__':
    unittest.main(verbosity=2)

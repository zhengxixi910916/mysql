# -*- coding: utf-8 -*-
# @Time    : 2022/02/17
# @Author  : Chen

import time
import unittest
from project.api import ApiProblemStatisticalReport
from project.case.file.runSql import db


class ProblemStatisticalReport(unittest.TestCase):
    """
    问题统计报表
    """
    project_id = db.project_id

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        print("delete sql")
        # db.delete_sql()

    def test_0100_getIssueChartUsingGET(self):
        """问题统计报表"""
        r = ApiProblemStatisticalReport.getIssueChartUsingGET(self,
                                                              project_id=ProblemStatisticalReport.project_id,
                                                              ymonth=time.strftime('%Y-%m', time.localtime())
                                                              )
        print("r:", r)

    # def test_0200_exportIssueChartUsingGET(self):
    #     """导出项目问题报表"""
    #     ApiProblemStatisticalReport.exportIssueChartUsingGET(self,
    #
    #                                                          )


if __name__ == '__main__':
    unittest.main()

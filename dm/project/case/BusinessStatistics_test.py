# -*- coding: utf-8 -*-
# @Time    : 2022/02/22
# @Author  : Chen
import time
import unittest
from project.api import ApiBusinessStatistics
from project.case.file.runSql import db


class BusinessStatistics(unittest.TestCase):
    """业务统计"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass

    def test_0100_queryBusinessCountUsingGET(self):
        """
        接口名称：业务数据统计未创建流程的、未完成的数量
        接口地址：/proj/business/statistics/count
        """
        ApiBusinessStatistics.queryBusinessCountUsingGET(self,
                                                         project="all",
                                                         type="all",
                                                         assignee=db.user_id,
                                                         startDate="2001-01-01",
                                                         endDate=time.strftime('%Y-%m-%d',time.localtime()),
                                                         expiredNdaysUnfinished="",
                                                         createNdaysUnStartProcess="",
                                                         page_index="1",
                                                         page_size="10"
                                                         )

    def test_0200_queryBusinessDataUsingGET(self):
        """
        接口名称：业务数据统计未创建流程的、未完成的数据
        接口地址：/proj/business/statistics/data
        """
        ApiBusinessStatistics.queryBusinessDataUsingGET(self,
                                                        project="all",
                                                        type="all",
                                                        assignee=db.user_id,
                                                        startDate="2001-01-01",
                                                        endDate=time.strftime('%Y-%m-%d', time.localtime()),
                                                        expiredNdaysUnfinished="",
                                                        createNdaysUnStartProcess="",
                                                        page_index="1",
                                                        page_size="10",
                                                        condition="createNdaysUnStartProcess"
                                                        )


if __name__ == '__main__':
    unittest.main()
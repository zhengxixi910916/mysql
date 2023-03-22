# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 15:04
# @Author  : Liao

import time
import unittest

from project.api import ApiTaskStatistic
from project.case.file.runSql import db


class TaskStatistics(unittest.TestCase):
    """任务统计"""
    user_id = db.user_id
    static_date = time.strftime('%Y-%m', time.localtime())

    @classmethod
    def setUpClass(cls):
        print(__name__)
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_get_statistic_members(self):
        """
        查询统计人员列表
        """
        # /plan/v1/statistic/members
        static_members = ApiTaskStatistic.get_statistic_members(self)
        print(static_members)

    def test_0200_get_worksummary(self):
        """
        成员个人工作总结统计报表
        """
        # /plan/v1/statistic/{userId}/worksummary
        worksummary = ApiTaskStatistic.get_worksummary(self,
                                                       TaskStatistics.user_id,
                                                       TaskStatistics.static_date)
        print(worksummary)


if __name__ == '__main__':
    unittest.main()

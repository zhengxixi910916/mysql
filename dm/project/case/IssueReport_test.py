# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 15:31
# @Author  : Liao
import time
import unittest
from project.api import ApiIssueReport


class IssueReport(unittest.TestCase):
    """问题报表"""

    def test_0100_classified_statistics(self):
        """
        问题分类统计
        """
        # /issue/v1/classifiedStatistics
        classified_static = ApiIssueReport.classified_statistics(self)
        print(classified_static)

    def test_0200_closing_rate(self):
        """
        问题关闭率
        """
        # /issue/v1/closingRate
        dimension = "week"
        startDate = time.strftime('%Y-%m-%d', time.localtime())
        finishDate = time.strftime('%Y-%m-%d', time.localtime())
        state = "CLOSED"
        close_rate = ApiIssueReport.closing_rate(self, dimension, startDate, finishDate, state)
        print(close_rate)

    def test_0300_improvement_time_statistics(self):
        """
        解析改善时间统计
        """
        # /issue/v1/improvementTimeStatistics
        improve_time_static = ApiIssueReport.improvement_time_statistics(self)
        print(improve_time_static)

    def test_0400_overdue_closed_statistics(self):
        """
        超期未关闭
        """
        # /issue/v1/overdueNotClosedStatistics
        overdue_closed_static = ApiIssueReport.overdue_closed_statistics(self)
        print(overdue_closed_static)

    def test_0500_issue_risk_statistics(self):
        """
        问题的风险统计 （高中低）
        """
        # /issue/v1/riskStatistics
        risk_statistics = ApiIssueReport.issue_risk_statistics(self)
        print(risk_statistics)

if __name__ == '__main__':
    unittest.TestCase()
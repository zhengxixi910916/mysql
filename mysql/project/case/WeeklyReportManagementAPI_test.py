# -*- coding: utf-8 -*-
# @Time    : 2022/02/17
# @Author  : Chen

import unittest
from project.api import ApiWeeklyReportManagementAPI
from project.case.file.runSql import db
import datetime
import random


class WeeklyReportManagementAPI(unittest.TestCase):
    """周报管理Api"""

    @classmethod
    def tearDownClass(cls):
        db.delete_sql()

    @staticmethod
    def get_week():
        y = random.randint(1949, datetime.datetime.now().year)
        m = random.randint(1, 12)
        d = random.randint(1, 28)
        week_num = datetime.datetime(int(y), int(m), int(d)).isocalendar()[1]
        day_time = f"{y}-{m}-{d}"
        return y, day_time, week_num

    @staticmethod
    def get_week_monday_and_sunday_by_date(date_str):
        """
        :param date_str:
        :return: 周一和周日的日期
        """
        now_time = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        week_start_time = now_time - datetime.timedelta(days=now_time.weekday())
        week_end_time = week_start_time + datetime.timedelta(days=6)
        return week_start_time.date(), week_end_time.date()

    @unittest.skip('该接口已未使用')
    def test_0100_addWeeklyUsingPOST(self):
        """
        接口名称：添加周报数据
        接口地址：/rpt/$VERSION$/api/weekly
        """
        # 获取随机日起在当年的周
        year, day, week = self.get_week()
        # 返回日期当前周的周一和周日
        monday, sunday = self.get_week_monday_and_sunday_by_date(day)
        ApiWeeklyReportManagementAPI.addWeeklyUsingPOST(self,
                                                        year=year,
                                                        weekOfYear=week,
                                                        startTime=str(monday),
                                                        finishTime=str(sunday),
                                                        title="测试",
                                                        remark="",
                                                        reporterId="SYS_E39B20EA11E7A81AC85B767C89C1",
                                                        submitId="SYS_E39B20EA11E7A81AC85B767C89C1",
                                                        takeoverIds=db.user_id,
                                                        copyToIds="",
                                                        stateKey="1",
                                                        )


if __name__ == '__main__':
    unittest.main()

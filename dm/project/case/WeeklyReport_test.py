# -*- coding: utf-8 -*-
# @Time    : 2022/2/23
# @Author  : yangjiong

import unittest
from project.api import ApiWeekReport
from project.api import ApiWeekReport
from project.case.file.runSql import db
import datetime
import random


class WeeklyReport(unittest.TestCase):
    """周报管理Api"""

    # 问题报告接收人id
    takeoverIds = db.user_id
    project_id = db.project_id
    projectName = db.project_name
    week_id = ''
    start_date = ''
    end_date = ''
    week_userId = ''
    year = ''
    week = ''
    week_of_year = ''
    task_list = None

    def setUp(self) -> None:
        # 获取随机日起在当年的周
        year, day, week = self.get_week()
        # 返回日期当前周的周一和周日
        monday, sunday = self.get_week_monday_and_sunday_by_date(day)
        WeeklyReport.year = year
        WeeklyReport.week = week
        WeeklyReport.start_date = monday
        WeeklyReport.end_date = sunday

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

    def test_0100_getDurationTasksUsingGET(self):
        """
        接口名称：获取任务列表
        接口地址：/rpt/$VERSION$/tasks
        """
        r = ApiWeekReport.getDurationTasksUsingGET(self,
                                                   checker=None,
                                                   startDate=WeeklyReport.start_date,
                                                   endDate=WeeklyReport.end_date
                                                   )
        WeeklyReport.task_list = r['res']['data']

    def test_0200_addWeeklyUsingPOST(self):
        """
        接口名称：添加周报数据
        接口地址：/rpt/$VERSION$/api/weekly
        """
        # 获取任务信息
        task_dir_list = []
        for task in WeeklyReport.task_list:
            task_dir_list.append({
                "taskId": task['id'],
                "projectId": task['projectId'],
                "projectName": "",
                "name": task['name'],
                "description": "",
                "startTime": None,
                "endTime": None,
                "stateKey": "PROCESSION",
                "percentage": None,
                "planflag": "1",
                "estimatedDuration": None,
                "cumulativeDuration": None,
                "actualDuration": None,
                "nowWeeklyWork": None,
                "state": "PROCESSION",
                "roleKey": [],
                "roleKey1": [
                    "管理员"
                ],
                "roleKey2": [],
                "weeklyWorkRecord": task['weeklyWorkRecord']
            })

        data = {
            "year": WeeklyReport.year,
            "weekOfYear": WeeklyReport.week,
            "startTime": str(WeeklyReport.start_date),
            "finishTime": str(WeeklyReport.end_date),
            "title": f"管理员 {WeeklyReport.year}第{WeeklyReport.week}周的周报",
            "remark": '',
            "reporterId": "SYS_E39B20EA11E7A81AC85B767C89C1",
            "submitId": "SYS_E39B20EA11E7A81AC85B767C89C1",
            "takeoverIds": WeeklyReport.takeoverIds,
            "copyToIds": '',
            "stateKey": 1,
            "weeklyPlan": [],
            "weeklyFinish": task_dir_list,
            "weeklyTimesheet": [
                {
                    "workDate": 1645401600000,
                    "startTime": 1645403400000,
                    "endTime": 1645437600000,
                    "type": 0,
                    "freeWorkTime": 1.5,
                    "workTime": 8,
                    "project_id": WeeklyReport.project_id,
                    "projectName": WeeklyReport.projectName,
                    "isTravel": 0,
                    "remarks": '',
                    "sort": 0
                },
                {
                    "workDate": 1645488000000,
                    "startTime": 1645489800000,
                    "endTime": 1645524000000,
                    "type": 0,
                    "freeWorkTime": 1.5,
                    "workTime": 8,
                    "project_id": WeeklyReport.project_id,
                    "projectName": WeeklyReport.projectName,
                    "isTravel": 0,
                    "remarks": '',
                    "sort": 1
                },
                {
                    "workDate": 1645574400000,
                    "startTime": 1645576200000,
                    "endTime": 1645610400000,
                    "type": 0,
                    "freeWorkTime": 1.5,
                    "workTime": 8,
                    "project_id": WeeklyReport.project_id,
                    "projectName": WeeklyReport.projectName,
                    "isTravel": 0,
                    "remarks": '',
                    "sort": 2
                },
                {"workDate": 1645660800000,
                 "startTime": 1645662600000,
                 "endTime": 1645696800000,
                 "type": 0,
                 "freeWorkTime": 1.5,
                 "workTime": 8,
                 "project_id": WeeklyReport.project_id,
                 "projectName": WeeklyReport.projectName,
                 "isTravel": 0,
                 "remarks": '',
                 "sort": 3
                 },
                {"workDate": 1645747200000,
                 "startTime": 1645749000000,
                 "endTime": 1645783200000,
                 "type": 0,
                 "freeWorkTime": 1.5,
                 "workTime": 8,
                 "project_id": WeeklyReport.project_id,
                 "projectName": WeeklyReport.projectName,
                 "isTravel": 0,
                 "remarks": '',
                 "sort": 4
                 },
            ]
        }

        r = ApiWeekReport.addWeeklyUsingPOST_1(self,
                                               checker=None,
                                               data=data
                                               )
        WeeklyReport.week_id = r['res']['data']

    def test_0300_updateDraftUsingPUT(self):
        """
        接口名称：修改周报草稿数据
        接口地址：/rpt/$VERSION$/weekly/draft
        """
        # 获取随机日起在当年的周
        year, day, week = self.get_week()
        # 返回日期当前周的周一和周日
        monday, sunday = self.get_week_monday_and_sunday_by_date(day)
        WeeklyReport.start_date = monday
        WeeklyReport.end_date = sunday
        WeeklyReport.year = year
        WeeklyReport.week_of_year = week
        data = {
            "id": WeeklyReport.week_id,
            "year": year,
            "weekOfYear": week,
            "startTime": str(monday),
            "finishTime": str(sunday),
            "title": f"管理员 {year}第{week}周的周报",
            "remark": '',
            "reporterId": "SYS_E39B20EA11E7A81AC85B767C89C1",
            "submitId": "SYS_E39B20EA11E7A81AC85B767C89C1",
            "takeoverIds": WeeklyReport.takeoverIds,
            "copyToIds": "",
            "weeklyTimesheet": [
                {
                    "workDate": 1645747200000,
                    "startTime": 1645749000000,
                    "endTime": 1645783200000,
                    "type": "0",
                    "freeWorkTime": 1.5,
                    "workTime": 8,
                    "projectId": WeeklyReport.project_id,
                    "projectName": WeeklyReport.projectName,
                    "isTravel": 0,
                    "remarks": "",
                    "sort": 0
                },
                {
                    "workDate": 1645660800000,
                    "startTime": 1645662600000,
                    "endTime": 1645696800000,
                    "type": "0",
                    "freeWorkTime": 1.5,
                    "workTime": 8,
                    "projectId": WeeklyReport.project_id,
                    "projectName": WeeklyReport.projectName,
                    "isTravel": 0,
                    "remarks": "",
                    "sort": 1
                },
                {
                    "workDate": 1645574400000,
                    "startTime": 1645576200000,
                    "endTime": 1645610400000,
                    "type": "0",
                    "freeWorkTime": 1.5,
                    "workTime": 8,
                    "projectId": WeeklyReport.project_id,
                    "projectName": WeeklyReport.projectName,
                    "isTravel": 0,
                    "remarks": "",
                    "sort": 2
                },
                {
                    "workDate": 1645488000000,
                    "startTime": 1645489800000,
                    "endTime": 1645524000000,
                    "type": "0",
                    "freeWorkTime": 1.5,
                    "workTime": 8,
                    "projectId": WeeklyReport.project_id,
                    "projectName": WeeklyReport.projectName,
                    "isTravel": 0,
                    "remarks": "",
                    "sort": 3
                },
                {
                    "workDate": 1645401600000,
                    "startTime": 1645403400000,
                    "endTime": 1645437600000,
                    "type": "0",
                    "freeWorkTime": 1.5,
                    "workTime": 8,
                    "projectId": WeeklyReport.project_id,
                    "projectName": WeeklyReport.projectName,
                    "isTravel": 0,
                    "remarks": "",
                    "sort": 4
                }
            ],
            "stateKey": 1
        }
        r = ApiWeekReport.updateDraftUsingPUT(self,
                                              checker={
                                                  "code": '10003',
                                                  "success": False
                                              },
                                              data=data
                                              )
        if r['code'] == "200":
            WeeklyReport.week_userId = r['res']['data']

    def test_0400_queryWeeklyUsingGET(self):
        """
        接口名称：根据id获取周报数据
        接口地址：/rpt/$VERSION$/weekly/{id}
        """
        ApiWeekReport.queryWeeklyUsingGET(self,
                                          checker=None,
                                          week_id=WeeklyReport.week_id
                                          )

    @unittest.skip('没有找到接口，应该没用了')
    def test_0500_queryByYearAndWeekUsingGET(self):
        """
        接口名称：根据年月获取周报
        接口地址：/rpt/$VERSION$/weekly/{year}/{week}
        """
        ApiWeekReport.queryByYearAndWeekUsingGET(self,
                                                 checker=None,
                                                 year=WeeklyReport.year,
                                                 weekOfYear=WeeklyReport.week_of_year
                                                 )

    # todo
    @unittest.skip('无返回码，需要断言其他的')
    def test_0600_downloadFileUsingGET(self):
        """
        接口名称：导出周报timesheet
        接口地址：/rpt/$VERSION$/export/excel
        """
        ApiWeekReport.downloadFileUsingGET(self,
                                           checker=None
                                           )

    def test_0900_queryPageUsingGET_1(self):
        """
        接口名称：获取周报分页数据
        接口地址：/rpt/$VERSION$/weeklies
        """
        ApiWeekReport.queryPageUsingGET_1(self)

    def test_1000deleteDraftUsingDELETE(self):
        """
        接口名称：删除周报草稿
        接口地址：/rpt/$VERSION$/weekly/{id}
        """
        ApiWeekReport.deleteDraftUsingDELETE(self,
                                             checker=None,
                                             id=WeeklyReport.week_id
                                             )


if __name__ == '__main__':
    unittest.main()

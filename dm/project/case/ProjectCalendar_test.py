# -*- coding: utf-8 -*-
# @Time    : 2022/02/22
# @Author  : Chen

import unittest, time
from project.api import ApiProjectCalendar,ApiProject
from project.case.file.runSql import db


class ProjectCalendar(unittest.TestCase):
    """项目日历"""
    holiday_id = ""
    project_id = ""

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_updateCalendarUsingPUT(self):
        """
        接口名称：修改日历
        接口地址：/proj/$VERSION$/calendar/{project_id}
        """
        # 新增项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        addProjectUsingPOST_1 = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        print(addProjectUsingPOST_1)
        ProjectCalendar.project_id = addProjectUsingPOST_1.get("id")


        ApiProjectCalendar.updateCalendarUsingPUT(self,
                                                  project_id=ProjectCalendar.project_id,
                                                  calendar={
                                                      "cycle": "1,2,3,4,5",
                                                      "isIncludeException": "0",
                                                      "startTime": "2022-02-22",
                                                      "repeatMode": "1",
                                                      "lastMonth": 1,
                                                      "weeks": 6,
                                                      "fewWeeks": -1,
                                                      "repeatCycle": "",
                                                      "happenTime": "",
                                                      "computeType": "0",
                                                      "repetitions": 1,
                                                      "finishTime": "",
                                                      "id": db.projCalendar_id,
                                                      "projectId": ProjectCalendar.project_id ,
                                                      "sysCalendarId": db.sysCalendar_id
                                                  }
                                                  )

    def test_0200_addHolidayUsingPOST(self):
        """
        接口名称：新增日历节假日
        接口地址：/proj/$VERSION$/holiday
        """
        ApiProjectCalendar.addHolidayUsingPOST(self,
                                               calendarId=db.sysCalendar_id,
                                               name="test_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime()),
                                               startTime=time.strftime('%Y-%m', time.localtime()) + "-1",
                                               finishTime=time.strftime('%Y-%m-%d', time.localtime()),
                                               year=time.strftime('%Y', time.localtime()),
                                               dayType="0",
                                               project_id=ProjectCalendar.project_id
                                               )

    def test_0300_getCalendarByIdUsingGET(self):
        """
        接口名称：查询项目日历
        接口地址：/proj/$VERSION$/calendar/{project_id}
        """
        r = ApiProjectCalendar.getCalendarByIdUsingGET(self,
                                                       project_id=ProjectCalendar.project_id ,
                                                       year=time.strftime('%Y', time.localtime())
                                                       )
        print("r:", r)
        ProjectCalendar.holiday_id = r["listProjectHoliday"][0]["id"]
        print("ProjectCalendar.holiday_id:", ProjectCalendar.holiday_id)

    def test_0400_getHolidayByIdUsingGET(self):
        """
        接口名称：查询节假日详情
        接口地址：/proj/$VERSION$/holiday/{id}
        """
        ApiProjectCalendar.getHolidayByIdUsingGET(self,
                                                  projCalendar_id=ProjectCalendar.holiday_id,
                                                  year=time.strftime('%Y', time.localtime())
                                                  )

    def test_0500_updateHolidayUsingPUT(self):
        """
        接口名称：修改节假日
        接口地址：/proj/$VERSION$/holiday/{id}
        """
        ApiProjectCalendar.updateHolidayUsingPUT(self,
                                                 id=ProjectCalendar.holiday_id,
                                                 cHoliday={
                                                     "id": ProjectCalendar.holiday_id,
                                                     "name": "测试13123111",
                                                     "startTime": "2022-04-05",
                                                     "finishTime": "2022-04-06",
                                                     "year": 2022,
                                                     "dayType": "1",
                                                     "projectId": ProjectCalendar.project_id
                                                 }
                                                 )

    def test_0600_deleteHolidayUsingDELETE(self):
        """
        接口名称：删除节假日
        接口地址：/proj/$VERSION$/holiday
        """
        ApiProjectCalendar.deleteHolidayUsingDELETE(self,
                                                    arrayIds=["ProjectCalendar.holiday_id"]
                                                    )

        # 删除项目
        deleteProjectUsingDELETE = ApiProject.deleteProjectUsingDELETE(self, project_id=ProjectCalendar.project_id)
        print(deleteProjectUsingDELETE)



if __name__ == '__main__':
    unittest.main()

import time
import unittest
from project.api import ApiSchedule
from project.case.file.runSql import db


class Schedule(unittest.TestCase):
    """日程"""
    agenda_id = ""
    user_id = "SYS_E39B20EA11E7A81AC85B767C89C1"

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_saveAgendaUsingPOST(self):
        """
        接口名称：保存日程及相关信息，发送提醒信息
        接口地址：/agenda/$VERSION$/save
        """
        r = ApiSchedule.saveAgendaUsingPOST(self,
                                            topicType="0",
                                            topicId="",
                                            type="1",
                                            name="test1",
                                            project_id="",
                                            startTime="2022-03-18 16:16:56",
                                            endTime="2022-03-18 23:16:56",
                                            recurrence="0",
                                            remindMinite="0",
                                            userId=Schedule.user_id,
                                            description=None
                                            )
        print(r)

    def test_0200_getFormeAgendaListUsingGET(self):
        """
        接口名称：我的工作台获取日程信息
        接口地址：/agenda/$VERSION$/forme/{startTime}/{endTime}
        """
        r = ApiSchedule.getFormeAgendaListUsingGET(self,
                                                   startTime="978278400000",  # 2001-01-01 00:00:00
                                                   endTime="4133952000000",  # 2101-01-01 00:00:00
                                                   showMode="-1"
                                                   )
        print(r)
        Schedule.agenda_id = r[0]["id"]
        print("Schedule.agendaId:", Schedule.agenda_id)

    def test_0300_getProjectAgendaListUsingGET(self):
        """
        接口名称：获取项目日程信息
        接口地址：/agenda/$VERSION$/project/agenda/{startTime}/{endTime}
        """
        ApiSchedule.getProjectAgendaListUsingGET(self,
                                                 startTime="978278400000",  # 2001-01-01 00:00:00
                                                 endTime="4133952000000",  # 2101-01-01 00:00:00
                                                 project_id=db.project_id,
                                                 showMode="-1   "
                                                 )

    def test_0400_getAgendaUsingGET(self):
        """
        接口名称：获取日程信息
        接口地址：/agenda/$VERSION$/{id}
        """
        ApiSchedule.getAgendaUsingGET(self,
                                      id=Schedule.agenda_id
                                      )

    def test_0500_editAgendaUsingPUT(self):
        """
        接口名称：修改日程信息
        接口地址：/agenda/$VERSION$/{id}/{editType}
        """
        ApiSchedule.editAgendaUsingPUT(self,
                                       id=Schedule.agenda_id,
                                       editType="1",
                                       arrs=[{"userId": db.user_id}],
                                       endTime="2021-08-06 13:17:29",
                                       name="test3",
                                       project_id="",
                                       remindMinite="0",
                                       startTime="2021-08-06 11:17:29",
                                       topicId="",
                                       topicType="0",
                                       type="1"
                                       )

    def test_0600_deleteAgendaUsingDELETE(self):
        """
        接口名称：删除日程
        接口地址：/agenda/$VERSION$/delete/{id}/{type}
        """
        ApiSchedule.deleteAgendaUsingDELETE(self,
                                            id=Schedule.agenda_id,
                                            type="1"
                                            )


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
# @Time    : 2022/02/17
# @Author  : Chen

import unittest
from project.api import ApiMilestoneReport
from project.case.file.runSql import db


class MilestoneReport(unittest.TestCase):
    """里程碑达成率统计/里程碑报表"""
    project_id = db.project_id

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_getProjectByTypeUsingGET(self):
        """
        接口名称：通过里程碑的名称获取项目
        接口地址：/plan/$VERSION$/getProjectByType
        """
        ApiMilestoneReport.getProjectByTypeUsingGET(self,
                                                    pmId="",
                                                    department="",
                                                    dimension="milestone",
                                                    statsType="actual",
                                                    departdimension="",
                                                    startDate="2021-11-19",
                                                    endDate="2022-02-17",
                                                    type="count",
                                                    name="测试2",
                                                    page_size="10",
                                                    page_index="1"
                                                    )

    # def test_0200_getTaskByproject_idsUsingGET(self):
    #     """
    #     接口名称：通过项目id获取里程碑数据
    #     接口地址：/plan/$VERSION$/getTaskByprojectIds
    #     """
    #     ApiMilestoneReport.getTaskByproject_idsUsingGET(self)

    def test_0300_milestoneAchievementRateUsingGET(self):
        """
        接口名称：里程碑达成率统计
        接口地址：/plan/$VERSION$/milestoneAchievementRate
        """
        ApiMilestoneReport.milestoneAchievementRateUsingGET(self,
                                                            pmId="",
                                                            department="",
                                                            dimension="milestone",
                                                            statsType="actual",
                                                            departdimension="",
                                                            startDate="2022-02-17",
                                                            endDate="2022-02-17"
                                                            )

    def test_0400_getPublishMilestoneUsingGET(self):
        """
        接口名称：通过项目获取立项里程碑数据
        接口地址：/plan/$VERSION$/{project_id}/baseline/milestone
        """
        ApiMilestoneReport.getPublishMilestoneUsingGET(self,
                                                       project_id=MilestoneReport.project_id
                                                       )


if __name__ == '__main__':
    unittest.main()

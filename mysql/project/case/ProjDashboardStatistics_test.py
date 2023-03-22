# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 17:36
# @Author  : Liao

import unittest
from project.api import ApiDashboard
from project.case.file.runSql import db


class ProjDashboardStatistics(unittest.TestCase):
    """项目Dashboard统计信息"""

    project_id = db.project_id
    print("project_id=",project_id)

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_get_proj_state(self):
        """
        获取项目状态分布
        """
        # /proj/v1/dashboard/project/state
        ApiDashboard.get_proj_state(self)

    def test_0200_select_proj_state(self):
        """
        获取项目状态
        """
        # /proj/v1/dashboard/project/taskstate
        # 发现必填limit参数可以不填
        ApiDashboard.select_proj_state(self, 5)

    def test_0300_get_proj_type(self):
        """
        获取项目类型分布
        """
        # /proj/v1/dashboard/project/type
        ApiDashboard.get_proj_state(self)

    def test_0400_get_proj_oneself(self):
        """
        工作台个人工作项目总数
        """
        # /proj/v1/dashboard/workbench
        one_workbench = ApiDashboard.get_proj_oneself(self)
        print(one_workbench)

    def test_0500_get_proj_progress(self):
        """
        获取项目进度
        """
        # /proj/v1/dashboard/{ids}/progress
        proj_grocess = ApiDashboard.get_proj_progress(self, eid=ProjDashboardStatistics.project_id)
        print(proj_grocess)

    def test_0600_get_proj_id_created_resolved(self):
        """
        根据项目ID查询业务的created & resolved情况
        """
        # /proj/v1/dashboard/{id}/created/resolved
        created_resolved = ApiDashboard.get_proj_id_created_resolved(self, eid=ProjDashboardStatistics.project_id)
        print(created_resolved)



if __name__ == '__main__':
    unittest.main()

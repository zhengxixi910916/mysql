# -*- coding: utf-8 -*-
# @Time    : 2022/02/24
# @Author  : Chen

import unittest
from project.api import ApiExport
from project.case.file.runSql import db


class ExportProjectTest(unittest.TestCase):
    """导出"""
    project_id = db.project_id

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_Export_project(self):
        """
        接口名称：导出项目
        接口地址：/proj/v2/export
        """
        r = ApiExport.ExportProject(self,
                                    exprotList="name",
                                    exportIdList="")
        print(r)

    def test_0200_Export_project_members(self):
        """
        接口名称：导出项目成员
        接口地址：/proj/v2/exportProjectMember
        """
        r = ApiExport.ExportProjectMembers(self,
                                           project_id=db.project_id)
        print(r)


if __name__ == '__main__':
    unittest.main()

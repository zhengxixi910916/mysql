# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 15:04
# @Author  : Liao
import unittest
from project.api import ApiMemberChange
from project.case.file.runSql import db


class MemberChange(unittest.TestCase):
    """项目成员替换历史查询"""

    project_id = db.project_id
    print(project_id)

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_get_member_change_data(self):
        """
        项目成员替换历史查询
        """
        # /proj/v1/change/member/{id}
        get_member_result = ApiMemberChange.get_member_change_data(self, MemberChange.project_id)
        print(get_member_result)

#
if __name__ == '__main__':
    unittest.main()

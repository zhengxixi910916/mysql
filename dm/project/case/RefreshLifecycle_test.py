# -*- coding: utf-8 -*-
# @Time    : 2022/02/16
# @Author  : Chen

import unittest
from project.api import ApiRefreshLifecycle
from project.case.file.runSql import db


class RefreshLifecycle(unittest.TestCase):
    """刷新生命周期"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass



    def test_0100_task(self):
        """
        接口名称：刷新生命周期
        接口地址：/proj/$VERSION$/refresh/lifecycle/{type}
        """
        list1 = [db.task_view_id, db.require_view_id, db.issue_view_id, db.risk_view_id]
        list2 = ["task", "require", "issue", "risk"]
        i = 0
        while i < 4:
            r = ApiRefreshLifecycle.refreshLifecycleUsingPUT(self,
                                                             list=[list1[i]],
                                                             type=list2[i]
                                                             )
            print("r:", r)
            print("list1:", list1[i])
            print("list2:", list2[i])
            i += 1

if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/11

import unittest
from workflow.api import ApiUserOrg


class WFProcinst(unittest.TestCase):
    """用户组织"""

    def test_0100_submit_issue_using(self):
        """
        接口名称：submitIssue;    接口地址：/workflow/$VERSION$/identity/changeloginuser；
        """
        r = ApiUserOrg.submit_issue_using(self,
                                          )
        print(r)

    def test_0200_check_user_in(self):
        """
        接口名称：判断用户是否存在流程中;    接口地址：/workflow/$VERSION$/identity/changeuser；
        """
        r = ApiUserOrg.check_user_in(self,
                                     )
        print(r)

    @unittest.skip("有问题，开发在帮忙定位。")
    def test_0300_query_all_user(self):
        """
        接口名称：queryAllUser;    接口地址：/workflow/$VERSION$/identity/users；
        """
        r = ApiUserOrg.query_all_user(self,
                                      )
        print(r)


if __name__ == "__main__":
    unittest.TestCase()

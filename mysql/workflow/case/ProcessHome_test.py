# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/10

import unittest
from workflow.api import ApiProcessHome


class ProcessHome(unittest.TestCase):
    """流程首页"""

    def test_0100_task_custom_condition(self):
        """
         接口名称：根据appId，role, userId, priority自定义查询条件代办任务;    接口地址：/workflow/$VERSION$/process/home/custom；
         """
        r = ApiProcessHome.task_custom_condition(self)
        print(r)

    def test_0200_task_processing_rate(self):
        """
         接口名称：统计一天内、一月以来、一年依赖的任务处理率;    接口地址：/workflow/$VERSION$/process/home/deal/rate；
         """
        r = ApiProcessHome.task_processing_rate(self)
        print(r)

    def test_0300_task_priority_using(self):
        """
        接口名称：根据优先级统计;    接口地址：/workflow/$VERSION$/process/home/priority；
        """
        r = ApiProcessHome.task_priority_using(self)
        print(r)

    def test_0300_query_todo_task(self):
        """
        接口名称：统计待我处理任务的数量;    接口地址：/workflow/$VERSION$/process/home/todo；
        """
        r = ApiProcessHome.query_todo_task(self)
        print(r)

    def test_0500_process_info2me_using(self):
        """
        接口名称：统计别人转给我的流程任务;    接口地址：/workflow/$VERSION$/process/home/transfer/me；
        """
        r = ApiProcessHome.process_info2me_using(self)
        print(r)


if __name__ == "__main__":
    unittest.TestCase()

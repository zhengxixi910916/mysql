# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/12

import unittest
from workflow.api import ApiThirdPartyTaskStorage


class ThirdPartyTaskStorage(unittest.TestCase):
    """第三方任务存储"""

    def test_0100_create_task_using(self):
        """
        接口名称：创建第三方任务;    接口地址：/workflow/thirdparty/createTask；
        """
        # 数据是通过第三方入口插入的，不用做参数化。一定要做到数据闭环，不然的话，待我处理页面就会报500。
        r = ApiThirdPartyTaskStorage.create_task_using(self,
                                                       task_json={"procDefId": "procDefId", "taskDefKey": "taskDefKey",
                                                                  "procInstId": "7bbf2bc4d1d811ec83700a580afd0399",
                                                                  "executionId": "7bbf2bc4d1d811ec83700a580afd0399",
                                                                  "name": "test_", "startUserId": "admin",
                                                                  "assignee": "admin", "priority": "50",
                                                                  "tenantId": "erdp", "category": "others",
                                                                  "businessName": "11111", "processName": "10000",
                                                                  "taskId": "7bbf2bc4d1d811ec83700a580afd0399",
                                                                  "businessState": "0", "source": "0", "url": "0"}
                                                       )
        print(r)

    def test_0200_create_history_task(self):
        """
        接口名称：创建第三方历史任务;    接口地址：/workflow/thirdparty/createHistoryTask；
        """
        r = ApiThirdPartyTaskStorage.create_history_task(self,
                                                         is_end=True,
                                                         proc_inst_id="7bbf2bc4d1d811ec83700a580afd0399",
                                                         source=0,
                                                         task_id="7bbf2bc4d1d811ec83700a580afd0399"
                                                         )
        print(r)

    def test_0300_delete_task_using(self):
        """
        接口名称：第三方任务删除根据任务IDs;    接口地址：/workflow/thirdparty/task/{taskIds}/{source}；
        """
        # 这个接口其实是删不掉数据的。taskid是自定义的；但数据生成后，后端会自动给一个主键ID，这个接口想删除数据，需要使用主键ID。
        r = ApiThirdPartyTaskStorage.delete_task_using(self,
                                                       task_id="7bbf2bc4d1d811ec83700a580afd0399"
                                                       )
        print(r)

    def test_0400_delete_process_using(self):
        """
        接口名称：第三方任务删除根据流程ids;    接口地址：/workflow/thirdparty/process/{processInstanceIds}/{source}；
        """
        # 这个接口是可以删掉数据的。测这些接口时，一定要做到数据闭环!!!
        r = ApiThirdPartyTaskStorage.delete_process_using(self,
                                                          proc_inst_id="7bbf2bc4d1d811ec83700a580afd0399"
                                                          )
        print(r)


if __name__ == '__main__':
    unittest.TestCase()

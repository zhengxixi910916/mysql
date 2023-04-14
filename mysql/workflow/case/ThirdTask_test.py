# -*- coding: utf-8 -*-#
# Author:       linxiaoyue
# Date:         2022/5/26

import unittest
from workflow.api import AipThirdPartTask


class ThirdPartyTaskStorage(unittest.TestCase):
    """第三方任务存储"""





    def test_001_create_task_using(self):
        """
        接口名称：创建第三方任务;    接口地址：/workflow/thirdparty/createTask；
        """
        r=AipThirdPartTask.create_task_using(self,
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

    def test_002_create_history_task(self):
        """
        接口名称：创建第三方历史任务;    接口地址：/workflow/thirdparty/createHistoryTask；
        """
        r=AipThirdPartTask.create_history_task(self,
                                               is_End=True,
                                               pro_InstId="7bbf2bc4d1d811ec83700a580afd0399",
                                               sourc_e=0,
                                               task_Id="7bbf2bc4d1d811ec83700a580afd0399"
                                               )
        print(r)




    def test_003_delete_process_using(self):
        """
        接口名称：第三方任务删除根据流程ids;    接口地址：/workflow/thirdparty/process/{processInstanceIds}/{source}；
        """
        r=AipThirdPartTask.delete_process_using(self,)
        print(r)
    def test_004_delete_task_using(self):
        """
        接口名称：第三方任务删除根据流程ids;    接口地址：/workflow/thirdparty/process/{processInstanceIds}/{source}；
        """
        r=AipThirdPartTask.delete_task_using(self,)
        print(r)
if __name__ == '__main__':
    unittest.TestCase()
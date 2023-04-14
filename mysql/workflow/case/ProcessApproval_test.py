# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/3/30

import unittest
import time
from workflow.api import ApiProcessApproval, ApiUserTaskProcessing, ApiPboManagement


class ProcessApproval(unittest.TestCase):
    """PBO-启动与审批/Pbo管理"""
    pbo_id0 = ""
    pbo_id1 = ""
    activity_id = ""

    # todo 具体的优化
    # def test_0100_start_process_by(self):
    #     """
    #     接口名称：基于PBO启动流程   ;  接口地址：/workflow/$VERSION$/start/processbypbo ;       调用位置：不知道
    #     """
    #     r = ApiProcessApproval.start_process_by(self,
    #                                             parameter_vo={
    #                                                 "baseForm": {
    #                                                     "processBasicInfo": {
    #                                                         "applicationKey": '',
    #                                                         "resourceKey": '',
    #                                                         "name": "111",
    #                                                         "description": "项目预算审批流程",
    #                                                         "procInstVariables": {}
    #                                                     },
    #                                                     "businessForm": {
    #                                                         "reviewItemList": []
    #                                                     },
    #                                                     "businessFormJsonStr": "{\"reviewItemList\":[]}"
    #                                                 },
    #                                                 "processDefKey": "BUDGET_APPROVE",
    #                                                 "isDraft": False,
    #                                                 "baseStartProcessDto": {
    #                                                     "title": "111",
    #                                                     "dueDate": "2023-03-06",
    #                                                     "description": "项目预算审批流程",
    #                                                     "priority": "50",
    #                                                     "uploadFileIds": [],
    #                                                     "deleteFileIds": [],
    #                                                     "userMap": {
    #                                                         "approve_candidateUsers": "SYS_E39B20EA11E7A81AC85B767C89C1",
    #                                                         "sid-E9E1828A-6C1D-403B-B875-0B2AF06D56B1_candidateUsers": "SYS_E39B20EA11E7A81AC85B767C89C1"
    #                                                     },
    #                                                     "roleMap": {
    #                                                         "approve_candidateRoles": "",
    #                                                         "sid-E9E1828A-6C1D-403B-B875-0B2AF06D56B1_candidateRoles": ""
    #                                                     },
    #                                                     "groupMap": {
    #                                                         "approve_candidateGroups": "",
    #                                                         "sid-E9E1828A-6C1D-403B-B875-0B2AF06D56B1_candidateGroups": ""
    #                                                     },
    #                                                     "category": "ppm_model",
    #                                                     "roleUserMap": {},
    #                                                     "groupUserMap": {},
    #                                                     "showUserJson": "[{\"memberType\":\"OPERATOR\",\"memberId\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"parentId\":\"-1\",\"actDefId\":\"approve\"},{\"memberType\":\"OPERATOR\",\"memberId\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"parentId\":\"-1\",\"actDefId\":\"sid-E9E1828A-6C1D-403B-B875-0B2AF06D56B1\"}]"
    #                                                 }
    #                                             }
    #                                             )
    #     print(r)
    #     ProcessApproval.pbo_id0 = r["data"]["erd.cloud.pbo.domain.vo.ParameterVO"]["pboId"]
    #     print("pbo_id0:", ProcessApproval.pbo_id0)
    #     pbo_id_ = ProcessApproval.pbo_id0.split(":")
    #     ProcessApproval.pbo_id1 = pbo_id_[1]
    #     print("pbo_id1:", ProcessApproval.pbo_id1)
    #     # ProcessApproval.activity_id = r["data"]["erd.cloud.dto.EtProcessInstance"]["activityId"]
    #     # print("activity_id:", ProcessApproval.activity_id)

    def test_0200_find_form_data(self):
        """
        接口名称：基于PBO和流程节点key查询FormData数据  ;   接口地址：/workflow/$VERSION$/findformdata/bypobandnodekey;      调用位置：不知道
        """
        r = ApiProcessApproval.find_form_data(self,
                                              pbo_id=ProcessApproval.pbo_id1,
                                              session_id="approve"
                                              )
        print(r)

    @unittest.skip('wait')
    def test_0300_submit_activity_task(self):
        """
        接口名称：审批流程任务  ;   接口地址：/workflow/$VERSION$/submit/process/submitActivityTask;        调用位置：不知道
        该接口已更换为: /workflow/v1/dynamic/api/submit/process/submitActivityTask； 在WF24NewApi_test.test_0005_WF24NewApiCase中实现
        """
        r0 = ApiUserTaskProcessing.query_todo_task1(self,
                                                    dto={
                                                        "category": "",
                                                        "pageSize": 20
                                                    }
                                                    )
        # print(r0)
        process_instance_id = r0["res"]["data"]["records"][0]["processInstanceId"]
        task_id = r0["res"]["data"]["records"][0]["id"]
        print("process_instance_id:", process_instance_id)
        print("task_id:", task_id)

        r = ApiProcessApproval.submit_activity_task(self,
                                                    parameter_vo={
                                                        "pboId": ProcessApproval.pbo_id0,
                                                        "baseForm": {
                                                            "businessForm": {
                                                                "reviewItemList": [
                                                                    {
                                                                        "oid": "OR:SYS_E39B20EA11E7A81AC85B767C89C1:erd.cloud.core.system.dto.EtUser"
                                                                    }
                                                                ]
                                                            },
                                                            "businessFormJsonStr": "{\"reviewItemList\":[{\"oid\":\"OR:SYS_E39B20EA11E7A81AC85B767C89C1:erd.cloud.core.system.dto.EtUser\"}]}"
                                                        },
                                                        "processInstanceId": process_instance_id,
                                                        "baseSubmitTaskDto": {
                                                            "routeFlag": "1",
                                                            "priority": 1,
                                                            "dueDate": "2022-03-30 11:13:26",
                                                            "sessionId": "keykqqa3i4f",
                                                            "taskId": task_id,
                                                            "comment": "commit"
                                                        }
                                                    }
                                                    )
        print(r)

    def test_0400_find_pbo_draft(self):
        """
        接口名称：查询PBO草稿详细数据;    接口地址：/workflow/$VERSION$/findPboDraftInfo/bypobandnodekey；
        """
        ApiProcessApproval.find_pbo_draft(self)

    def test_0500_get_pbo_list(self):
        """
        接口名称：查询Pbo列表;    接口地址：/workflow/pbo/list；
        """
        ApiPboManagement.get_pbo_list(self,
                                      )

    def test_0600_get_pbo_status(self):
        """
        接口名称：Pbo状态列表;    接口地址：/workflow/pbo/state/list；
        """
        ApiPboManagement.get_pbo_status(self,
                                        app_id="erdp"
                                        )


if __name__ == '__main__':
    unittest.TestCase()

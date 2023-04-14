# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/3/28

import unittest
import uuid
from workflow.api import ApiProcessInstance


class ProcessInstance(unittest.TestCase):
    """流程实例"""
    user_id = uuid.uuid1()  # 假设的用户id
    variable_name = "test"  # 假设的变量名称
    process_instance_id = ""
    process_definition_key = ""
    process_definition_id = ""
    business_state = ""

    def test_0101_query_submitted_process(self):
        """
        接口名称：查询当前用户启动的流程  ;   接口地址：/workflow/$VERSION$/procinst/submitted;      调用位置：工作台-办公-我发起的
        """
        r = ApiProcessInstance.query_submitted_process(self,
                                                       dto={
                                                           "category": "",
                                                           "pageSize": 20
                                                       }
                                                       )
        print(r)

    def test_0200_running_using_g(self):
        """
        接口名称：查询正在运行的流程   ;  接口地址：/workflow/$VERSION$/procinst/running;      调用位置：流程管理-实例维护
        """
        r = ApiProcessInstance.running_using_g(self,
                                               dto={
                                                   "category": "",
                                                   "pageSize": 20
                                               }
                                               )
        ProcessInstance.process_instance_id = r["res"]["data"]["records"][0]["processInstanceId"]
        print("ProcessInstance.process_instance_id:", ProcessInstance.process_instance_id)
        ProcessInstance.process_definition_key = r["res"]["data"]["records"][0]["processDefinitionKey"]
        print("ProcessInstance.process_definition_key:", ProcessInstance.process_definition_key)
        ProcessInstance.process_definition_id = r["res"]["data"]["records"][0]["processDefinitionId"]
        print("ProcessInstance.process_definition_id:", ProcessInstance.process_definition_id)
        ProcessInstance.business_state = r["res"]["data"]["records"][0]["activityId"]
        print("ProcessInstance.business_state:", ProcessInstance.business_state)

    def test_0210_running_by_user(self):
        """
        接口名称：查询正在运行的流程;    接口地址：/workflow/$VERSION$/procinst/running/{userId}；
        """
        r = ApiProcessInstance.running_by_user(self,
                                               user_id=ProcessInstance.user_id
                                               )
        print(r)

    def test_0300_check_user_in(self):
        """
        接口名称：判断人员是否在流程中;    接口地址：/workflow/$VERSION$/procinst/checkUserInProcess/{processInstanceId}；
        """
        r = ApiProcessInstance.check_user_in(self,
                                             process_instance_id=ProcessInstance.process_instance_id,
                                             user_id=ProcessInstance.user_id
                                             )
        print(r)

    def test_0400_query_process_instance3(self):
        """
        接口名称：判断人员是否在流程中;    接口地址：/workflow/$VERSION$/procinst/checkUserInProcess/{processInstanceId}；
        """
        r = ApiProcessInstance.query_process_instance3(self,
                                                       process_instance_id=ProcessInstance.process_instance_id,
                                                       variable_name=ProcessInstance.user_id
                                                       )
        print(r)

    def test_0500_update_process_name(self):
        """
        接口名称：修改流程实例的标题;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/updateProcessName；
        """
        r = ApiProcessInstance.update_process_name(self,
                                                   process_instance_id=ProcessInstance.process_instance_id,
                                                   title="test"
                                                   )
        print(r)

    def test_0600_suspend_process_instance(self):
        """
          接口名称：挂起流程实例;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/suspend；
          """
        r = ApiProcessInstance.suspend_process_instance(self,
                                                        process_instance_id=ProcessInstance.process_instance_id
                                                        )
        print(r)

    def test_0601_activate_process_instance(self):
        """
        接口名称：激活流程实例;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/activate；
        """
        r = ApiProcessInstance.activate_process_instance(self,
                                                         process_instance_id=ProcessInstance.process_instance_id
                                                         )
        print(r)

    def test_0602_get_assign_list(self):
        """
        接口名称：根据流程实例id查询处理人;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/assign；
        """
        r = ApiProcessInstance.get_assign_list(self,
                                               process_instance_id=ProcessInstance.process_instance_id
                                               )
        print(r)

    def test_0603_get_highlighted_using(self):
        """
        接口名称：当前活动节点;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/highlights；
        """
        r = ApiProcessInstance.get_highlighted_using(self,
                                                     process_instance_id=ProcessInstance.process_instance_id
                                                     )
        print(r)

    # def test_0700_set_process_users(self):
    #     """
    #     接口名称：设置节点处理人;    接口地址：/workflow/$VERSION$/procinst/{processInstanceId}/setProcessUsers；
    #     """
    #     r = ApiProcessInstance.set_process_users(self,
    #                                              process_instance_id=ProcessInstance.process_instance_id,
    #                                              list_=[{
    #                                                  "candidateUsers": ProcessInstance.business_state.lower() + "_candidateUsers",
    #                                                  "candidateGroups": ProcessInstance.business_state.lower() + "_candidateGroups",
    #                                                  "userIds": "", "roleCodes": "",
    #                                                  "taskId": ProcessInstance.business_state},
    #                                                  {
    #                                                      "candidateUsers": ProcessInstance.business_state.lower() + "_candidateUsers",
    #                                                      "candidateGroups": ProcessInstance.business_state.lower() + "_candidateGroups",
    #                                                      "userIds": "", "roleCodes": "", "taskId": ""}]
    #                                              )
    #     print(r)

    def test_0800_getlast_version_nodes1(self):
        """
        接口名称：根据业务类型定义及业务状态查询最新版本的流程定义的所有元素;    接口地址：/workflow/$VERSION$/procinst/{processDefinitionKey}/nodes/lastversion/{businessState}；
        """
        r = ApiProcessInstance.getlast_version_nodes(self,
                                                     process_definition_key=ProcessInstance.process_definition_key,
                                                     business_state=ProcessInstance.business_state,
                                                     process_instance_id=ProcessInstance.process_instance_id
                                                     )
        print(r)

    def test_0810_getlast_version_nodes1(self):
        """
        接口名称：查询最新版本的流程定义的所有元素;    接口地址：/workflow/$VERSION$/procinst/{processDefinitionKey}/nodes/lastversion；
        """
        r = ApiProcessInstance.getlast_version_nodes1(self,
                                                      process_definition_key=ProcessInstance.process_definition_key,
                                                      process_instance_id=ProcessInstance.process_instance_id
                                                      )
        print(r)

    def test_0820_get_diagram_by(self):
        """
        接口名称：查询当前流程实例所有元素;    接口地址：/workflow/$VERSION$/procinst/{processDefinitionId}/nodes；
        """
        r = ApiProcessInstance.get_diagram_by(self,
                                              process_definition_key=ProcessInstance.process_definition_key,
                                              process_instance_id=ProcessInstance.process_instance_id
                                              )
        print(r)

    def test_0830_business_key_start(self):
        """
        接口名称：根据业务对象ID查询是否有正在运行的流程;    接口地址：/workflow/$VERSION$/procinst/{businessKey}/businessKeyStartProcess；
        """
        r = ApiProcessInstance.business_key_start(self,
                                                  business_key=ProcessInstance.business_state
                                                  )
        print(r)

    def test_0900_query_process_instance(self):
        """
          接口名称：根据流程实例ID查询流程实例信息;    接口地址：/workflow/$VERSION$/procinst/query/{processInstanceId}；
          """
        r = ApiProcessInstance.query_process_instance(self,
                                                      process_instance_id=ProcessInstance.process_instance_id
                                                      )
        print(r)

    def test_1000_query_process_instance2(self):
        """
        接口名称：查询相同流程定义，且处于同一节点的流程实例;    接口地址：/workflow/$VERSION$/procinst/query/list/{processDefinitionId}/{activityId}；
        """
        r = ApiProcessInstance.query_process_instance2(self,
                                                       process_instance_id=ProcessInstance.process_instance_id,
                                                       activity_id=ProcessInstance.business_state
                                                       )
        print(r)

    def test_1100_query_process_instance1(self):
        """
        接口名称：查询流程实例所有节点的配置和接口调用日志;    接口地址：/workflow/$VERSION$/procinst/query/config/list/{processInstanceId}/{processDefinitionId}；
        """
        r = ApiProcessInstance.query_process_instance1(self,
                                                       process_instance_id=ProcessInstance.process_instance_id,
                                                       process_definition_id=ProcessInstance.process_definition_id
                                                       )
        print(r)


if __name__ == '__main__':
    unittest.TestCase()

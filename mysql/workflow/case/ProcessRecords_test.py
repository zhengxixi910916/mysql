# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/3/28

import unittest
import uuid

from workflow.api import ApiProcessRecords, ApiProcessHistoryInformation, ApiNodeActivityFlowchart, ApiUserTaskProcessing


class ProcessRecords(unittest.TestCase):
    """流程记录/流程历史记录信息/节点活动流程图"""
    records_id = ""
    records_id_1 = ""
    process_definition_id = ""
    task_id = ""

    def test_0101_query_inst_page_using_get(self):
        """
        接口名称：分页查询流程实例记录  ;   接口地址：/workflow/$VERSION$/process/record/queryInstPage;     调用位置：工作台-办公-流程记录
        """
        r = ApiProcessRecords.query_inst_page_using_get(self,
                                                        dto={
                                                            "category": "",
                                                            "pageSize": 20
                                                        }
                                                        )
        print(r)
        ProcessRecords.records_id = r["res"]["data"]["records"][0]["id"]
        print(ProcessRecords.records_id)
        ProcessRecords.process_definition_id = r["res"]["data"]["records"][0]["processDefinitionId"]
        print("ProcessRecords.process_definition_id:", ProcessRecords.process_definition_id)

    def test_0102_query_page_using_get_6(self):
        """
        接口名称：分页查询流程记录  ;   接口地址：/workflow/$VERSION$/process/record/page ;       调用位置：工作台-办公-流程记录-展开二级数据
        """
        r = ApiProcessRecords.query_page_using_get_6(self,
                                                     dto={
                                                         "category": "",
                                                         "pageSize": 20,
                                                         "processInstId": ProcessRecords.records_id
                                                     }
                                                     )
        print(r)
        ProcessRecords.records_id_1 = r["res"]["data"]["records"][-1]["id"]
        print("ProcessRecords.records_id_1:", ProcessRecords.records_id_1)

    def test_0103_query_informed_using_get(self):
        """
        接口名称：分页查询流程知会我的;        接口地址：/workflow/$VERSION$/process/record/informed/page
        """
        r = ApiProcessRecords.query_informed_using_get(self)
        print(r)

    def test_0104_mark_read_using_post(self):
        """
        接口名称：标记未读为已读;        接口地址：/workflow/$VERSION$/process/record/informed/mark/read
        """
        r = ApiProcessRecords.mark_read_using_post(self)
        print(r)

    def test_0105_informed_task_using_post(self):
        """
        接口名称：任务知会;        接口地址：/workflow/$VERSION$/process/record/informed
        """
        r = ApiUserTaskProcessing.query_todo_task1(self,
                                                                                          dto={
                                                                                              "category": "",
                                                                                              "pageSize": 20
                                                                                          }
                                                                                          )
        print(r)
        task_id = r["res"]["data"]["records"][0]["id"]
        ProcessRecords.task_id = task_id
        print("task_id:", task_id)
        r = ApiProcessRecords.informed_task_using_post(self,
                                                       comment="",
                                                       informed_user_id=uuid.uuid1(),
                                                       task_id=task_id
                                                       )
        print(r)

    def test_0106_del_read_informed_using_delete(self):
        """
        接口名称：删除已读的知会
        接口地址：/workflow/$VERSION$/process/record/del/read/{informedIds}
        """
        r = ApiProcessRecords.del_read_informed_using_delete(self,
                                                             informed_ids=ProcessRecords.task_id
                                                             )
        print(r)

    def test_0107_del_read_using_delete(self):
        """
        接口名称：删除流程记录 ;       接口地址：/workflow/$VERSION$/process/record/del/{ids};      调用位置：工作台-办公-流程记录-展开二级数据-勾选数据进行删除
        """
        r = ApiProcessRecords.del_read_using_delete(self,
                                                    records_id_1=ProcessRecords.records_id_1
                                                    )
        print(r)

    def test_0201_hist_comments_using(self):
        """
        接口名称：查询审批历史记录;    接口地址：/workflow/$VERSION$/hist/comments；
        """
        r = ApiProcessHistoryInformation.hist_comments_using(self,
                                                             records_id=ProcessRecords.records_id
                                                             )
        print(r)

    def test_0202_hist_comments_business(self):
        """
        接口名称：查询审批历史记录相关联的业务表单数据;    接口地址：/workflow/$VERSION$/hist/comments/businessdata；
        """
        r = ApiProcessHistoryInformation.hist_comments_business(self,
                                                                process_instance_id=ProcessRecords.process_definition_id
                                                                )
        print(r)

    def test_0203_claim_using_g(self):
        """
        接口名称：已经审批过的流程节点;    接口地址：/workflow/$VERSION$/hist/{processInstanceId}/completetask；
        """
        r = ApiProcessHistoryInformation.claim_using_g(self,
                                                       process_instance_id=ProcessRecords.process_definition_id
                                                       )
        print(r)

    def test_0301_get_diagram_by(self):
        """
        接口名称：根据流程定义ID查询流程定义所有元素;    接口地址：/flowchart/processdefinition/{processDefinitionId}/diagramlayout；
        """
        r = ApiNodeActivityFlowchart.get_diagram_by(self,
                                                    process_instance_id=ProcessRecords.records_id,
                                                    process_definition_id=ProcessRecords.process_definition_id
                                                    )
        print(r)

    def test_0302_get_diagram_by1(self):
        """
        接口名称：根据流程实例ID查询流程定义所有元素;    接口地址：/flowchart/processinstance/{processInstanceId}/diagramlayout；
        """
        r = ApiNodeActivityFlowchart.get_diagram_by1(self,
                                                     process_instance_id=ProcessRecords.records_id
                                                     )
        print(r)

    def test_0303_get_highlighted_using(self):
        """
        接口名称：高亮显示活动节点;    接口地址：/flowchart/processinstance/{processInstanceId}/highlights；
        """
        r = ApiNodeActivityFlowchart.get_highlighted_using(self,
                                                           process_instance_id=ProcessRecords.records_id
                                                           )
        print(r)

    def test_0304_get_highlighted_using1(self):
        """
        接口名称：高亮显示活动节点（流程图使用）;    接口地址：/flowchart/processinstance/{processInstanceId}/{processDefinitionId}/highlights；
        """
        r = ApiNodeActivityFlowchart.get_highlighted_using1(self,
                                                            process_instance_id=ProcessRecords.records_id,
                                                            process_definition_id=ProcessRecords.process_definition_id
                                                            )

        print(r)


if __name__ == '__main__':
    unittest.TestCase()

# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/10
import unittest
import time
import uuid
from workflow.api import ApiTaskinQuiry, ApiUserTaskProcessing, ApiProcessRecords


class TaskQuiry(unittest.TestCase):
    """任务询问"""
    user_id = str(uuid.uuid1())
    task_id = ""
    records_id = ""

    def test_0100_add_task_inquiry(self):
        """
        接口名称：任务询问;    接口地址：/workflow/$VERSION$/taskinquiry/add；
        """
        r = ApiUserTaskProcessing.query_todo_task1(self,
                                                                                          dto={
                                                                                              "category": "",
                                                                                              "pageSize": 20
                                                                                          }
                                                                                          )
        print(r)
        TaskQuiry.task_id = r["res"]["data"]["records"][0]["id"]
        print("TaskQuiry.task_id:", TaskQuiry.task_id)
        r = ApiTaskinQuiry.add_task_inquiry(self,
                                            task_inquiry={"taskId": TaskQuiry.task_id,
                                                          "inquiryUserId": TaskQuiry.user_id,
                                                          "inquiryRoleId": "", "content": "测试",
                                                          "dueDate": time.strftime("%Y-%m-%d"),
                                                          "priority": "50"}
                                            )
        print(r)

    def test_0200_detail_by_task(self):
        """
         接口名称：查询详情;    接口地址：/workflow/$VERSION$/taskinquiry/detail/{taskId}；
         """
        r = ApiTaskinQuiry.detail_by_task(self,
                                          task_id=TaskQuiry.task_id
                                          )
        print(r)

    def test_0300_query_page_using(self):
        """
        接口名称：查询当前用户的询问记录;    接口地址：/workflow/$VERSION$/taskinquiry/page；
        """
        r = ApiTaskinQuiry.query_page_using(self,
                                            user_id=TaskQuiry.user_id
                                            )
        print(r)

    def test_0400_reply_list_using(self):
        """
        接口名称：查询询问的回复记录;    接口地址：/workflow/$VERSION$/taskinquiry/reply/{inquiryId}；
        """
        r = ApiProcessRecords.query_inst_page_using_get(self,
                                                        dto={
                                                            "category": "",
                                                            "pageSize": 20
                                                        }
                                                        )
        print(r)
        records_id = r["res"]["data"]["records"][0]["id"]
        print(records_id)
        r = ApiProcessRecords.query_page_using_get_6(self,
                                                     dto={
                                                         "category": "",
                                                         "pageSize": 20,
                                                         "processInstId": records_id
                                                     }
                                                     )
        print(r)
        TaskQuiry.records_id = r["res"]["data"]["records"][0]["id"]
        print("records_id:", TaskQuiry.records_id)
        r = ApiTaskinQuiry.reply_list_using(self,
                                            inquiry_id=TaskQuiry.records_id
                                            )
        print(r)

    def test_0500_reply_task_inquiry(self):
        """
        接口名称：任务询问回复;    接口地址：/workflow/$VERSION$/taskinquiry/reply/{inquiryId}；
        """
        r = ApiTaskinQuiry.reply_task_inquiry(self,
                                              inquiry_id=TaskQuiry.records_id,
                                              task_inquiry={
                                                  "category": "",
                                                  "content": "",
                                                  "createBy": "",
                                                  "createTime": "",
                                                  "dueDate": "",
                                                  "ext": {},
                                                  "id": "",
                                                  "inquiryRoleId": "",
                                                  "inquiryUserId": "",
                                                  "orderBy": "",
                                                  "pageIndex": 0,
                                                  "pageSize": 0,
                                                  "parentId": "",
                                                  "priority": "",
                                                  "processDefinitionId": "",
                                                  "processInstanceId": "",
                                                  "remark": "",
                                                  "sortBy": "",
                                                  "status": 0,
                                                  "taskId": "",
                                                  "tenantId": "",
                                                  "title": "",
                                                  "typeOf": 0
                                              }
                                              )
        print(r)

    @unittest.skip("存在问题，开发在帮忙定位。")
    def test_0600_cancle_task_inquiry(self):
        """
        接口名称：任务询问取消;    接口地址：/workflow/$VERSION$/taskinquiry/cancle/{inquiryId}；
        """
        r = ApiTaskinQuiry.cancle_task_inquiry(self,
                                               inquiry_id=TaskQuiry.records_id
                                               )
        print(r)


if __name__ == "__main__":
    unittest.TestCase()

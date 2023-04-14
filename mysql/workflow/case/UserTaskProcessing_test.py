# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/3/28

import unittest
from workflow.api import ApiUserTaskProcessing


class UserTaskProcessing(unittest.TestCase):
    """用户任务处理"""
    records_id = ""
    process_definition_id = ""
    process_instance_id = ""
    task_id = ""
    task_def_key = ""

    def test_0101_query_todo_task1(self):
        """
        接口名称：queryTodoTaskListByUserIdAndSystemId     ;接口地址：/workflow/$VERSION$/task/todotask;      调用位置：工作台-办公-待我处理
        """
        r = ApiUserTaskProcessing.query_todo_task1(self,
                                                   dto={
                                                       "category": "",
                                                       "pageSize": 20
                                                   }
                                                   )
        UserTaskProcessing.process_definition_id = r["res"]["data"]["records"][0]["processDefinitionId"]
        print("UserTaskProcessing.process_definition_id:", UserTaskProcessing.process_definition_id)
        UserTaskProcessing.process_instance_id = r["res"]["data"]["records"][0]["processInstanceId"]
        print("UserTaskProcessing.process_instance_id:", UserTaskProcessing.process_instance_id)
        UserTaskProcessing.task_id = r["res"]["data"]["records"][0]["id"]
        print("UserTaskProcessing.task_id:", UserTaskProcessing.task_id)
        UserTaskProcessing.task_def_key = r["res"]["data"]["records"][0]["taskDefKey"]
        print("UserTaskProcessing.task_def_key:", UserTaskProcessing.task_def_key)

    def test_0102_get_activity_img(self):
        """
        接口名称：当前流程活动节点坐标信息 x,y,height,width;    接口地址：/workflow/$VERSION$/task/activitycoor/{processInstanceId}；
        """
        r = ApiUserTaskProcessing.get_activity_img(self,
                                                   process_instance_id=UserTaskProcessing.process_instance_id
                                                   )
        print(r)

    def test_0103_get_attachment_list(self):
        """
        接口名称：获取附件列表;    接口地址：/workflow/$VERSION$/task/attachments；
        """
        r = ApiUserTaskProcessing.get_attachment_list(self,
                                                      process_instance_id=UserTaskProcessing.process_instance_id
                                                      )
        print(r)

    def test_0104_query_done_page(self):
        """
        接口名称：一级实例列表   ;  接口地址：/workflow/$VERSION$/task/donepage;        调用位置；工作台-办公-我已处理
        """
        r = ApiUserTaskProcessing.query_done_page(self,
                                                  dto={
                                                      "category": "",
                                                      "pageSize": 20
                                                  }
                                                  )
        print(r)
        self.assertEqual("200", r["code"])
        # UserTaskProcessing.records_id = r["res"]["data"]["records"][0]["id"]
        # print(UserTaskProcessing.records_id)

    def test_0105_query_done_task(self):
        """
        接口名称：查询已处理任务列表  ;   接口地址：/workflow/$VERSION$/task/donetask;     调用位置：工作台-办公-我已处理-展开二级数据
        """
        r = ApiUserTaskProcessing.query_done_task(self,
                                                  dto={
                                                      "category": "",
                                                      "pageSize": 20,
                                                      "processInstanceId": UserTaskProcessing.records_id
                                                  }
                                                  )
        print(r)

    def test_0106_get_executor_change(self):
        """
        接口名称：流程转办/委派记录查询;    接口地址：/workflow/$VERSION$/task/executor；
        """
        r = ApiUserTaskProcessing.get_executor_change(self)
        print(r)

    def test_0107_get_next_process_gate(self):
        """
        接口名称：获取当前节点的路由网关;    接口地址：/workflow/$VERSION$/task/formproperties/{taskId}；
        """
        r = ApiUserTaskProcessing.next_process_gate(self,
                                                    task_id=UserTaskProcessing.task_id
                                                    )
        print(r)

    def test_0108_query_business_key(self):
        """
        接口名称：获取当前节点的路由网关;    接口地址：/workflow/$VERSION$/task/formproperties/{taskId}；
        """
        r = ApiUserTaskProcessing.query_business_key(self,
                                                     task_def_key=UserTaskProcessing.task_def_key
                                                     )
        print(r)

    def test_0109_next_process_task(self):
        """
        接口名称：获取下一个用户节点信息;    接口地址：/workflow/$VERSION$/task/nexttask/{processInstanceId}/{routeFlag}；
        """
        r = ApiUserTaskProcessing.next_process_task(self,
                                                    process_instance_id=UserTaskProcessing.process_instance_id,
                                                    route_flag=0
                                                    )
        print(r)

    def test_0110_query_task_by(self):
        """
        接口名称：查询任务信息;    接口地址：/workflow/$VERSION$/task/query/{taskId}；
        """
        r = ApiUserTaskProcessing.query_task_by(self,
                                                task_id=UserTaskProcessing.task_id
                                                )
        print(r)

    def test_0111_get_running_user(self):
        """
        接口名称：查询当前正在运行的用户节点;    接口地址：/workflow/$VERSION$/task/runningusertask/{processInstanceId}；
        """
        r = ApiUserTaskProcessing.get_running_user(self,
                                                   process_instance_id=UserTaskProcessing.process_instance_id
                                                   )
        print(r)

    def test_0112_query_todo_task2(self):
        """
        接口名称：按人员查询所有待办任务;    接口地址：/workflow/$VERSION$/task/todotask/dimissionid；
        """
        r = ApiUserTaskProcessing.query_todo_task2(self, )
        print(r)

    def test_0113_query_historic_detail(self):
        """
        接口名称：查询流程历史表单数据;    接口地址：/workflow/$VERSION$/task/{processInstanceId}/history/formdata；
        """
        r = ApiUserTaskProcessing.query_historic_detail(self,
                                                        process_instance_id=UserTaskProcessing.process_instance_id
                                                        )
        print(r)

    def test_0114_query_my_focus(self):
        """
        接口名称：我关注的   ;  接口地址：/workflow/$VERSION$/task/focus;     调用位置：工作台-办公-我订阅的
        """
        r = ApiUserTaskProcessing.query_my_focus(self,
                                                 dto={
                                                     "category": "",
                                                     "pageSize": 20
                                                 }
                                                 )
        print(r)

    def test_0115_task_view_using(self):
        """
        接口名称：查询审批详情页面;        接口地址：/workflow/$VERSION$/task/taskview;
        """
        r = ApiUserTaskProcessing.task_view_using(self,
                                                  process_definition_id=UserTaskProcessing.process_definition_id,
                                                  process_instance_id=UserTaskProcessing.process_instance_id,
                                                  task_def_key=UserTaskProcessing.task_def_key,
                                                  task_id=""
                                                  )
        print(r)

    def test_0116_read_task_using(self):
        """
        接口名称：设置已读;    接口地址：/workflow/$VERSION$/task/read；
        """
        r = ApiUserTaskProcessing.read_task_using(self,
                                                  task_id=UserTaskProcessing.task_id
                                                  )
        print(r)

    def test_0117_query_todo_task(self):
        """
        接口名称：queryTodoTaskList;    接口地址：/workflow/$VERSION$/task/todo/task；
        """
        ApiUserTaskProcessing.query_todo_task(self,
                                              dto={
                                                  "assignee": "",
                                                  "flag": "",
                                                  "processInstanceId": "",
                                                  "taskDefKey": ""
                                              }
                                              )

    def test_0118_unclaim_using_p(self):
        """
        接口名称：退回签收;    接口地址：/workflow/$VERSION$/task/unclaim;
        """
        r = ApiUserTaskProcessing.unclaim_using_p(self,
                                                  task_id=UserTaskProcessing.task_id
                                                  )
        print(r)

    def test_0119_transfer_assignee_cancel(self):
        """
        接口名称：任务转办取消;    接口地址：/workflow/$VERSION$/task/transfer/cancle；
        """
        r = ApiUserTaskProcessing.transfer_assignee_cancel(self,
                                                           task_id=UserTaskProcessing.task_id,
                                                           comment=""
                                                           )
        print(r)

    def test_0120_claim_using_p(self):
        """
        接口名称：任务签收;    接口地址：/workflow/$VERSION$/task/claim；
        """
        r = ApiUserTaskProcessing.claim_using_p(self,
                                                task_id=UserTaskProcessing.task_id,
                                                process_instance_id=UserTaskProcessing.process_instance_id
                                                )
        print(r)


if __name__ == '__main__':
    unittest.TestCase()

import unittest
import workflow.api.ApiWorkbenchPending as ApiWorkbenchPending
from workflow.api.ApiWorkbench import *
from workflow.api.WF24NewApi import *
import workflow.api.WF24NewApi as WF24NewApi


class Workbench_pending(unittest.TestCase):
    """工作台-待我处理"""
    # 接口地址已修改
    # def test_0001_workbench_pending(self):
    #     """
    #     接口:获取任务类型;地址:/workflow/v1/dynamic/api/status/enums/TaskTypeEnum;
    #     """
    #     r = enums_TaskTypeEnum()
    #     print(r)
    #     self.assertEqual('200', r['code'])
    #     print(r)
    #
    # def test_0002_workbench_pending(self):
    #     """
    #     接口名称：批量审批接口;接口地址：/workflow/v1/dynamic/api/task/completetasks；
    #     """
    #     # 创建流程分类
    #     add_category()
    #     # 创建流程模板
    #     saveOrUpdate_model()
    #     # 发起流程
    #     pboId, id, processInstanceId, number, processDefinitionId = start_processbypbo()
    #     # 查询流程任务id
    #     taskid, tmp = runningusertask(processInstanceId)
    #     # 批量审批流程
    #     r = task_completetasks(taskid)
    #     self.assertEqual('200', r['code'])
    #
    # def test_0003_workbench_pending(self):
    #     """
    #     接口名称：属性配置下拉框查询;接口地址：/workflow/v1/dynamic/api/columns/todoList;
    #     """
    #     r = columns_groupCode()
    #     print(r)
    #     self.assertEqual('200', r['code'])
    #
    # def test_0004_workbench_pending(self):
    #     """
    #     接口名称：查询待我处理列表;接口地址：/workflow/v1/dynamic/api/common/pageQuery/todoList/20/1;
    #     """
    #     r = ApiWorkbenchPending.todoList_pagesize_pageindex()
    #     print(r)
    #     self.assertEqual('200', r['code'])
    #
    # def test_0005_workbench_pending(self):
    #     """
    #     接口名称：批量审批任务查询接口;接口地址：/workflow/v1/dynamic/api/task/tasks/grouped；
    #     """
    #     # 查询taskid列表
    #     taskids = WF24NewApi.pageQuery_todoList()
    #     # 批量审批任务查询接口
    #     r = ApiWorkbenchPending.tasks_grouped(taskids=taskids)
    #
    #     self.assertEqual('200', r['code'])
    #
    # def test_0006_workbench_pending(self):
    #     """
    #     接口名称：pbo审批接口;接口地址：/workflow/v1/dynamic/api/submit/process/submitActivityTask;
    #     """
    #     # 创建流程分类
    #     add_category()
    #     # 创建流程模板
    #     saveOrUpdate_model()
    #     # 发起流程
    #     pboId, id, processInstanceId, number, processDefinitionId = start_processbypbo()
    #     print(pboId)
    #     # 查询流程任务id
    #     taskid, tmp = runningusertask(processInstanceId)
    #     print("taskid:", taskid)
    #     # pbo审批
    #     r = submitActivityTask(pboId, id, processInstanceId, number, taskid)
    #     self.assertEqual('200', r['code'])
    #
    # def test_0007_workbench_pending(self):
    #     """
    #     接口名称：获取任务状态类型;接口地址：/workflow/v1/dynamic/api/status/enums/EtActivityLifecycleEnum;
    #     """
    #     r = ApiWorkbenchPending.enums_EtActivityLifecycleEnum()
    #     print(r)
    #     self.assertEqual('200', r['code'])


if __name__ == '__main__':
    unittest.main()

import unittest
import workflow.api.ApiWorkbench as ApiWorkbench
import workflow.api.ApiWorkbenchIStart as ApiWorkbenchIStart


class Workbench_i_start(unittest.TestCase):
    """工作台-我发起的"""
    # 停止不用，改了接口地址
    # def test_0001_workbench_i_start(self):
    #     """
    #     接口:统计已完成任务数量;地址:/workflow/v1/procinst/submitted/status/count/completed;
    #     """
    #     r = ApiWorkbench.count_completed()
    #     print(r)
    #     self.assertEqual('200', r['code'])
    #     print(r)
    #
    # def test_0002_workbench_i_start(self):
    #     """
    #     接口:统计进行中任务数量;地址:/workflow/v1/procinst/submitted/status/count/running;
    #     """
    #     r = ApiWorkbench.count_running()
    #     self.assertEqual('200', r['code'])
    #     print(r)
    #
    # def test_0003_workbench_i_start(self):
    #     """
    #     接口:统计挂起任务数量;地址:/workflow/v1/procinst/submitted/status/count/suspended;
    #     """
    #     r = ApiWorkbench.count_suspended()
    #     self.assertEqual('200', r['code'])
    #     print(r)
    #
    # def test_0004_workbench_i_start(self):
    #     """
    #     接口:统计挂起任务数量;地址:/workflow/v1/dynamic/api/common/pageQuery/launchRecord/20/1;
    #     """
    #     r = ApiWorkbenchIStart.pageQuery_launchRecord()
    #     print(r)
    #     self.assertEqual('200', r['code'])

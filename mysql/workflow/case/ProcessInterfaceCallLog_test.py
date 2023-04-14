# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/3/28

import unittest
from workflow.api import ApiProcessInterfaceCallLog


class ProcessInterfaceCallLog(unittest.TestCase):
    """流程接口调用日志"""
    procInst_id = ""
    id_ = ""
    params_ = ""

    def test_0100_get_interface_invoke_inst_log_using_get(self):
        """
        接口名称：查询流程实例调用记录   ;  接口地址：/workflow/$VERSION$/interfaceinvoklog/query/inst/page;        调用位置：流程管理-调用日志
        """
        r = ApiProcessInterfaceCallLog.get_interface_invoke_inst_log_using_get(self,
                                                                               dto={
                                                                                   "category": "",
                                                                                   "pageSize": 20
                                                                               }
                                                                               )
        print(r)
        self.assertEqual("200",r["code"])
        # ProcessInterfaceCallLog.procInst_id = r["res"]["data"]["records"][0]["procInstId"]
        # print(ProcessInterfaceCallLog.procInst_id)

    def test_0200_get_interface_invoke_log_using_get(self):
        """
        接口名称：查询流程实例调用记录   ;  接口地址：/workflow/$VERSION$/interfaceinvoklog/query/log/list;     调用位置：流程管理-调用日志-展开二级数据
        """
        r = ApiProcessInterfaceCallLog.get_interface_invoke_log_using_get(self,
                                                                          dto={
                                                                              "category": "",
                                                                              "pageSize": 20,
                                                                              "procInstId": ProcessInterfaceCallLog.procInst_id
                                                                          }
                                                                          )
        print(r)
        self.assertEqual("200", r["code"])
        # ProcessInterfaceCallLog.id_ = r["res"]["data"][0]["id"]
        # print("ProcessInterfaceCallLog.id_:", ProcessInterfaceCallLog.id_)
        # ProcessInterfaceCallLog.params_ = r["res"]["data"][0]["params"]
        # print("ProcessInterfaceCallLog.params_:", ProcessInterfaceCallLog.params_)

    def test_0300_get_invoke_log_history_using_get(self):
        """
        接口名称：查看调用记录历史  ;   接口地址：/workflow/$VERSION$/interfaceinvoklog/getHistory/{invokeLogId};     调用位置：流程管理-调用日志-展开二级数据-点击流程实例ID-点击查看记录
        """
        r = ApiProcessInterfaceCallLog.get_invoke_log_history_using_get(self, )
        print(r)

    def test_0400_get_interface_record_using_get(self):
        """
        接口名称：查看调用记录   ;  接口地址：/workflow/$VERSION$/interfaceinvoklog/queryPage;      调用位置：不知道
        """
        ApiProcessInterfaceCallLog.get_interface_record_using_get(self,
                                                                  dto={
                                                                      "category": "",
                                                                      "pageSize": 20
                                                                  }
                                                                  )

    # def test_0500_retry_using_post(self):
    #     """
    #     接口名称：接口调用重试  ;   接口地址：/workflow/$VERSION$/interfaceinvoklog/retry;      调用位置：流程管理-调用日志-展开二级数据-点击流程实例ID-重试(调用失败的接口,页面才会显示重试)
    #     """
    #     r = ApiProcessInterfaceCallLog.retry_using_post(self, dto={})
    #     print(r)


if __name__ == '__main__':
    unittest.TestCase()

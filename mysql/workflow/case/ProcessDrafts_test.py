# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/4/14

import unittest
import time
from workflow.api import ApiProcessDrafts


class ProcessDrafts(unittest.TestCase):
    """流程草稿"""
    ids = ""
    category = ""
    process_definition_key = ""

    def test_0100_save_using_p(self):
        """
        接口名称：保存流程草稿;        接口地址：/workflow/$VERSION$/proccessDraft/{processDefinitionKey}/{category}
        """
        time_ = time.strftime("%Y-%m-%d")
        r = ApiProcessDrafts.save_using_p(self,
                                          dto={
                                              "title_process_submit": "test_" + time_,
                                              "description": "计划发布流程_" + time_,
                                              "title": "计划发布流程_" + time_,
                                              "dueDate": time_,
                                          }
                                          )
        print(r)

    def test_0200_list_using_g(self):
        """
        接口名称：查询流程草稿;        接口地址：/workflow/$VERSION$/proccessDraft/;        调用位置：工作台-办公-我的草稿
        """
        r = ApiProcessDrafts.list_using_g(self,
                                          create_time="",
                                          title_process_submit="",
                                          tenant_id="type1",
                                          page_index=1,
                                          page_size=10
                                          )
        # print(r)
        ProcessDrafts.ids = r["res"]["data"]["records"][0]["id"]
        print("ProcessDrafts.ids:", ProcessDrafts.ids)
        ProcessDrafts.category = r["res"]["data"]["records"][0]["category"]
        print("ProcessDrafts.category:", ProcessDrafts.category)
        ProcessDrafts.process_definition_key = r["res"]["data"]["records"][0]["processDefinitionKey"]
        print("ProcessDrafts.process_definition_key:", ProcessDrafts.process_definition_key)

    @unittest.skip("这个接口不支持pbo的流程数据，但现在新启的流程都是pbo流程。")
    def test_0300_get_using_g(self):
        """
        接口名称：通过ID查询草稿;        接口地址：/workflow/$VERSION$/proccessDraft/{id};      调用位置：不知道
        """
        ApiProcessDrafts.get_using_g(self,
                                     ids=ProcessDrafts.ids
                                     )

    def test_0400_get_by_business(self):
        """
        接口名称：通过业务businessKey来查询对于的草稿;        接口地址：/workflow/$VERSION$/proccessDraft/businessKey/{businessKey}
        """
        r = ApiProcessDrafts.get_by_business(self,
                                             business_key=ProcessDrafts.ids,
                                             def_key=ProcessDrafts.process_definition_key
                                             )
        print(r)

    def test_0500_start_using_p(self):
        """
        接口名称：通过草稿启动流程;        接口地址：/workflow/$VERSION$/proccessDraft/{id}
        """
        r = ApiProcessDrafts.start_using_p(self,
                                           ids=ProcessDrafts.ids
                                           )
        print(r)

    def test_0600_delete_using_d(self):
        """
        接口名称：删除流程草稿;        接口地址：/workflow/$VERSION$/proccessDraft/;        调用位置：工作台-办公-我的草稿-勾选数据进行删除
        """
        r = ApiProcessDrafts.delete_using_d(self,
                                            ids=ProcessDrafts.ids
                                            )
        print(r)


if __name__ == '__main__':
    unittest.TestCase()

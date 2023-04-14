# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/11
import unittest
import time
from workflow.api import ApiMessageModle


class MessageModle(unittest.TestCase):
    """消息模板管理"""
    mode_ids = ""

    def test_0100_add_using_p(self):
        """
        接口名称：创建消息模板;    接口地址：/workflow/$VERSION$/msgmode；
        """

        r = ApiMessageModle.add_using_p(self,
                                        dto={
                                            "modeName": "转办通知_" + time.strftime("%H%M%S"),
                                            "templateCode": "code_" + time.strftime("%H%M%S"),
                                        }
                                        )
        print(r)

    def test_0200_query_page_using(self):
        """
        接口名称：分页查询消息模板;    接口地址：/workflow/$VERSION$/msgmode/page；
        """
        r = ApiMessageModle.query_page_using(self,
                                             dto={}
                                             )
        print(r)
        MessageModle.mode_ids = r["res"]["data"]["records"][0]["id"]
        print("MessageModle.mode_ids:", MessageModle.mode_ids)

    def test_0300_modify_using_p(self):
        """
         接口名称：修改消息模板;    接口地址：/workflow/$VERSION$/msgmode；
         """
        r = ApiMessageModle.modify_using_p(self,
                                           message_mode={"modeName": "转办通知_095348", "notifyType": "transfer",
                                                         "templateCode": "test001", "dateNode": 0, "sendTime": "00:00",
                                                         "available": "N", "flexAttrs": {},
                                                         "id": MessageModle.mode_ids}
                                           )
        print(r)

    def test_0400_query_by_variables(self):
        """
        接口名称：获取模板变量列表;    接口地址：/workflow/$VERSION$/msgmode/variables；
        """
        r = ApiMessageModle.query_by_variables(self)
        print(r)

    def test_0500_query_by_id(self):
        """
        接口名称：根据ID查询消息模板;    接口地址：/workflow/$VERSION$/msgmode/{modeId}；
        """
        r = ApiMessageModle.query_by_id(self,
                                        mode_ids=MessageModle.mode_ids
                                        )
        print(r)

    def test_0600_del_using_dd(self):
        """
        接口名称：删除消息模板;    接口地址：/workflow/$VERSION$/msgmode/{modeIds}；
        """
        r = ApiMessageModle.del_using_d(self,
                                        mode_ids=MessageModle.mode_ids
                                        )
        print(r)


if __name__ == "__main__":
    unittest.TestCase()

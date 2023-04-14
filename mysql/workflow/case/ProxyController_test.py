# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/10

import unittest
import time
from workflow.api import ApiProxyController
from workflow.api.ApiTools import createUser


class ProxyController(unittest.TestCase):
    """流程代理配置"""
    proxy_id = ""
    proxy_id2 = ""
    user_id = ""

    def test_0100_add_act_proxy(self):
        """
        接口名称：创建流程代理配置-过期;    接口地址：/workflow/$VERSION$/proxy；
        """
        userid = createUser()
        print(userid)
        r = ApiProxyController.add_act_proxy(userid)

        self.assertEqual('200', r['code'])

    def test_0200_query_page_using(self):
        """
        接口名称：流程代理配置列表;    接口地址：/workflow/$VERSION$/proxy/page；
        """
        r = ApiProxyController.query_page_using(self,
                                                dto={}
                                                )
        print(r)
        ProxyController.proxy_id = r["res"]["data"]["records"][0]["id"]
        print("ProxyController.proxy_id:", ProxyController.proxy_id)
        ProxyController.user_id = r["res"]["users"][0]["id"]
        print("ProxyController.user_id:", ProxyController.user_id)

    def test_0300_query_act_proxy(self):
        """
        接口名称：获取流程代理配置根据id;    接口地址：/workflow/$VERSION$/proxy/{id}；
        """
        r = ApiProxyController.query_act_proxy(self,
                                               ids=ProxyController.proxy_id
                                               )
        print(r)

    def test_0400_update_act_proxy(self):
        """
         接口名称：更新流程代理配置;    接口地址：/workflow/$VERSION$/proxy/{id}；
         """
        r = ApiProxyController.update_act_proxy(self,
                                                ids=ProxyController.proxy_id,
                                                proxy_v2={"proxyName": "修改代理", "proxyType": "all-agent",
                                                          "startDate": "2029-12-01", "endDate": "2029-12-31",
                                                          "proxyUserids": ProxyController.user_id,
                                                          "createBy": "SYS_E39B20EA11E7A81AC85B767C89C1",
                                                          "flexAttrs": {}, "processDefinitionKeys": "",
                                                          "processNames": ""}
                                                )
        print(r)

    def test_0500_cancle_using_g(self):
        """
        接口名称：取消流程代理配置;    接口地址：/workflow/$VERSION$/proxy/cancle/{ids}；
        """
        r = ApiProxyController.cancle_using_g(self,
                                              ids=ProxyController.proxy_id
                                              )
        print(r)

    def test_0600_replace_proxy_page(self):
        """
        接口名称：遗留事项查询daili;    接口地址：/workflow/$VERSION$/proxy/replace/{userId}；
        """
        r = ApiProxyController.replace_proxy_page(self,
                                                  user_id="45c194615170f2f770a301f46b00e167"
                                                  )
        print(r)

    # def test_0700_add_act_proxy1(self):
    #     """
    #     接口名称：创建流程代理配置;    接口地址：/workflow/v2/proxy；
    #     """
    #     r = ApiProxyController.add_act_proxy1(self,
    #                                           proxy_v2={"proxyName": "代理2", "proxyType": "all-agent",
    #                                                     "startDate": time.strftime("%Y-%m-%d",
    #                                                                                time.localtime(
    #                                                                                    time.time() + 3600 * 2400)),
    #                                                     "endDate": time.strftime("%Y-%m-%d",
    #                                                                              time.localtime(
    #                                                                                  time.time() + 3600 * 2424)),
    #                                                     "proxyUserids": "SYS_E39B20EA11E7A81AC85B767C89C1",
    #                                                     "createBy": ProxyController.user_id, "flexAttrs": {},
    #                                                     "processDefinitionKeys": "", "processNames": ""}
    #                                           )
    #     print(r)

    def test_0800_delete_using_d(self):
        """
        接口名称：删除流程代理配置;    接口地址：/workflow/$VERSION$/proxy/{ids}；
        """
        r = ApiProxyController.query_page_using(self,
                                                dto={}
                                                )
        print(r)
        ProxyController.proxy_id2 = r["res"]["data"]["records"][0]["id"]
        print("ProxyController.proxy_id2:", ProxyController.proxy_id2)
        r = ApiProxyController.delete_using_d(self,
                                              ids=ProxyController.proxy_id
                                              )
        print(r)
        r = ApiProxyController.delete_using_d(self,
                                              ids=ProxyController.proxy_id2
                                              )
        print(r)


if __name__ == "__main__":
    unittest.TestCase()

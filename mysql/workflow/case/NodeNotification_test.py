# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/11

import unittest
from workflow.api import ApiNodeNotification, ApiTools

class NodeNotification(unittest.TestCase):
    """节点通知配置"""
    act_id = ""
    def_id = ""
    mode_ids = ""

    def setUp(self) -> None:
        NodeNotification.mode_ids = ApiTools.saveOrUpdate_model()
        # 模板维护
        # r = ApiProcessTemplateManagement.query_page_using_get_5(self,
        #                                                         dto={
        #                                                             "category": "others",
        #                                                             "pageSize": 20
        #                                                         }
        #                                                         )
        #
        # def_id = r["res"]["data"]["records"][0]["processDefinitionId"]
        # print("def_id:", def_id)
        # NodeNotification.def_id = def_id
        # # 节点配置
        # r = ApiProcactdefconfig.query_acts_using(self,
        #                                          proc_def_id=def_id,
        #                                          proc_inst_id=""
        #                                          )
        #
        # act_id = r["res"]["data"][-2]["id"]
        # print("act_id:", act_id)
        # NodeNotification.act_id = act_id
        # # 消息模板
        # r = ApiMessageModle.query_page_using(self,
        #                                      dto={}
        #                                      )
        #
        # NodeNotification.mode_ids = r["res"]["data"]["records"][0]["id"]
        # print("mode_ids:", NodeNotification.mode_ids)

    #
    # def test_0100_modify_notify_using(self):
    #     """
    #     接口名称：修改节点通知;    接口地址：/workflow/$VERSION$/ntfcfg；
    #     """
    #
    #     r = ApiNodeNotification.modify_notify_using(self,
    #                                                 act_id=NodeNotification.act_id,
    #                                                 def_id=NodeNotification.def_id,
    #                                                 list_=[
    #                                                     {
    #                                                         "actDefId": "",
    #                                                         "createBy": "",
    #                                                         "createTime": "",
    #                                                         "dateNode": 0,
    #                                                         "id": "",
    #                                                         "messageModel": {
    #                                                             "available": "",
    #                                                             "createBy": "",
    #                                                             "createTime": "",
    #                                                             "dateNode": 0,
    #                                                             "ext": {},
    #                                                             "id": "",
    #                                                             "modeName": "",
    #                                                             "notifyId": "",
    #                                                             "notifyType": "",
    #                                                             "orderBy": "",
    #                                                             "pageIndex": 0,
    #                                                             "pageSize": 0,
    #                                                             "sendTime": "",
    #                                                             "sortBy": "",
    #                                                             "templateCode": "",
    #                                                             "tenantId": "",
    #                                                             "updateBy": "",
    #                                                             "updateTime": ""
    #                                                         },
    #                                                         "modeId": "",
    #                                                         "notifyInterfaceRelList": [
    #                                                             {
    #                                                                 "id": "",
    #                                                                 "interfaceName": "",
    #                                                                 "notifyId": ""
    #                                                             }
    #                                                         ],
    #                                                         "procDefId": "",
    #                                                         "sendTime": "",
    #                                                         "updateBy": "",
    #                                                         "updateTime": "",
    #                                                         "userNotifyRelList": [
    #                                                             {
    #                                                                 "id": "",
    #                                                                 "notifyId": "",
    #                                                                 "userId": ""
    #                                                             }
    #                                                         ]
    #                                                     }
    #                                                 ]
    #                                                 )
    #     print(r)

    # def test_0200_add_notify_user(self):
    #     """
    #      接口名称：添加通知用户;    接口地址：/workflow/$VERSION$/ntfcfg/notify/user；
    #      """
    #     r = ApiNodeNotification.add_notify_user(self,
    #                                             list_=[
    #                                                 {
    #                                                     "id": "",
    #                                                     "notifyId": "",
    #                                                     "userId": ""
    #                                                 }
    #                                             ]
    #                                             )
    #     print(r)

    # def test_0300_add_notify_using(self):
    #     """
    #     接口名称：添加节点通知;    接口地址：/workflow/$VERSION$/ntfcfg/{procDefId}/{actDefId}；
    #     """
    #     r = ApiNodeNotification.add_notify_using(self,
    #                                              act_id=NodeNotification.act_id,
    #                                              def_id=NodeNotification.def_id,
    #                                              list_=[{
    #                                                  "procDefId": NodeNotification.def_id,
    #                                                  "actDefId": NodeNotification.act_id,
    #                                                  "modeId": NodeNotification.mode_ids,
    #                                                  "userNotifyRelList": [], "notifyInterfaceRelList": []}]
    #                                              )
    #     print(r)

    # def test_0400_update_notify_using(self):
    #     """
    #     接口名称：修改节点通知;    接口地址：/workflow/$VERSION$/ntfcfg/{procDefId}/{actDefId}/{notifyId}；
    #     """
    #     r = ApiNodeNotification.update_notify_using(self,
    #                                                 act_id=NodeNotification.act_id,
    #                                                 def_id=NodeNotification.def_id,
    #                                                 mode_ids=NodeNotification.mode_ids,
    #                                                 dto={}
    #                                                 )
    #     print(r)

    # def test_0500_del_notify_using(self):
    #     """
    #      接口名称：节点删除通知;    接口地址：/workflow/$VERSION$/ntfcfg/{ids}；
    #      """
    #     r = ApiNodeNotification.del_notify_using(self,
    #                                              ids=NodeNotification.mode_ids
    #                                              )
    #     print(r)
    #

if __name__ == '__main__':
    unittest.TestCase()

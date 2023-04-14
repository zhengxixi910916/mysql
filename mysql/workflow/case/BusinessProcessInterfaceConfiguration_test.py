# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/3/28

import unittest
from workflow.api import ApiBusinessProcessInterfaceConfiguration


class BusinessProcessInterfaceConfiguration(unittest.TestCase):
    """业务流程接口配置"""
    records_id = ""
    category = ""

    def test_0100_query_interface_type_list_using_get(self):
        """
        接口名称：查询接口类型   ;  接口地址：/workflow/$VERSION$/interface/type   ;  调用位置：流程管理-接口配置
        """
        r = ApiBusinessProcessInterfaceConfiguration.query_interface_type_list_using_get(self,
                                                                                         )
        print(r)
        BusinessProcessInterfaceConfiguration.category = r["res"]["data"]["数据接口"]
        print(BusinessProcessInterfaceConfiguration.category)

    def test_0101_add_interface_using_post(self):
        """
        接口名称：新增业务接口;     接口地址：/workflow/$VERSION$/interface/add;        调用位置：流程管理-接口配置-新增（业务/审批）接口配置
        """
        # 新增业务接口
        r = ApiBusinessProcessInterfaceConfiguration.add_interface_using_post(self,
                                                                              dto={"category": "business",
                                                                                   "name": "测试新增业务接口",
                                                                                   "type": "dubbo",
                                                                                   "rpcInterface": "www.ddpami.com",
                                                                                   "group": "1", "method": "1",
                                                                                   "version": 1, "syncFlag": "2",
                                                                                   "failureNumber": "5",
                                                                                   "intervalTime": "10", "params": "{}",
                                                                                   "description": "", "appId": "type1"}
                                                                              )
        print(r)

    def test_0102_business_interface_using_get(self):
        """
        接口名称：查询流程配置   ;  接口地址：/workflow/$VERSION$/interface/config  ;   调用位置：流程管理-接口配置
        """
        r = ApiBusinessProcessInterfaceConfiguration.business_interface_using_get(self,
                                                                                  dto={
                                                                                      "pageIndex": 1,
                                                                                      "pageSize": 20
                                                                                  }
                                                                                  )
        print(r)
        BusinessProcessInterfaceConfiguration.records_id = r["res"]["data"]["records"][0]["id"]
        print(BusinessProcessInterfaceConfiguration.records_id)

    def test_0103_get_et_business_by_id_using_get(self):
        """
        接口名称：查询流程配置;        接口地址：/workflow/$VERSION$/interface/config/{id};     调用位置：流程管理-接口配置-点击接口名称
        """
        r = ApiBusinessProcessInterfaceConfiguration.get_et_business_by_id_using_get(self,
                                                                                     records_id=BusinessProcessInterfaceConfiguration.records_id
                                                                                     )
        print(r)

    def test_0104_invoke_pth_by_id_using_get(self):
        """
        接口名称：根据接口ID获取对应接口数据;        接口地址：/workflow/$VERSION$/interface/rest/id/{id}
        """
        # r = ApiBusinessProcessInterfaceConfiguration.invoke_pth_by_id_using_get(ids=BusinessProcessInterfaceConfiguration.records_id)
        r = ApiBusinessProcessInterfaceConfiguration.invoke_pth_by_id_using_get(ids='de8b9044132fedb51042acc85f381995')
        self.assertEqual('10002',r["code"])
        print(r)

    def test_0105_query_interface_and_model_link_using_get(self):
        """
        接口名称：查询接口和模板的关联关系 ;    接口地址：/workflow/$VERSION$/interface/model/link/page;      调用位置：流程管理-接口配置-关联的流程定义
        """
        r = ApiBusinessProcessInterfaceConfiguration.query_interface_and_model_link_using_get(self,
                                                                                              records_id=BusinessProcessInterfaceConfiguration.records_id,
                                                                                              pager_name=10
                                                                                              )
        print(r)

    def test_0106_query_history_page_using_get(self):
        """
        接口名称：分页查询历史版本业务接口;        接口地址：/workflow/$VERSION$/interface/history/{id};      调用位置：流程管理-接口配置-业务接口的历史版本
        """
        ApiBusinessProcessInterfaceConfiguration.query_history_page_using_get(self,
                                                                              records_id=BusinessProcessInterfaceConfiguration.records_id,
                                                                              page_index=1,
                                                                              page_size=20
                                                                              )

    def test_0107_enabled_using_put(self):
        """
        接口名称：设置启用或禁用;        接口地址：/workflow/$VERSION$/interface/enable/{enable}
        """
        r = ApiBusinessProcessInterfaceConfiguration.enabled_using_put(self,
                                                                       enable=0,
                                                                       ids=BusinessProcessInterfaceConfiguration.records_id
                                                                       )
        print(r)

        r = ApiBusinessProcessInterfaceConfiguration.business_interface_using_get(self,
                                                                                  dto={
                                                                                      "category": "business",
                                                                                      "pageIndex": 1,
                                                                                      "pageSize": 20
                                                                                  }
                                                                                  )
        print(r)
        BusinessProcessInterfaceConfiguration.records_id = r["res"]["data"]["records"][0]["id"]
        print(BusinessProcessInterfaceConfiguration.records_id)

    def test_0108_update_interface_using_put(self):
        """
        接口名称：修改业务接口;        接口地址：/workflow/$VERSION$/interface/update/{id};       调用位置：流程管理-接口配置-编辑接口配置
        """
        r = ApiBusinessProcessInterfaceConfiguration.update_interface_using_put(self,
                                                                                records_id=BusinessProcessInterfaceConfiguration.records_id,
                                                                                business_interface={
                                                                                    "category": "business",
                                                                                    "name": "测试新增业务接口", "type": "dubbo",
                                                                                    "rpcInterface": "www.ddpami.com",
                                                                                    "group": "1", "method": "1",
                                                                                    "version": "1", "syncFlag": "2",
                                                                                    "failureNumber": "5",
                                                                                    "intervalTime": "10",
                                                                                    "params": "{}",
                                                                                    "description": "测试编辑",
                                                                                    "id": BusinessProcessInterfaceConfiguration.records_id,
                                                                                    "appId": "erdp"}
                                                                                )
        print(r)

    def test_0109_invoke_pth_by_type_using_get(self):
        """
        接口名称：根据接口类型获取对应接口数据;        接口地址：/workflow/$VERSION$/interface/rest/{category}
        """
        r=ApiBusinessProcessInterfaceConfiguration.invoke_pth_by_type_using_get(self,'rest')
        print(r)
        self.assertEqual(False,r['success'])

    def test_0199_business_interface_using_delete(self):
        """
        接口名称：删除流程配置;        接口地址：/workflow/$VERSION$/interface/config;      调用位置：流程管理-接口配置-删除接口配置
        """
        r = ApiBusinessProcessInterfaceConfiguration.business_interface_using_delete(self,
                                                                                     records_id=BusinessProcessInterfaceConfiguration.records_id
                                                                                     )
        print(r)


if __name__ == '__main__':
    unittest.TestCase()

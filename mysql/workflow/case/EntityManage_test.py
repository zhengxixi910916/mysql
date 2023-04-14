# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/9

import unittest
import time
from workflow.api import ApiEntityManage


class EntityManage(unittest.TestCase):
    """实体管理"""
    time_str = time.strftime("%H%M%S")
    ids_ = ""
    attr_ids = ""

    def test_0100_create_entity_using(self):
        """
        接口名称：创建实体;    接口地址：/workflow/$VERSION$/entity；
        """
        r = ApiEntityManage.create_entity_using(self,
                                                dto={
                                                    "entityTitle": "实体_" + EntityManage.time_str,
                                                    "entityAlias": "实体_" + EntityManage.time_str,
                                                    "entityTable": "ENTITY_" + EntityManage.time_str,
                                                    "description": "测试_" + EntityManage.time_str,
                                                    "entityAttrs[0].name": "ext_" + EntityManage.time_str,
                                                    "entityAttrs[0].attrKey": "ext_" + EntityManage.time_str,
                                                    "entityAttrs[0].attrType": "varchar",
                                                    "entityAttrs[0].typeLength": 255,
                                                    "entityAttrs[0].defaultValue": "",
                                                    "entityAttrs[0].attrName": "ext_" + EntityManage.time_str,
                                                }
                                                )
        print(r)

    def test_0200_query_page_using(self):
        """
        接口名称：查询实体列表;    接口地址：/workflow/$VERSION$/entity/page；
        """
        r = ApiEntityManage.query_page_using(self,
                                             dto={}
                                             )
        print(r)
        EntityManage.ids_ = r["res"]["data"]["records"][-1]["id"]
        print("EntityManage.ids_:", EntityManage.ids_)

    def test_0300_query_attr_by(self):
        """
        接口名称：根据属性id查询属性对象;    接口地址：/workflow/$VERSION$/entity/attr/{attrId}；
        """
        r = ApiEntityManage.query_attr_by(self,
                                          ids_=EntityManage.ids_
                                          )
        print(r)

    def test_0400_query_attr_list(self):
        """
        接口名称：查询实体属性列表;    接口地址：/workflow/$VERSION$/entity/{entityId}/attrs；
        """
        r = ApiEntityManage.query_attr_list(self,
                                            ids_=EntityManage.ids_
                                            )
        print(r)
        EntityManage.attr_ids = r["res"]["data"][0]["id"]
        print("EntityManage.attr_ids:", EntityManage.attr_ids)

    def test_0500_query_by_id(self):
        """
        接口名称：根据id查询实体;    接口地址：/workflow/$VERSION$/entity/{entityId}；
        """
        r = ApiEntityManage.query_by_id(self,
                                        ids_=EntityManage.ids_
                                        )
        print(r)

    def test_0600_create_entity_attr(self):
        """
        接口名称：新增实体属性;    接口地址：/workflow/$VERSION$/entity/attrs；
        """
        r = ApiEntityManage.create_entity_attr(self,
                                               ids_=EntityManage.ids_,
                                               dto={
                                                   "entityAttrs[0].name": "ext_0" + EntityManage.time_str,
                                                   "entityAttrs[0].attrKey": "ext_0" + EntityManage.time_str,
                                                   "entityAttrs[0].attrType": "varchar",
                                                   "entityAttrs[0].typeLength": 255,
                                                   "entityAttrs[0].defaultValue": "",
                                                   "entityAttrs[0].attrName": "ext_0" + EntityManage.time_str,
                                               }
                                               )
        print(r)

    def test_0700_query_list_using(self):
        """
        接口名称：查询已经发布实体;    接口地址：/workflow/$VERSION$/entity/list；
        """
        r = ApiEntityManage.query_list_using(self)
        print(r)

    def test_0800_modify_attr_using(self):
        """
        接口名称：修改未发布的实体属性列表;    接口地址：/workflow/$VERSION$/entity/attrs/{entityId}；
        """
        r = ApiEntityManage.modify_attr_using(self,
                                              ids_=EntityManage.ids_,
                                              dto=[
                                                  {
                                                      "attrKey": "ext_0" + EntityManage.time_str,
                                                      "attrName": "",
                                                      "attrType": "",
                                                      "available": "",
                                                      "createBy": "",
                                                      "createTime": "",
                                                      "dataFormat": "",
                                                      "defaultValue": "",
                                                      "entityId": "",
                                                      "id": "",
                                                      "required": "",
                                                      "typeLength": "",
                                                      "updateBy": "",
                                                      "updateTime": ""
                                                  }
                                              ]
                                              )
        print(r)

    def test_0900_update_entity_using(self):
        """
        接口名称：修改实体;    接口地址：/workflow/$VERSION$/entity/{entityId}；
        """
        r = ApiEntityManage.update_entity_using(self,
                                                ids_=EntityManage.ids_,
                                                dto={}
                                                )
        print(r)

    def test_1000_deploy_using_p(self):
        """
        接口名称：发布实体;    接口地址：/workflow/$VERSION$/entity/deploy/{entityId}；
        """
        r = ApiEntityManage.deploy_using_p(self,
                                           ids_=EntityManage.ids_,
                                           )
        print(r)

    def test_1100_delete_attr_using(self):
        """
        接口名称：删除未发布的实体属性列表;    接口地址：/workflow/$VERSION$/entity/{entityId}/attrs/{attrIds}；
        """
        r = ApiEntityManage.delete_attr_using(self,
                                              ids_=EntityManage.ids_,
                                              attr_ids=EntityManage.attr_ids
                                              )
        print(r)

    def test_1200_delete_entity_using(self):
        """
        接口名称：删除实体;    接口地址：/workflow/$VERSION$/entity/{entityIds}；
        """
        r = ApiEntityManage.delete_entity_using(self,
                                                ids_=EntityManage.ids_,
                                                )
        print(r)


if __name__ == '__main__':
    unittest.TestCase()

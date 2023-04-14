# -*- coding: utf-8 -*-
# @Time    : 2022/6/23
# @Author  : linxiaoyue
import datetime
import time
import unittest, requests
from project.api import ApiCustomBusinessTypeManager
import json
import random

class Virtualorg(unittest.TestCase):
    layout_id = ''
    arr_id = ''
    @classmethod
    def setUpClass(cls):
        pass

    def test_00100_select_business_list(self):
        """
        接口名称：查询属性列表
        接口地址：/proj/basis/$VERSION$/businesslist
        """
        r = ApiCustomBusinessTypeManager.select_business_list(self,
                                                              type_Dto="req"
                                                              )

        print(r)

    def test_00200_create_type_using(self):
        """
        接口名称：创建类型
        接口地址：/proj/basis/$VERSION$/type
        """
        r = ApiCustomBusinessTypeManager.create_type_using(self,
                                                           n_ame="test",
                                                           param_Name="test"
                                                           )
        print(r)
        ApiCustomBusinessTypeManager.id = r["id"]
        print(type(r))

    def test_00300_save_attr_using(self):
        """
        接口名称：创建属性
        接口地址：/proj/basis/$VERSION$/type/attr
        """
        time2 = int(time.time())
        # 创建数据库字段
        data1 = {
            "entityAttrs[0].attrName": "xxxx"+str(time2),
            "entityAttrs[0].attrKey": "ext_xxxx"+str(time2),
            "entityAttrs[0].attrType": "varchar",
            "entityAttrs[0].typeLength": 32,
            "entityAttrs[0].defaultValue": ""
        }
        r1 = ApiCustomBusinessTypeManager.createDatabaseFiled(data1)

        # 创建属性
        data2 = {
            "code": "xxxxxx"+str(time2),
            "displayName": "嘻嘻测试属性"+str(time2),
            "paramName": "xxxxxx",
            "fieldColumn": "ext_xxxx"+str(time2),
            "fieldEdit": "",
            "fieldType": "text-input",
            "logicType": 1,
            "defaultField": 0,
            "oper": "like,between,eq",
            "id": "",
            "name": "xxxxxx"+str(time2),
            "businessType": "erd.cloud.issue.dto.EtIssue",
            "typedefId": 4,
            "advancedSearch": 1,
            "typeConfig": '''{"attrType":"base","sort":true,"fieldEdit":"","advancedSearch":true,"mpxIndex":""}'''
        }
        r2 = ApiCustomBusinessTypeManager.save_attr_using(data2)
        print(r2)
        Virtualorg.arr_id = r2['res']['data']['id']
        self.assertEqual("200", r2["code"])

    def test_00400_get_attr_using(self):
        """
        接口名称：获取属性定义详情
        接口地址：/proj/basis/$VERSION$/type/attr/{id}
        """
        r = ApiCustomBusinessTypeManager.get_attr_using(self,
                                                        get_id=Virtualorg.arr_id
                                                        )

    def test_00500_update_attr_using(self):
        """
        接口名称：更新属性
        接口地址：/proj/basis/$VERSION$/type/attr/{id}
        """
        r = ApiCustomBusinessTypeManager.update_attr_using(self,
                                                           update_id=Virtualorg.arr_id,
                                                           dto={
                                                               "advancedSearch": 0,
                                                               "businessType": "erd.cloud.issue.dto.EtIssue",
                                                               "code": "xxxxxx",
                                                               "defaultField": "0",
                                                               "displayName": "嘻嘻测试属性",
                                                               "fieldColumn": "ext_xxxx",
                                                               "fieldEdit": "",
                                                               "fieldType": "text-input",
                                                               "flexAttrs": {},
                                                               "name": "xxxxxx",
                                                               "oper": "like,between,eq",
                                                               "paramName": "xxxxxx",
                                                               "typeConfig": "{\"attrType\":\"base\",\"sort\":true,\"fieldEdit\":\"\",\"advancedSearch\":true,\"mpxIndex\":\"\",\"fieldType\":\"varchar\"}",
                                                               "typedefId": "4",
                                                           }
                                                           )
        print(r)

    def test_00600_del_attr_using(self):
        """
        接口名称：删除属性定义
        接口地址：/proj/basis/$VERSION$/type/attrs/{ids}
        """

        ApiCustomBusinessTypeManager.del_attr_using(Virtualorg.arr_id)



    def test_00700_save_layout_using(self):
        """
        接口名称：创建类型布局
        接口地址：/proj/$VERSION$/type/layout
        """
        data = {
            "name": f"布局{int(time.time())}",
            "projectType": "ITProject",
            "tplType": "create",
            "template": '',
            "contextId": '',
            "contextType": "system",
            "active": 0,
            "typedefId": 4,
            "typedefName": "erd.cloud.issue.dto.EtIssue",
            "typeDef.id": 4,
            "typeDef.createBy": 1,
            "typeDef.createTime": "",
            "typeDef.updateBy": 1,
            "typeDef.updateTime": "2017-09-26 12:08:23",
            "typeDef.delFlag": 0,
            "typeDef.name": "erd.cloud.issue.dto.EtIssue",
            "typeDef.paramName": "ELIssue",
            "typeDef.displayCn": "问题",
            "typeDef.displayEn": "Issue",
            "typeDef.description": "问题定义",
            "typeDef.icon": '',
            "typeDef.instantiable": 1
        }
        r = ApiCustomBusinessTypeManager.save_layout_using(self, data=data)

        Virtualorg.layout_id = r['res']['data']['id']

        self.assertEqual("200", r["code"])

    def test_00800_get_layout_by(self):
        """
        接口名称：获取属性布局详情
        接口地址：/proj/basis/$VERSION$/type/layout/{id}
        """

        # 查看布局详情
        data = {"_": "1656987163698"}
        r = ApiCustomBusinessTypeManager.get_layout_by(Virtualorg.layout_id, data)
        self.assertEqual("200", r["code"])
        # # 删除布局
        # ApiCustomBusinessTypeManager.del_layout_using1(layout_id)

    def test_00900_enable_layout_using(self):
        """
        接口名称：启用类型布局
        接口地址：/proj/$VERSION$/type/layout/{id}
        """
        # 启用布局
        r = ApiCustomBusinessTypeManager.enable_layout_using(Virtualorg.layout_id)
        self.assertEqual("200", r["code"])

    def test_01000_update_layout_using1(self):
        """
        接口名称：更新类型布局
        接口地址：/proj/basis/$VERSION$/type/layout/{id}
        """
        # # 创建布局
        # layout_id, layout_name = ApiCustomBusinessTypeManager.create_default_layout(self)
        # 更新布局-用例
        data = {
            "tplJson": "{}",
            "typedefId": "4",
            "typedefName": "erd.cloud.issue.dto.EtIssue",
            "active": "0",
            "contextType": "system",
            "typeDef.id": "4",
            "typeDef.createBy": "1",
            "typeDef.createTime": "2017-09-26 12:08:23",
            "typeDef.updateBy": "1",
            "typeDef.updateTime": "2017-09-26 12:08:23",
            "typeDef.delFlag": "0",
            "typeDef.name": "erd.cloud.issue.dto.EtIssue",
            "typeDef.paramName": "ELIssue",
            "typeDef.displayCn": "问题",
            "typeDef.displayEn": "Issue",
            "typeDef.description": "问题定义",
            "typeDef.icon": "",
            "typeDef.instantiable": 1,
            "name": "update"+f"布局{int(time.time())}"
        }
        r = ApiCustomBusinessTypeManager.update_layout_using1(self, layout_id=Virtualorg.layout_id, json=data)
        self.assertEqual("200", r["code"])
        print(r)



    def test_01200_get_layout_by1(self):
        """
        接口名称：根据类型获取属性布局详情
        接口地址：/proj/basis/$VERSION$/type/typedefId/layouts
        """
        r = ApiCustomBusinessTypeManager.get_layout_by1(self)
        print(r)

    def test_01300_proj_basis_v1_types(self):
        """
        接口名称：获取类型定义列表数据
        接口地址：/proj/basis/v1/types
        """
        data = {
            "pagesize": 9999,
            "pageIndex": 1,
            "_": int(time.time()),
        }
        r = ApiCustomBusinessTypeManager.projBasisV1Types(data)
        self.assertEqual("200", r["code"])
        print(r)

    def test_01400_proj_v1_lifecycle_state(self):
        """
        接口名称：获取类型定义列表数据
        接口地址：/proj/v1/lifecycle/state
        """
        data = {
            "stateNameCN": "",
            "sort_by": "",
            "order_by": "",
            "page_size": 10,
            "pageindex": 1,
            "lifecycleTemplateId": "021c58072097fc2fac93f12632e53216",
            "_": 1657501360608,
        }
        r = ApiCustomBusinessTypeManager.proj_v1_lifecycle_state(data)
        self.assertEqual("200", r["code"])
        print(r)

    def test_01500_proj_v1_lifecycle_state(self):
        """
        接口名称：获取类型定义列表数据
        接口地址：/proj/basis/v1/type/{typeDefId}/attrs
        """
        data = {
            "displayName": "",
            "fieldType": "",
            "sort_by": "",
            "order_by": "",
            "_": int(time.time()),
        }
        r = ApiCustomBusinessTypeManager.proj_basis_v1_type_typeDefId_attrs(4, data)
        self.assertEqual("200", r["code"])
        print(r)

    def test_01100_del_layout_using1(self):
        """
        接口名称：删除类型布局
        接口地址：/proj/basis/$VERSION$/type/layout/{id}
        """
        # # 创建布局
        # layout_id, layout_name = ApiCustomBusinessTypeManager.create_default_layout(self)
        # 删除布局
        r = ApiCustomBusinessTypeManager.del_layout_using1(Virtualorg.layout_id)
        self.assertEqual("200", r["code"])
        print(r)

if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/4/22
import unittest
import time
from workflow.api import ApiApplyAction, ApiComponentOperation


class ApplyAction(unittest.TestCase):
    """应用操作/组件操作"""
    app_id = ""
    app_id_key = ""
    kit_id = ""
    kit_id_key = ""
    get_type = ""
    process_definition_id = ""
    model_id = ""

    def test_0100_find_mode_ids(self):
        """
        接口名称：模板列表;    接口地址：/workflow/$VERSION$/resource/app/findModeIdsByAppId；     调用位置：流程管理->应用组件->组件注册->组件详情
        """
        r = ApiApplyAction.find_mode_ids(self,
                                         app_id=""
                                         )
        print(r)

    def test_0101_get_list_using(self):
        """
        接口名称：app不分页列表;    接口地址：/workflow/$VERSION$/resource/app/getList；    调用位置：不知道
        """
        r = ApiApplyAction.get_list_using(self,
                                          )
        print(r)

    def test_0102_app_registry_using(self):
        """
        接口名称：app注册;    接口地址：/workflow/$VERSION$/resource/app/registry；      调用位置：流程管理->应用组件->应用注册->新增
        """
        r = ApiApplyAction.app_registry_using(self,
                                              app_dto={
                                                  "appName": time.strftime("%H:%M:%S", time.localtime()),
                                                  "idKey": "test_" + time.strftime("%Y%m%d%H%M%S", time.localtime())
                                              }
                                              )
        print(r)

    def test_0103_list_using_g(self):
        """
        接口名称：list;    接口地址：/workflow/$VERSION$/resource/app/{current}/{size}；       调用位置：流程管理->应用组件->应用注册
        """
        r = ApiApplyAction.list_using_g(self,
                                        )
        print(r)
        ApplyAction.app_id = r["res"]["data"]["records"][0]["id"]
        print("ApplyAction.app_id:", ApplyAction.app_id)
        ApplyAction.app_id_key = r["res"]["data"]["records"][0]["idKey"]
        print("ApplyAction.app_id_key:", ApplyAction.app_id_key)

    def test_0104_detail_using_g(self):
        """
        接口名称：app详细;    接口地址：/workflow/$VERSION$/resource/app/{id}；  调用位置：流程管理->应用组件->应用注册->应用详情
        """
        r = ApiApplyAction.detail_using_g(self,
                                          id_=ApplyAction.app_id
                                          )
        print(r)

    def test_0105_app_update_using(self):
        """
        接口名称：app修改;    接口地址：/workflow/$VERSION$/resource/app/update；    调用位置；流程管理->应用组件->应用注册->编辑
        """
        ApiApplyAction.app_update_using(self,
                                        app_dto={"id": ApplyAction.app_id,
                                                 "idKey": ApplyAction.app_id_key,
                                                 "appName": "update_" + time.strftime("%H:%M:%S", time.localtime()),
                                                 }
                                        )

    def test_0200_get_kit_resource(self):
        """
        接口名称：根据获取组件类型;    接口地址：/workflow/$VERSION$/resource/kit/getType；    调用位置：流程管理->应用组件->组件注册
        """
        r = ApiComponentOperation.get_kit_resource(self)
        print(r)
        ApplyAction.get_type = r["res"]["data"][0]["code"]
        print("ApplyAction.get_type:", ApplyAction.get_type)

    def test_0201_add_kit_resource(self):
        """
        接口名称：增加组件;    接口地址：/workflow/$VERSION$/resource/kit；    调用位置：流程管理->应用组件->组件注册->新增
        """
        r = ApiComponentOperation.add_kit_resource(self,
                                                   kit_resource_vo={
                                                       "id": "",
                                                       "resourceName": time.strftime("%H:%M:%S", time.localtime()),
                                                       "resourceKey": "test_" + time.strftime("%Y%m%d%H%M%S",
                                                                                              time.localtime()),
                                                       "resourceType": "business",
                                                       "appId": "12208c63cf0879048dcdbdc839b46f56",
                                                       "procModelId": "0566f69a116b11ed9e81f20639cc2c4b",
                                                       "resourceContent": "08d60bc2c22011ec91930a580afd039f",  # 资源包ID
                                                       "enabled": "Enabled"
                                                   }
                                                   )
        print(r)

    def test_0202_find_kit_resource(self):
        """
        接口名称：查询组件列表;    接口地址：/workflow/$VERSION$/resource/kit/{current}/{size}；     调用位置：流程管理->应用组件->组件注册
        """
        r = ApiComponentOperation.find_kit_resource(self, )
        print(r)
        ApplyAction.kit_id = r["res"]["data"]["records"][0]["id"]
        print("ApplyAction.kit_id:", ApplyAction.kit_id)
        ApplyAction.kit_id_key = r["res"]["data"]["records"][0]["resourceKey"]
        print("ApplyAction.kit_id_key:", ApplyAction.kit_id_key)

    def test_0203_get_kit_resource_1(self):
        """
        接口名称：根据id获取组件详情;    接口地址：/workflow/$VERSION$/resource/kit/{id}；      调用位置：流程管理->应用组件->组件注册->编辑
        """
        ApiComponentOperation.get_kit_resource_1(self,
                                                 id_=ApplyAction.kit_id
                                                 )

    def test_0204_update_kit_resource(self):
        """
        接口名称：修改组件;    接口地址：/workflow/$VERSION$/resource/kit；    调用位置：流程管理->应用组件->组件注册->编辑
        """
        ApiComponentOperation.update_kit_resource(self,
                                                  kit_resource_vo={
                                                      "id": ApplyAction.kit_id,
                                                      "resourceKey": ApplyAction.kit_id_key,
                                                      "resourceName": "update_" + time.strftime("%H:%M:%S",
                                                                                                time.localtime()),
                                                      "resourceType": ApplyAction.get_type,
                                                      "appId": ApplyAction.app_id
                                                  }
                                                  )

    def test_0500_find_model_kit(self):
        """
        接口名称：查询模板关联的组件信息;    接口地址：/workflow/$VERSION$/resource/kit/refmodel/{modelId}/{processDefinitionId}；
        """
        model_id1 = ApplyAction.process_definition_id.split(":")
        model_id2 = model_id1[0]
        ApplyAction.model_id = model_id2
        ApiComponentOperation.find_model_kit(self,
                                             model_id=model_id2,
                                             process_definition_id=ApplyAction.process_definition_id
                                             )

    def test_0210_remove_kit_resource(self):
        """
        接口名称：根据id删除组件;    接口地址：/workflow/$VERSION$/resource/kit/{id}；        调用位置：流程管理->应用组件->组件注册->删除
        """
        ApiComponentOperation.remove_kit_resource(self,
                                                  id_=ApplyAction.kit_id
                                                  )

    # def test_1001_find_app_by(self):
    #     """
    #     接口名称：根据模板id查询应用信息;    接口地址：/workflow/$VERSION$/resource/app/refmodel/{modelId}；
    #     """
    #     ApiApplyAction.find_app_by(self, model_id=ApplyAction.model_id)
    #      该接口不再调用
    def test_01100_app_delete_using(self):
        """
        接口名称：app删除;    接口地址：/workflow/$VERSION$/resource/app/{id}；      调用位置：流程管理->应用组件->应用注册->删除
        """
        r = ApiApplyAction.app_delete_using(self,
                                            id_=ApplyAction.app_id
                                            )
        print(r)


if __name__ == '__main__':
    unittest.TestCase()

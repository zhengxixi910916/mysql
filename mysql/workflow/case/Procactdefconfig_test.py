# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/10

import unittest
import time
from workflow.api import ApiProcactdefconfig, ApiProcessTemplateManagement, ApiProcessVariableDefinitionOperation


class Procactdefconfig(unittest.TestCase):
    """节点表单配置/流程变量定义操作"""
    process_definition_id = ""
    proc_model_id = ""
    act_def_id = ""


    # def test_0200_query_acts_using(self):
    #     """
    #     接口名称：查询流程定义开始、结束、用户节点;    接口地址：/workflow/$VERSION$/procactdefconfig/act；
    #     """
    #     r = ApiProcessTemplateManagement.query_page_using_get_5(self,
    #                                                             dto={
    #                                                                 "category": "others",
    #                                                                 "pageSize": 20
    #                                                             }
    #                                                             )
    #     print(type(r),r,)
    #     print(r['res']['data']['records'][0])
    #     Procactdefconfig.process_definition_id = r["res"]["data"]["records"][0]["id"]
    #     print("Procactdefconfig.process_definition_id:", Procactdefconfig.process_definition_id)
    #     Procactdefconfig.proc_model_id = r["res"]["data"]["records"][0]["id"]
    #     print("Procactdefconfig.proc_model_id:", Procactdefconfig.proc_model_id)
    #     r1 = ApiProcactdefconfig.query_acts_using(self,
    #                                               proc_def_id=Procactdefconfig.process_definition_id,
    #                                               proc_inst_id=""
    #                                               )
    #     print(r1)
    #     Procactdefconfig.act_def_id = r1["res"]["data"][1]["id"]
    #     print("Procactdefconfig.act_def_id:", Procactdefconfig.act_def_id)

    def test_0300_find_list_using(self):
        """
        接口名称：查询流程变量定义集合;    接口地址：/workflow/$VERSION$/variable/definition；
        """
        # 全局变量
        r1 = ApiProcessVariableDefinitionOperation.find_list_using(self,
                                                                   act_def_id="",
                                                                   proc_model_id=Procactdefconfig.proc_model_id,
                                                                   variable_type="GLOBAL"
                                                                   )
        print(r1)
        # 节点变量
        r2 = ApiProcessVariableDefinitionOperation.find_list_using(self,
                                                                   act_def_id=Procactdefconfig.act_def_id,
                                                                   proc_model_id=Procactdefconfig.proc_model_id,
                                                                   variable_type="LOCAL"
                                                                   )
        print(r2)

    # def test_0400_save_using_p(self):
    #     """
    #     接口名称：保存流程变量定义;    接口地址：/workflow/$VERSION$/variable/definition；
    #     """
    #     # 全局变量
    #     r1 = ApiProcessVariableDefinitionOperation.save_using_p(self,
    #                                                             process_variable_def_table_vo=
    #                                                             {"variableType": "GLOBAL",
    #                                                              "procModelId": Procactdefconfig.proc_model_id,
    #                                                              "actDefId": "",
    #                                                              "insertVariableList": [{
    #                                                                  "variableKey": "key_0" + time.strftime("%H%M%S",
    #                                                                                                        time.localtime()),
    #                                                                  "variableLabel": "test_" + time.strftime("%H%M%S",
    #                                                                                                           time.localtime()),
    #                                                                  "componentContent": "{\"componentType\":\"input\",\"props\":{\"type\":\"text\",\"defaultValue\":null,\"placeholder\":null,\"placeholderLang\":\"\",\"maxlength\":128,\"minLength\":null,\"max\":null,\"min\":null,\"rows\":3,\"showWordLimit\":true,\"clearable\":true}}",
    #                                                                  "readOnly": "N",
    #                                                                  "display": "Y",
    #                                                                  "variableType": "GLOBAL",
    #                                                                  "procModelId": Procactdefconfig.proc_model_id,
    #                                                                  "delFlag": "0"}],
    #                                                              "updateVariableList": [],
    #                                                              "deleteVariableList": []}
    #                                                             )
    #     print(r1)
    #     # 节点变量
    #     r2 = ApiProcessVariableDefinitionOperation.save_using_p(self,
    #                                                             process_variable_def_table_vo=
    #                                                             {
    #                                                                 "variableType": "LOCAL",
    #                                                                 "procModelId": Procactdefconfig.proc_model_id,
    #                                                                 "actDefId": Procactdefconfig.act_def_id,
    #                                                                 "insertVariableList": [
    #                                                                     {
    #                                                                         "variableKey": "key_" + time.strftime(
    #                                                                             "%H%M%S",
    #                                                                             time.localtime()),
    #                                                                         "variableLabel": "test_" + time.strftime(
    #                                                                             "%H%M%S",
    #                                                                             time.localtime()),
    #                                                                         "componentContent": "{\"componentType\":\"input\",\"props\":{\"type\":\"text\",\"defaultValue\":null,\"placeholder\":null,\"placeholderLang\":\"\",\"maxlength\":128,\"minLength\":null,\"max\":null,\"min\":null,\"rows\":3,\"showWordLimit\":true,\"clearable\":true}}",
    #                                                                         "readOnly": "N",
    #                                                                         "display": "Y",
    #                                                                         "variableType": "LOCAL",
    #                                                                         "procModelId": Procactdefconfig.proc_model_id,
    #                                                                         "actDefId": Procactdefconfig.act_def_id,
    #                                                                         "delFlag": "0"
    #                                                                     }
    #                                                                 ],
    #                                                                 "updateVariableList": [],
    #                                                                 "deleteVariableList": []
    #                                                             }
    #                                                             )
    #     print(r2)

    @unittest.skip("接口在前后端都未被使用，所以跳过！")
    def test_0500_edit_using_p(self):
        """
        接口名称：编辑流程变量定义;    接口地址：/workflow/$VERSION$/variable/definition；
        """
        ApiProcessVariableDefinitionOperation.edit_using_p(self)

    def test_0600_find_type_list(self):
        """
        接口名称：查询流程变量类型集合;    接口地址：/workflow/$VERSION$/variable/variable-type；
        """
        r = ApiProcessVariableDefinitionOperation.find_type_list(self)
        print(r)

    # def test_0800_query_act_def(self):
    #     """
    #     接口名称：根据流程定义ID查询所有节点表单布局ID;    接口地址：/workflow/$VERSION$/procactdefconfig/def/{procDefId}；
    #     """
    #     r = ApiProcactdefconfig.query_act_def(self,
    #                                           proc_def_id=Procactdefconfig.process_definition_id,
    #                                           proc_inst_id=""
    #                                           )
    #     print(r)

    # def test_0900_query_act_config(self):
    #     """
    #     接口名称：查询节点表单布局及表单数据;    接口地址：/workflow/$VERSION$/procactdefconfig/def/{procDefId}/{actDefId}；
    #     """
    #     r = ApiProcactdefconfig.query_act_config(self,
    #                                              act_def_id=Procactdefconfig.act_def_id,
    #                                              proc_inst_id=Procactdefconfig.process_definition_id
    #                                              )
    #     print(r)

    def test_01000_add_read_config(self):
        """
        接口名称：修改阅读提示;    接口地址：/workflow/$VERSION$/procactdefconfig/readconfig；
        """
        r = ApiProcactdefconfig.add_read_config(self,
                                                act_def_id=Procactdefconfig.act_def_id,
                                                config_type=4
                                                )
        print(r)


if __name__ == '__main__':
    unittest.main()

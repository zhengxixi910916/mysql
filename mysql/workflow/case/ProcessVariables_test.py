# -*- coding: utf-8 -*-
# @Time    :  2021/12/22
# @Author  : zhihuimin

import unittest
from workflow.api import ApiProcessVariables, ApiUserTaskProcessing


class ProcessVariables(unittest.TestCase):
    """流程变量接口"""
    task_id = ""
    process_inds_id = ""
    node_key_name = ""

    def test_01000_fina_variable_byprocess_instance_usingpost(self):
        """
        接口名称：根据流程实例ID获取流程变量
        接口地址：/workflow/$VERSION$/variable/getvariable/{processIndsId}
        """

        # 获取参数
        r = ApiUserTaskProcessing.query_todo_task1(self,
                                                                                          dto={
                                                                                              "category": "",
                                                                                              "pageSize": 20
                                                                                          }
                                                                                          )
        print(r)
        ProcessVariables.process_inds_id = r["res"]["data"]["records"][0]["processInstanceId"]
        ProcessVariables.node_key_name = r["res"]["data"]["records"][0]["taskName"]
        ProcessVariables.task_id = r["res"]["data"]["records"][0]["id"]

        fina = ApiProcessVariables.find_variable_by(self,
                                                    process_inds_id=ProcessVariables.process_inds_id)
        print("fina", fina)

    @unittest.skip("接口存在问题，开发已在开发分支修改，但不会合入当前的2.3版本，所以先跳过。")
    def test_01100_update_variable_byprocess_instance_usingpost(self):
        """
        接口名称：根据流程实例ID更新流程变量
        接口地址：/workflow/$VERSION$/variable/addorupdate/variable/{processIndsId}
        """
        r = ApiProcessVariables.update_variable_by(self,
                                                   process_inds_id=ProcessVariables.process_inds_id)
        print(r)

    @unittest.skip("接口存在问题，开发已在开发分支修改，但不会合入当前的2.3版本，所以先跳过。")
    def test_01200_update_variableLocal_byprocess_instance_usingpost(self):
        """
        接口名称：根据流程实例ID更新流程局布流程变量
        接口地址：/workflow/$VERSION$/variable/addorupdate/variableLocal/{processIndsId}
        """
        r = ApiProcessVariables.update_variable_local(self,
                                                      process_inds_id=ProcessVariables.process_inds_id,
                                                      node_key_name=ProcessVariables.node_key_name)
        print(r)


if __name__ == '__main__':
    unittest.main()

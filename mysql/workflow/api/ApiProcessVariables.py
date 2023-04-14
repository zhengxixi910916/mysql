# -*- coding: utf-8 -*-
# @Time    :  2021/12/22
# @Author  : zhihuimin

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "update_variable_by": "/workflow/$VERSION$/variable/addorupdate/variable/%s",  # 根据流程实例ID更新流程变量
    "update_variable_local": "/workflow/$VERSION$/variable/addorupdate/variableLocal/%s",  # 根据流程实例ID更新流程局布流程变量
    "find_variable_by": "/workflow/$VERSION$/variable/getvariable/%s",  # 根据流程实例ID获取流程变量
})


def update_variable_by(self, process_inds_id, checker=None):
    """
    接口名称：根据流程实例ID更新流程变量
    接口地址：/workflow/$VERSION$/variable/addorupdate/variable/{processIndsId}
    """
    r = RequestService.call_post(apis.get("update_variable_by", process_inds_id), json=[
        {
            "nodeKeyName": "",
            "variableName": "test",
            "variableValue": {"test1": "ssl"}
        }
    ]  # variableDtoList - required: True
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def update_variable_local(self, process_inds_id, node_key_name, checker=None):
    """
    接口名称：根据流程实例ID更新流程局布流程变量
    接口地址：/workflow/$VERSION$/variable/addorupdate/variableLocal/{processIndsId}
    """
    r = RequestService.call_post(apis.get("update_variable_local", process_inds_id), json=[
        {
            "nodeKeyName": node_key_name,
            "variableName": "test",
            "variableValue": {"test1": "ssl"}
        }
    ])
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def find_variable_by(self, process_inds_id, checker=None):
    """
    接口名称：根据流程实例ID获取流程变量
    接口地址：/workflow/$VERSION$/variable/getvariable/{processIndsId}
    """
    r = RequestService.call_post(apis.get("find_variable_by", process_inds_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

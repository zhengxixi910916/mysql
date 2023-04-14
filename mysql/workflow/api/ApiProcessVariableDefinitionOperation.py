from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "find_list_using": "/workflow/$VERSION$/variable/definition",  # 查询流程变量定义集合/保存流程变量定义/编辑流程变量定义
    "find_type_list": "/workflow/$VERSION$/variable/variable-type",  # 查询流程变量类型集合
})


def find_list_using(self, act_def_id, proc_model_id, variable_type, checker=None):
    """
    接口名称：查询流程变量定义集合;    接口地址：/workflow/$VERSION$/variable/definition；	
    """
    r = RequestService.call_get(apis.get("find_list_using", None), params={
        "actDefId": act_def_id,  # 流程节点id - required: False
        "procModelId": proc_model_id,
        "variableType": variable_type
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def save_using_p(self, process_variable_def_table_vo, checker=None):
    """
    接口名称：保存流程变量定义;    接口地址：/workflow/$VERSION$/variable/definition；	
    """
    r = RequestService.call_post(apis.get("find_list_using", None), json=process_variable_def_table_vo, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def edit_using_p(self, checker=None):
    """
    接口名称：编辑流程变量定义;    接口地址：/workflow/$VERSION$/variable/definition；	
    """
    r = RequestService.call_put(apis.get("find_list_using", None), json={
        "processVariableDefVO": ""  # processVariableDefVO - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def find_type_list(self, checker=None):
    """
    接口名称：查询流程变量类型集合;    接口地址：/workflow/$VERSION$/variable/variable-type；	
    """
    r = RequestService.call_get(apis.get("find_type_list", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

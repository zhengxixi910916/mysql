from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "query_acts_using": "/workflow/$VERSION$/procactdefconfig/act",  # 查询流程定义开始、结束、用户节点
    "query_act_def": "/workflow/$VERSION$/procactdefconfig/def/%s",  # 根据流程定义ID查询所有节点表单布局ID
    "query_act_config": "/workflow/$VERSION$/procactdefconfig/def/%s/%s",  # 查询节点表单布局及表单数据
    "add_read_config": "/workflow/$VERSION$/procactdefconfig/readconfig",  # 修改阅读提示
})


def query_acts_using(self, proc_def_id, proc_inst_id, checker=None):
    """
    接口名称：查询流程定义开始、结束、用户节点;    接口地址：/workflow/$VERSION$/procactdefconfig/act；
    """
    r = RequestService.call_get(apis.get("query_acts_using", None), params={
        "procDefId": proc_def_id,  # 流程定义ID - required: True
        "procInstId": proc_inst_id,  # 流程实例ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_act_def(self, proc_def_id, proc_inst_id, checker=None):
    """
    接口名称：根据流程定义ID查询所有节点表单布局ID;    接口地址：/workflow/$VERSION$/procactdefconfig/def/{procDefId}；
    """
    r = RequestService.call_get(apis.get("query_act_def", proc_def_id), params={
        "procInstId": proc_inst_id  # 流程实例ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_act_config(self, act_def_id, proc_inst_id, checker=None):
    """
    接口名称：查询节点表单布局及表单数据;    接口地址：/workflow/$VERSION$/procactdefconfig/def/{procDefId}/{actDefId}；
    """
    r = RequestService.call_get(apis.get("query_act_config", act_def_id, proc_inst_id, ), params={
        "actInstId": "",  # 流程实例ID - required: False
        "procInstId": "",  # 流程实例ID - required: False
        "taskId": "",  # taskId - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_read_config(self, act_def_id, config_type=4, checker=None):
    """
    接口名称：修改阅读提示;    接口地址：/workflow/$VERSION$/procactdefconfig/readconfig；
    """
    r = RequestService.call_post(apis.get("add_read_config", None), params={
        "actDefId": act_def_id,  # 任务定义Id - required: False
        "configType": config_type,  # 1布局 2保存接口 3提交接口 4已读 7询问 - required: False
        "configValue": "",  # 配置值 - required: False
        "createBy": "",  # None - required: False
        "createTime": "",  # None - required: False
        "id": "",  # 对象Id - required: False
        "procDefId": "",  # 流程定义Id - required: False
        "updateBy": "",  # None - required: False
        "updateTime": "",  # None - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

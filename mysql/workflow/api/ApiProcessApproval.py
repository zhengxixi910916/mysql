from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "find_pbo_draft": "/workflow/$VERSION$/findPboDraftInfo/bypobandnodekey",  # 查询PBO草稿详细数据
    "find_form_data": "/workflow/$VERSION$/findformdata/bypobandnodekey",  # 基于PBO和流程节点key查询FormData数据
    "start_process_by": "/workflow/$VERSION$/start/processbypbo",  # 基于PBO启动流程
    "submit_activity_task": "/workflow/$VERSION$/submit/process/submitActivityTask",  # 审批流程任务
})
def find_pbo_draft(self, checker=None):
    """
    接口名称：查询PBO草稿详细数据;    接口地址：/workflow/$VERSION$/findPboDraftInfo/bypobandnodekey；
    """
    r = RequestService.call_post(apis.post("find_pbo_draft", None),params= {
                    "executionId": "",  # 流程执行id - required: False
                    "pboId": "",  # PBO信息 - required: False
                    "processDefinitionId": "",  # 流程定义id - required: False
                    "sessionId": "",  # 节点上的唯一标识 - required: False
                    "taskId": "",  # 任务id - required: False
                },)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def find_form_data(self, pbo_id, session_id, checker=None):
    """
    接口名称：基于PBO和流程节点key查询FormData数据
    接口地址：/workflow/$VERSION$/findformdata/bypobandnodekey
    """
    r = RequestService.call_post(apis.post("find_form_data", None), params={
        "pboId": pbo_id,  # PBO信息 - required: False
        "sessionId": session_id,  # 节点上的唯一标识 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def start_process_by(self, parameter_vo, checker=None):
    """
    接口名称：基于PBO启动流程
    接口地址：/workflow/$VERSION$/start/processbypbo
    """
    r = RequestService.call_post(apis.post("start_process_by", None), json=parameter_vo)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def submit_activity_task(self, parameter_vo, checker=None):
    """
    接口名称：审批流程任务
    接口地址：/workflow/$VERSION$/submit/process/submitActivityTask
    """
    r = RequestService.call_post(apis.get("submit_activity_task", None), json=parameter_vo)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

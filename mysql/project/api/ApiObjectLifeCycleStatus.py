from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "selectEtLifeCycleStateUsingGET": "/proj/$VERSION$/lifecycle/state",  # 生命周期状态查询条件信息
    "insetEtLifeCycleStateUsingPUT": "/proj/$VERSION$/lifecycle/state",  # 新增或修改生命周期状态
    "deleteEtLifeCycleStateByIdUsingDELETE": "/proj/$VERSION$/lifecycle/state",  # 删除
})


def select_et_life_cycle_state_using_get(self,  life_template_id, checker=None):
    """
    接口名称：生命周期状态查询条件信息
    接口地址：/proj/$VERSION$/lifecycle/state
    """
    r = RequestService.call_get(apis.get("selectEtLifeCycleStateUsingGET", None), params={
        "ifecycleTemplateId": life_template_id
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r['res']['data']


def inset_et_life_cycle_state_using_put(self, life_template_id, life_state_id, checker=None):
    """
    接口名称：新增或修改生命周期状态
    接口地址：/proj/$VERSION$/lifecycle/state
    """
    r = RequestService.call_put(apis.get("insetEtLifeCycleStateUsingPUT", None), json=[
        {
            "id": life_state_id,
            "lifecycleTemplateId": life_template_id,
            "order": 0,
            "stateNameCN": "待提交5",
            "stateNameEN": "待提交5",
            "value": "DRAFT",
            "context": "",
            "active": 1,
            "isDefault": 1,
            "procDefName": "风险流程",
            "lifecycleStateModes": [
                {
                    "procDefId": "PPM_RISK:1:acabc384071811ec9c214a65b460b2ff",
                    "procDefName": "风险流程"
                }
            ],
            "createBy": "SYS_E39B20EA11E7A81AC85B767C89C1",
            "createTime": "2022-07-06 14:42:47",
            "updateBy": "SYS_E39B20EA11E7A81AC85B767C89C1",
            "updateTime": "2022-07-06 14:42:47",
            "delFlag": "0",
            "procDefId": ""
        }
    ])
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_et_life_cycle_state_by_id_using_delete(self, checker=None):
    """
    接口名称：删除
    接口地址：/proj/$VERSION$/lifecycle/state
    """
    r = RequestService.call_delete(apis.get("deleteEtLifeCycleStateByIdUsingDELETE", None), json={
        "id": ""  # 生命周期状态id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

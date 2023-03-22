from erdcloud import CommonServer
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "findElLifecycleTemplateUsingGET": "/proj/$VERSION$/lifecycle/template",  # 生命周期模板列表
    "insertElLifecycleTemplateUsingPOST": "/proj/$VERSION$/lifecycle/template",  # 新增或修改生命周期模板
    "deleteElLifecycleTemplateByIdUsingDELETE": "/proj/$VERSION$/lifecycle/template",  # 删除生命周期
    "releaseElLifecycleTemplateUsingPOST": "/proj/$VERSION$/lifecycle/template/release",  # 发布生命周期模板
    "getLifecycleTemplateUsingGET": "/proj/$VERSION$/lifecycle/template/states",  # 获取所有关联生命周期模板状态key对应中文名
    "findLifecycleTemplateAndStateUsingGET": "/proj/$VERSION$/lifecycle/template/templates/states",  # 生命周期模板列表及对应状态列表
    "getLifecycleTemplateByIdUsingGET": "/proj/$VERSION$/lifecycle/template/{id}",  # 根据模板ID获取生命周期模板详细信息
    "getStateModesByTempStateUsingGET": "/proj/$VERSION$/lifecycle/template/{id}/modes",  # 根据模板ID及状态值流程列表
    "getTempVersionsByIdUsingGET": "/proj/$VERSION$/lifecycle/template/{id}/release/versions",  # 根据模板ID获取对应所有已发布版本
    "getTempAllStateByIdUsingGET": "/proj/$VERSION$/lifecycle/template/%s/state",  # 根据模板ID获取对应所有版本的状态并去重
    "getTempAllVersionsByIdUsingGET": "/proj/$VERSION$/lifecycle/template/%s/versions",  # 根据模板ID获取对应所有版本
})


def find_el_lifecycle_template_using_get(self, checker=None):
    """
    接口名称：生命周期模板列表
    接口地址：/proj/$VERSION$/lifecycle/template
    """
    r = RequestService.call_get(apis.get("findElLifecycleTemplateUsingGET", None),
                                params={
                                    "version": "new",  # 版本 - required: False
                                }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r['res']['data']


def insert_el_lifecycle_template_using_post(self, checker=None):
    """
    接口名称：新增或修改生命周期模板
    接口地址：/proj/$VERSION$/lifecycle/template
    """
    r = RequestService.call_post(apis.get("insertElLifecycleTemplateUsingPOST", None), params={
        "active": "",  # 是否有效，1有效 0 无效 - required: False
        "bindingEntity": "",  # 模板是否绑定业务对象，0：未绑定 1：以绑定 - required: False
        "code": "",  # 模板标识位（同一模板code相同） - required: False
        "context": "",  # 上下文，默认：系统 - required: False
        "delFlag": "",  # None - required: False
        "entityId": "",  # 模板关联的业务类型ID - required: False
        "entityType": "",  # 模板关联的业务类型 - required: False
        "id": "",  # ID - required: False
        "lifecycleStates[0].active": "",  # 是否有效 - required: False
        "lifecycleStates[0].context": "",  # 描述 - required: False
        "lifecycleStates[0].id": "",  # ID - required: False
        "lifecycleStates[0].isDefault": "",  # 是否默认状态，1:是 0:否 - required: False
        "lifecycleStates[0].lifecycleStateModes[0].createBy": "",  # None - required: False
        "lifecycleStates[0].lifecycleStateModes[0].createTime": "",  # None - required: False
        "lifecycleStates[0].lifecycleStateModes[0].delFlag": "",  # None - required: False
        "lifecycleStates[0].lifecycleStateModes[0].id": "",  # 对象Id - required: False
        "lifecycleStates[0].lifecycleStateModes[0].lifecycleStateId": "",  # 生命周期状态ID - required: False
        "lifecycleStates[0].lifecycleStateModes[0].procDefId": "",  # 流程定义Id - required: False
        "lifecycleStates[0].lifecycleStateModes[0].procDefName": "",  # 流程名称 - required: False
        "lifecycleStates[0].lifecycleStateModes[0].updateBy": "",  # None - required: False
        "lifecycleStates[0].lifecycleStateModes[0].updateTime": "",  # None - required: False
        "lifecycleStates[0].lifecycleTemplateId": "",  # 生命周期模板ID - required: False
        "lifecycleStates[0].order": "",  # 顺序 - required: False
        "lifecycleStates[0].procDefName": "",  # 流程名称 - required: False
        "lifecycleStates[0].stateNameCN": "",  # 状态中文名称 - required: False
        "lifecycleStates[0].stateNameEN": "",  # 状态英文名称 - required: False
        "lifecycleStates[0].value": "",  # 数据值 - required: False
        "refId": "",  # 生命周期模板关联Id - required: False
        "templateName": "",  # 模板名称 - required: False
        "version": "",  # 版本 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_el_lifecycle_template_by_id_using_delete(self, checker=None):
    """
    接口名称：删除生命周期
    接口地址：/proj/$VERSION$/lifecycle/template
    """
    r = RequestService.call_delete(apis.get("deleteElLifecycleTemplateByIdUsingDELETE", None), json={
        "id": ""  # 生命周期id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def release_el_lifecycle_template_using_post(self, to_be_released_id, checker=None):
    """
    接口名称：发布生命周期模板
    接口地址：/proj/$VERSION$/lifecycle/template/release
    """
    com = CommonServer()
    token = com.get_token()
    r = RequestService.call_post(apis.get("releaseElLifecycleTemplateUsingPOST", None),
                                 headers={
                                     'Authorization': "Bearer " + token,
                                     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                 },
                                 data={
                                     "id": to_be_released_id,
                                     "active": 1
                                 }
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_lifecycle_template_using_get(self, checker=None):
    """
    接口名称：获取所有关联生命周期模板状态key对应中文名
    接口地址：/proj/$VERSION$/lifecycle/template/states
    """
    r = RequestService.call_get(apis.get("getLifecycleTemplateUsingGET", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def find_lifecycle_template_and_state_using_get(self, checker=None):
    """
    接口名称：生命周期模板列表及对应状态列表
    接口地址：/proj/$VERSION$/lifecycle/template/templates/states
    """
    r = RequestService.call_get(apis.get("findLifecycleTemplateAndStateUsingGET", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_lifecycle_template_by_id_using_get(self, checker=None):
    """
    接口名称：根据模板ID获取生命周期模板详细信息
    接口地址：/proj/$VERSION$/lifecycle/template/{id}
    """
    r = RequestService.call_get(apis.get("getLifecycleTemplateByIdUsingGET", None), json={
        "state": ""  # 生命周期模板状态 - required: False
    }, path={
        "id": ""  # 模板ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_state_modes_by_temp_state_using_get(self, checker=None):
    """
    接口名称：根据模板ID及状态值流程列表
    接口地址：/proj/$VERSION$/lifecycle/template/{id}/modes
    """
    r = RequestService.call_get(apis.get("getStateModesByTempStateUsingGET", None), json={
        "state": ""  # 生命周期模板状态 - required: False
    }, path={
        "id": ""  # 模板ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_temp_versions_by_id_using_get(self, checker=None):
    """
    接口名称：根据模板ID获取对应所有已发布版本
    接口地址：/proj/$VERSION$/lifecycle/template/{id}/release/versions
    """
    r = RequestService.call_get(apis.get("getTempVersionsByIdUsingGET", None), path={
        "id": ""  # 模板ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_temp_all_state_by_id_using_get(self, life_template_id, checker=None):
    """
    接口名称：根据模板ID获取对应所有版本的状态并去重
    接口地址：/proj/$VERSION$/lifecycle/template/{id}/state
    """
    r = RequestService.call_get(apis.get("getTempAllStateByIdUsingGET", life_template_id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_temp_all_versions_by_id_using_get(self, life_template_id, checker=None):
    """
    接口名称：根据模板ID获取对应所有版本
    接口地址：/proj/$VERSION$/lifecycle/template/{id}/versions
    """
    r = RequestService.call_get(apis.get("getTempAllVersionsByIdUsingGET", life_template_id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r['res']['data']

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "add_kit_resource": "/workflow/$VERSION$/resource/kit",  # 增加组件
    "update_kit_resource": "/workflow/$VERSION$/resource/kit",  # 修改组件
    "get_kit_resource": "/workflow/$VERSION$/resource/kit/getType",  # 根据获取组件类型
    "find_model_kit": "/workflow/$VERSION$/resource/kit/refmodel/%s/%s",  # 查询模板关联的组件信息
    "find_kit_resource": "/workflow/$VERSION$/resource/kit/%s/%s",  # 查询组件列表
    "get_kit_resource_1": "/workflow/$VERSION$/resource/kit/%s",  # 根据id获取组件详情
    "remove_kit_resource": "/workflow/$VERSION$/resource/kit/%s",  # 根据id删除组件
})


def add_kit_resource(self, kit_resource_vo, checker=None):
    """
    接口名称：增加组件;    接口地址：/workflow/$VERSION$/resource/kit；	
    """
    r = RequestService.call_post(apis.get("add_kit_resource", None), json=kit_resource_vo, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_kit_resource(self, kit_resource_vo, checker=None):
    """
    接口名称：修改组件;    接口地址：/workflow/$VERSION$/resource/kit；	
    """
    r = RequestService.call_put(apis.get("update_kit_resource", None), json=kit_resource_vo)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_kit_resource(self, checker=None):
    """
    接口名称：根据获取组件类型;    接口地址：/workflow/$VERSION$/resource/kit/getType；	
    """
    r = RequestService.call_get(apis.get("get_kit_resource", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def find_model_kit(self, model_id, process_definition_id, checker=None):
    """
    接口名称：查询模板关联的组件信息;    接口地址：/workflow/$VERSION$/resource/kit/refmodel/{modelId}/{processDefinitionId}；
    """
    r = RequestService.call_get(apis.get("find_model_kit", model_id, process_definition_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def find_kit_resource(self, current=1, size=20, checker=None):
    """
    接口名称：查询组件列表;    接口地址：/workflow/$VERSION$/resource/kit/{current}/{size}；	
    """
    r = RequestService.call_get(apis.get("find_kit_resource", current, size), params={
        "appId": "",  # 所属应用id - required: False
        "createBy": "",  # 创建者 - required: False
        "createTime": "",  # 创建时间 - required: False
        "createUserInfo.active": "",  # 用户在职状态(1.在职 2.离职) - required: False
        "createUserInfo.avatar": "",  # 头像 - required: False
        "createUserInfo.code": "",  # 用户编码（工号） - required: False
        "createUserInfo.displayEn": "",  # 真实名称(拼音) - required: False
        "createUserInfo.displayName": "",  # 真实名称(显示名) - required: False
        "createUserInfo.email": "",  # 电子邮箱 - required: False
        "createUserInfo.id": "",  # id - required: False
        "createUserInfo.leader": "",  # 是否leader，0：默认否,1:是 - required: False
        "createUserInfo.mobile": "",  # 手机号码 - required: False
        "createUserInfo.name": "",  # 用户名(登录名) - required: False
        "createUserInfo.orgId": "",  # 组织Id - required: False
        "createUserInfo.orgName": "",  # 组织名称 - required: False
        "createUserInfo.status": "",  # 用户状态 - required: False
        "createUserInfo.type": "",  # 用户类型 - required: False
        "delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "enabled": "",  # 是否有效 - required: False
        "id": "",  # 对象Id - required: False
        "idKey": "",  # 业务主键 - required: False
        "modeKey": "",  # 流程模板key - required: False
        "procModelId": "",  # 流程模板id - required: False
        "registryType": "",  # 注册类型（资源包注册/前端注册） - required: False
        "resourceContent": "",  # 组件资源内容（路径） - required: False
        "resourceKey": "",  # 组件KEY - required: False
        "resourceName": "",  # 组件名称 - required: False
        "resourceType": "",  # 资源类型（选择组件/审批组件等） - required: False
        "sureRepeat": "",  # 确认覆盖标识 - required: False
        "tenantId": "",  # 审计字段 - required: False
        "updateBy": "",  # 更新者 - required: False
        "updateTime": "",  # 更新时间 - required: False
        "updateUserInfo.active": "",  # 用户在职状态(1.在职 2.离职) - required: False
        "updateUserInfo.avatar": "",  # 头像 - required: False
        "updateUserInfo.code": "",  # 用户编码（工号） - required: False
        "updateUserInfo.displayEn": "",  # 真实名称(拼音) - required: False
        "updateUserInfo.displayName": "",  # 真实名称(显示名) - required: False
        "updateUserInfo.email": "",  # 电子邮箱 - required: False
        "updateUserInfo.id": "",  # id - required: False
        "updateUserInfo.leader": "",  # 是否leader，0：默认否,1:是 - required: False
        "updateUserInfo.mobile": "",  # 手机号码 - required: False
        "updateUserInfo.name": "",  # 用户名(登录名) - required: False
        "updateUserInfo.orgId": "",  # 组织Id - required: False
        "updateUserInfo.orgName": "",  # 组织名称 - required: False
        "updateUserInfo.status": "",  # 用户状态 - required: False
        "updateUserInfo.type": "",  # 用户类型 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_kit_resource_1(self, id_, checker=None):
    """
    接口名称：根据id获取组件详情;    接口地址：/workflow/$VERSION$/resource/kit/{id}；	
    """
    r = RequestService.call_get(apis.get("get_kit_resource_1", id_), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def remove_kit_resource(self, id_, checker=None):
    """
    接口名称：根据id删除组件;    接口地址：/workflow/$VERSION$/resource/kit/{id}；	
    """
    r = RequestService.call_delete(apis.get("remove_kit_resource", id_), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

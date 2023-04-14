from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "find_mode_ids": "/workflow/$VERSION$/resource/app/findModeIdsByAppId",  # 模板列表
    "get_list_using": "/workflow/$VERSION$/resource/app/getList",  # app不分页列表
    "find_app_by": "/workflow/$VERSION$/resource/app/refmodel/%s",  # 根据模板id查询应用信息
    "app_registry_using": "/workflow/$VERSION$/resource/app/registry",  # app注册
    "app_update_using": "/workflow/$VERSION$/resource/app/update",  # app修改
    "list_using_g": "/workflow/$VERSION$/resource/app/%s/%s",  # list
    "detail_using_g": "/workflow/$VERSION$/resource/app/%s",  # app详细
    "app_delete_using": "/workflow/$VERSION$/resource/app/%s",  # app删除
})


def find_mode_ids(self, app_id, checker=None):
    """
    接口名称：模板列表;    接口地址：/workflow/$VERSION$/resource/app/findModeIdsByAppId；	
    """
    r = RequestService.call_get(apis.get("find_mode_ids", None), params={
        "appId": app_id  # appId - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_list_using(self, checker=None):
    """
    接口名称：app不分页列表;    接口地址：/workflow/$VERSION$/resource/app/getList；	
    """
    r = RequestService.call_get(apis.get("get_list_using", None), params={
        "appDisplay": "",  # 展示名称 - required: False
        "appName": "",  # 应用code - required: False
        "createBy": "",  # 创建者 - required: False
        "createTime": "",  # 创建时间 - required: False
        "delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "id": "",  # 对象Id - required: False
        "idKey": "",  # IT主键 - required: False
        "likeAppName": "",  # 应用code - required: False
        "tenantId": "",  # 审计字段 - required: False
        "updateBy": "",  # 更新者 - required: False
        "updateTime": "",  # 更新时间 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def find_app_by(self, model_id, checker=None):
    """
    接口名称：根据模板id查询应用信息;    接口地址：/workflow/$VERSION$/resource/app/refmodel/{modelId}；
    """
    r = RequestService.call_get(apis.get("find_app_by", model_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def app_registry_using(self, app_dto, checker=None):
    """
    接口名称：app注册;    接口地址：/workflow/$VERSION$/resource/app/registry；	
    """
    r = RequestService.call_post(apis.get("app_registry_using", None), json=app_dto, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def app_update_using(self, app_dto, checker=None):
    """
    接口名称：app修改;    接口地址：/workflow/$VERSION$/resource/app/update；	
    """
    r = RequestService.call_put(apis.get("app_update_using", None), json=app_dto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def list_using_g(self, current=1, size=20, checker=None):
    """
    接口名称：list;    接口地址：/workflow/$VERSION$/resource/app/{current}/{size}；	
    """
    r = RequestService.call_get(apis.get("list_using_g", current, size), params={
        "appDisplay": "",  # 展示名称 - required: False
        "appName": "",  # 应用code - required: False
        "createBy": "",  # 创建者 - required: False
        "createTime": "",  # 创建时间 - required: False
        "delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "id": "",  # 对象Id - required: False
        "idKey": "",  # IT主键 - required: False
        "likeAppName": "",  # 应用code - required: False
        "tenantId": "",  # 审计字段 - required: False
        "updateBy": "",  # 更新者 - required: False
        "updateTime": "",  # 更新时间 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def detail_using_g(self, id_, checker=None):
    """
    接口名称：app详细;    接口地址：/workflow/$VERSION$/resource/app/{id}；	
    """
    r = RequestService.call_get(apis.get("detail_using_g", id_), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def app_delete_using(self, id_, checker=None):
    """
    接口名称：app删除;    接口地址：/workflow/$VERSION$/resource/app/{id}；	
    """
    r = RequestService.call_delete(apis.get("app_delete_using", id_), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "add_interface_using_post": "/workflow/$VERSION$/interface/add",  # 新增业务接口
    "business_interface_using_get_post_delete": "/workflow/$VERSION$/interface/config",  # 查询流程配置、增加流程配置、删除流程配置
    "get_et_business_by_id_using_get": "/workflow/$VERSION$/interface/config/%s",  # 查询流程配置
    "enabled_using_put": "/workflow/$VERSION$/interface/enable/%s",  # 设置启用或禁用
    "query_history_page_using_get": "/workflow/$VERSION$/interface/history/%s",  # 分页查询历史版本业务接口
    "query_interface_and_model_link_using_get": "/workflow/$VERSION$/interface/model/link/page",  # 查询接口和模板的关联关系
    "invoke_pth_by_id_using_get": "/workflow/$VERSION$/interface/rest/id/%s",  # 根据接口ID获取对应接口数据
    "invoke_pth_by_type_using_get": "/workflow/$VERSION$/interface/rest/%s",  # 根据接口类型获取对应接口数据
    "query_interface_type_list_using_get": "/workflow/$VERSION$/interface/type",  # 查询接口类型
    "update_interface_using_put": "/workflow/$VERSION$/interface/update/%s",  # 修改业务接口
})


def add_interface_using_post(self, dto, checker=None):
    """
    接口名称：新增业务接口
    接口地址：/workflow/$VERSION$/interface/add
    """
    r = RequestService.call_post(apis.get("add_interface_using_post", None), json=dto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def business_interface_using_get(self, dto, checker=None):
    """
    接口名称：查询流程配置
    接口地址：/workflow/$VERSION$/interface/config
    """
    r = RequestService.call_get(apis.get("business_interface_using_get_post_delete", None), params={
        "tenantId": dto.get("tenantId", "type1"),
        "name": dto.get("name", ""),
        "category": dto.get("category", "lifecircle,role,user,userById"),
        "type": dto.get("type", ""),
        "requestMethod": dto.get("requestMethod", ""),
        "syncFlag": dto.get("syncFlag", ""),
        "sortBy": dto.get("sortBy", ""),
        "orderBy": dto.get("orderBy", ""),
        "pageSize": dto.get("pageSize", "20"),
        "pageIndex": dto.get("pageIndex", "1"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def business_interface_using_post(self, checker=None):
    """
    接口名称：增加流程配置
    接口地址：/workflow/$VERSION$/interface/config
    """
    r = RequestService.call_post(apis.get("business_interface_using_get_post_delete", None), json={
        "businessInterface": ""  # 流程业务接口配置表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def business_interface_using_delete(self, records_id, checker=None):
    """
    接口名称：删除流程配置
    接口地址：/workflow/$VERSION$/interface/config
    """
    r = RequestService.call_delete(apis.get("business_interface_using_get_post_delete", None), params={
        "id": records_id  # 流程业务接口id列表，支持多个，逗号分隔 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_et_business_by_id_using_get(self, records_id, checker=None):
    """
    接口名称：查询流程配置
    接口地址：/workflow/$VERSION$/interface/config/{id}
    """
    r = RequestService.call_get(apis.get("get_et_business_by_id_using_get", records_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def enabled_using_put(self, ids, enable, checker=None):
    """
    接口名称：设置启用或禁用
    接口地址：/workflow/$VERSION$/interface/enable/{enable}
    """
    r = RequestService.call_put(apis.get("enabled_using_put", enable), params={
        "ids": ids  # 接口ids，多个逗号隔开 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def query_history_page_using_get(self, records_id, page_index, page_size, checker=None):
    """
    接口名称：分页查询历史版本业务接口
    接口地址：/workflow/$VERSION$/interface/history/{id}
    """
    r = RequestService.call_get(apis.get("query_history_page_using_get", records_id), params={
        "pageIndex": page_index,  # 页码 - required: False
        "pageSize": page_size,  # 页大小 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def query_interface_and_model_link_using_get(self, records_id, pager_name, checker=None):
    """
    接口名称：查询接口和模板的关联关系
    接口地址：/workflow/$VERSION$/interface/model/link/page
    """
    r = RequestService.call_get(apis.get("query_interface_and_model_link_using_get", None), params={
        "id": records_id,
        "pager_name": pager_name,
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def invoke_pth_by_id_using_get(ids):
    """
    接口名称：根据接口ID获取对应接口数据
    接口地址：/workflow/$VERSION$/interface/rest/id/{id}
    """
    r = RequestService.call_get(apis.get("invoke_pth_by_id_using_get", ids), )
    return r


def invoke_pth_by_type_using_get(self, category="lifecircle", checker=None):
    """
    接口名称：根据接口类型获取对应接口数据
    接口地址：/workflow/$VERSION$/interface/rest/{category}
    """
    r = RequestService.call_get(apis.get("invoke_pth_by_type_using_get", category), )
    return r


def query_interface_type_list_using_get(self, checker=None):
    """
    接口名称：查询接口类型
    接口地址：/workflow/$VERSION$/interface/type
    """
    r = RequestService.call_get(apis.get("query_interface_type_list_using_get", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def update_interface_using_put(self, business_interface, records_id, checker=None):
    """
    接口名称：修改业务接口
    接口地址：/workflow/$VERSION$/interface/update/{id}
    """
    r = RequestService.call_put(apis.get("update_interface_using_put", records_id), json=business_interface)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

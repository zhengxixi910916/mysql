from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "create_entity_using": "/workflow/$VERSION$/entity",  # 创建实体
    "query_attr_by": "/workflow/$VERSION$/entity/attr/%s",  # 根据属性id查询属性对象
    "create_entity_attr": "/workflow/$VERSION$/entity/attrs",  # 新增实体属性
    "modify_attr_using": "/workflow/$VERSION$/entity/attrs/%s",  # 修改未发布的实体属性列表
    "deploy_using_p": "/workflow/$VERSION$/entity/deploy/%s",  # 发布实体
    "query_list_using": "/workflow/$VERSION$/entity/list",  # 查询已经发布实体
    "query_page_using": "/workflow/$VERSION$/entity/page",  # 查询实体列表
    "delete_update_query_entity_using": "/workflow/$VERSION$/entity/%s",  # 删除实体、根据id查询实体、修改实体
    "query_attr_list": "/workflow/$VERSION$/entity/%s/attrs",  # 查询实体属性列表
    "delete_attr_using": "/workflow/$VERSION$/entity/%s/attrs/%s",  # 删除未发布的实体属性列表
})


def create_entity_using(self, dto, checker=None):
    """
    接口名称：创建实体;    接口地址：/workflow/$VERSION$/entity；
    """
    r = RequestService.call_post(apis.get("create_entity_using", None), params={
        "entityTitle": dto.get("entityTitle", "实体001"),
        "entityAlias": dto.get("entityAlias", "实体001"),
        "entityTable": dto.get("entityTable", "ENTITY001"),
        "description": dto.get("description", "测试"),
        "entityAttrs[0].name": dto.get("entityAttrs[0].name", "ext_001"),
        "entityAttrs[0].attrKey": dto.get("entityAttrs[0].attrKey", "ext_001"),
        "entityAttrs[0].attrType": dto.get("entityAttrs[0].attrType", "varchar"),
        "entityAttrs[0].typeLength": dto.get("entityAttrs[0].typeLength", "255"),
        "entityAttrs[0].defaultValue": dto.get("entityAttrs[0].defaultValue", ""),
        "entityAttrs[0].attrName": dto.get("entityAttrs[0].attrName", "ext_001"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_attr_by(self, ids_, checker=None):
    """
    接口名称：根据属性id查询属性对象;    接口地址：/workflow/$VERSION$/entity/attr/{attrId}；
    """
    r = RequestService.call_get(apis.get("query_attr_by", ids_), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def create_entity_attr(self, ids_, dto, checker=None):
    """
    接口名称：新增实体属性;    接口地址：/workflow/$VERSION$/entity/attrs；
    """
    r = RequestService.call_post(apis.get("create_entity_attr", None), params={
        "id": ids_,
        "entityAttrs[0].name": dto.get("entityAttrs[0].name", "ext_001"),
        "entityAttrs[0].attrKey": dto.get("entityAttrs[0].attrKey", "ext_001"),
        "entityAttrs[0].attrType": dto.get("entityAttrs[0].attrType", "varchar"),
        "entityAttrs[0].typeLength": dto.get("entityAttrs[0].typeLength", "255"),
        "entityAttrs[0].defaultValue": dto.get("entityAttrs[0].defaultValue", ""),
        "entityAttrs[0].attrName": dto.get("entityAttrs[0].attrName", "ext_001"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def modify_attr_using(self, ids_, dto, checker=None):
    """
    接口名称：修改未发布的实体属性列表;    接口地址：/workflow/$VERSION$/entity/attrs/{entityId}；
    """
    r = RequestService.call_put(apis.get("modify_attr_using", ids_), json=dto, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def deploy_using_p(self, ids_, checker=None):
    """
    接口名称：发布实体;    接口地址：/workflow/$VERSION$/entity/deploy/{entityId}；
    """
    r = RequestService.call_post(apis.get("deploy_using_p", ids_), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_list_using(self, checker=None):
    """
    接口名称：查询已经发布实体;    接口地址：/workflow/$VERSION$/entity/list；
    """
    r = RequestService.call_get(apis.get("query_list_using", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_page_using(self, dto, checker=None):
    """
    接口名称：查询实体列表;    接口地址：/workflow/$VERSION$/entity/page；
    """
    r = RequestService.call_get(apis.get("query_page_using", None), params={
        "tenantId ": dto.get("tenantId", "department"),
        "entityTitle": dto.get("entityTitle", ""),
        "pager_name ": dto.get("pager_name ", "20"),
        "sortBy ": dto.get("sortBy", ""),
        "orderBy": dto.get("orderBy", ""),
        "pageSize ": dto.get("pageSize", "100"),
        "pageIndex": dto.get("pageIndex", " 1"),
        "contextType": dto.get("contextType", "0"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_entity_using(self, ids_, checker=None):
    """
    接口名称：删除实体;    接口地址：/workflow/$VERSION$/entity/{entityIds}；
    """
    r = RequestService.call_delete(apis.get("delete_update_query_entity_using", ids_), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_by_id(self, ids_, checker=None):
    """
    接口名称：根据id查询实体;    接口地址：/workflow/$VERSION$/entity/{entityId}；
    """
    r = RequestService.call_get(apis.get("delete_update_query_entity_using", ids_), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_entity_using(self, ids_, dto, checker=None):
    """
    接口名称：修改实体;    接口地址：/workflow/$VERSION$/entity/{entityId}；
    """
    r = RequestService.call_put(apis.get("delete_update_query_entity_using", ids_), json=dto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_attr_list(self, ids_, checker=None):
    """
    接口名称：查询实体属性列表;    接口地址：/workflow/$VERSION$/entity/{entityId}/attrs；
    """
    r = RequestService.call_get(apis.get("query_attr_list", ids_), params={
        "attrName": "",  # 属性名称 - required: False
        "deployed": "",  # 是否已发布(Y：只查询已经发布的属性) - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_attr_using(self, ids_, attr_ids, checker=None):
    """
    接口名称：删除未发布的实体属性列表;    接口地址：/workflow/$VERSION$/entity/{entityId}/attrs/{attrIds}；
    """
    r = RequestService.call_delete(apis.get("delete_attr_using",  ids_, attr_ids), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

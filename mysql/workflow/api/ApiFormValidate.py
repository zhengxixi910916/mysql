from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "add_validate_using": "/workflow/$VERSION$/form/validate",  # 添加表单验证规则
    "get_validates_using": "/workflow/$VERSION$/form/validate/list",  # 分页查询表单验证规则列表
    "validate_using": "/workflow/$VERSION$/form/validate/%s",  # 批量删除表单验证规则、查询单个表单验证规则详情、修改表单验证规则
})


def add_validate_using(self, reg_name="token", reg_val='"token":"(.+?)"', rule_value="workflow", error_info="输入有误。",
                       description="测试", checker=None):
    """
    接口名称：添加表单验证规则;    接口地址：/workflow/$VERSION$/form/validate；
    """
    r = RequestService.call_post(apis.get("add_validate_using", None), params={
        "regName": reg_name,  # 规则名 - required: False
        "regVal": reg_val,  # 规则值 - required: False
        "ruleValue": rule_value,
        "errorInfo": error_info,
        "description": description,
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_validates_using(self, dto, checker=None):
    """
    接口名称：分页查询表单验证规则列表;    接口地址：/workflow/$VERSION$/form/validate/list；
    """
    r = RequestService.call_get(apis.get("get_validates_using", None), params={
        "tenantId": dto.get("tenantId", "department"),
        "regName": dto.get("regName", ""),
        "pager_name": dto.get("pager_name", "20"),
        "sortBy": dto.get("sortBy", ""),
        "orderBy": dto.get("orderBy", ""),
        "pageSize": dto.get("pageSize", "100"),
        "pageIndex": dto.get("pageIndex", "1"),
        "contextType": dto.get("contextType", "0"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def del_validate_using(self, id_, checker=None):
    """
    接口名称：批量删除表单验证规则;    接口地址：/workflow/$VERSION$/form/validate/{ids}；
    """
    r = RequestService.call_delete(apis.get("validate_using", id_), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_validate_using(self, id_, checker=None):
    """
    接口名称：查询单个表单验证规则详情;    接口地址：/workflow/$VERSION$/form/validate/{id}；
    """
    r = RequestService.call_get(apis.get("validate_using", id_), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def edit_validate_using(self, id_, dto, checker=None):
    """
    接口名称：修改表单验证规则;    接口地址：/workflow/$VERSION$/form/validate/{id}；
    """
    r = RequestService.call_put(apis.get("validate_using", id_), json=dto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

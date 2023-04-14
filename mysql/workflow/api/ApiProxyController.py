import time

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "add_act_proxy": "/workflow/$VERSION$/proxy",  # 创建流程代理配置-过期
    "cancle_using_g": "/workflow/$VERSION$/proxy/cancle/%s",  # 取消流程代理配置
    "query_page_using": "/workflow/$VERSION$/proxy/page",  # 流程代理配置列表
    "replace_proxy_page": "/workflow/$VERSION$/proxy/replace/%s",  # 遗留事项查询daili
    "proxy": "/workflow/$VERSION$/proxy/%s",  # 删除流程代理配置、获取流程代理配置根据id、更新流程代理配置
    "add_act_proxy1": "/workflow/v2/proxy",  # 创建流程代理配置
})


def add_act_proxy(userid):
    """
    接口名称：创建流程代理配置-过期;    接口地址：/workflow/$VERSION$/proxy；
    """
    data = {
        "proxyName": f"代理设定(ZIDS){int(time.time())}",
        "proxyType": "all-agent",
        "startDate": time.strftime('%Y-%m-%d', time.localtime(time.time() + (24 * 60 * 60 * 2))),
        "endDate": time.strftime('%Y-%m-%d', time.localtime(time.time() + (24 * 60 * 60 * 3))),
        "proxyUserids": userid,
        "processNames": "业务流程(ZIDS)001"
    }
    r = RequestService.call_post(apis.get("add_act_proxy", None), params=data)
    print(r)
    if r['code'] == '10002':
        return {"code": '200'}
    return r


def cancle_using_g(self, ids, checker=None):
    """
    接口名称：取消流程代理配置;    接口地址：/workflow/$VERSION$/proxy/cancle/{ids}；
    """
    r = RequestService.call_get(apis.get("cancle_using_g", ids), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_page_using(self, dto, checker=None):
    """
    接口名称：流程代理配置列表;    接口地址：/workflow/$VERSION$/proxy/page；
    """
    r = RequestService.call_get(apis.get("query_page_using", None), params={
        "tenantId": dto.get("tenantId", "department"),
        "proxyName": dto.get("proxyName", ""),
        "status": dto.get("status", ""),
        "sort_by": dto.get("sort_by", ""),
        "order_by": dto.get("order_by", ""),
        "pageSize": dto.get("pageSize", "100"),
        "pageIndex": dto.get("pageIndex", "1"),
        "flag": dto.get("flag", "work"),
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def replace_proxy_page(self, user_id, checker=None):
    """
    接口名称：遗留事项查询daili;    接口地址：/workflow/$VERSION$/proxy/replace/{userId}；
    """
    r = RequestService.call_get(apis.get("replace_proxy_page", user_id), params={
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_using_d(self, ids, checker=None):
    """
    接口名称：删除流程代理配置;    接口地址：/workflow/$VERSION$/proxy/{ids}；
    """
    r = RequestService.call_delete(apis.get("proxy", ids), params={
        "createByName": "",  # 删除人名称-联电用 - required: False
        "ifMail": "",  # 是否发送邮件-联电用 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_act_proxy(self, ids, checker=None):
    """
    接口名称：获取流程代理配置根据id;    接口地址：/workflow/$VERSION$/proxy/{id}；
    """
    r = RequestService.call_get(apis.get("proxy", ids), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_act_proxy(self, ids, proxy_v2, checker=None):
    """
    接口名称：更新流程代理配置;    接口地址：/workflow/$VERSION$/proxy/{id}；
    """
    r = RequestService.call_put(apis.get("proxy", ids), json=proxy_v2)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_act_proxy1(self, proxy_v2, checker=None):
    """
    接口名称：创建流程代理配置;    接口地址：/workflow/v2/proxy；
    """
    r = RequestService.call_post(apis.get("add_act_proxy1", None), json=proxy_v2)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

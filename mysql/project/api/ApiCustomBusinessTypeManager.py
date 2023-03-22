import time

import requests
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
from erdcloud.HttpClient import commonServer
import configparser

apis = Api({
    "select_business_list": "/proj/basis/$VERSION$/businesslist",  # 查询属性列表
    "create_type_using": "/proj/basis/$VERSION$/type",  # 创建类型
    "save_attr_using": "/proj/basis/$VERSION$/type/attr",  # 创建属性
    "get_attr_using": "/proj/basis/$VERSION$/type/attr/%s",  # 获取属性定义详情
    "update_attr_using": "/proj/basis/$VERSION$/type/attr/%s",  # 更新属性
    "del_attr_using": "/proj/basis/$VERSION$/type/attrs/{ids}",  # 删除属性定义
    "save_layout_using": "/proj/basis/$VERSION$/type/layout",  # 创建类型布局
    "get_layout_by": "/proj/basis/$VERSION$/type/layout/{id}",  # 获取属性布局详情
    "enable_layout_using": "/proj/basis/$VERSION$/type/layout/%s",  # 启用类型布局
    "update_layout_using1": "/proj/basis/$VERSION$/type/layout/%s",  # 更新类型布局
    "del_layout_using1": "/proj/basis/$VERSION$/type/layout/%s",  # 删除类型布局
    "get_layout_by1": "/proj/basis/$VERSION$/type/typedefId/layouts",  # 根据类型获取属性布局详情
    "get_type_by": "/proj/basis/$VERSION$/type/{id}",  # 获取类型定义详情
    "update_type_by": "/proj/basis/$VERSION$/type/{id}",  # 修改类型
    "attr_list_using": "/proj/basis/$VERSION$/type/{typeDefId}/attrs",  # 获取属性定义列表数据
    "query_type_page": "/proj/basis/$VERSION$/types",  # 获取类型定义列表数据
    "type_page_contain": "/proj/basis/$VERSION$/types/state",  # 获取类型定义包含状态列表数据
    "save_layout_using1": "/proj/$VERSION$/type/layout",  # 创建类型布局
    "enable_layout_using1": "/proj/$VERSION$/type/layout/{id}",  # 启用类型布局
    "update_layout_using2": "/proj/$VERSION$/type/layout/{id}",  # 更新类型布局
    "del_layout_using2": "/proj/$VERSION$/type/layout/{id}",  # 删除类型布局
})

envIniPath = './config/env.ini'


def select_business_list(self, type_Dto, checker=None):
    """
    接口名称：查询属性列表
    接口地址：/proj/basis/$VERSION$/businesslist
    """
    r = RequestService.call_get(apis.get("select_business_list"), params=type_Dto)
    print(r)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def create_type_using(self, n_ame, param_Name, checker=None):
    """
    接口名称：创建类型
    接口地址：/proj/basis/$VERSION$/type
    """
    r = RequestService.call_post(apis.post("create_type_using"), params={
        "description": "",  # 描述 - required: False
        "displayCn": "",  # 中文显示名 - required: False
        "displayEn": "",  # 英文显示名 - required: False
        "icon": "",  # 类型图标 - required: False
        "instantiable": "",  # 是否可实例化标识，用于后续动态生成类型表 - required: False
        "name": n_ame,  # 名称 - required: False
        "paramName": param_Name,  # 接口参数名称 - required: False
        "parentClassName": "",  # 父类名称 - required: False
        "parentId": "",  # 父类id - required: False
    })
    print(r)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def save_attr_using(data):
    """
    接口名称：创建属性
    接口地址：/proj/basis/$VERSION$/type/attr
    """
    # r = RequestService.call_post(apis.post("save_attr_using"), data=data)
    # return r
    host = commonServer.host
    url = host + "/proj/basis/v1/type/attr"
    headers = commonServer.get_headers()
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
    r = requests.request("POST", url=url, headers=headers, data=data)
    return r.json()


def get_attr_using(self, get_id, checker=None):
    """
    接口名称：获取属性定义详情
    接口地址：/proj/basis/$VERSION$/type/attr/{id}
    """
    r = RequestService.call_get(apis.get("get_attr_using", get_id), )
    print(r)
    self.assertEqual("200", r["code"])


def update_attr_using(self, update_id, dto, checker=None):
    """
    接口名称：更新属性
    接口地址：/proj/basis/$VERSION$/type/attr/{id}
    """
    r = RequestService.call_put(apis.put("update_attr_using", update_id), json=dto)

    self.assertEqual("200", r["code"])
    return r


def del_attr_using(id):
    """
    接口名称：删除属性定义
    接口地址：/proj/basis/$VERSION$/type/attrs/{ids}
    """
    # r = RequestService.call_delete(apis.delete("del_attr_using"), )
    # return r
    host = commonServer.host
    url = host + f"/proj/basis/v1/type/attrs/{id}"
    headers = commonServer.get_headers()
    # headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
    r = requests.request("DELETE", url=url, headers=headers)
    return r.json()


# def save_layout_using(self,nam_e,typedef_Id,active=0 ,checker=0,):
def save_layout_using(self, data):
    """
    接口名称：创建类型布局
    接口地址：/proj/basis/$VERSION$/type/layout
    """
    # r = RequestService.call_post(apis.post("save_layout_using"),params={
    #                 "active": "",  # 当前启用状态, 默认值1，有效：1、失效：0 - required: False
    #                 "contextId": "",  # 项目id - required: False
    #                 "contextType": "",  # 上下文类型 - required: False
    #                 "name": nam_e,  # 名称 - required: False
    #                 "projectType": "",  # 项目类型 - required: False
    #                 "tplJson": "",  # 模板JSON - required: False
    #                 "tplType": "",  # 模板类型 - required: False
    #                 "typedefId": typedef_Id,  # 类型定义Id - required: False
    #                 "typedefName": "",  # 类型定义名称 - required: False
    #             })

    r = RequestService.call_post(apis.post("save_layout_using"), params=data)
    # b=dict(r)
    # print(b)
    #
    # c=b["res"]["data"]["id"]

    return r


def get_layout_by(layout_id, data):
    """
    接口名称：获取属性布局详情
    接口地址：/proj/basis/$VERSION$/type/layout/{id}
    """
    # r = RequestService.call_get(apis.get("get_layout_by",layout_id),params=data)
    host = commonServer.host
    url = host + f"/proj/basis/v1/type/layout/{layout_id}"
    headers = commonServer.get_headers()
    r = requests.request("GET", url=url, headers=headers, params=data)
    return r.json()


def enable_layout_using(py_id):
    """
    接口名称：启用类型布局
    接口地址：/proj/basis/$VERSION$/type/layout/{id}
    """
    r = RequestService.call_post(apis.post("enable_layout_using", py_id), )
    return r


def create_default_layout(self):
    """
            接口名称：创建类型布局
            接口地址：/proj/$VERSION$/type/layout
    """
    default_layout_name = f"布局{int(time.time())}"
    data = {
        "name": default_layout_name,
        "projectType": -1,
        "tplType": "update",
        "template": '',
        "contextId": '',
        "contextType": "system",
        "active": 0,
        "typedefId": 4,
        "typedefName": "erd.cloud.issue.dto.EtIssue",
        "typeDef.id": 4,
        "typeDef.createBy": 1,
        "typeDef.createTime": "",
        "typeDef.updateBy": 1,
        "typeDef.updateTime": "2017-09-26 12:08:23",
        "typeDef.delFlag": 0,
        "typeDef.name": "erd.cloud.issue.dto.EtIssue",
        "typeDef.paramName": "ELIssue",
        "typeDef.displayCn": "问题",
        "typeDef.displayEn": "Issue",
        "typeDef.description": "问题定义",
        "typeDef.icon": '',
        "typeDef.instantiable": 1
    }
    res = save_layout_using(self, data=data)
    if res["code"] != "200":
        print(f"创建布局({default_layout_name})失败!")
    return res["res"]["data"]["id"], default_layout_name


def update_layout_using1(self, layout_id, json):
    """
    接口名称：更新类型布局
    接口地址：/proj/basis/$VERSION$/type/layout/{id}
    """
    r = RequestService.call_put(apis.put("update_layout_using1", layout_id), json=json)
    return r


def del_layout_using1(layout_id):
    """
    接口名称：删除类型布局
    接口地址：/proj/basis/$VERSION$/type/layout/{id}
    """
    r = RequestService.call_delete(apis.delete("del_layout_using1", layout_id), )
    return r


def get_layout_by1(self, acti_ve=0, checker=None):
    """
    接口名称：根据类型获取属性布局详情
    接口地址：/proj/basis/$VERSION$/type/typedefId/layouts
    """
    r = RequestService.call_get(apis.get("get_layout_by1"), params={
        "active": acti_ve,  # 当前启用状态, 默认值1，有效：1、失效：0 - required: False
        "contextId": "",  # 项目id - required: False
        "contextType": "",  # 上下文类型 - required: False
        "createBy": "",  # 创建者 - required: False
        "createTimeEnd": "",  # 创建时间结束 - required: False
        "createTimeStart": "",  # 创建时间开始 - required: False
        "delFlag": "",  # 删除标记（0：正常；1：删除；） - required: False
        "groupFields": "",  # 分组属性 - required: False
        "id": "",  # 对象Id - required: False
        "includeFields": "",  # 包含的属性 - required: False
        "orderBy": "",  # 字段排序 - required: False
        "projectType": "",  # 项目类型 - required: False
        "sortBy": "",  # 排序方式，asc,desc - required: False
        "tplType": "",  # 模板类型 - required: False
        "typeDefId": "",  # 类型定义Id - required: False
        "typedefName": "",  # 类型定义名称 - required: False
        "updateBy": "",  # 更新者 - required: False
        "updateTimeEnd": "",  # 更新时间结束 - required: False
        "updateTimeStart": "",  # 更新时间开始 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def get_type_by(self, checker):
    """
    接口名称：获取类型定义详情
    接口地址：/proj/basis/$VERSION$/type/{id}
    """
    r = RequestService.call_get(apis.get("get_type_by"), )
    apis.check(self, r, checker["code"], checker["success"])
    return r


def update_type_by(self, checker):
    """
    接口名称：修改类型
    接口地址：/proj/basis/$VERSION$/type/{id}
    """
    r = RequestService.call_put(apis.put("update_type_by"), json={
        "type": ""  # 类型定义 - required: False
    })
    apis.check(self, r, checker["code"], checker["success"])
    return r


def attr_list_using(self, checker):
    """
    接口名称：获取属性定义列表数据
    接口地址：/proj/basis/$VERSION$/type/{typeDefId}/attrs
    """
    r = RequestService.call_get(apis.get("attr_list_using"), params={
        "tableFieldType": ""  # 数据库字段类型 - required: False
    })
    apis.check(self, r, checker["code"], checker["success"])
    return r


def query_type_page(self, checker):
    """
    接口名称：获取类型定义列表数据
    接口地址：/proj/basis/$VERSION$/types
    """
    r = RequestService.call_get(apis.get("query_type_page"), params={
        "pageIndex": "",  # None - required: True
        "pagesize": "",  # None - required: True
    })
    apis.check(self, r, checker["code"], checker["success"])
    return r


def type_page_contain(self, checker):
    """
    接口名称：获取类型定义包含状态列表数据
    接口地址：/proj/basis/$VERSION$/types/state
    """
    r = RequestService.call_get(apis.get("type_page_contain"), params={
        "pageIndex": "",  # None - required: True
        "pagesize": "",  # None - required: True
    })
    apis.check(self, r, checker["code"], checker["success"])
    return r


def save_layout_using1(self, typedef_Id, nam_e, active=0, checker=None):
    """
    接口名称：创建类型布局
    接口地址：/proj/$VERSION$/type/layout
    """
    r = RequestService.call_post(apis.post("save_layout_using1"), params={
        "active": "",  # 当前启用状态, 默认值1，有效：1、失效：0 - required: False
        "contextId": "",  # 项目id - required: False
        "contextType": "",  # 上下文类型 - required: False
        "name": nam_e,  # 名称 - required: False
        "projectType": "",  # 项目类型 - required: False
        "tplJson": "",  # 模板JSON - required: False
        "tplType": "",  # 模板类型 - required: False
        "typedefId": typedef_Id,  # 类型定义Id - required: False
        "typedefName": "",  # 类型定义名称 - required: False
    })
    apis.check(self, r, checker["code"], checker["success"])
    return r


def enable_layout_using1(self, checker):
    """
    接口名称：启用类型布局
    接口地址：/proj/$VERSION$/type/layout/{id}
    """
    r = RequestService.call_post(apis.post("enable_layout_using1"), )
    apis.check(self, r, checker["code"], checker["success"])
    return r


def update_layout_using2(self, checker):
    """
    接口名称：更新类型布局
    接口地址：/proj/$VERSION$/type/layout/{id}
    """
    r = RequestService.call_put(apis.put("update_layout_using2"), json={
        "layout": ""  # layout - required: True
    })
    apis.check(self, r, checker["code"], checker["success"])
    return r


def del_layout_using2(self, checker):
    """
    接口名称：删除类型布局
    接口地址：/proj/$VERSION$/type/layout/{id}
    """
    r = RequestService.call_delete(apis.delete("del_layout_using2"), )
    apis.check(self, r, checker["code"], checker["success"])
    return r


def createDatabaseFiled(data):
    host = commonServer.host
    url = host + "/proj/v1/extfields"
    headers = commonServer.get_headers()
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
    r = requests.request("POST", url=url, headers=headers, data=data)
    return r.json()


def getHost():
    """获取服务器地址"""
    host = commonServer.host
    return host


def projBasisV1Types(data):
    """
     接口名称：获取类型定义列表数据
     接口地址：/proj/basis/v1/types
    """
    host = getHost()
    url = host + "/proj/basis/v1/types"
    headers = commonServer.get_headers()
    r = requests.request("GET", url=url, headers=headers, params=data)
    return r.json()


def proj_v1_lifecycle_state(data):
    """
    接口名称：获取类型定义列表数据
    接口地址：/proj/basis/v1/types
    """
    host = getHost()
    url = host + "/proj/v1/lifecycle/state"
    headers = commonServer.get_headers()
    r = requests.request("GET", url=url, headers=headers, params=data)
    return r.json()


def proj_basis_v1_type_typeDefId_attrs(typeDefId, data):
    """
    接口名称：获取类型定义列表数据
    接口地址：/proj/basis/v1/type/4/attrs
    """
    host = getHost()
    url = host + f"/proj/basis/v1/type/{typeDefId}/attrs"
    headers = commonServer.get_headers()
    r = requests.request("GET", url=url, headers=headers, params=data)
    return r.json()

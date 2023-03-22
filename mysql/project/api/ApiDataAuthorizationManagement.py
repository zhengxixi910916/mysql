from erdcloud import CommonServer
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "createObjectAclUsingPOST": "/proj/$VERSION$/acl",  # 新增权限（授权）
    "updateObjectAclUsingPUT": "/proj/$VERSION$/acl",  # 修改权限（授权）
    "delObjectAclUsingDELETE": "/proj/$VERSION$/acl",  # 删除权限（授权）
    "getDataLimitUsingGET": "/proj/$VERSION$/acl/limit",  # 获取权限枚举信息
    "getObjectAclsUsingGET": "/proj/$VERSION$/acl/list",  # 根据用户id或者角色id获取授权列表
    "getUserAclUsingGET_1": "/proj/$VERSION$/acl/proj/{userId}",  # 获取用户系统权限
    "acUserUsingGET": "/proj/$VERSION$/user/me",  # 统一获取用户信息，包括基本信息、角色信息、权限信息
})


def create_object_acl_using_post(self, template_id, checker=None):
    """
    接口名称：新增权限（授权）
    接口地址：/proj/$VERSION$/acl
    """
    com = CommonServer()
    token = com.get_token()
    r = RequestService.call_post(apis.get("createObjectAclUsingPOST", None),
                                 headers={
                                     'Authorization': "Bearer " + token,
                                     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                 },
                                 data={
                                     "roleId": "MARKETING",
                                     "contextType": "ELProject",
                                     "contextId": template_id,
                                     "resIds": "",
                                 }
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_object_acl_using_put(self, template_id, acl_list, checker=None):
    """
    接口名称：修改权限（授权）
    接口地址：/proj/$VERSION$/acl
    """
    r = RequestService.call_post(apis.get("updateObjectAclUsingPUT", None),
                                json=acl_list,
                                params={
                                    "roleId": "MARKETING",
                                    "contextType": "ELProject",
                                    "contextId": template_id,
                                    "resIds": ''
                                }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def del_object_acl_using_delete(self, template_id, checker=None):
    """
    接口名称：删除权限（授权）
    接口地址：/proj/$VERSION$/acl
    """
    r = RequestService.call_delete(apis.get("delObjectAclUsingDELETE", None),
                                   params={
                                       "roleId": "MARKETING",
                                       "contextType": "ELProject",
                                       "contextId": template_id
                                   }
                                   )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_data_limit_using_get(self, checker=None):
    """
    接口名称：获取权限枚举信息
    接口地址：/proj/$VERSION$/acl/limit
    """
    r = RequestService.call_get(apis.get("getDataLimitUsingGET", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_object_acls_using_get(self, template_id, checker=None):
    """
    接口名称：根据用户id或者角色id获取授权列表
    接口地址：/proj/$VERSION$/acl/list
    """
    r = RequestService.call_get(apis.get("getObjectAclsUsingGET", None), params={
        "roleId": "MARKETING",
        "contextType": "ELProject",
        "contextId": template_id,
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_user_acl_using_get_1(self, checker=None):
    """
    接口名称：获取用户系统权限
    接口地址：/proj/$VERSION$/acl/proj/{userId}
    """
    r = RequestService.call_get(apis.get("getUserAclUsingGET_1", None), params={
        "userId": ""  # 用户id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def ac_user_using_get(self, checker=None):
    """
    接口名称：统一获取用户信息，包括基本信息、角色信息、权限信息
    接口地址：/proj/$VERSION$/user/me
    """
    r = RequestService.call_get(apis.get("acUserUsingGET"))

    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

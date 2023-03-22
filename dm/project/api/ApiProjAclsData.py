from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目权限信息
'''
apis = Api({
    "get_proj_acl_system_role": "/proj/$VERSION$/acl/sys",  # 获取用户系统角色 对项目的操作权限
    "get_all_acl_system_roles": "/proj/$VERSION$/acls/sys",  # 获取用户系统角色 对所有对象的操作权限
    "get_obj_acl_proj_role": "/proj/$VERSION$/%s/acl",  # 获取用户项目角色 对对象的操作权限
    "get_all_acl_proj_roles": "/proj/$VERSION$/%s/acls",  # 获取用户项目角色 所有对象的操作权限
})


def get_proj_acl_system_role(self):
    """
    接口名称：获取用户系统角色 对项目的操作权限
    接口地址：/proj/$VERSION$/acl/sys
    """
    r = RequestService.call_get(apis.get("get_proj_acl_system_role"))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_all_acl_system_roles(self):
    """
    接口名称：获取用户系统角色 对所有对象的操作权限
    接口地址：/proj/$VERSION$/acls/sys
    """
    r = RequestService.call_get(apis.get("get_all_acl_system_roles"))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_obj_acl_proj_role(self, eid, objectType):
    """
    接口名称：获取用户项目角色 对对象的操作权限
    接口地址：/proj/$VERSION$/{id}/acl
    """
    r = RequestService.call_get(apis.get("get_obj_acl_proj_role", eid), params={
        "objectType": objectType  # 对象类型[可以是ELTask,ELIssue,ELRequirement,...] - required: True
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_all_acl_proj_roles(self, eid):
    """
    接口名称：获取用户项目角色 所有对象的操作权限
    接口地址：/proj/$VERSION$/{id}/acls
    """
    r = RequestService.call_get(apis.get("get_all_acl_proj_roles", eid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r

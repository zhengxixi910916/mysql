from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目角色
'''
apis = Api({
    "getAdvancSearchRoleTreeUsingGET": "/proj/$VERSION$/advancSearch/%s/role/tree",  # 高级查询角色树
    "copyProjectMembersRolesUsingGET": "/proj/$VERSION$/project/copy/role",  # 根据项目ID复制人员角色
    "deleteMemberRolesUsingDELETE": "/proj/$VERSION$/project/member/list",  # 删除当前项目下所有成员和角色
    "addProjectRoleUsingPOST": "/proj/$VERSION$/project/role",  # 新增项目角色
    "editProjectRoleUsingPUT": "/proj/$VERSION$/project/role",  # 修改项目角色
    "delProjectRoleUsingDELETE": "/proj/$VERSION$/project/role",  # 删除项目角色
    "getProjectRoleMembersUsingGET": "/proj/$VERSION$/project/role/members",  # 查询当前项目角色下的项目成员
    "delProjectRoleMemberUsingDELETE": "/proj/$VERSION$/project/role/members",  # 删除项目角色成员
    "SelectProjectRoleMembersUsingGET": "/proj/$VERSION$/project/%s/member/list",  # 查询当前项目下所有成员和角色
    "editProjectRoleMemberUsingPUT": "/proj/$VERSION$/project/%s/role/member",  # 修改项目成员角色
    "addProjectRoleMemberUsingPUT": "/proj/$VERSION$/project/%s/role/members",  # 新增项目角色成员
    "getProjectRoleTreeUsingGET": "/proj/$VERSION$/project/%s/role/tree",  # 查询项目角色树
    "getProjectRoleUsingGET": "/proj/$VERSION$/sys/roles",  # 查询系统配置的项目角色
})


def getAdvancSearchRoleTreeUsingGET(self, checker):
    """
    接口名称：高级查询角色树
    接口地址：/proj/$VERSION$/advancSearch/{project_id}/role/tree
    """
    r = RequestService.call_get(apis.get("getAdvancSearchRoleTreeUsingGET"), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def copyProjectMembersRolesUsingGET(self, oldproject_id, newproject_id, checker=None):
    """
    接口名称：根据项目ID复制人员角色
    接口地址：/proj/$VERSION$/project/copy/role
    """
    r = RequestService.call_get(apis.get("copyProjectMembersRolesUsingGET"), params={
        "oldProjectId": oldproject_id,
        "newProjectId": newproject_id
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteMemberRolesUsingDELETE(self, memberIds, project_id, checker=None):
    """
    接口名称：删除当前项目下所有成员和角色
    接口地址：/proj/$VERSION$/project/member/list
    """
    r = RequestService.call_delete(apis.get("deleteMemberRolesUsingDELETE"), json=memberIds,
                                   params={
                                       "projectId": project_id  # 项目id - required: True
                                   }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def addProjectRoleUsingPOST(self, isKeyMember, objectId, roleKey, checker=None):
    """
    接口名称：新增项目角色
    接口地址：/proj/$VERSION$/project/role
    """
    r = RequestService.call_post(apis.get("addProjectRoleUsingPOST"), params={
        "isKeyMember": isKeyMember,  # 是否为核心成员（非核心：0；核心：1） - required: False
        "objectId": objectId,  # 对象Id - required: False
        "roleKey": roleKey,  # 流程角色 - required: False

    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']


def editProjectRoleUsingPUT(self, isKeyMember, objectId, roleKey, checker=None):
    """
    接口名称：修改项目角色
    接口地址：/proj/$VERSION$/project/role
    """
    r = RequestService.call_put(apis.get("editProjectRoleUsingPUT"), json={
        "isKeyMember": isKeyMember,  # 是否为核心成员（非核心：0；核心：1） - required: False
        "objectId": objectId,  # 对象Id - required: False
        "roleKey": roleKey,  # 流程角色 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delProjectRoleUsingDELETE(self, HE, project_id, checker=None):
    """
    接口名称：删除项目角色
    接口地址：/proj/$VERSION$/project/role
    """
    r = RequestService.call_delete(apis.get("delProjectRoleUsingDELETE"), json=[HE],
                                   params={
                                       "projectId": project_id  # 项目id - required: True
                                   }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getProjectRoleMembersUsingGET(self, orderBy, page_index, page_size, project_id, roleKey, sortBy, checker=None):
    """
    接口名称：查询当前项目角色下的项目成员
    接口地址：/proj/$VERSION$/project/role/members
    """
    r = RequestService.call_get(apis.get("getProjectRoleMembersUsingGET"), params={
        "orderBy": orderBy,  # 排序字段 - required: False
        "pageindex": page_index,  # 页数 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
        "projectId": project_id,  # 项目ID - required: False
        "roleKey": roleKey,  # 项目角色KEY - required: False
        "sortBy": sortBy,  # 排序顺序 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delProjectRoleMemberUsingDELETE(self, checker):
    """
    接口名称：删除项目角色成员
    接口地址：/proj/$VERSION$/project/role/members
    """
    r = RequestService.call_delete(apis.get("delProjectRoleMemberUsingDELETE"), json={
        "memberIds": ""  # 成员Id列表 - required: False
    }, params={
        "projectId": ""  # 项目id - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def SelectProjectRoleMembersUsingGET(self, project_id, checker=None):
    """
    接口名称：查询当前项目下所有成员和角色
    接口地址：/proj/$VERSION$/project/{project_id}/member/list
    """
    r = RequestService.call_get(apis.get("SelectProjectRoleMembersUsingGET", project_id), params={

    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def editProjectRoleMemberUsingPUT(self, checker):
    """
    接口名称：修改项目成员角色
    接口地址：/proj/$VERSION$/project/{project_id}/role/member
    """
    r = RequestService.call_put(apis.get("editProjectRoleMemberUsingPUT"), json={
        "projectMember": ""  # 项目成员 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def addProjectRoleMemberUsingPUT(self, project_id, userId, roleKey, checker=None):
    """
    接口名称：新增项目角色成员
    接口地址：/proj/$VERSION$/project/{project_id}/role/members
    """
    r = RequestService.call_put(apis.get("addProjectRoleMemberUsingPUT", project_id), json=[{"userId": userId,
                                                                                            "roleKey": roleKey}]
                                , )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getProjectRoleTreeUsingGET(self, project_id, checker=None):
    """
    接口名称：查询项目角色树
    接口地址：/proj/$VERSION$/project/{project_id}/role/tree
    """
    r = RequestService.call_get(apis.get("getProjectRoleTreeUsingGET", project_id), params={

    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getProjectRoleUsingGET(self, project_id, checker=None):
    """
    接口名称：查询系统配置的项目角色
    接口地址：/proj/$VERSION$/sys/roles
    """
    r = RequestService.call_get(apis.get("getProjectRoleUsingGET"), params={
        "projectId": project_id  # 项目id - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

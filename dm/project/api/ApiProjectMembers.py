from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目成员
'''
apis = Api({
    "importMultipleProjectMemberUsingPOST": "/proj/$VERSION$/member/import",  # 导入项目成员
    "importProjectMemberUsingPOST": "/proj/$VERSION$/member/import/project",  # 项目成员导入项目
    "exportMultipleProjectMemberTemplateUsingGET": "/proj/$VERSION$/member/template/export",  # 下载多项目成员导入模板
    "updateRoleUsingPUT": "/proj/$VERSION$/project/member",  # 修改项目成员角色
    "deleteProjectMemberUsingPUT": "/proj/$VERSION$/project/members",  # 删除项目成员
    "replaceMemberUsingGET": "/proj/$VERSION$/project/replace/member",  # 替换项目成员
    "replaceMemberUsingPUT": "/proj/$VERSION$/project/replace/member",  # 替换项目成员
    "getProjectMemberRoleByUserUsingGET": "/proj/$VERSION$/project/{id}/member/role",  # 获取项目下当前用户的所有项目角色
    "getProjectMemberUsingGET": "/proj/$VERSION$/project/{id}/members",  # 项目成员查询
    "addMembersUsingPUT": "/proj/$VERSION$/project/%s/role/members",  # 添加项目成员
    "addProjectMemberUsingPOST": "/proj/$VERSION$/project/{project_id}/member/save",  # 添加或替换项目成员
})


def importMultipleProjectMemberUsingPOST(self, checker):
    """
    接口名称：导入项目成员
    接口地址：/proj/$VERSION$/member/import
    """
    r = RequestService.call_post(apis.get("importMultipleProjectMemberUsingPOST", None), data={
        "file": ""  # file - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def importProjectMemberUsingPOST(self, checker):
    """
    接口名称：项目成员导入项目
    接口地址：/proj/$VERSION$/member/import/project
    """
    r = RequestService.call_post(apis.get("importProjectMemberUsingPOST", None), data={
        "file": ""  # file - required: True
    }, params={
        "projectId": ""  # 项目id - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def exportMultipleProjectMemberTemplateUsingGET(self, checker):
    """
    接口名称：下载多项目成员导入模板
    接口地址：/proj/$VERSION$/member/template/export
    """
    r = RequestService.call_get(apis.get("exportMultipleProjectMemberTemplateUsingGET", None), None)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateRoleUsingPUT(self, checker):
    """
    接口名称：修改项目成员角色
    接口地址：/proj/$VERSION$/project/member
    """
    r = RequestService.call_put(apis.get("updateRoleUsingPUT", None), params={
        "id": "",  # 成员UUID - required: True
        "roleKey": "",  # 成员角色 - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteProjectMemberUsingPUT(self, checker):
    """
    接口名称：删除项目成员
    接口地址：/proj/$VERSION$/project/members
    """
    r = RequestService.call_put(apis.get("deleteProjectMemberUsingPUT", None), json={
        "memberList": ""  # 项目成员列表 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def replaceMemberUsingGET(self, id, newMemberId, checker=None):
    """
    接口名称：替换项目成员
    接口地址：/proj/$VERSION$/project/replace/member
    """
    r = RequestService.call_get(apis.get("replaceMemberUsingGET", None), params={
        "id": id,
        "newMemberId": newMemberId,
        "remark": '121'
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def replaceMemberUsingPUT(self, checker):
    """
    接口名称：替换项目成员
    接口地址：/proj/$VERSION$/project/replace/member
    """
    r = RequestService.call_put(apis.get("replaceMemberUsingPUT", None), json={
        "id": "",  # 项目成员数据Id - required: True
        "newMemberId": "",  # 替换的成员ID - required: True
        "remark": "",  # 备注 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getProjectMemberRoleByUserUsingGET(self, checker):
    """
    接口名称：获取项目下当前用户的所有项目角色
    接口地址：/proj/$VERSION$/project/{id}/member/role
    """
    r = RequestService.call_get(apis.get("getProjectMemberRoleByUserUsingGET", None), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getProjectMemberUsingGET(self, checker):
    """
    接口名称：项目成员查询
    接口地址：/proj/$VERSION$/project/{id}/members
    """
    r = RequestService.call_get(apis.get("getProjectMemberUsingGET", None), params={
        "active": "",  # 状态流中当前处理人标识(初始化：0 : 待处理：1 : 已处理：2) - required: False
        "ids": "",  # Id集合 - required: False
        "isKeyMember": "",  # 是否为核心成员（非核心：0；核心：1） - required: False
        "objectClassName": "",  # 对象ClassName - required: False
        "objectId": "",  # 对象Id - required: False
        "objectIds": "",  # 对象Id集合 - required: False
        "orderBy": "",  # 排序字段 - required: False
        "pageindex": "",  # 页码 - required: False
        "pagesize": "",  # 每页条数 - required: False
        "roleKey": "",  # 流程角色 - required: False
        "sort": "",  # 排序 - required: False
        "sortBy": "",  # 正序反序（ASC|DESC） - required: False
        "state": "",  # 状态 - required: False
        "userId": "",  # 成员用户Id - required: False
        "userIdIsNotNull": "",  # userid是否不为空 - required: False
        "userIds": "",  # 成员用户Id集合 - required: False
        "userName": "",  # 用户名称 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def addMembersUsingPUT(self, project_id, roleKey,checker=None):
    """
    接口名称：添加项目成员
    接口地址：/proj/$VERSION$/project/{id}/role/members
    """
    r = RequestService.call_put(apis.get("addMembersUsingPUT", project_id), json=[{"userId":"SYS_E39B20EA11E7A81AC85B767C89C1","roleKey": roleKey}])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def addProjectMemberUsingPOST(self, project_id, dataId, userId, remark, roleKey, checker=None):
    """
    接口名称：添加或替换项目成员
    接口地址：/proj/$VERSION$/project/{project_id}/member/save
    """
    r = RequestService.call_post(apis.get("addProjectMemberUsingPOST", project_id),
                                 json=[dataId, roleKey, remark, userId]

                                 # {
                                 #     "dataId": "",  # 数据Id - required: False
                                 #     "remark": "",  # 备注 - required: False
                                 #     "roleKey": roleKey,  # 角色Id - required: False
                                 #     "userId": userId,  # 用户Id - required: False
                                 # },
                                 )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

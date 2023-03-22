from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目文档数据权限接口
'''
apis = Api({
    "deleteAclUsingDELETE": "/proj/$VERSION$/doc/acl/%s",  # 删除数据操作权限
    "getUserAclsUsingGET": "/proj/$VERSION$/doc/user/%s/acls",  # 获取当前用户的数据操作权限
    "setAclUsingPUT": "/proj/$VERSION$/doc/%s/acl",  # 设置数据操作权限
    "getAclsUsingGET": "/proj/$VERSION$/doc/%s/acls",  # 获取数据操作权限
    "setAclUsingPOST": "/proj/$VERSION$/doc/%s/acls",  # 设置数据操作权限
})


def deleteAclUsingDELETE(self, aclId, checker=None):
    """
    接口名称：删除数据操作权限
    接口地址：/proj/$VERSION$/doc/acl/{aclId}
    """
    r = RequestService.call_delete(apis.get("deleteAclUsingDELETE", aclId), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getUserAclsUsingGET(self, project_id, type, checker=None):
    """
    接口名称：获取当前用户的数据操作权限
    接口地址：/proj/$VERSION$/doc/user/{objectId}/acls
    """
    r = RequestService.call_get(apis.get("getUserAclsUsingGET", project_id), params={
        "type": type  # 对象类型 - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def setAclUsingPUT(self, objectId, objectAcl, checker=None):
    """
    接口名称：设置数据操作权限
    接口地址：/proj/$VERSION$/doc/{objectId}/acl
    """
    r = RequestService.call_put(apis.get("setAclUsingPUT", objectId), json={
        "objectAcl": objectAcl  # 数据权限配置 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getAclsUsingGET(self, objectId, type, checker=None):
    """
    接口名称：获取数据操作权限
    接口地址：/proj/$VERSION$/doc/{objectId}/acls
    """
    r = RequestService.call_get(apis.get("getAclsUsingGET", objectId), params={
        "type": type  # 对象类型 - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def setAclUsingPOST(self, objectId, type, accessLimit0, accessType0, contextId0, contextType0, objectId0,
                    objectState0, objectType0, principalId0, principalType0, accessLimit1, accessType1,
                    contextId1, contextType1, objectId1, objectState1, objectType1,
                    principalId1, principalType1, checker=None):
    """
    接口名称：设置数据操作权限
    接口地址：/proj/$VERSION$/doc/{objectId}/acls
    """
    r = RequestService.call_post(apis.get("setAclUsingPOST", objectId), params={
        "type": type,
        "objectAcls[0].accessLimit": accessLimit0,
        "objectAcls[0].accessType": accessType0,
        "objectAcls[0].contextId": contextId0,
        "objectAcls[0].contextType": contextType0,
        "objectAcls[0].objectId": objectId0,
        "objectAcls[0].objectState": objectState0,
        "objectAcls[0].objectType": objectType0,
        "objectAcls[0].principalId": principalId0,
        "objectAcls[0].principalType": principalType0,
        "objectAcls[1].accessLimit": accessLimit1,
        "objectAcls[1].accessType": accessType1,
        "objectAcls[1].contextId": contextId1,
        "objectAcls[1].contextType": contextType1,
        "objectAcls[1].objectId": objectId1,
        "objectAcls[1].objectState": objectState1,
        "objectAcls[1].objectType": objectType1,
        "objectAcls[1].principalId": principalId1,
        "objectAcls[1].principalType": principalType1,
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

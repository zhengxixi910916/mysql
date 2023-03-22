
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
虚拟部门API
'''
apis = Api({
    "AddVirtualorgPost": "/proj/$VERSION$/virtualorg/add",  # 添加虚拟部门
    "DeleteVirtualorgDelete": "/proj/$VERSION$/virtualorg/delete/%s",  # 删除虚拟部门
    "QueryVirtualorgGet": "/proj/$VERSION$/virtualorg/list",  # 查询虚拟部门
    "UpdateVirtualorgPut": "/proj/$VERSION$/virtualorg/update",  # 修改虚拟部门
    "VirtualorgGet": "/proj/$VERSION$/virtualorg/%s",  # 根据ID查询虚拟部门详情
    "getVirtualchildenUsingGET": "/proj/$VERSION$/virtualorg/%s/list",  # 根据id查询所有子部门
})


def AddVirtualorgPost(self, name, parentId, leader, pmo, description, checker=None):
    """
    接口名称：添加虚拟部门
    接口地址：/proj/$VERSION$/virtualorg/add
    """
    r = RequestService.call_post(apis.post("AddVirtualorgPost"), params={
        "name": name,  # 是否有权限:0 没有权限 1 有权限 - required: False
        "parentId": parentId,  # 是否有权限:0 没有权限 1 有权限 - required: False
        "leader": leader,  # 领导 - required: False
        "pmo": pmo,  # pmo - required: False
        "description": description
    }, )
    print(r)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def DeleteVirtualorgDelete(self, id, checker=None):
    """
    接口名称：删除虚拟部门
    接口地址：/proj/$VERSION$/virtualorg/delete/{id}
    """
    r = RequestService.call_delete(apis.delete("DeleteVirtualorgDelete", id))
    print(r)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def QueryVirtualorgGet(self, checker=None):
    """
    接口名称：查询虚拟部门
    接口地址：/proj/$VERSION$/virtualorg/list
    """
    r = RequestService.call_get(apis.get("QueryVirtualorgGet"), params={
    }, )
    # print(r)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    # print(r['res']["data"][-1]['id'])
    # print(r['res']["data"][-1]['parentId'])
    return r['res']["data"][-1]['id'], r['res']["data"][-1]['parentId']


def UpdateVirtualorgPut(self, description, flexAttrs, id, leader, name, parentId, pmo, checker=None):
    """
    接口名称：修改虚拟部门
    接口地址：/proj/$VERSION$/virtualorg/update
    """
    r = RequestService.call_put(apis.put("UpdateVirtualorgPut"), json={

        "description": description,
        "flexAttrs": flexAttrs,
        "id": id,
        "leader": leader,
        "name": name,
        "parentId": parentId,
        "pmo": pmo
    }, )
    # print(r)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def VirtualorgGet(self, id, checker=None):
    """
    接口名称：根据ID查询虚拟部门详情
    接口地址：/proj/$VERSION$/virtualorg/{id}
    """
    r = RequestService.call_get(apis.get("VirtualorgGet", id), )
    # print(r)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getVirtualchildenUsingGET(self, parentId, checker=None):
    """
    接口名称：根据id查询所有子部门
    接口地址：/proj/$VERSION$/virtualorg/{id}/list
    """
    r = RequestService.call_get(apis.get("getVirtualchildenUsingGET", parentId), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

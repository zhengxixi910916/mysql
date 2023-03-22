from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "createFolderUsingPOST": "/proj/$VERSION$/doc/folder",  # 创建文件夹
    "folderTeeListUsingGET": "/proj/$VERSION$/doc/folder/tree",  # 根据根节点获取文件夹树
    "updateFolderUsingPUT": "/proj/$VERSION$/doc/folder/%s",  # 修改文件夹
    "deleteFolderUsingDELETE": "/proj/$VERSION$/doc/folder/%s",  # 根据ID删除文件夹
    "folderIsNullUsingGET": "/proj/$VERSION$/doc/folder/%s/isnull",  # 根据ID判断文件夹是否为空
    "folderTeeAllListUsingGET": "/proj/$VERSION$/doc/folder/%s/children",  # 根据父ID查询子文件夹
})


def createFolderUsingPOST(self, context_id, context_type, parent_id, checker=None):
    """
    接口名称：创建文件夹
    接口地址：/proj/$VERSION$/doc/folder
    """
    r = RequestService.call_post(apis.get("createFolderUsingPOST", None), params={
        "contextId": context_id,  # 上下文id - required: False
        "contextType": context_type,  # 上下文类型 - required: False
        "description": "",  # 文件夹描述 - required: False
        "id": "",  # None - required: False
        "name": "新建文件夹",  # 文件夹名称 - required: False
        "operateType": "",  # 对象处理类型(不需要前端传) - required: False
        "parentId": parent_id,  # 父文件夹ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r['res']['data']


def folderTeeListUsingGET(self, tree_id, checker=None):
    """
    接口名称：根据根节点获取文件夹树
    接口地址：/proj/$VERSION$/doc/folder/tree
    """
    r = RequestService.call_get(apis.get("folderTeeListUsingGET", None), params={
        "id": tree_id,  # id - required: True
        "taskName": "",  # taskName - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def updateFolderUsingPUT(self, folder_id, checker=None):
    """
    接口名称：修改文件夹
    接口地址：/proj/$VERSION$/doc/folder/{id}
    """
    r = RequestService.call_put(apis.get("updateFolderUsingPUT", folder_id), json={
        "name": "重命名文件夹"  # 文件夹对象 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def deleteFolderUsingDELETE(self, folder_id, checker=None):
    """
    接口名称：根据ID删除文件夹
    接口地址：/proj/$VERSION$/doc/folder/{id}
    """
    r = RequestService.call_delete(apis.get("deleteFolderUsingDELETE", folder_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def folderIsNullUsingGET(self, folder_id, checker=None):
    """
    接口名称：根据ID判断文件夹是否为空
    接口地址：/proj/$VERSION$/doc/folder/{id}/isnull
    """
    r = RequestService.call_get(apis.get("folderIsNullUsingGET", folder_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def folderTeeAllListUsingGET(self, parentid, checker=None):
    """
    接口名称：根据父ID查询子文件夹
    接口地址：/proj/$VERSION$/doc/folder/{parentid}/children
    """
    r = RequestService.call_get(apis.get("folderTeeAllListUsingGET", parentid), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

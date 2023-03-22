
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
et-document-view-controller
'''
apis = Api({
    "getFileInfoUsingGET": "/wopi/files/%s",  # getFileInfo
    "getFileContentsUsingGET": "/wopi/files/%s/contents",  # getFileContents
})


def getFileInfoUsingGET(self, doc_id, token, checker=None):
    """
    接口名称：getFileInfo
    接口地址：/wopi/files/{id}
    """
    r = RequestService.call_get(apis.get("getFileInfoUsingGET", doc_id), params={
        "access_token": token  # 可访问token - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getFileContentsUsingGET(self, doc_id, token, checker=None):
    """
    接口名称：getFileContents
    接口地址：/wopi/files/{id}/contents
    """
    r = RequestService.call_get(apis.get("getFileContentsUsingGET", doc_id), params={
        "access_token": token  # 可访问token - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
import requests
from erdcloud import CommonServer
from erdcloud.HttpClient import commonServer
import os

file_name = None

apis = Api({
    "queryAttListByObjectUsingPOST": "/proj/$VERSION$/doc/attachment/objects/list",  # 根据业务ID查找文件
    "createDocUsingPOST": "/proj/$VERSION$/doc/doc",  # 创建文档
    "deleteAttachUsingDELETE_1": "/proj/$VERSION$/doc/doc/%s/%s",  # 删除文件附件
    "document_path": "/proj/$VERSION$/doc/doc/%s",  # 查询文档详情、# 修改文档、# 删除文档
    "historyDocDetailUsingGET": "/proj/$VERSION$/doc/doc/%s/history",  # 查询历史文档详情
    "createAttachDocUsingPOST": "/proj/$VERSION$/doc/docs",  # 批量创建文档
    "pageUsingGET_1": "/proj/$VERSION$/doc/list",  # 查询文档分页
    "moveDocumentUsingPUT": "/proj/$VERSION$/doc/move",  # 移动文件夹（文档）
    "searchlistUsingGET": "/proj/$VERSION$/doc/searchlist",  # 项目文档搜索分页
    "uploadAttachUsingPOST_1": "/proj/$VERSION$/doc/upload",  # 上传文件，支持批量
    "uploadCoverAttachUsingPOST": "/proj/$VERSION$/doc/upload/cover",  # 修改文件
    "queryAttListUsingGET": "/proj/$VERSION$/doc/%s/list",  # 查询历史版本文件list
    "docHistoryListUsingGET": "/proj/$VERSION$/doc/%s/histories",  # 根据文档id查询该文档历史记录
})


def query_attlist_by_object(self, checker=None):
    """
    接口名称：根据业务ID查找文件
    接口地址：/proj/$VERSION$/doc/attachment/objects/list
    """
    r = RequestService.call_post(apis.get("queryAttListByObjectUsingPOST", None), json={
        "objectIds": ""  # objectIds - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def create_doc(self, context_id, context_type):
    """
    接口名称：创建文档
    接口地址：/proj/$VERSION$/doc/doc
    """
    # 获取上一级目录
    dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    dir_document = dir_path + r'/document'
    li = os.listdir(dir_document)  # 列出文件夹下所有的目录与文件
    global file_name
    file_name = os.path.join(dir_document, li[0])

    com = CommonServer()
    token = com.get_token()
    context = commonServer.get_context()
    api_path = commonServer.get_host() + context + apis.get("createDocUsingPOST")
    with open(file_name, 'rb') as file:
        file = {'file': file}
        data = {
            "title": "test",
            "type": "PP",
            "folderId": "",
            "description": "",
            "contextId": context_id,
            "contextType": context_type,
            "stateKey": "PENDINGAUDIT",
            "flag": True,
            "name": ""
        }
        r = requests.post(url=api_path,
                          headers={
                              'Authorization': 'Bearer ' + token,
                          },
                          data=data,
                          files=file
                          )
    apis.check_success(self, r.json())
    return r.json()['res']['data']


def delete_attach(self, doc_id, file_id, checker=None):
    """
    接口名称：删除文件附件
    接口地址：/proj/$VERSION$/doc/doc/{docid}/{fid}
    """
    r = RequestService.call_delete(apis.get("deleteAttachUsingDELETE_1", doc_id, file_id), params={
        "ismain": ""
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def doc_detail(self, doc_id, checker=None):
    """
    接口名称：查询文档详情
    接口地址：/proj/$VERSION$/doc/doc/{id}
    """
    r = RequestService.call_get(apis.get("document_path", doc_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def update_doc(self, doc_id, folder_id, checker=None):
    """
    接口名称：修改文档
    接口地址：/proj/$VERSION$/doc/doc/{id}
    """
    r = RequestService.call_put(apis.get("document_path", doc_id), json={
        "title": file_name,
        "type": "PP",
        "folderId": folder_id,
        "description": "123",
        "flexAttrs": {}
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def delete_doc(self, doc_id, checker=None):
    """
    接口名称：删除文档
    接口地址：/proj/$VERSION$/doc/doc/{id}
    """
    r = RequestService.call_delete(apis.get("document_path", doc_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def history_doc_detail(self, doc_id, checker=None):
    """
    接口名称：查询历史文档详情
    接口地址：/proj/$VERSION$/doc/doc/{id}/history
    """
    r = RequestService.call_get(apis.get("historyDocDetailUsingGET", doc_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def create_attach_doc(self, context_id, folder_id):
    """
    接口名称：批量创建文档
    接口地址：/proj/$VERSION$/doc/docs
    """
    com = CommonServer()
    token = com.get_token()
    context = commonServer.get_context()
    api_path = commonServer.get_host() + context + apis.get("createAttachDocUsingPOST")
    with open(file_name, 'rb') as file:
        file = {'file': file}
        data = {
            "contextId": context_id,
            "folderId": folder_id,
            "contextType": 1,
        }
        r = requests.post(url=api_path,
                          headers={
                              'Authorization': 'Bearer ' + token,
                          },
                          data=data,
                          files=file
                          )
    apis.check_success(self, r.json())
    return r


def page(self, context_id, folder_id, name, order, order_by_field, page_no, page_size, checker=None):
    """
    接口名称：查询文档分页
    接口地址：/proj/$VERSION$/doc/list
    """
    r = RequestService.call_get(apis.get("pageUsingGET_1", None), params={
        "contextId": context_id,  # 项目id - required: True
        "folderId": folder_id,  # 文件夹id - required: False
        "name": name,  # 文档名称 - required: False
        "order": order,  # 排序(默认升序) - required: False
        "orderByField": order_by_field,  # 排序字段(默认名称) - required: False
        "pageNo": page_no,  # 页码 - required: True
        "pagesize": page_size,  # 每页条数 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def move_document(self, df_id, folder_id, checker=None):
    """
    接口名称：移动文件夹（文档）
    接口地址：/proj/$VERSION$/doc/move
    """
    r = RequestService.call_put(apis.get("moveDocumentUsingPUT", None), json={
        "dfId": df_id,
        "folderId": folder_id,
        "isFolder": "0"  # 文件移动信息 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def search_list(self, order, page_no, page_size, order_by_field, name, context_id, checker=None):
    """
    接口名称：项目文档搜索分页
    接口地址：/proj/$VERSION$/doc/searchlist
    """
    r = RequestService.call_get(apis.get("searchlistUsingGET", None), params={
        "contextId": context_id,  # 项目id - required: True
        "name": name,  # 文档名称 - required: False
        "order": order,  # 排序(默认升序) - required: False
        "orderByField": order_by_field,  # 排序字段(默认名称) - required: False
        "pageNo": page_no,  # 页码 - required: True
        "pagesize": page_size,  # 每页条数 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def upload_attach(self, doc_id, checker=None):
    """
    接口名称：上传文件，支持批量
    接口地址：/proj/$VERSION$/doc/upload
    """
    with open(file_name, 'rb') as file:
        file = {'file': file}
    r = RequestService.call_post(apis.get("uploadAttachUsingPOST_1", None), data={
        "file": file,  # file - required: False
        "main": file,  # main - required: False
    }, params={
        "doc_id": doc_id,  # 文档doc_id - required: True
        "flag": True,  # insertFlag:true/false - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def upload_cover_attach(self, doc_id, file_id):
    """
    接口名称：修改文件
    接口地址：/proj/$VERSION$/doc/upload/cover
    """
    com = CommonServer()
    token = com.get_token()
    context = commonServer.get_context()
    api_path = commonServer.get_host() + context + apis.get("createDocUsingPOST")
    with open(file_name, 'rb') as file:
        file = {'file': file}
        data = {
            "doc_id": doc_id,
            "file_id": file_id
        }
        r = requests.post(url=api_path,
                          headers={
                              'Authorization': "Bearer " + token,
                          },
                          data=data,
                          files=file
                          )
    apis.check_success(self, r.json())
    return r


def query_attlist(self, cid, checker=None):
    """
    接口名称：查询历史版本文件list
    接口地址：/proj/$VERSION$/doc/{cid}/list
    """
    r = RequestService.call_get(apis.get("queryAttListUsingGET", cid), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def doc_history_list(self, doc_id, checker=None):
    """
    接口名称：根据文档id查询该文档历史记录
    接口地址：/proj/$VERSION$/doc/{id}/histories
    """
    r = RequestService.call_get(apis.get("docHistoryListUsingGET", doc_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


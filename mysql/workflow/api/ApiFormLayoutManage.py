from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "add_form_layout": "/workflow/$VERSION$/formlayout",  # 新增、修改表单布局
    "update_form_layout": "/workflow/$VERSION$/formlayout",  # 修改表单布局
    "add_form_layout1": "/workflow/$VERSION$/formlayout/package",  # 新增、修改表单布局(资源包)
    "select_package_file": "/workflow/$VERSION$/formlayout/package/item/download",  # 下载资源文件内容
    "get_form_layout": "/workflow/$VERSION$/formlayout/package/item/filename",  # 获取表单布局(资源包),根据名称路劲获取
    "update_package_file": "/workflow/$VERSION$/formlayout/package/item/update/%s",  # 更新资源文件内容
    "select_package_file1": "/workflow/$VERSION$/formlayout/package/item/%s",  # 下载资源文件内容
    "get_form_layout1": "/workflow/$VERSION$/formlayout/package/layoutId/%s",  # 获取表单布局(资源包中html)
    "get_form_layout2": "/workflow/$VERSION$/formlayout/package/%s",  # 获取表单布局(资源包)
    "query_page_using": "/workflow/$VERSION$/formlayout/page",  # 表单布局分页列表
    "query_layout_proc": "/workflow/$VERSION$/formlayout/page/%s",  # 表单布局绑定的流程定义
    "del_form_layout": "/workflow/$VERSION$/formlayout/%s",  # 删除表单布局
    "query_by_id": "/workflow/$VERSION$/formlayout/%s",  # 根据ID查询表单布局
})


def add_form_layout(self, dto, checker=None):
    """
    接口名称：新增、修改表单布局;    接口地址：/workflow/$VERSION$/formlayout；
    """
    r = RequestService.call_post(apis.get("add_form_layout", None), json=dto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_form_layout(self, dto, checker=None):
    """
    接口名称：修改表单布局;    接口地址：/workflow/$VERSION$/formlayout；
    """
    r = RequestService.call_put(apis.get("update_form_layout", None), json=dto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_form_layout1(self, checker=None):
    """
    接口名称：新增、修改表单布局(资源包);    接口地址：/workflow/$VERSION$/formlayout/package；
    """
    r = RequestService.call_post(apis.get("add_form_layout1", None), data={
        "file": "",  # file - required: True
        "files": "",  # files - required: True
    }, params={
        "category": "",  # 布局分类 - required: False
        "formName": "",  # formName - required: True
        "global": "",  # global - required: True
        "layoutType": "",  # layoutType - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def select_package_file(self, checker=None):
    """
    接口名称：下载资源文件内容;    接口地址：/workflow/$VERSION$/formlayout/package/item/download；
    """
    r = RequestService.call_get(apis.get("select_package_file", None), params={
        "filename": ""  # filename - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_form_layout(self, checker=None):
    """
    接口名称：获取表单布局(资源包),根据名称路劲获取;    接口地址：/workflow/$VERSION$/formlayout/package/item/filename；
    """
    r = RequestService.call_get(apis.get("get_form_layout", None), params={
        "filename": ""  # filename - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_package_file(self, checker=None):
    """
    接口名称：更新资源文件内容;    接口地址：/workflow/$VERSION$/formlayout/package/item/update/{id}；
    """
    r = RequestService.call_put(apis.get("update_package_file", None), json={
        "map": ""  # map - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def select_package_file1(self, checker=None):
    """
    接口名称：下载资源文件内容;    接口地址：/workflow/$VERSION$/formlayout/package/item/{id}；
    """
    r = RequestService.call_get(apis.get("select_package_file1", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_form_layout1(self, checker=None):
    """
    接口名称：获取表单布局(资源包中html);    接口地址：/workflow/$VERSION$/formlayout/package/layoutId/{layoutId}；
    """
    r = RequestService.call_get(apis.get("get_form_layout1", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_form_layout2(self, checker=None):
    """
    接口名称：获取表单布局(资源包);    接口地址：/workflow/$VERSION$/formlayout/package/{itemId}；
    """
    r = RequestService.call_get(apis.get("get_form_layout2", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_page_using(data):
    """
    接口名称：表单布局分页列表;    接口地址：/workflow/$VERSION$/formlayout/page；
    """
    r = RequestService.call_get(apis.get("query_page_using", None), params=data)
    return r


def query_layout_proc(self, layout_id, checker=None):
    """
    接口名称：表单布局绑定的流程定义;    接口地址：/workflow/$VERSION$/formlayout/page/{layoutId}；
    """
    r = RequestService.call_get(apis.get("query_layout_proc", layout_id), params={
        "pageIndex": 1,  # None - required: True
        "pageSize": 20,  # None - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def del_form_layout(self, layout_id, checker=None):
    """
    接口名称：删除表单布局;    接口地址：/workflow/$VERSION$/formlayout/{formLayoutIds}；
    """
    r = RequestService.call_delete(apis.get("del_form_layout", layout_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_by_id(self, layout_id, checker=None):
    """
    接口名称：根据ID查询表单布局;    接口地址：/workflow/$VERSION$/formlayout/{formLayoutId}；
    """
    r = RequestService.call_get(apis.get("query_by_id", layout_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r
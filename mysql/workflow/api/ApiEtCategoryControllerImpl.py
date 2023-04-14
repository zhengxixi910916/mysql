from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "insert_one_using_post": "/workflow/$VERSION$/category/add",  # 新增一条记录
    "update_data_using_put": "/workflow/$VERSION$/category/change/%s",  # 更新一条记录
    "delete_one_using_delete": "/workflow/$VERSION$/category/delete/%s",  # deleteOne
    "get_one_using_get": "/workflow/$VERSION$/category/get/%s",  # getOne
    "query_all_using_get": "/workflow/$VERSION$/category/getAll",  # 查询所有的类型
    "select_all_with_relation_using_get": "/workflow/$VERSION$/category/relation",  # 查询出的类型按照子父关系排好
})


def insert_one_using_post(self, category_dto, checker=None):
    """
    接口名称：新增一条记录
    接口地址：/workflow/$VERSION$/category/add
    """
    r = RequestService.call_post(apis.post("insert_one_using_post", None), json=category_dto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def update_data_using_put(self, category_dto, category_id, checker=None):
    """
    接口名称：更新一条记录
    接口地址：/workflow/$VERSION$/category/change/{id}
    """
    r = RequestService.call_put(apis.get("update_data_using_put", category_id), json=category_dto)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def delete_one_using_delete(self, category_id, checker=None):
    """
    接口名称：deleteOne
    接口地址：/workflow/$VERSION$/category/delete/{id}
    """
    r = RequestService.call_delete(apis.get("delete_one_using_delete", category_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_one_using_get(self, category_id, checker=None):
    """
    接口名称：getOne
    接口地址：/workflow/$VERSION$/category/get/{id}
    """
    r = RequestService.call_get(apis.get("get_one_using_get", category_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def query_all_using_get(self, checker=None):
    """
    接口名称：查询所有的类型
    接口地址：/workflow/$VERSION$/category/getAll
    """
    r = RequestService.call_get(apis.get("query_all_using_get", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def select_all_with_relation_using_get(self, checker=None):
    """
    接口名称：查询出的类型按照子父关系排好
    接口地址：/workflow/$VERSION$/category/relation
    """
    r = RequestService.call_get(apis.get("select_all_with_relation_using_get", None), params={
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

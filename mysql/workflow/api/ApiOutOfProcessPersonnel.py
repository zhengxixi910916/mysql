from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "bind_user_using_post": "/workflow/$VERSION$/view/bind",  # 绑定用户
    "get_bind_user_using_get": "/workflow/$VERSION$/view/{modelKey}",  # 查看绑定得用户
})


def bind_user_using_post(self, category, model_key, user_ids, checker=None):
    """
    接口名称：绑定用户
    接口地址：/workflow/$VERSION$/view/bind
    """
    r = RequestService.call_post(apis.get("bind_user_using_post", None), params={
        "category": category,  # 分类 - required: False
        "modelKey": model_key,  # 模板ID - required: True
        "userIds": user_ids,  # userIds，多个逗号隔开 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def get_bind_user_using_get(self, model_key, category, checker=None):
    """
    接口名称：查看绑定得用户
    接口地址：/workflow/$VERSION$/view/{modelKey}
    """
    r = RequestService.call_get(apis.get("get_bind_user_using_get", None), params={
        "modelKey": model_key,  # 模板ID - required: True
        "category": category  # 分类 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

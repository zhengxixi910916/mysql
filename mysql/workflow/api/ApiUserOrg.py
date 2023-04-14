from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "submit_issue_using": "/workflow/$VERSION$/identity/changeloginuser",  # submitIssue
    "check_user_in": "/workflow/$VERSION$/identity/changeuser",  # 判断用户是否存在流程中
    "query_all_user": "/workflow/$VERSION$/identity/users",  # queryAllUser
})


def submit_issue_using(self, user_id="", checker=None):
    """
    接口名称：submitIssue;    接口地址：/workflow/$VERSION$/identity/changeloginuser；
    """
    r = RequestService.call_get(apis.get("submit_issue_using", None), params={
        "loginUserId": user_id  # 登录用户Id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def check_user_in(self, checker=None):
    """
    接口名称：判断用户是否存在流程中;    接口地址：/workflow/$VERSION$/identity/changeuser；
    """
    r = RequestService.call_get(apis.get("check_user_in", None), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_all_user(self, checker=None):
    """
    接口名称：queryAllUser;    接口地址：/workflow/$VERSION$/identity/users；
    """
    r = RequestService.call_get(apis.get("query_all_user", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

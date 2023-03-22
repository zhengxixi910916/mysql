from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
需求统计
'''
apis = Api({
    "getRequiresUsingGET_1": "/req/$VERSION$/requires/count",  # 根据项目ID统计需求相关数量
})


def getRequiresUsingGET_1(self, checker):
    """
    接口名称：根据项目ID统计需求相关数量
    接口地址：/req/$VERSION$/requires/count
    """
    r = RequestService.call_get(apis.get("getRequiresUsingGET_1", None), params={
        "business_type": "",  # 需求类型 - required: False
        "label_id": "",  # 标签id - required: False
        "member_id": "",  # 责任人id - required: False
        "projectId": "",  # 项目id - required: True
        "reqSource ": "",  # 需求来源 - required: False
        "state": "",  # 需求状态 - required: False
        "submitter_id": "",  # 提出人id - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

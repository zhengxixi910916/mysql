from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
任务统计
'''
apis = Api({
    "get_statistic_members": "/plan/$VERSION$/statistic/members",  # 查询统计人员列表
    "get_worksummary": "/plan/$VERSION$/statistic/%s/worksummary",  # 成员个人工作总结统计报表
})


def get_statistic_members(self):
    """
    接口名称：查询统计人员列表
    接口地址：/plan/$VERSION$/statistic/members
    """
    r = RequestService.call_get(apis.get("get_statistic_members"))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_worksummary(self, user_id, date):
    """
    接口名称：成员个人工作总结统计报表
    接口地址：/plan/$VERSION$/statistic/{userId}/worksummary
    """
    r = RequestService.call_get(apis.get("get_worksummary", user_id), params={
        "date": date  # 日期，年-月（yyyy-MM格式） - required: True
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r

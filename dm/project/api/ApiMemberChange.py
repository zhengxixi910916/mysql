from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
"""
项目成员替换历史查询
"""
apis = Api({
    "get_member_change_data": "/proj/$VERSION$/change/member/%s",  # 项目成员替换历史查询
})


def get_member_change_data(self, project_id, page_index=1, page_size=50):
    """
    接口名称：项目成员替换历史查询
    接口地址：/proj/$VERSION$/change/member/{id}
    """
    r = RequestService.call_get(apis.get("get_member_change_data", project_id), params={
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

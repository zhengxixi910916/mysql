from workflow.api import ApiTools as ApiTools
from erdcloud.erdApi import Api

apis = Api({
    "pageQuery_launchRecord": "/workflow/$VERSION$/dynamic/api/common/pageQuery/launchRecord/20/1",  # 获取任务类型
})


def pageQuery_launchRecord():
    # 查询我发起的列表
    apis.get('pageQuery_launchRecord', None)
    data = {"pageSize": 20, "currentPage": 1, "dynamicCondition": [], "orders": [], "keyword": ""}
    api = '/workflow/v1/dynamic/api/common/pageQuery/launchRecord/20/1'
    return ApiTools.call(method='POST', api=api, json=data)

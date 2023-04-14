import time

from workflow.api import ApiTools as ApiTools
from erdcloud.erdApi import Api

apis = Api({
    "pageQuery_model_zids": "/workflow/$VERSION$/dynamic/api/common/pageQuery/launchRecord/pageSize/pageIndex",  # 分页查询流程模板
    "checkedout_model":"/workflow/v1/procmodel/checkedout/model/%s", #检出模板
})


def pageQuery_model():
    """
    接口名称：查询模板列表;
    接口地址：/workflow/$VERSION$/dynamic/api/common/pageQuery/launchRecord/pageSize/pageIndex；
    """
    apis.get('pageQuery_model_zids',None)
    data = {"pageSize": 20, "currentPage": 1, "dynamicCondition": [], "orders": [], "keyword": ""}
    api = '/workflow/v1/dynamic/api/common/pageQuery/launchRecord/20/1'
    return ApiTools.call(method='POST', api=api, json=data)

def checkedout_model(id):
    """
    接口名称：检出模板像;
    接口地址：/workflow/v1/procmodel/checkedout/model/%s；
    """
    apis.get('checkedout_model', None)
    data = {"_": int(time.time())}
    print(data)
    api = f'/workflow/v1/procmodel/checkedout/model/{id}'
    return ApiTools.call(method='GET', api=api, params=data)
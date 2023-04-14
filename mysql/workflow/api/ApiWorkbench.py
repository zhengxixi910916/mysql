import time
from workflow.api import ApiTools as ApiTools
import requests
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "enums_TaskTypeEnum": "/workflow/$VERSION$/dynamic/api/status/enums/TaskTypeEnum",  # 获取任务类型
    "columns_launchRecord": "/workflow/$VERSION$/dynamic/api/columns/launchRecord",  # 获取各列的判断条件
    "count_completed": "/workflow/$VERSION$/procinst/submitted/status/count/completed",  # 获取状态为已完成的任务的数量
    "count_running":"/workflow/$VERSION$/procinst/submitted/status/count/running",#获取状态为进行中的任务的数量
    "count_suspended":"/workflow/$VERSION$/procinst/submitted/status/count/suspended",#获取状态为挂起的任务的数量
    "columns_groupCode":"/workflow/$VERSION$/dynamic/api/columns/todoList",#属性配置下拉框查询
    "pageQuery_groupCode":"/workflow/$VERSION$/dynamic/api/common/pageQuery/launchRecord/20/1",#-公共分页查询api
})


def enums_TaskTypeEnum():
    """
    获取任务类型
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/dynamic/api/status/enums/TaskTypeEnum"
    apis.get("enums_TaskTypeEnum", None)
    r = requests.request("GET", url=url, headers=headers, params={'_': int(time.time())})
    return r.json()


def columns_launchRecord():
    """
    获取各列的判断条件
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/dynamic/api/columns/launchRecord"
    apis.get("columns_launchRecord", None)
    r = requests.request("GET", url=url, headers=headers, params={'_': int(time.time())})
    return r.json()


def count_completed():
    """
    入口:工作台-我发起的
    名称:获取状态为已完成的任务的数量
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/procinst/submitted/status/count/completed"
    apis.get("count_completed", None)
    r = requests.request("GET", url=url, headers=headers, params={'_': int(time.time())})
    return r.json()


def count_running():
    """
    入口:工作台-我发起的
    名称:获取状态为进行中的任务的数量
    """
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/procinst/submitted/status/count/running"
    apis.get("count_running", None)
    r = requests.request("GET", url=url, headers=headers, params={'_': int(time.time())})
    return r.json()


def count_suspended():
    """
    入口:工作台-我发起的
    名称:获取状态为挂起的任务的数量
    """
    apis.get("count_suspended", None)
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/procinst/submitted/status/count/suspended"
    r = requests.request("GET", url=url, headers=headers, params={'_': int(time.time())})
    return r.json()


def columns_groupCode():
    """
    接口名称：属性配置下拉框查询; 接口地址：/workflow/v1/dynamic/api/columns/{groupCode}；
    """
    apis.get("columns_groupCode", None)
    host, headers = ApiTools.getHostAndHeaders()
    url = host + "/workflow/v1/dynamic/api/columns/todoList"
    print(url)
    r = requests.request("GET", url=url, headers=headers, params={'_': int(time.time())})
    return r.json()


def pageQuery_groupCode(groupCode='launchRecord'):
    """
    接口名称：公共分页查询api;    接口地址：/workflow/v1/dynamic/api/common/pageQuery/launchRecord/20/1；
    """

    data = {"pageSize": 20, "currentPage": 1, "dynamicCondition": [], "orders": [], "keyword": ""}
    host, headers = ApiTools.getHostAndHeaders()
    # apis.get("pageQuery_groupCode", None)
    apis.post(key="pageQuery_groupCode")
    url = host + f"/workflow/v1/dynamic/api/common/pageQuery/{groupCode}/20/1"
    r = requests.request("POST", url=url, headers=headers, json=data)
    return r.json()

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目Dashboard统计信息
'''
apis = Api({
    "get_proj_state": "/proj/$VERSION$/dashboard/project/state",  # 获取项目状态分布
    "select_proj_state": "/proj/$VERSION$/dashboard/project/taskstate",  # 获取项目状态
    "get_proj_type": "/proj/$VERSION$/dashboard/project/type",  # 获取项目类型分布
    "get_proj_oneself": "/proj/$VERSION$/dashboard/workbench",  # 工作台个人工作项目总数
    "get_proj_progress": "/proj/$VERSION$/dashboard/%s/progress",  # 获取项目进度
    "get_proj_id_created_resolved": "/proj/$VERSION$/dashboard/%s/created/resolved",  # 根据项目ID查询业务的created&resolved情况
})


def get_proj_state(self):
    """
    接口名称：获取项目状态分布
    接口地址：/proj/$VERSION$/dashboard/project/state
    """
    r = RequestService.call_get(apis.get("get_proj_state"))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def select_proj_state(self, limit):
    """
    接口名称：获取项目状态
    接口地址：/proj/$VERSION$/dashboard/project/taskstate
    """
    r = RequestService.call_get(apis.get("select_proj_state"), params={
        "limit": limit  # 任务数据条数 - required: True
    })
    apis.check_success(self, r)
    # if limit is not None:
    #     self.assertEqual(limit, r["res"]["data"])
    return r['res']["data"]


def get_proj_type(self):
    """
    接口名称：获取项目类型分布
    接口地址：/proj/$VERSION$/dashboard/project/type
    """
    r = RequestService.call_get(apis.get("get_proj_type"))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_proj_oneself(self):
    """
    接口名称：工作台个人工作项目总数
    接口地址：/proj/$VERSION$/dashboard/workbench
    """
    r = RequestService.call_get(apis.get("get_proj_oneself"))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_proj_progress(self, eid):
    """
    接口名称：获取项目进度
    接口地址：/proj/$VERSION$/dashboard/{ids}/progress
    """
    r = RequestService.call_get(apis.get("get_proj_progress", eid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_proj_id_created_resolved(self, eid, object=None, startDate=None):
    """
    接口名称：根据项目ID查询业务的created&resolved情况
    接口地址：/proj/$VERSION$/dashboard/{id}/created/resolved
    """
    r = RequestService.call_get(apis.get("get_proj_id_created_resolved", eid), params={
        "object": object,  # 业务对象(require,issue,task,risk) - required: False
        "startDate": startDate,  # 统计开始时间(yyyy-MM-dd) - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r

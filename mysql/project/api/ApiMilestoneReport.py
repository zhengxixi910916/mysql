from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
里程碑达成率统计/里程碑报表
'''
apis = Api({
    "getProjectByTypeUsingGET": "/plan/$VERSION$/getProjectByType",  # 通过里程碑的名称获取项目
    "getTaskByproject_idsUsingGET": "/plan/$VERSION$/getTaskByprojectIds",  # 通过项目id获取里程碑数据
    "milestoneAchievementRateUsingGET": "/plan/$VERSION$/milestoneAchievementRate",  # 里程碑达成率统计
    "getPublishMilestoneUsingGET": "/plan/$VERSION$/%s/baseline/milestone",  # 通过项目获取立项里程碑数据
})


def getProjectByTypeUsingGET(self, pmId, department, dimension, statsType, departdimension, startDate, endDate,
                             type, name, page_size, page_index, checker=None):
    """
    接口名称：通过里程碑的名称获取项目
    接口地址：/plan/$VERSION$/getProjectByType
    """
    r = RequestService.call_get(apis.get("getProjectByTypeUsingGET", None), params={
        "pmId": pmId,
        "department": department,
        "dimension": dimension,
        "statsType": statsType,
        "departdimension": departdimension,
        "startDate": startDate,
        "endDate": endDate,
        "type": type,
        "name": name,
        "pagesize": page_size,
        "pageindex": page_index

    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getTaskByproject_idsUsingGET(self, checker=None):
    """
    接口名称：通过项目id获取里程碑数据
    接口地址：/plan/$VERSION$/getTaskByprojectIds
    """
    r = RequestService.call_get(apis.get("getTaskByproject_idsUsingGET", None), params={
        # "departdimension": departdimension,  # 部门查询维度 - required: False
        # "department": department,  # 部门 - required: False
        # "dimension": dimension,  # 维度 - required: False
        # "endDate": endDate,  # 结束时间 - required: False
        # "ext": ext,  # 扩展条件 - required: False
        # "filter": filter,  # 过滤规则，&filter=id_L_3_EQ_OR_,name_S_张三_EQ_OR_,name_S_李四_EQ_OR_ - required: False
        # "name": name,  # 里程碑的名称 - required: False
        # "orderBy": orderBy,  # 排序，默认createTime_desc - required: False
        # "pageindex": page_index,  # 页数，默认1 - required: False
        # "pagesize": page_size,  # 每页条数，默认10 - required: False
        # "pmId": pmId,  # 项目经理Id - required: False
        # "projectId": project_id,  # 项目id - required: False
        # "startDate": startDate,  # 开始时间 - required: False
        # "statsType": statsType,  # 里程碑的状态类型 - required: False
        # "type": type,  # 通过里程碑查询项目表示 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def milestoneAchievementRateUsingGET(self, pmId, department, dimension, statsType, departdimension, startDate, endDate,
                                     checker=None):
    """
    接口名称：里程碑达成率统计
    接口地址：/plan/$VERSION$/milestoneAchievementRate
    """
    r = RequestService.call_get(apis.get("milestoneAchievementRateUsingGET", None), params={
        "pmId": pmId,
        "department": department,
        "dimension": dimension,
        "statsType": statsType,
        "departdimension": departdimension,
        "startDate": startDate,
        "endDate": endDate

    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getPublishMilestoneUsingGET(self, project_id, checker=None):
    """
    接口名称：通过项目获取立项里程碑数据
    接口地址：/plan/$VERSION$/{project_id}/baseline/milestone
    """
    r = RequestService.call_get(apis.get("getPublishMilestoneUsingGET", project_id), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r

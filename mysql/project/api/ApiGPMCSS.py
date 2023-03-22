from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
获取项目成员完成状况统计
'''
apis = Api({
    "exportMemberCompletionStatusUsingGET": "/plan/$VERSION$/exportMemberCompletionStatus",  # 导出项目概况统计报表
    "getMemberCompletionDataUsingGET": "/plan/$VERSION$/getMemberCompletionData",  # 点击报表统计数量，查询数据
    "getMemberCompletionStatusUsingGET": "/plan/$VERSION$/getMemberCompletionStatus",  # 获取项目成员完成状况
    "getMemberCompletionStatusDetailsUsingGET": "/plan/$VERSION$/getMemberCompletionStatus/details",  # 获取项目成员完成情况详情
})


def exportMemberCompletionStatusUsingGET(self, checker):
    """
    接口名称：导出项目概况统计报表
    接口地址：/plan/$VERSION$/exportMemberCompletionStatus
    """
    r = RequestService.call_get(apis.get("exportMemberCompletionStatusUsingGET", None), params={
        "endDate": "",  # 结束时间 - required: False
        "orgId": "",  # 组织部门id - required: False
        "project_ids": "",  # 项目ids - required: False
        "startDate": "",  # 开始时间 - required: False
        "taskName": "",  # 任务名称 - required: False
        "type": "",  # 查看的数量的类型，新增，待完成，已延期，已完成 - required: False
        "userId": "",  # 责任人 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getMemberCompletionDataUsingGET(self, endDate, orgId, project_ids, startDate, taskName,
                                    type,  userId, checker=None):
    """
    接口名称：点击报表统计数量，查询数据
    接口地址：/plan/$VERSION$/getMemberCompletionData
    """
    r = RequestService.call_get(apis.get("getMemberCompletionDataUsingGET", None), params={
        "endDate": endDate,  # 结束时间 - required: False
        "orgId": orgId,  # 组织部门id - required: False
        "project_ids": project_ids,  # 项目ids - required: False
        "startDate": startDate,  # 开始时间 - required: False
        "taskName": taskName,  # 任务名称 - required: False
        "type": type,  # 查看的数量的类型，新增，待完成，已延期，已完成 - required: False
        "userId": userId,  # 责任人 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getMemberCompletionStatusUsingGET(self, userId, project_ids, taskName, orgId, startDate, endDate, checker=None):
    """
    接口名称：获取项目成员完成状况
    接口地址：/plan/$VERSION$/getMemberCompletionStatus
    """
    r = RequestService.call_get(apis.get("getMemberCompletionStatusUsingGET", None), params={
        "endDate": endDate,  # 结束时间 - required: False
        "orgId": orgId,  # 组织部门id - required: False
        "project_ids": project_ids,  # 项目ids - required: False
        "startDate": startDate,  # 开始时间 - required: False
        "taskName": taskName,  # 任务名称 - required: False
        "type": type,  # 查看的数量的类型，新增，待完成，已延期，已完成 - required: False
        "userId": userId,  # 责任人 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getMemberCompletionStatusDetailsUsingGET(self, userId, project_ids, taskName, orgId, startDate,
                                             page_index, page_size, endDate, checker=None):
    """
    接口名称：获取项目成员完成情况详情
    接口地址：/plan/$VERSION$/getMemberCompletionStatus/details
    """
    r = RequestService.call_get(apis.get("getMemberCompletionStatusDetailsUsingGET", None), params={
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
        "endDate": endDate,  # 结束时间 - required: False
        "orgId": orgId,  # 组织部门id - required: False
        "project_ids": project_ids,  # 项目ids - required: False
        "startDate": startDate,  # 开始时间 - required: False
        "taskName": taskName,  # 任务名称 - required: False
        "type": type,  # 查看的数量的类型，新增，待完成，已延期，已完成 - required: False
        "userId": userId,  # 责任人 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

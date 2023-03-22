from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
问题报表
'''
apis = Api({
    "classified_statistics": "/issue/$VERSION$/classifiedStatistics",  # 问题分类统计
    "closing_rate": "/issue/$VERSION$/closingRate",  # 问题关闭率
    "improvement_time_statistics": "/issue/$VERSION$/improvementTimeStatistics",  # 解析改善时间统计
    "overdue_closed_statistics": "/issue/$VERSION$/overdueNotClosedStatistics",  # 超期未关闭
    "issue_risk_statistics": "/issue/$VERSION$/riskStatistics",  # 问题的风险统计 （高中低）
})


def classified_statistics(self,
                          dimension=None,
                          endDate=None,
                          endFinishDate=None,
                          ext=None,
                          finishDate=None,
                          project_ids=None,
                          projectType=None,
                          startDate=None,
                          startFinishDate=None,
                          state=None,
                          type=None
                          ):
    """
    接口名称：问题分类统计
    接口地址：/issue/$VERSION$/classifiedStatistics
    """
    r = RequestService.call_get(apis.get("classified_statistics"), params={
        "dimension": dimension,  # 维度 - required: False
        "endDate": endDate,  # 结束时间 - required: False
        "endFinishDate": endFinishDate,  # None - required: False
        "ext": ext,  # 扩展条件 - required: False
        "finishDate": finishDate,  # 自定义时间类 - required: False
        "project_ids": project_ids,  # 项目ids - required: False
        "projectType": projectType,  # 项目类型 - required: False
        "startDate": startDate,  # 开始时间 - required: False
        "startFinishDate": startFinishDate,  # None - required: False
        "state": state,  # 问题状态 - required: False
        "type": type  # 问题类型 - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def closing_rate(self,
                 dimension,
                 endDate,
                 startDate,
                 state,
                 endFinishDate=None,
                 ext=None,
                 finishDate=None,
                 project_ids=None,
                 projectType=None,
                 startFinishDate=None,
                 type=None
                 ):
    """
    接口名称：问题关闭率
    接口地址：/issue/$VERSION$/closingRate
    """
    r = RequestService.call_get(apis.get("closing_rate"), params={
        "dimension": dimension,  # 维度 - required: False
        "endDate": endDate,  # 结束时间 - required: False
        "endFinishDate": endFinishDate,  # None - required: False
        "ext": ext,  # 扩展条件 - required: False
        "finishDate": finishDate,  # 自定义时间类 - required: False
        "project_ids": project_ids,  # 项目ids - required: False
        "projectType": projectType,  # 项目类型 - required: False
        "startDate": startDate,  # 开始时间 - required: False
        "startFinishDate": startFinishDate,  # None - required: False
        "state": state,  # 问题状态 - required: False
        "type": type,  # 问题类型 - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def improvement_time_statistics(self,
                                dimension=None,
                                endDate=None,
                                endFinishDate=None,
                                ext=None,
                                finishDate=None,
                                project_ids=None,
                                projectType=None,
                                startDate=None,
                                startFinishDate=None,
                                state=None,
                                type=None
                                ):
    """
    接口名称：解析改善时间统计
    接口地址：/issue/$VERSION$/improvementTimeStatistics
    """
    r = RequestService.call_get(apis.get("improvement_time_statistics"),   params={
        "dimension": dimension,  # 维度 - required: False
        "endDate": endDate,  # 结束时间 - required: False
        "endFinishDate": endFinishDate,  # None - required: False
        "ext": ext,  # 扩展条件 - required: False
        "finishDate": finishDate,  # 自定义时间类 - required: False
        "project_ids": project_ids,  # 项目ids - required: False
        "projectType": projectType,  # 项目类型 - required: False
        "startDate": startDate,  # 开始时间 - required: False
        "startFinishDate": startFinishDate,  # None - required: False
        "state": state,  # 问题状态 - required: False
        "type": type,  # 问题类型 - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def overdue_closed_statistics(self,
                              dimension=None,
                              endDate=None,
                              endFinishDate=None,
                              ext=None,
                              finishDate=None,
                              project_ids=None,
                              projectType=None,
                              startDate=None,
                              startFinishDate=None,
                              state=None,
                              type=None
                              ):
    """
    接口名称：超期未关闭
    接口地址：/issue/$VERSION$/overdueNotClosedStatistics
    """
    r = RequestService.call_get(apis.get("overdue_closed_statistics"),  params={
        "dimension": dimension,  # 维度 - required: False
        "endDate": endDate,  # 结束时间 - required: False
        "endFinishDate": endFinishDate,  # None - required: False
        "ext": ext,  # 扩展条件 - required: False
        "finishDate": finishDate,  # 自定义时间类 - required: False
        "project_ids": project_ids,  # 项目ids - required: False
        "projectType": projectType,  # 项目类型 - required: False
        "startDate": startDate,  # 开始时间 - required: False
        "startFinishDate": startFinishDate,  # None - required: False
        "state": state,  # 问题状态 - required: False
        "type": type,  # 问题类型 - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def issue_risk_statistics(self,
                          dimension=None,
                          endDate=None,
                          endFinishDate=None,
                          ext=None,
                          finishDate=None,
                          project_ids=None,
                          projectType=None,
                          startDate=None,
                          startFinishDate=None,
                          state=None,
                          type=None
                          ):
    """
    接口名称：问题的风险统计 （高中低）
    接口地址：/issue/$VERSION$/riskStatistics
    """
    r = RequestService.call_get(apis.get("issue_risk_statistics"), params={
        "dimension": dimension,  # 维度 - required: False
        "endDate": endDate,  # 结束时间 - required: False
        "endFinishDate": endFinishDate,  # None - required: False
        "ext": ext,  # 扩展条件 - required: False
        "finishDate": finishDate,  # 自定义时间类 - required: False
        "project_ids": project_ids,  # 项目ids - required: False
        "projectType": projectType,  # 项目类型 - required: False
        "startDate": startDate,  # 开始时间 - required: False
        "startFinishDate": startFinishDate,  # None - required: False
        "state": state,  # 问题状态 - required: False
        "type": type,  # 问题类型 - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

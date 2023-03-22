from erdcloud import CommonServer
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "getAllProjectScoresUsingGET": "/decision/$VERSION$/all/project/{portfolioId}/score",  # 获取项目组合下所有项目提案的评分
    "updateProposalDecisionUsingPUT": "/decision/$VERSION$/project",  # 设置决策结论
    "userEvaluateScoreStartNotifyUsingPOST": "/decision/$VERSION$/project/score/end",  # 流程评分结束调用
    "addUsingPOST_1": "/decision/$VERSION$/project/%s",  # 添加项目组合关联关系
    "getscoresUsingGET": "/decision/$VERSION$/project/{portfolioId}/score",  # 获取项目机会评分
    "getuserscoresUsingGET": "/decision/$VERSION$/project/{portfolioId}/userscore",  # 获取当前登录人的项目机会评分
    "deleteLinkUsingDELETE": "/decision/$VERSION$/project/{portfolioId}/{project_id}",  # 删除项目组合关联关系
    "addscoresUsingPOST": "/decision/$VERSION$/project/{portfolioId}/{project_id}/score",  # 新增项目机会评分
    "savescoresUsingPUT": "/decision/$VERSION$/project/{portfolioId}/{project_id}/score",  # 修改项目机会评分
    "getScoreByproject_idUsingGET": "/decision/$VERSION$/project_id/score",  # 获取单个项目机会评分
    "editscoresUsingPUT": "/decision/$VERSION$/update/project/{portfolioId}/score",  # 调整项目机会评分
    "projectsUsingGET_1": "/decision/$VERSION$/{portfolioId}/projects",  # 查询组合下项目机会列表
    "getscorelistUsingGET": "/decision/$VERSION$/{portfolioId}/score",  # 获取项目机会评分汇总
    "addProjectUsingPOST_1": "/proj/$VERSION$/project",  # 新建项目提案
})


def getAllProjectScoresUsingGET(self, checker=None):
    """
    接口名称：获取项目组合下所有项目提案的评分
    接口地址：/decision/$VERSION$/all/project/{portfolioId}/score
    """
    r = RequestService.call_get(apis.get("getAllProjectScoresUsingGET", None), path={
        "portfolioId": ""  # 组合id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def updateProposalDecisionUsingPUT(self, checker=None):
    """
    接口名称：设置决策结论
    接口地址：/decision/$VERSION$/project
    """
    r = RequestService.call_put(apis.get("updateProposalDecisionUsingPUT", None), json={
        "project": ""  # 项目提案信息 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def userEvaluateScoreStartNotifyUsingPOST(self, checker=None):
    """
    接口名称：流程评分结束调用
    接口地址：/decision/$VERSION$/project/score/end
    """
    r = RequestService.call_post(apis.get("userEvaluateScoreStartNotifyUsingPOST", None), json={
        "params": ""  # 流程业务对象 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def addUsingPOST_1(self, checker=None, portfolioId=None, score_id=None):
    """
    接口名称：添加项目组合关联关系
    接口地址：/decision/$VERSION$/project/{portfolioId}
    """
    r = RequestService.call_post(apis.get("addUsingPOST_1", portfolioId), json={
        "id": score_id
    }
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getscoresUsingGET(self, checker=None):
    """
    接口名称：获取项目机会评分
    接口地址：/decision/$VERSION$/project/{portfolioId}/score
    """
    r = RequestService.call_get(apis.get("getscoresUsingGET", None), params={
        "procInstId": "",  # 项目id - required: False
        "projectId": "",  # 项目id - required: False
        "userId": "",  # 项目id - required: False
    }, path={
        "portfolioId": ""  # 组合id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getuserscoresUsingGET(self, checker=None):
    """
    接口名称：获取当前登录人的项目机会评分
    接口地址：/decision/$VERSION$/project/{portfolioId}/userscore
    """
    r = RequestService.call_get(apis.get("getuserscoresUsingGET", None), params={
        "projectId": ""  # 项目id - required: False
    }, path={
        "portfolioId": ""  # 组合id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def deleteLinkUsingDELETE(self, checker=None):
    """
    接口名称：删除项目组合关联关系
    接口地址：/decision/$VERSION$/project/{portfolioId}/{project_id}
    """
    r = RequestService.call_delete(apis.get("deleteLinkUsingDELETE", None), path={
        "portfolioId": "",  # 组合Id - required: True
        "projectId": "",  # 项目机会id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def addscoresUsingPOST(self, checker=None):
    """
    接口名称：新增项目机会评分
    接口地址：/decision/$VERSION$/project/{portfolioId}/{project_id}/score
    """
    r = RequestService.call_post(apis.get("addscoresUsingPOST", None), params={
        "createBy": "",  # 创建者 - required: False
        "createTime": "",  # 创建时间 - required: False
        "delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "id": "",  # 对象Id - required: False
        "projectEvaluateScore[0].createBy": "",  # 创建者 - required: False
        "projectEvaluateScore[0].createTime": "",  # 创建时间 - required: False
        "projectEvaluateScore[0].delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "projectEvaluateScore[0].id": "",  # 对象Id - required: False
        "projectEvaluateScore[0].indElemId": "",  # 指标要素id - required: False
        "projectEvaluateScore[0].portfolioId": "",  # 组合id - required: False
        "projectEvaluateScore[0].processInstanceId": "",  # 流程实例id - required: False
        "projectEvaluateScore[0].project_id": "",  # 项目id - required: False
        "projectEvaluateScore[0].score": "",  # 评分 - required: False
        "projectEvaluateScore[0].scoreUserId": "",  # 评分用户Id - required: False
        "projectEvaluateScore[0].scoreUserName": "",  # 评分用户名 - required: False
        "projectEvaluateScore[0].updateBy": "",  # 更新者 - required: False
        "projectEvaluateScore[0].updateTime": "",  # 更新时间 - required: False
        "updateBy": "",  # 更新者 - required: False
        "updateTime": "",  # 更新时间 - required: False
    }, path={
        "portfolioId": "",  # 组合id - required: True
        "projectId": "",  # 项目id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def savescoresUsingPUT(self, checker=None):
    """
    接口名称：修改项目机会评分
    接口地址：/decision/$VERSION$/project/{portfolioId}/{project_id}/score
    """
    r = RequestService.call_put(apis.get("savescoresUsingPUT", None), json={
        "projectEvaluateScore": ""  # 项目评分对象 - required: False
    }, path={
        "portfolioId": "",  # 项目组合id - required: True
        "projectId": "",  # 项目id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getScoreByproject_idUsingGET(self, checker=None):
    """
    接口名称：获取单个项目机会评分
    接口地址：/decision/$VERSION$/project_id/score
    """
    r = RequestService.call_get(apis.get("getScoreByproject_idUsingGET", None), params={
        "portfolioId": "",  # 项目组合id - required: True
        "projectId": "",  # 项目id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def editscoresUsingPUT(self, checker=None):
    """
    接口名称：调整项目机会评分
    接口地址：/decision/$VERSION$/update/project/{portfolioId}/score
    """
    r = RequestService.call_put(apis.get("editscoresUsingPUT", None), json={
        "projectEvaluateScore": ""  # 项目评分对象 - required: False
    }, path={
        "portfolioId": ""  # 项目组合id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def projectsUsingGET_1(self, checker=None):
    """
    接口名称：查询组合下项目机会列表
    接口地址：/decision/$VERSION$/{portfolioId}/projects
    """
    r = RequestService.call_get(apis.get("projectsUsingGET_1", None), path={
        "portfolioId": ""  # 项目组合ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getscorelistUsingGET(self, checker=None):
    """
    接口名称：获取项目机会评分汇总
    接口地址：/decision/$VERSION$/{portfolioId}/score
    """
    r = RequestService.call_get(apis.get("getscorelistUsingGET", None), path={
        "portfolioId": ""  # 组合id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def addProjectUsingPOST_1(self, checker=None, proposal_name=None):
    """
    接口名称：新增项目提案
    接口地址：/proj/$VERSION$/project
    """
    com = CommonServer()
    token = com.get_token()
    r = RequestService.call_post(apis.get("addProjectUsingPOST_1"),
                                 data=
                                 {
                                     "name": proposal_name,
                                     "description": "<p>description</p>",
                                     "1645609422341-4": '',
                                     "state": "SKETCH",
                                     "decisionState": "PENDINGANALYSIS",
                                     "flexAttrs[decisionState]": "PENDINGANALYSIS",
                                     "flexAttrs[decisionMaking]": '',
                                     "decisionMaking": '',
                                     "budget": '',
                                     "workload": '',
                                     "startTime": "2022-02-22T00:00:00.000Z",
                                     "finishTime": "2022-02-28T00:00:00.000Z",
                                     "pmId": "SYS_E39B20EA11E7A81AC85B767C89C1",
                                     "contextType": "Portfolio",
                                     "pmIds[0]": "SYS_E39B20EA11E7A81AC85B767C89C1"
                                 },
                                 headers={
                                     'Authorization': "Bearer " + token,
                                     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                 }
                                 )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r

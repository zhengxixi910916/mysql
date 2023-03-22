from erdcloud.HttpClient import RequestService, commonServer
from erdcloud.erdApi import Api

apis = Api({
    "create_portfolio": "/portfolio/$VERSION$/portfolio",  # 新增组合
    "update_portfolio": "/portfolio/$VERSION$/portfolio",  # 修改组合基本信息
    "archive_portfolio": "/portfolio/$VERSION$/portfolio/archive/%s",  # 项目组合归档
    "get_archives": "/portfolio/$VERSION$/portfolio/archives/%s",  # 查询用户归档项目组合
    "add_attention": "/portfolio/$VERSION$/portfolio/attention",  # 添加关注/收藏/打开对象
    "cancel_attention": "/portfolio/$VERSION$/portfolio/attention",  # 取消关注/收藏/打开对象
    "get_attentions": "/portfolio/$VERSION$/portfolio/attentions",  # 查询用户关注/收藏/打开对象
    "get_candidates": "/portfolio/$VERSION$/portfolio/candidates",  # 查询候选项目
    "search_proj_prog": "/portfolio/$VERSION$/portfolio/paramsearch",  # 根据Code、名称查询项目群、项目
    "add_subs_proj": "/portfolio/$VERSION$/portfolio/subs/%s",  # 添加、移除项目
    "get_portfolio_tree": "/portfolio/$VERSION$/portfolio/tree/%s",  # 查询组合树
    "get_portfolio_by_id": "/portfolio/$VERSION$/portfolio/%s",  # 查询单个项目组合详情
    "delete_portfolio": "/portfolio/$VERSION$/portfolio/%s",  # 删除组合
    "get_portfolio_proj": "/portfolio/$VERSION$/portfolio/%s/projects",  # 查询组合名下所有项目列表
    "get_portfolio_list": "/portfolio/$VERSION$/portfolios",  # 查询项目组合
    "get_all_portfolio": "/portfolio/$VERSION$/portfolios/all",  # 查询所有项目组合
    "get_page_portfolio": "/portfolio/$VERSION$/portfolios/all/page",  # 查询所有项目组合列表分页
    "selectFilterListUsingPOST_2": "/portfolio/$VERSION$/portfolios/filterlist",  # 过滤业务数据

    "getAllProjectScoresUsingGET": "/decision/$VERSION$/all/project/%s/score",  # 获取项目组合下所有项目提案的评分
    "updateProposalDecisionUsingPUT": "/decision/$VERSION$/project",  # 设置决策结论
    "userEvaluateScoreStartNotifyUsingPOST": "/decision/$VERSION$/project/score/end",  # 流程评分结束调用
    "addUsingPOST_1": "/decision/$VERSION$/project/%s",  # 添加项目组合关联关系
    "getscoresUsingGET": "/decision/$VERSION$/project/%s/score",  # 获取项目机会评分
    "getuserscoresUsingGET": "/decision/$VERSION$/project/%s/userscore",  # 获取当前登录人的项目机会评分
    "deleteLinkUsingDELETE": "/decision/$VERSION$/project/%s/%s",  # 删除项目组合关联关系
    "addscoresUsingPOST": "/decision/$VERSION$/project/%s/%s/score",  # 新增项目机会评分
    "savescoresUsingPUT": "/decision/$VERSION$/project/%s/%s/score",  # 修改项目机会评分
    "getScoreByproject_idUsingGET": "/decision/$VERSION$/project_id/score",  # 获取单个项目机会评分
    "editscoresUsingPUT": "/decision/$VERSION$/update/project/%s/score",  # 调整项目机会评分
    "projectsUsingGET_1": "/decision/$VERSION$/%s/projects",  # 查询组合下项目机会列表
    "getscorelistUsingGET": "/decision/$VERSION$/%s/score",  # 获取项目机会评分汇总
})


def create_portfolio(self, name, strategyGoalId):
    """
    接口名称：新增组合
    接口地址：/portfolio/$VERSION$/portfolio
    """
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer " + commonServer.get_token()
    }
    r = RequestService.call_post(apis.get("create_portfolio"), json={
        "name": name,
        "departmentId": "SYS_2d28fff04a3da56f410a241528b4",
        "portfolioManagerId": "SYS_E39B20EA11E7A81AC85B767C89C1",
        "strategyGoalId": strategyGoalId,
        "startTime": "2023-03-01",
        "finishTime": "2030-07-01",
        "budget": "21", "description": "21212", "isArchived": 0},
        headers=headers)
    apis.check_success(self, r)

    return r['res']["data"]


def update_portfolio(self, portfolioId, name):
    """
    接口名称：修改组合基本信息
    接口地址：/portfolio/$VERSION$/portfolio
    """
    r = RequestService.call_put(apis.get("update_portfolio"), json={
        "code": "PORT2022015",
        "name": name,
        "departmentId": "SYS_2d28fff04a3da56f410a241528b4",
        "portfolioManagerId": "SYS_E39B20EA11E7A81AC85B767C89C1",
        "strategyGoalId": "2ab83ec845d0292431ecf6b84834c248",
        "startTime": "2022-11-23",
        "finishTime": "2030-11-26",
        "budget": "1.00",
        "description": "1",
        "flexAttrs": {},
        "id": portfolioId
    }, )
    apis.check_success(self, r)
    return r['res']["data"]


def archive_portfolio(self, portfolioId):
    """
    接口名称：项目组合归档
    接口地址：/portfolio/$VERSION$/portfolio/archive/{id}
    """
    r = RequestService.call_put(apis.get("archive_portfolio", portfolioId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_archives(self, userId):
    """
    接口名称：查询用户归档项目组合
    接口地址：/portfolio/$VERSION$/portfolio/archives/{userId}
    """
    r = RequestService.call_get(apis.get("get_archives", userId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_attention(self, portfolioId, type):
    """
    接口名称：添加关注/收藏/打开对象
    接口地址：/portfolio/$VERSION$/portfolio/attention
    """
    r = RequestService.call_post(apis.get("add_attention"), params={
        "portfolioId": portfolioId,  # 项目组合ID - required: True
        "type": type,  # 类型，0:最近打开的;1:我关注的; 2:我收藏的 - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def cancel_attention(self, portfolioId, type):
    """
    接口名称：取消关注/收藏/打开对象
    接口地址：/portfolio/$VERSION$/portfolio/attention
    """
    r = RequestService.call_delete(apis.get("cancel_attention"), params={
        "portfolioId": portfolioId,  # 项目组合ID - required: True
        "type": type,  # 类型，0:最近打开的;1:我关注的; 2:我收藏的 - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_attentions(self, type):
    """
    接口名称：查询用户关注/收藏/打开对象
    接口地址：/portfolio/$VERSION$/portfolio/attentions
    """
    r = RequestService.call_get(apis.get("get_attentions"), params={
        "type": type  # 类型，0:最近打开的;1:我关注的; 2:我收藏的 - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_candidates(self, type, code=None, name=None):
    """
    接口名称：查询候选项目
    接口地址：/portfolio/$VERSION$/portfolio/candidates
    """
    r = RequestService.call_get(apis.get("get_candidates"), params={
        "code": code,  # code - required: False
        "name": name,  # name - required: False
        "type": type,  # type,取值：program/project - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def search_proj_prog(self, code, name, type):
    """
    接口名称：根据Code、名称查询项目群、项目
    接口地址：/portfolio/$VERSION$/portfolio/paramsearch
    """
    r = RequestService.call_get(apis.get("search_proj_prog"), params={
        "code": code,  # code - required: True
        "name": name,  # name - required: True
        "type": type,  # type,取值：program/project - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def select_filter_list_using_post_2(self, el_condition_list, checker=None):
    """
    接口名称：过滤业务数据
    接口地址：/portfolio/$VERSION$/portfolios/filterlist
    """
    r = RequestService.call_post(apis.get("selectFilterListUsingPOST_2", None),
                                 json={
                                     "elConditionList": el_condition_list,
                                     "pageindex": 1,
                                     "pagesize": 20
                                 }
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_subs_proj(self, portfolioId, project_id, type, operation):
    """
    接口名称：添加、移除项目
    接口地址：/portfolio/$VERSION$/portfolio/subs/{id}
    """
    r = RequestService.call_put(apis.get("add_subs_proj", portfolioId), json={
        "list": [
            {
                "id": project_id,
                "type": type
            }
        ],
        "operation": operation
        # 添加/移除子项目群、子项目参数实体对象 - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_portfolio_tree(self, portfolioId):
    """
    接口名称：查询组合树
    接口地址：/portfolio/$VERSION$/portfolio/tree/{id}
    """
    r = RequestService.call_get(apis.get("get_portfolio_tree", portfolioId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_portfolio_by_id(self, portfolioId):
    """
    接口名称：查询单个项目组合详情
    接口地址：/portfolio/$VERSION$/portfolio/{id}
    """
    r = RequestService.call_get(apis.get("get_portfolio_by_id", portfolioId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delete_portfolio(self, portfolioId):
    """
    接口名称：删除组合
    接口地址：/portfolio/$VERSION$/portfolio/{id}
    """
    r = RequestService.call_delete(apis.get("delete_portfolio", portfolioId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_portfolio_proj(self, portfolioId):
    """
    接口名称：查询组合名下所有项目列表
    接口地址：/portfolio/$VERSION$/portfolio/{id}/projects
    """
    r = RequestService.call_get(apis.get("get_portfolio_proj", portfolioId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_portfolio_list(self, name=None):
    """
    接口名称：查询项目组合
    接口地址：/portfolio/$VERSION$/portfolios
    """
    r = RequestService.call_get(apis.get("get_portfolio_list"), params={
        "name": name  # 项目组合名称 - required: False
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_all_portfolio(self, name=None):
    """
    接口名称：查询所有项目组合
    接口地址：/portfolio/$VERSION$/portfolios/all
    """
    r = RequestService.call_get(apis.get("get_all_portfolio"), params={
        "name": name  # 项目组合名称 - required: False
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_page_portfolio(self, createBy=None, departmentId=None, isArchived=None, name=None, pageNo=None, page_size=None,
                       portfolioManagerId=None, sortField=None, sortMode=None):
    """
    接口名称：查询所有项目组合列表分页
    接口地址：/portfolio/$VERSION$/portfolios/all/page
    """
    r = RequestService.call_get(apis.get("get_page_portfolio"), params={
        "createBy": createBy,  # 项目组合创建人ID - required: False
        "departmentId": departmentId,  # 项目组合所属部门ID - required: False
        "isArchived": isArchived,  # 项目组合是否归档0:未归档,1:已归档 - required: False
        "name": name,  # 项目组合名称 - required: False
        "pageNo": pageNo,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
        "portfolioManagerId": portfolioManagerId,  # 项目组合经理ID - required: False
        "sortField": sortField,  # 项目组合排序字段，默认update_time - required: False
        "sortMode": sortMode,  # 项目组合排序方式:asc,desc，默认desc - required: False
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getAllProjectScoresUsingGET(self, portfolioId, checker=None):
    """
    接口名称：获取项目组合下所有项目提案的评分
    接口地址：/decision/$VERSION$/all/project/{portfolioId}/score
    """
    r = RequestService.call_get(apis.get("getAllProjectScoresUsingGET", portfolioId), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateProposalDecisionUsingPUT(self, project, checker=None):
    """
    接口名称：设置决策结论
    接口地址：/decision/$VERSION$/project
    """
    r = RequestService.call_put(apis.get("updateProposalDecisionUsingPUT", None), json={
        "project": project  # 项目提案信息 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def userEvaluateScoreStartNotifyUsingPOST(self, params, checker=None):
    """
    接口名称：流程评分结束调用
    接口地址：/decision/$VERSION$/project/score/end
    """
    r = RequestService.call_post(apis.get("userEvaluateScoreStartNotifyUsingPOST", None), json={
        "params": params  # 流程业务对象 - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def addUsingPOST_1(self, portfolioId, checker=None):
    """
    接口名称：添加项目组合关联关系
    接口地址：/decision/$VERSION$/project/{portfolioId}
    """
    r = RequestService.call_post(apis.get("addUsingPOST_1", portfolioId), json={
        "budget": "",  # 预算人民币 - required: False
        "children[0].requireIdList": "",  # 新增项目提案,关联需求的id - required: False
        "code": "",  # 编码 - required: False
        "contextType": "",  # 用于却分项目/项目计划(Project/Portfolio) - required: False
        "createBy": "",  # 创建者 - required: False
        "createTime": "",  # 创建时间 - required: False
        "delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "departmentId": "",  # 所属部门 - required: False
        "description": "",  # 描述 - required: False
        "finishTime": "",  # 完成时间 - required: False
        "flexAttrs": "",  # 扩展属性 - required: False
        "id": "",  # 对象Id - required: False
        "isArchived": "",  # 项目是否归档 - required: False
        "isDefaultTemplate": "",  # 是否是默认模板 - required: False
        "isFirstLevel": "",  # 在子项目列表中表示是否是第一层子项目 - required: False
        "isTemplate": "",  # 是否模板(是:1; 否:0) - required: False
        "lifecycleTemplateId": "",  # 生命周期模板ID - required: False
        "name": "",  # 名称 - required: False
        "parent.requireIdList": "",  # 新增项目提案,关联需求的id - required: False
        "parentId": "",  # 父节点Id - required: False
        "parentIdPath": "",  # 所有父级IdPath - required: False
        "phase": "",  # 项目阶段 - required: False
        "pmId": "",  # 项目经理ID - required: False
        "pmIds": "",  # 多个项目经理ID的列表 - required: False
        "pmName": "",  # 项目经理姓名 - required: False
        "productCategoryId": "",  # 产品-产品分类 - required: False
        "productId": "",  # 所属产品线ID - required: False
        "projCategory": "",  # 项目分类 - required: False
        "projectMemberList[0].active": "",  # 状态流中当前处理人标识(初始化：0 : 待处理：1 : 已处理：2) - required: False
        "projectMemberList[0].avatar": "",  # 成员头像  - required: False
        "projectMemberList[0].id": "",  # 对象Id - required: False
        "projectMemberList[0].isKeyMember": "",  # 是否为核心成员（非核心：0；核心：1） - required: False
        "projectMemberList[0].joinTime": "",  # 投入时间 - required: False
        "projectMemberList[0].objectClassName": "",  # 对象ClassName - required: False
        "projectMemberList[0].objectId": "",  # 需求Id - required: False
        "projectMemberList[0].percentage": "",  # 投入百分比 - required: False
        "projectMemberList[0].releaseTime": "",  # 释放时间 - required: False
        "projectMemberList[0].remark": "",  # 备注 - required: False
        "projectMemberList[0].roleKey": "",  # 流程角色 - required: False
        "projectMemberList[0].sort": "",  # 排序 - required: False
        "projectMemberList[0].state": "",  # 状态 - required: False
        "projectMemberList[0].userId": "",  # 成员用户Id - required: False
        "projectMemberList[0].userName": "",  # 成员用户姓名 - required: False
        "requireIdList": "",  # 新增项目提案,关联需求的id - required: False
        "sketchId": "",  # 草稿ID - required: False
        "startTime": "",  # 启动时间 - required: False
        "state": "",  # 项目状态 - required: False
        "stateTemplateId": "",  # 状态模板ID - required: False
        "templateId": "",  # 模板ID - required: False
        "type": "",  # 项目类型 - required: False
        "updateBy": "",  # 更新者 - required: False
        "updateTime": "",  # 更新时间 - required: False
        "visibleRange": "",  # 项目可见范围 - required: False
        "workload": "",  # 工作量 - required: False
    },)

    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def getscoresUsingGET(self, portfolioId, procInstId, project_id, userId, checker=None):
    """
    接口名称：获取项目机会评分
    接口地址：/decision/$VERSION$/project/{portfolioId}/score
    """
    r = RequestService.call_get(apis.get("getscoresUsingGET", portfolioId), params={
        "procInstId": procInstId,  # 项目id - required: False
        "projectId": project_id,  # 项目id - required: False
        "userId": userId,  # 项目id - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getuserscoresUsingGET(self, portfolioId, project_id, checker=None):
    """
    接口名称：获取当前登录人的项目机会评分
    接口地址：/decision/$VERSION$/project/{portfolioId}/userscore
    """
    r = RequestService.call_get(apis.get("getuserscoresUsingGET", portfolioId), params={
        "projectId": project_id  # 项目id - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteLinkUsingDELETE(self, portfolioId, project_id, checker=None):
    """
    接口名称：删除项目组合关联关系
    接口地址：/decision/$VERSION$/project/{portfolioId}/{project_id}
    """
    r = RequestService.call_delete(apis.get("deleteLinkUsingDELETE", portfolioId, project_id), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
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
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def savescoresUsingPUT(self, checker):
    """
    接口名称：修改项目机会评分
    接口地址：/decision/$VERSION$/project/{portfolioId}/{project_id}/score
    """
    r = RequestService.call_put(apis.get("savescoresUsingPUT", None), json={
        "projectEvaluateScore": ""  # 项目评分对象 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getScoreByproject_idUsingGET(self, portfolioId, project_id, checker=None):
    """
    接口名称：获取单个项目机会评分
    接口地址：/decision/$VERSION$/project_id/score
    """
    r = RequestService.call_get(apis.get("getScoreByproject_idUsingGET", None), params={
        "portfolioId": portfolioId,  # 项目组合id - required: True
        "projectId": project_id,  # 项目id - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def editscoresUsingPUT(self, portfolioId, projectEvaluateScore, checker=None):
    """
    接口名称：调整项目机会评分
    接口地址：/decision/$VERSION$/update/project/{portfolioId}/score
    """
    r = RequestService.call_put(apis.get("editscoresUsingPUT", portfolioId), json=projectEvaluateScore)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def projectsUsingGET_1(self, portfolioId, checker=None):
    """
    接口名称：查询组合下项目机会列表
    接口地址：/decision/$VERSION$/{portfolioId}/projects
    """
    r = RequestService.call_get(apis.get("projectsUsingGET_1", portfolioId), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getscorelistUsingGET(self, portfolioId, checker=None):
    """
    接口名称：获取项目机会评分汇总
    接口地址：/decision/$VERSION$/{portfolioId}/score
    """
    r = RequestService.call_get(apis.get("getscorelistUsingGET", portfolioId), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

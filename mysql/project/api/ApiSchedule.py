from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
日程/日程参与者
'''
apis = Api({
    "AgendaPOST": "/agenda/$VERSION$/save",  # 新增日程
    "getFormeAgendaListUsingGET": "/agenda/$VERSION$/forme/%s/%s",  # 我的工作台获取日程信息
    "deleteAgendaUsingDELETE": "/agenda/$VERSION$/delete/%s/%s",  # 删除日程
    "getProjectAgendaListUsingGET": "/agenda/$VERSION$/project/agenda/%s/%s",  # 获取项目日程信息
    "saveAgendaUsingPOST": "/agenda/$VERSION$/save",  # 保存日程及相关信息，发送提醒信息
    "syncAgendaUsingPOST": "/agenda/$VERSION$/sync/agenda",  # 同步日程
    "getAgendaUsingGET": "/agenda/$VERSION$/%s",  # 获取日程信息
    "editAgendaUsingPUT": "/agenda/$VERSION$/%s/%s",  # 修改日程信息
    "updateAgendaResponsibleRelationUsingPUT": "/agenda/$VERSION$/focus/%s",  # updateAgendaResponsibleRelation
})


def AgendaPOST(self, topicType, type, name, startTime, endTime, recurrence,
               remindMinite, userId, project_id=None, topicId=None, checker=None):
    """
    接口名称：新增日程
    接口地址：/erd-proj/agenda/$VERSION$/save
    """
    r = RequestService.call_post(apis.get("AgendaPOST"), params={
        "topicType": topicType,
        "topicId": topicId,
        "type": type,
        "name": name,
        "projectId": project_id,
        "startTime": startTime,
        "endTime": endTime,
        "recurrence": recurrence,
        "remindMinite": remindMinite,
        "arrs[0].userId": userId
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getFormeAgendaListUsingGET(self, startTime, endTime, showMode, checker=None):
    """
    接口名称：我的工作台获取日程信息
    接口地址：/agenda/$VERSION$/forme/{startTime}/{endTime}
    """
    r = RequestService.call_get(apis.get("getFormeAgendaListUsingGET", startTime, endTime), params={
        "showMode": showMode,  # 显示过滤：全部[-1];仅日程[0];计划[1];问题[2];需求[3];风险[4] - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteAgendaUsingDELETE(self, id, type, checker=None):
    """
    接口名称：删除日程
    接口地址：/agenda/$VERSION$/delete/{id}/{type}
    """
    r = RequestService.call_delete(apis.get("deleteAgendaUsingDELETE", id, type), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def getProjectAgendaListUsingGET(self, startTime, endTime, project_id, showMode, checker=None):
    """
    接口名称：获取项目日程信息
    接口地址：/agenda/$VERSION$/project/agenda/{startTime}/{endTime}
    """
    r = RequestService.call_get(apis.get("getProjectAgendaListUsingGET", startTime, endTime), params={
        "projectId": project_id,  # 项目ID - required: True
        "showMode": showMode,  # 显示过滤：全部[-1];仅日程[0];计划[1];问题[2];需求[3];风险[4] - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def saveAgendaUsingPOST(self, userId, description, endTime, name, project_id, recurrence,
                        remindMinite, startTime, topicId, topicType, type, checker=None):
    """
    接口名称：保存日程及相关信息，发送提醒信息
    接口地址：/agenda/$VERSION$/save
    """
    r = RequestService.call_post(apis.get("saveAgendaUsingPOST"), params={
        "arrs[0].userId": userId,  # 成员用户Id - required: False
        "description": description,  # 日程描述 - required: False
        "endTime": endTime,  # 结束时间 - required: False
        "name": name,  # 名称 - required: False
        "projectId": project_id,  # 项目Id - required: False
        "recurrence": recurrence,  # 日程重复。0：不重复，1： 每日重复，2：每周重复，3：每月重复，4：每年重复 - required: False
        "remindMinite": remindMinite,  # 提前提醒的分钟数 - required: False
        "startTime": startTime,  # 开始时间 - required: False
        "topicId": topicId,  # 日程目标Id - required: False
        "topicType": topicType,  # 日程类型 - required: False
        "type": type,  # 类型 - required: False

    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def syncAgendaUsingPOST(self, checker):
    """
    接口名称：同步日程
    接口地址：/agenda/$VERSION$/sync/agenda
    """
    r = RequestService.call_post(apis.get("syncAgendaUsingPOST"), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getAgendaUsingGET(self, id, checker=None):
    """
    接口名称：获取日程信息
    接口地址：/agenda/$VERSION$/{id}
    """
    r = RequestService.call_get(apis.get("getAgendaUsingGET", id), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def editAgendaUsingPUT(self, id, editType, arrs, endTime, name, project_id, remindMinite,
                       startTime, topicId, topicType, type, checker=None):
    """
    接口名称：修改日程信息
    接口地址：/agenda/$VERSION$/{id}/{editType}
    """
    r = RequestService.call_put(apis.get("editAgendaUsingPUT", id, editType), json={
        "arrs": arrs,
        "endTime": endTime,
        "name": name,
        "projectId": project_id,
        "remindMinite": remindMinite,
        "startTime": startTime,
        "topicId": topicId,
        "topicType": topicType,
        "type": type
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def updateAgendaResponsibleRelationUsingPUT(self, agendaId, agenda, checker=None):
    """
    接口名称：updateAgendaResponsibleRelation
    接口地址：/agenda/$VERSION$/focus/{agendaId}
    """
    r = RequestService.call_put(apis.get("updateAgendaResponsibleRelationUsingPUT", agendaId), json={
        "agenda": agenda  # 日程对象 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

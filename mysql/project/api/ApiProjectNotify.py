

from erdcloud.CommonServerTest import CommonServer
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
import json


apis = Api({
    "filterListUsingGET": "/proj/$VERSION$/msg/v2/configure/list/%s",  # 消息通知配置列表
    "configureUsingPOST": "/proj/$VERSION$/msg/v2/configure/%s",  # 消息通知配置
    "getWorkRemindUsingGET": "/proj/$VERSION$/msg/v2/getWorkRemind/%s",  # 获取每日工作条件
    "setWorkRemindUsingPUT": "/proj/$VERSION$/msg/v2/setWorkRemind/%s",  # 设置每日工作提醒
    "addNotifyConfigUsingPOST": "/proj/$VERSION$/notify",  # 新增消息通知配置
    "deleteNotifyConfigsUsingDELETE": "/proj/$VERSION$/notify",  # 批量删除项目消息通知配置信息
    "updateNotifyConfigUsingPUT": "/proj/$VERSION$/notify/{configId}",  # 修改消息通知配置/刷新本地配置的模板id
    "getNotifyConfigUsingGET": "/proj/$VERSION$/notify/%s/list",  # 查询项目消息通知配置信息
})


def filterListUsingGET(self, project_id, checker=None):
    """
    接口名称：消息通知配置列表
    接口地址：/proj/$VERSION$/msg/v2/configure/list/{project_id}
    """
    r = RequestService.call_get(apis.get("filterListUsingGET", project_id), params={
        # 项目id - required: False
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def configureUsingPOST(self, project_id, remindActions, checker=None):
    """
    接口名称：消息通知配置
    接口地址：/proj/$VERSION$/msg/v2/configure/{project_id}
    """
    com = CommonServer()
    token = com.get_token()

    r = RequestService.call_post(apis.get("configureUsingPOST", project_id),
                                 data=remindActions,
                                 headers={
                                     'Authorization': "Bearer " + token,
                                     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                 }
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getWorkRemindUsingGET(self, project_id, checker=None):
    """
    接口名称：获取每日工作条件
    接口地址：/proj/$VERSION$/msg/v2/getWorkRemind/{project_id}
    """
    r = RequestService.call_get(apis.get("getWorkRemindUsingGET", project_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r["res"]["data"]


def setWorkRemindUsingPUT(self, project_id, messageWorkReminds, checker=None):
    """
    接口名称：设置每日工作提醒
    接口地址：/proj/$VERSION$/msg/v2/setWorkRemind/{project_id}
    """
    r = RequestService.call_put(apis.get("setWorkRemindUsingPUT", project_id), json=messageWorkReminds
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def addNotifyConfigUsingPOST(self, project_id, checker=None):
    """
    接口名称：新增消息通知配置
    接口地址：/proj/$VERSION$/notify
    """
    r = RequestService.call_post(apis.get("addNotifyConfigUsingPOST", None), json={
        "contextType": "issue_custom",
        "contextId": project_id,
        "action": "create",
        "isNotifyHandler": 1,
        "notifyUsers": ["SYS_E39B20EA11E7A81AC85B767C89C1"],
        "notifyRoles": []
    }
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r["res"]["data"]


def deleteNotifyConfigsUsingDELETE(self, configid, checker=None):
    """
    接口名称：批量删除项目消息通知配置信息
    接口地址：/proj/$VERSION$/notify
    """
    r = RequestService.call_delete(apis.get("deleteNotifyConfigsUsingDELETE", None), params={
        "configIds": configid
    }
                                   )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r["res"]["data"]


def updateNotifyConfigUsingPUT(self, project_id, configid, checker=None):
    """
    接口名称：修改消息通知配置/刷新本地配置的模板id
    接口地址：/proj/$VERSION$/notify/{configId}
    """
    r = RequestService.call_put(apis.get("updateNotifyConfigUsingPUT", None), json={
        "id": configid,
        "contextId": project_id,
        "contextType": "risk_custom",
        "isRefreshTmpl": 1
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r["res"]["data"]


def getNotifyConfigUsingGET(self, project_id, checker=None):
    """
    接口名称：查询项目消息通知配置信息
    接口地址：/proj/$VERSION$/notify/{project_id}/list
    """
    r = RequestService.call_get(apis.get("getNotifyConfigUsingGET", project_id),
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r["res"]["data"]

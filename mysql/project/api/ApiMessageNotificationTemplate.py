
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
'''
消息通知模板
'''
apis = Api({
    "createUsingPOST": "/proj/$VERSION$/msg/v3/create",  # 创建消息模板
    "deleteUsingDELETE_2": "/proj/$VERSION$/msg/v3/delete/{ids}",  # 删除消息模板
    "findUsingGET": "/proj/$VERSION$/msg/v3/find/{id}",  # 获取消息模板
    "queryPageUsingGET": "/proj/$VERSION$/msg/v3/page",  # 消息模板列表
    "updateUsingPUT_1": "/proj/$VERSION$/msg/v3/update/{id}",  # 修改消息模板
})
def createUsingPOST(self, checker):
    """
    接口名称：创建消息模板
    接口地址：/proj/$VERSION$/msg/v3/create
    """
    r = RequestService.call_post(apis.get("createUsingPOST", None),params= {
                    "available": "",  # 是否有效 - required: False
                    "messageBody": "",  # 消息体 - required: False
                    "projectId": "",  # 项目Id - required: False
                    "selectedFields": "",  # 已选中的字段 - required: False
                    "templateName": "",  # 模板名称 - required: False
                    "typedefId": "",  # 关联的类型id - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def deleteUsingDELETE_2(self, checker):
    """
    接口名称：删除消息模板
    接口地址：/proj/$VERSION$/msg/v3/delete/{ids}
    """
    r = RequestService.call_delete(apis.get("deleteUsingDELETE_2", None),path= {
                    "ids": ""  # 模板ids - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def findUsingGET(self, checker):
    """
    接口名称：获取消息模板
    接口地址：/proj/$VERSION$/msg/v3/find/{id}
    """
    r = RequestService.call_get(apis.get("findUsingGET", None),path= {
                    "id": ""  # 模板id - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def queryPageUsingGET(self, checker):
    """
    接口名称：消息模板列表
    接口地址：/proj/$VERSION$/msg/v3/page
    """
    r = RequestService.call_get(apis.get("queryPageUsingGET", None),params= {
                    "available": "",  # 是否有效 - required: False
                    "createBy": "",  # 创建人 - required: False
                    "pageindex": "",  # page_index - required: False
                    "pagesize": "",  # page_size - required: False
                    "templateName": "",  # 模板名称 - required: False
                    "typedefId": "",  # 关联的类型id - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updateUsingPUT_1(self, checker):
    """
    接口名称：修改消息模板
    接口地址：/proj/$VERSION$/msg/v3/update/{id}
    """
    r = RequestService.call_put(apis.get("updateUsingPUT_1", None),json= {
                    "messageTemplateAddDto": ""  # messageTemplateAddDto - required: True
                },path= {
                    "id": ""  # 模板id - required: False
                },)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


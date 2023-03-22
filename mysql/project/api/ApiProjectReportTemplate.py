from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "addTemplateUsingPOST": "/rpt/$VERSION$/template",  # 创建项目报告模板
    "delTemplateUsingDELETE": "/rpt/$VERSION$/template",  # 删除项目报告模板,支持多个删除
    "getTemplateUsingGET": "/rpt/$VERSION$/template/%s",  # 获取项目报告模板信息
    "updateTemplateUsingPUT": "/rpt/$VERSION$/template/%s",  # 更新项目报告模板
    "getTemplatesUsingGET": "/rpt/$VERSION$/templates",  # 获取项目报告模板分页列表
    "getUuIdUsingGET": "/rpt/$VERSION$/uuid",  # 获取UUID
})
def addTemplateUsingPOST(self,uu_id,project_id,checker=None):
    """
    接口名称：创建项目报告模板
    接口地址：/rpt/$VERSION$/template
    """
    r = RequestService.call_post(apis.get("addTemplateUsingPOST", None),json={
                    "description" : "",
                    "id" : uu_id,
                    "items": [],
                    "name" : "111",
                    "projectId" : project_id,
                    "status" : 1,
                    "type" : "2"

                }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

def delTemplateUsingDELETE(self,template_id, checker=None):
    """
    接口名称：删除项目报告模板,支持多个删除
    接口地址：/rpt/$VERSION$/template
    """
    r = RequestService.call_delete(apis.get("delTemplateUsingDELETE", None),json=[
                    template_id  # ids - required: True
                ], )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

def getTemplateUsingGET(self, template_id,checker=None):
    """
    接口名称：获取项目报告模板信息
    接口地址：/rpt/$VERSION$/template/{id}
    """
    r = RequestService.call_get(apis.get("getTemplateUsingGET", template_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

def updateTemplateUsingPUT(self, template_id,project_id,checker=None):
    """
    接口名称：更新项目报告模板
    接口地址：/rpt/$VERSION$/template/{id}
    """
    r = RequestService.call_put(apis.get("updateTemplateUsingPUT", template_id),json={
                    "description" : "",
                    "items": [],
                    "name" : "222",
                    "projectId" : project_id,
                    "status" : 1,
                    "type" : "2"
                },  )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

def getTemplatesUsingGET(self,project_id, checker=None):
    """
    接口名称：获取项目报告模板分页列表
    接口地址：/rpt/$VERSION$/templates
    """
    r = RequestService.call_get(apis.get("getTemplatesUsingGET", None),params={
                    "createBy": "",  # 创建人 - required: False
                    "name": "",  # 名称 - required: False
                    "orderBy": "",  # 排序字段（默认createTime - required: False
                    "pageindex": 1,  # 页码 - required: False
                    "pagesize": 20,  # 每页数目 - required: False
                    "projectId": project_id,  # 项目ID - required: False
                    "sortBy": "",  # 排序方式（默认DESC - required: False
                    "status": "",  # 状态：1可用 0不可用 - required: False
                    "type": 2,  # 类型 - required: False
                    "updateBy": "",  # 更新人 - required: False
                }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r['res']['data']['records']

def getUuIdUsingGET(self, checker=None):
    """
    接口名称：获取UUID
    接口地址：/rpt/$VERSION$/uuid
    """
    r = RequestService.call_get(apis.get("getUuIdUsingGET", None),None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r['res']['uuid']
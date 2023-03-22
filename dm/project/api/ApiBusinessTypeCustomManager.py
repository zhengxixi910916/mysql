from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "saveLayoutUsingPOST": "/proj/$VERSION$/type/layout",  # 创建类型布局
    "enableLayoutUsingPOST": "/proj/$VERSION$/type/layout/%s",  # 启用类型布局
    "updateLayoutUsingPUT": "/proj/$VERSION$/type/layout/%s",  # 更新类型布局
    "delLayoutUsingDELETE": "/proj/$VERSION$/type/layout/%s",  # 删除类型布局
})


def saveLayoutUsingPOST(self, active, template, contextId, contextType, name, projectType, tplType, typedefId,
                        typedefName, typeDef_createTime, typeDef_updateTime, typeDef_id=3, typeDef_createBy=1,
                        typeDef_updateBy=1, typeDef_delFlag=0, typeDef_name="erd.cloud.plan.dto.EtTask",
                        typeDef_paramName="ELTask", typeDef_displayCn="任务", typeDef_displayEn="Task",
                        typeDef_description="任务定义", typeDef_icon=None, typeDef_instantiable=1,
                        checker=None):
    """
    接口名称：创建类型布局
    接口地址：/proj/$VERSION$/type/layout
    """
    r = RequestService.call_post(apis.get("saveLayoutUsingPOST", None), params={
        "name": name,
        "projectType": projectType,
        "tplType": tplType,
        "template": template,
        "contextId": contextId,
        "contextType": contextType,
        "active": active,
        "typedefId": typedefId,
        "typedefName": typedefName,
        "typeDef.id": typeDef_id,
        "typeDef.createBy": typeDef_createBy,
        "typeDef.createTime": typeDef_createTime,
        "typeDef.updateBy": typeDef_updateBy,
        "typeDef.updateTime": typeDef_updateTime,
        "typeDef.delFlag": typeDef_delFlag,
        "typeDef.name": typeDef_name,
        "typeDef.paramName": typeDef_paramName,
        "typeDef.displayCn": typeDef_displayCn,
        "typeDef.displayEn": typeDef_displayEn,
        "typeDef.description": typeDef_description,
        "typeDef.icon": typeDef_icon,
        "typeDef.instantiable": typeDef_instantiable,
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def enableLayoutUsingPOST(self, TypelayoutID, checker=None):
    """
    接口名称：启用类型布局
    接口地址：/proj/$VERSION$/type/layout/{id}
    """
    r = RequestService.call_post(apis.get("enableLayoutUsingPOST", TypelayoutID), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def updateLayoutUsingPUT(self, TypelayoutID, layout, checker=None):
    """
    接口名称：更新类型布局
    接口地址：/proj/$VERSION$/type/layout/{id}
    """
    r = RequestService.call_put(apis.get("updateLayoutUsingPUT", TypelayoutID), json=layout)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def delLayoutUsingDELETE(self, TypelayoutID, checker=None):
    """
    接口名称：删除类型布局
    接口地址：/proj/$VERSION$/type/layout/{id}
    """
    r = RequestService.call_delete(apis.get("delLayoutUsingDELETE", TypelayoutID), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r

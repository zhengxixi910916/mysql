import os
import random
import time
from contextlib import closing

from erdcloud.HttpClient import RequestService, commonServer
from erdcloud.erdApi import Api


from project.api.ApiRequireManage import delete_document_file



'''
项目风险
'''

# 获取上一级目录
dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dir_document = dir_path + r'/document'
times = time.strftime("%Y-%m-%d %H %M %S", time.localtime(time.time()))
file_name = "risk_" + times + ".xlsx"
file_path = dir_document + '/' + file_name

apis = Api({
    "add_risk": "/risk/v1",  # 添加风险
    "update_risk": "/risk/v1",  # 修改风险
    "search_business": "/risk/$VERSION$/api/list",  # 通用查询逻辑
    "get_risk_chart": "/risk/$VERSION$/chart/%s",  # 风险报表
    "export_risk_chart": "/risk/$VERSION$/chartexport/%s",  # 导出项目风险报表
    "select_business_export": "/risk/$VERSION$/export",  # 导出业务数据
    "select_avlb_fieldlist": "/risk/$VERSION$/extfields",  # 查询可用的扩展列名称
    "add_extfields": "/risk/$VERSION$/extfields",  # 添加可扩展列
    "import_business": "/risk/$VERSION$/import",  # 导入业务数据
    "get_business_type_count": "/risk/$VERSION$/item/count/%s",  # 获取风险的相关项的条目数
    "query_list_by_ids": "/risk/$VERSION$/list/%s",  # 根据ID列表查询对象列表
    "care_risk": "/risk/$VERSION$/myCare",  # 收藏/取消收藏
    "update_checklist": "/risk/$VERSION$/risk/checklist",  # 修改规避措施
    "editbatch_risk": "/risk/$VERSION$/risk/editBatch",  # 批量修改风险
    "insertbatch_risk": "/risk/$VERSION$/risk/insertBatch",  # 批量添加风险
    "get_checklist_by_id": "/risk/$VERSION$/risk/%s/checklist",  # 根据风险id查询规避措施
    "add_checklist": "/risk/$VERSION$/risk/%s/checklist",  # 添加规避措施
    "delete_checklist": "/risk/$VERSION$/risk/%s/checklist/%s",  # 删除规避措施
    "get_labels_list_by_id": "/risk/$VERSION$/risk/%s/labels",  # 根据风险id查询标签
    "add_labels": "/risk/$VERSION$/risk/%s/labels",  # 添加标签，标签ID多个用逗号分隔
    "delete_labels": "/risk/$VERSION$/risk/%s/labels/%s",  # 删除标签，标签ID多个用逗号分隔
    "copy_risk": "/risk/$VERSION$/risk/%s/copy",  # 复制|移动
    "get_project_risk": "/risk/$VERSION$/risks",  # 分页获取风险列表（项目下）
    "delete_risk": "/risk/$VERSION$/risks",  # 删除风险
    "get_risk_me": "/risk/$VERSION$/risks/me",  # 分页获取风险列表（个人工作台）
    "update_state_flow_members": "/risk/$VERSION$/stateflow/members",  # 修改状态流程成员
    "export_business_template": "/risk/$VERSION$/template/export",  # 导出业务数据模板
    "get_risk_by_id": "/risk/$VERSION$/%s",  # 获取风险详细信息
    "select_business_table": "/risk/$VERSION$/%s/businessTable",  # 查询业务表格列
    "select_business_list": "/risk/$VERSION$/%s/businesslist",  # 查询业务数据
    "select_filterlist": "/risk/$VERSION$/%s/filterlist",  # 过滤业务数据
    "release_plan_comfirm": "/risk/$VERSION$/%s/releasePlanComfirm",  # 发布计划前判断是否可以发布
    "add_dict": "/sys/$VERSION$/dictionary",
})


def add_dict(self, name, typename, attribute, value, sort, display_cn, display_en, parent_id="-1",
             context_id=str(random.randint(100, 999)), context_type="System"):
    """
    新增字典

    Args:
        self:testcase
        name:字典名称
        typename:类型
        attribute:属性
        parent_id:父id
        value:数据值
        sort:排序
        display_cn:中文显示名
        display_en:英文显示名
        context_id:上下文id
        context_type:上下文类型（System/Organization/Project）
    """
    r = RequestService.call_post_params(apis.get("add_dict"), params={
        "typeName": typename,
        "attribute": attribute,
        "parentId": parent_id,
        "value": value,
        "sort": sort,
        "displayCn": display_cn,
        "displayEn": display_en,
        "contextId": context_id,
        "contextType": context_type,
        "name": name
    })
    apis.check_success(self, r)
    return r["res"]["data"]


def add_risk(self, project_id, name="risk_" + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()), grade="3", state="DRAFT", type="1", fileIds=None,
             description=None, phase=None, planCloseTime=None,
             labelLinkIds=None, checker=None):
    """
    接口名称：添加风险
    接口地址：/risk/v1
    """
    r = RequestService.call_post(apis.get("add_risk"), json={
        "fileIds": fileIds  # 字段Id,支持多值,逗号分割 - required: False
    }, params={
        "description": description,  # 描述 - required: False
        "grade": grade,  # 风险等级 - required: False
        "labelLinkIds": labelLinkIds,  # 标签 - required: False
        "name": name,  # 名称 - required: False
        "phase": phase,  # 阶段 - required: False
        "planCloseTime": planCloseTime,  # 计划关闭时间 - required: False
        "projectId": project_id,  # 项目id - required: False
        "state": state,  # 风险状态 - required: False
        "type": type,  # 风险类别 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_risk(self, eid, riskname, submmitid, project_id, grade, type, state,
                avatar="./img/downLoad/a31c41a88a88ec29599de33695e173b1?_=1620869754349",
                code="code_" + time.strftime('%H%M%S', time.localtime()), name="name", displayName="displayName",
                flexAttrs=None, label_list=None, verifiers=None, planCloseTime=None, phase=None, description=None,
                checker=None):
    """
    接口名称：修改风险
    接口地址：/risk/v1
    """
    if flexAttrs is None:
        flexAttrs = {}
    if label_list is None:
        label_list = []
    if verifiers is None:
        verifiers = []
    r = RequestService.call_put(apis.get("update_risk"), json={
        "code": code,
        "description": description,
        "flexAttrs": flexAttrs,
        "grade": grade,
        "id": eid,
        "label_list": label_list,
        "name": riskname,
        "phase": phase,
        "planCloseTime": planCloseTime,
        "projectId": project_id,
        "state": state,
        "submitter": {
            "avatar": avatar,
            "code": code,
            "displayName": displayName,
            "id": submmitid,
            "name": name
        },
        "type": type,
        "verifiers": verifiers
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def search_business(self, checker=None):
    """
    接口名称：通用查询逻辑
    接口地址：/risk/$VERSION$/api/list
    """
    r = RequestService.call_post(apis.get("search_business"), json={
        "elViewDto": ""  # 条件列表 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_risk_chart(self, project_id, ymonth=time.strftime('%Y-%m', time.localtime()), checker=None):
    """
    接口名称：风险报表
    接口地址：/risk/$VERSION$/chart/{project_id}
    """
    r = RequestService.call_get(apis.get("get_risk_chart", project_id), params={
        "ymonth": ymonth  # 年-月（yyyy-MM格式） - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def export_risk_chart(self, project_id, month=time.strftime('%Y-%m', time.localtime())):
    """
    接口名称：导出项目风险报表
    接口地址：/risk/$VERSION$/chartexport/{project_id}
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("export_risk_chart", project_id), params={
        "month": month  # 月份(yyyy-MM) - required: False
    })) as response:
        with open(dir_document + r"\export_risk_chart_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def select_business_export(self, businessType, exprotList, viewid, exportIdList):
    """
    接口名称：导出业务数据
    接口地址：/risk/$VERSION$/export
    """
    # old_count = len(os.listdir(dir_document))
    # with closing(RequestService.call_get_download(apis.get("select_business_export"), params={
    #     "businessType": businessType,  # 业务对象 - required: True
    #     "elConditionList": elConditionList,  # 条件 - required: False
    #     "exportIdList": exportIdList,  # 导出数据的id - required: False
    #     "exprotList": exprotList,  # 导出字段 - required: True
    #     "isFilter": isFilter,  # 是否过滤查询 - required: False
    #     "isMyCare": isMyCare,  # 是否查询我的收藏 - required: False
    #     "mgReqFlag": mgReqFlag,  # 是否需求管理 - required: False
    #     "nameOrcode": nameOrcode,  # 首页高级查询 - required: False
    #     "projectId": project_id,  # 项目ID - required: False
    #     "relationship": relationship,  # 过滤关系and-or - required: False
    #     "viewid": viewid,  # 视图ID - required: False
    # })) as response:
    #     with open(dir_document + r"\export_risk_" + times + ".xlsx", "wb") as file:
    #         for data in response.iter_content(128):
    #             file.write(data)
    # new_count = len(os.listdir(dir_document))
    # self.assertTrue(new_count > old_count)

    try:
        delete_document_file(dir_document)
    except Exception as e:
        print(e)
        pass
    old_count = len(os.listdir(dir_document))
    r = RequestService.call_get_download(apis.get("select_business_export"),
                                         params={
                                             "exprotList": exprotList,
                                             "isFilter": False,
                                             "mgReqFlag": False,
                                             "businessType": businessType,
                                             "viewid": viewid,
                                             "exportIdList": exportIdList
                                         }
                                         )

    if r.status_code == 200:
        with open(file_path, "wb") as file:
            for data in r.iter_content(128):
                file.write(data)

    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def select_avlb_fieldlist(self, checker=None):
    """
    接口名称：查询可用的扩展列名称
    接口地址：/risk/$VERSION$/extfields
    """
    r = RequestService.call_get(apis.get("select_avlb_fieldlist"))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_extfields(self, attrKey, attrName, attrType, typeLength, defaultValue=None, checker=None):
    """
    接口名称：添加可扩展列
    接口地址：/risk/$VERSION$/extfields
    """
    r = RequestService.call_post(apis.get("add_extfields"), params={
        "entityAttrs[0].attrKey": attrKey,  # None - required: False
        "entityAttrs[0].attrName": attrName,  # None - required: False
        "entityAttrs[0].attrType": attrType,  # None - required: False
        "entityAttrs[0].defaultValue": defaultValue,  # None - required: False
        "entityAttrs[0].typeLength": typeLength  # None - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def import_business(self, checker=None):
    """
    接口名称：导入业务数据
    接口地址：/risk/$VERSION$/import
    """
    r = RequestService.call_post(apis.get("import_business"), data={
        "file": ""  # file - required: True
    }, params={
        "businessType": "",  # 业务对象 - required: True
        "projectId": "",  # 项目ID - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_business_type_count(self, riskid, cttType, itemList, scence, checker=None):
    """
    接口名称：获取风险的相关项的条目数
    接口地址：/risk/$VERSION$/item/count/{id}
    """
    r = RequestService.call_get(apis.get("get_business_type_count", riskid), params={
        "cttType": cttType,
        "itemList": itemList,
        "scence": scence
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def query_list_by_ids(self, eid, checker=None):
    """
    接口名称：根据ID列表查询对象列表
    接口地址：/risk/$VERSION$/list/{ids}
    """
    r = RequestService.call_get(apis.get("query_list_by_ids", eid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def care_risk(self, eid, name, checker=None):
    """
    接口名称：收藏/取消收藏
    接口地址：/risk/$VERSION$/myCare
    """
    r = RequestService.call_post(apis.get("care_risk"), params={
        "id": eid,  # id - required: True
        "name": name,  # 名称 - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_checklist(self, checkid, objectId, state, checker=None):
    """
    接口名称：修改规避措施
    接口地址：/risk/$VERSION$/risk/checklist
    """
    r = RequestService.call_put(apis.get("update_checklist"), json={
        "id": checkid,
        "objectId": objectId,
        "state": state
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def editbatch_risk(self, eid, project_id, type, checker=None):
    """
    接口名称：批量修改风险
    接口地址：/risk/$VERSION$/risk/editBatch
    """
    r = RequestService.call_put(apis.get("editbatch_risk"), json=[{
        "id": eid,
        "projectId": project_id,
        "type": type
    }])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def insertbatch_risk(self, name, project_id, grade, type, state, description=None, phase=None, riskMemberList=None,
                     checker=None):
    """
    接口名称：批量添加风险
    接口地址：/risk/$VERSION$/risk/insertBatch
    """
    if riskMemberList is None:
        riskMemberList = []
    r = RequestService.call_put(apis.get("insertbatch_risk"), json=[
        {
            "description": description,
            "grade": grade,
            "name": name,
            "phase": phase,
            "projectId": project_id,
            "riskMemberList": riskMemberList,
            "state": state,
            "type": type
        }])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_checklist_by_id(self, riskid, checker=None):
    """
    接口名称：根据风险id查询规避措施
    接口地址：/risk/$VERSION$/risk/{id}/checklist
    """
    r = RequestService.call_get(apis.get("get_checklist_by_id", riskid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_checklist(self, eid, name, deliverableFlag, checker=None):
    """
    接口名称：添加规避措施
    接口地址：/risk/$VERSION$/risk/{id}/checklist
    """
    r = RequestService.call_post(apis.get("add_checklist", eid), params={
        "deliverableFlag": deliverableFlag,  # 是否交付件（0：否；1：是） - required: False
        "name": name,  # 名称 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delete_checklist(self, riskid, checklistid, checker=None):
    """
    接口名称：删除规避措施
    接口地址：/risk/$VERSION$/risk/{id}/checklist/{cid}
    """
    r = RequestService.call_delete(apis.get("delete_checklist", riskid, checklistid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def get_labels_list_by_id(self, riskid, checker=None):
    """
    接口名称：根据风险id查询标签
    接口地址：/risk/$VERSION$/risk/{id}/labels
    """
    r = RequestService.call_get(apis.get("get_labels_list_by_id", riskid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_labels(self, eid, labelIds, checker=None):
    """
    接口名称：添加标签，标签ID多个用逗号分隔
    接口地址：/risk/$VERSION$/risk/{id}/labels
    """
    r = RequestService.call_post(apis.get("add_labels", eid), params={
        "labelIds": labelIds  # 标签ID多个用逗号或分号分隔 - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delete_labels(self, eid, labelIds, checker=None):
    """
    接口名称：删除标签，标签ID多个用逗号分隔
    接口地址：/risk/$VERSION$/risk/{id}/labels/{labelIds}
    """
    r = RequestService.call_delete(apis.get("delete_labels", eid, labelIds))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def copy_risk(self, eid, riskIds, project_id, type, state, createBy=None, checker=None):
    """
    接口名称：复制|移动
    接口地址：/risk/$VERSION$/risk/{project_id}/copy
    """
    r = RequestService.call_post(apis.get("copy_risk", eid), params={
        "createBy": createBy,  # 用户ID - required: False
        "projectId": project_id,  # 目标project_id - required: True
        "riskIds": riskIds,  # 风险ID串 - required: True
        "state": state,  # Risk状态 - required: False
        "type": type,  # 复制/移动[1：复制；2：移动] - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_project_risk(self, checker=None):
    """
    接口名称：分页获取风险列表（项目下）
    接口地址：/risk/$VERSION$/risks
    """
    r = RequestService.call_get(apis.get("get_project_risk"), params={
        "create_by": "",  # 提出人id - required: False
        "flow_state": "",  # 流程状态 - required: False
        "grade": "",  # 风险等级 - required: False
        "name": "",  # 风险名称 - required: False
        "order_by": "",  # 排序字段，默认创建时间 - required: False
        "pageindex": "",  # 页码 - required: False
        "pagesize": "",  # 每页条数 - required: False
        "principal": "",  # 责任人id - required: False
        "projectId": "",  # 项目id - required: False
        "sort_by": "",  # 排序方式，默认倒序 - required: False
        "state": "",  # 风险状态 - required: False
        "type": "",  # 风险类型 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delete_risk(self, eid, checker=None):
    """
    接口名称：删除风险
    接口地址：/risk/$VERSION$/risks
    """
    r = RequestService.call_delete(apis.get("delete_risk"), json=[
        eid  # 风险对象id集合 - required: False
    ])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def get_risk_me(self, checker=None):
    """
    接口名称：分页获取风险列表（个人工作台）
    接口地址：/risk/$VERSION$/risks/me
    """
    r = RequestService.call_get(apis.get("get_risk_me"), params={
        "create_by": "",  # 提出人id - required: False
        "flow_state": "",  # 流程状态 - required: False
        "grade": "",  # 风险等级（多个状态用逗号分隔） - required: False
        "name": "",  # 风险名称 - required: False
        "order_by": "",  # 排序字段，默认创建时间 - required: False
        "pageindex": "",  # 页码 - required: False
        "pagesize": "",  # 每页条数 - required: False
        "principal": "",  # 责任人id（多个状态用逗号分隔） - required: False
        "projectId": "",  # 项目id - required: False
        "sort_by": "",  # 排序方式，默认倒序 - required: False
        "state": "",  # 风险状态（多个状态用逗号分隔） - required: False
        "type": "",  # 风险类型（多个状态用逗号分隔） - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_state_flow_members(self, checker=None):
    """
    接口名称：修改状态流程成员
    接口地址：/risk/$VERSION$/stateflow/members
    """
    r = RequestService.call_put(apis.get("update_state_flow_members"), json={
        "members": ""  # members - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def export_business_template(self, businessType, exprotList, viewid, isFilter="false", mgReqFlag="false",
                             exportIdList=None):
    """
    接口名称：导出业务数据模板
    接口地址：/risk/$VERSION$/template/export
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("export_business_template"), params={
        "businessType": businessType,  # 业务对象 - required: True
        "exprotList": exprotList,  # 导出字段 - required: True
        "isFilter": isFilter,
        "mgReqFlag": mgReqFlag,
        "viewid": viewid,
        "exportIdList": exportIdList
    })) as response:
        with open(dir_document + r"\export_risk_tem_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def get_risk_by_id(self, riskid, checker=None):
    """
    接口名称：获取风险详细信息
    接口地址：/risk/$VERSION$/{id}
    """
    r = RequestService.call_get(apis.get("get_risk_by_id", riskid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def select_business_table(self, viewid, checker=None):
    """
    接口名称：查询业务表格列
    接口地址：/risk/$VERSION$/{viewid}/businessTable
    """
    r = RequestService.call_post(apis.get("select_business_table", viewid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def select_business_list(self, viewid, mgReqFlag="true", page_index=1, page_size=20, checker=None):
    """
    接口名称：查询业务数据
    接口地址：/risk/$VERSION$/{viewid}/businesslist
    """
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer " + commonServer.get_token()
    }
    r = RequestService.call_post(apis.get("select_business_list", viewid), json={
        "mgReqFlag": mgReqFlag,
        "pageindex": page_index,
        "pagesize": page_size
    }, headers=headers)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def select_filterlist(self, viewid, mgReqFlag="true", page_index=1, page_size=20, checker=None):
    """
    接口名称：过滤业务数据
    接口地址：/risk/$VERSION$/{viewid}/filterlist
    """
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer " + commonServer.get_token()
    }
    r = RequestService.call_post(apis.get("select_filterlist", viewid), json={
        "elConditionList": [
            {
                "fieldType": "datetime",
                "name": "createTime",
                "oper": "between",
                "value": "2014-05-30"
            }
        ],
        "elView": {
            "affiliation": "system",
            "businessType": "erd.cloud.risk.dto.EtRisk",
            "conditionRef": "and",
            "contextType": "3",
            "id": viewid,
            "selectedFields": "179,180,171,174,169,176,702,704,700,168,701,175,703,181",
        },
        "mgReqFlag": mgReqFlag,
        "pageindex": page_index,
        "pagesize": page_size
    }, headers=headers)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def release_plan_comfirm(self, viewid, checker=None):
    """
    接口名称：发布计划前判断是否可以发布
    接口地址：/risk/$VERSION$/{viewid}/releasePlanComfirm
    """
    r = RequestService.call_post(apis.get("release_plan_comfirm", viewid), json={
        "viewDto": ""  # 条件列表 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

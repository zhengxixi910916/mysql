import os
import time
from contextlib import closing

from erdcloud.HttpClient import RequestService, commonServer
from erdcloud.erdApi import Api




'''
问题基础信息操作
'''

# 获取上一级目录
dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dir_document = dir_path + r'/document'
times = time.strftime("%Y-%m-%d %H %M %S", time.localtime(time.time()))
file_name = "issue_" + times + ".xlsx"
file_path = dir_document + '/' + file_name

apis = Api({
    "search_business": "/issue/$VERSION$/api/list",  # 通用查询逻辑
    "select_business_export": "/issue/$VERSION$/export",  # 导出业务数据
    "select_avlb_fieldlist": "/issue/$VERSION$/extfields",  # 查询可用的扩展列名称
    "add_extfields": "/issue/$VERSION$/extfields",  # 添加可扩展列
    "import_business": "/issue/$VERSION$/import",  # 导入业务数据
    "add_issue": "/issue/$VERSION$/issue",  # 新建问题
    "editbatch_issue": "/issue/$VERSION$/issue/editBatch",  # 批量修改问题
    "insertbatch_issue": "/issue/$VERSION$/issue/insertBatch",  # 批量添加问题
    "get_labels_list": "/issue/$VERSION$/issue/labels",  # 获取系统标签列表
    "update_issue": "/issue/$VERSION$/issue/%s",  # 修改问题信息
    "add_checklist": "/issue/$VERSION$/issue/%s/checklist",  # 添加检查项
    "update_checklist": "/issue/$VERSION$/issue/%s/checklist",  # 修改检查项
    "delete_checklist": "/issue/$VERSION$/issue/%s/checklist/%s",  # 删除检查项
    "add_labels": "/issue/$VERSION$/issue/%s/labels",  # 添加标签，标签ID多个用逗号或分号分隔
    "delete_labels": "/issue/$VERSION$/issue/%s/labels/%s",  # 删除标签，标签ID多个用逗号或分号分隔
    "add_members": "/issue/$VERSION$/issue/%s/members",  # 添加责任人，责任人ID多个用逗号或分号分隔
    "delete_members": "/issue/$VERSION$/issue/%s/members/%s",  # 删除责任人，责任人ID多个用逗号或分号分隔
    "copy_issue": "/issue/$VERSION$/issue/%s/copy",  # 复制|移动
    "get_project_issues": "/issue/$VERSION$/issues",  # 分页获取问题列表（项目下）
    "delete_issue": "/issue/$VERSION$/issues",  # 删除问题
    "get_issues_me": "/issue/$VERSION$/issues/me",  # 分页获取问题列表（个人工作台）
    "get_issue_by_id": "/issue/$VERSION$/issues/%s",  # 获取问题详细信息
    "get_business_type_count": "/issue/$VERSION$/item/count/%s",  # 获取问题的相关项的条目数
    "query_list_by_ids": "/issue/$VERSION$/list/%s",  # 根据ID列表查询对象列表
    "care_issue": "/issue/$VERSION$/myCare",  # 收藏/取消收藏
    "update_state_flow_members": "/issue/$VERSION$/stateflow/members",  # 修改状态流程成员
    "export_business_template": "/issue/$VERSION$/template/export",  # 导出业务数据模板
    "select_business_table": "/issue/$VERSION$/%s/businessTable",  # 查询业务表格列
    "select_business_list": "/issue/$VERSION$/%s/businesslist",  # 查询业务数据
    "select_filterlist": "/issue/$VERSION$/%s/filterlist",  # 过滤业务数据
    "release_plan_comfirm": "/issue/$VERSION$/%s/releasePlanComfirm",  # 发布计划前判断是否可以发布
})


def search_business(self):
    """
    接口名称：通用查询逻辑
    接口地址：/issue/$VERSION$/api/list
    """
    r = RequestService.call_post(apis.get("search_business"), json={
        "elViewDto": ""  # 条件列表 - required: False
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delete_document_file(path):
    if len(os.listdir(path)) > 0:
        for root, dir_, file in os.walk(path):
            for files in file:
                file_path = os.path.join(root, files)
                print(f'被删除的文件：{file_path}')
                if os.path.exists(file_path):
                    os.remove(file_path)
                else:
                    print('文件不存在')
    else:
        print('文件夹为空')


def select_business_export(self, businessType, exprotList, viewid, exportIdList=None):
    """
    接口名称：导出业务数据
    接口地址：/issue/$VERSION$/export
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
    #     with open(dir_document + r"\export_issue_" + times + ".xlsx", "wb") as file:
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


def select_avlb_fieldlist(self):
    """
    接口名称：查询可用的扩展列名称
    接口地址：/issue/$VERSION$/extfields
    """
    r = RequestService.call_get(apis.get("select_avlb_fieldlist"))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_extfields(self, attrKey, attrName, attrType, typeLength, defaultValue=None):
    """
    接口名称：添加可扩展列
    接口地址：/issue/$VERSION$/extfields
    """
    r = RequestService.call_post(apis.get("add_extfields"), params={
        "entityAttrs[0].attrKey": attrKey,  # None - required: False
        "entityAttrs[0].attrName": attrName,  # None - required: False
        "entityAttrs[0].attrType": attrType,  # None - required: False
        "entityAttrs[0].defaultValue": defaultValue,  # None - required: False
        "entityAttrs[0].typeLength": typeLength  # None - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def import_business(self):
    """
    接口名称：导入业务数据
    接口地址：/issue/$VERSION$/import
    """
    r = RequestService.call_post(apis.get("import_business"), data={
        "file": ""  # file - required: True
    }, params={
        "businessType": "",  # 业务对象 - required: True
        "projectId": "",  # 项目ID - required: False
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_issue(self, project_id, submitid, name="issue_"+time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()), priority="1", state="DRAFT", type="1",
              submitdisplayname="name", submitcode=time.strftime('%H%M%S', time.localtime()), submitname="name",
              submitavatar="./img/downLoad/d0e47e26b1e84170ab995cc2de5fb310?_=1620804962106", finishDate=None,
              description=None, workload=None, actualFinishDate=None, actualStartDate=None, fileIds=None,
              labelLinkIds=None):
    """
    接口名称：新建问题
    接口地址：/issue/$VERSION$/issue
    """
    r = RequestService.call_post(apis.get("add_issue"), json={
        "fileIds": fileIds  # 字段，多个 - required: False
    }, params={
        "actualFinishDate": actualFinishDate,  # 实际完成时间  - required: False
        "actualStartDate": actualStartDate,  # 实际开始时间 - required: False
        "description": description,  # 描述 - required: False
        "finishDate": finishDate,  # 计划完成时间 - required: False
        "labelLinkIds": labelLinkIds,  # 标签 - required: False
        "name": name,  # 名称 - required: False
        "priority": priority,  # 优先级 - required: False
        "projectId": project_id,  # 项目ID - required: False
        "state": state,  # 问题状态（待处理[0];已处理[1];已过期[2]） - required: False
        "type": type,  # 类型 - required: False
        "workload": workload,  # 工作量 - required: False
        "submitter[id]": submitid,
        "submitter[displayName]": submitdisplayname,
        "submitter[code]": submitcode,
        "submitter[name]": submitname,
        "submitter[avatar]": submitavatar
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def editbatch_issue(self, eid, project_id, type):
    """
    接口名称：批量修改问题
    接口地址：/issue/$VERSION$/issue/editBatch
    """
    r = RequestService.call_put(apis.get("editbatch_issue"), json=[{
        "id": eid,
        "projectId": project_id,
        "type": type
    }])
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def insertbatch_issue(self, name, project_id, userId, roleKey, type, state, priority, description=None, dueDate=None,
                      submitTime=None, workload=None):
    """
    接口名称：批量添加问题
    接口地址：/issue/$VERSION$/issue/insertBatch
    """
    r = RequestService.call_put(apis.get("insertbatch_issue"), json=[
        {
            "description": description,
            "dueDate": dueDate,
            "flexAttrs": {
                "dueDate": dueDate,
                "submitTime": submitTime
            },
            "issueMemberList": [
                {
                    "roleKey": roleKey,
                    "userId": userId,
                }
            ],
            "name": name,
            "priority": priority,
            "projectId": project_id,
            "state": state,
            "submitTime": submitTime,
            "type": type,
            "workload": workload
        }
    ])
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_labels_list(self):
    """
    接口名称：获取系统标签列表
    接口地址：/issue/$VERSION$/issue/labels
    """
    r = RequestService.call_get(apis.get("get_labels_list"))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_issue(self, eid, issuename, submmitid, project_id, priority, type, state,
                 avatar="./img/downLoad/a31c41a88a88ec29599de33695e173b1?_=1620869754349",
                 code="code_" + time.strftime('%H%M%S', time.localtime()), name="name", displayName="displayName",
                 actualFinishDate=None, actualStartDate=None, description=None, finishDate=None, workload=None):
    """
    接口名称：修改问题信息
    接口地址：/issue/$VERSION$/issue/{id}
    """
    r = RequestService.call_put(apis.get("update_issue", eid), json={
        "actualFinishDate": actualFinishDate,
        "actualStartDate": actualStartDate,
        "code": code,
        "description": description,
        "finishDate": finishDate,
        "flexAttrs": {},
        "label_list": [],
        "name": issuename,
        "priority": priority,
        "processors": [{
            "avatar": avatar,
            "code": code,
            "displayName": displayName,
            "id": submmitid,
            "name": name
        }],
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
        "workload": workload
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def add_checklist(self, eid, name, deliverableFlag):
    """
    接口名称：添加检查项
    接口地址：/issue/$VERSION$/issue/{id}/checklist
    """
    r = RequestService.call_post(apis.get("add_checklist", eid), params={
        "deliverableFlag": deliverableFlag,  # 是否交付件（0：否；1：是） - required: False
        "name": name,  # 名称 - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_checklist(self, eid, checkid, state):
    """
    接口名称：修改检查项
    接口地址：/issue/$VERSION$/issue/{id}/checklist
    """
    r = RequestService.call_put(apis.get("update_checklist", eid), json={
        "id": checkid,
        "state": state
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def delete_checklist(self, eid, checkid):
    """
    接口名称：删除检查项
    接口地址：/issue/$VERSION$/issue/{id}/checklist/{checkListIds}
    """
    r = RequestService.call_delete(apis.get("delete_checklist", eid, checkid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def add_labels(self, eid, labelIds):
    """
    接口名称：添加标签，标签ID多个用逗号或分号分隔
    接口地址：/issue/$VERSION$/issue/{id}/labels
    """
    r = RequestService.call_post(apis.get("add_labels", eid), params={
        "labelIds": labelIds  # 标签ID多个用逗号或分号分隔 - required: True
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def delete_labels(self, eid, labelIds):
    """
    接口名称：删除标签，标签ID多个用逗号或分号分隔
    接口地址：/issue/$VERSION$/issue/{id}/labels/{labelIds}
    """
    r = RequestService.call_delete(apis.get("delete_labels", eid, labelIds))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def add_members(self, eid):
    """
    接口名称：添加责任人，责任人ID多个用逗号或分号分隔
    接口地址：/issue/$VERSION$/issue/{id}/members
    """
    r = RequestService.call_post(apis.get("add_members", eid), params={
        "memberIds": eid  # 成员ID多个用逗号或分号分隔 - required: True
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delete_members(self, eid):
    """
    接口名称：删除责任人，责任人ID多个用逗号或分号分隔
    接口地址：/issue/$VERSION$/issue/{id}/members/{memberIds}
    """
    r = RequestService.call_delete(apis.get("delete_members", eid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def copy_issue(self, eid, issueIds, project_id, type, state, createBy=None):
    """
    接口名称：复制|移动
    接口地址：/issue/$VERSION$/issue/{project_id}/copy
    """
    r = RequestService.call_post(apis.get("copy_issue", eid), params={
        "createBy": createBy,  # 用户ID - required: False
        "projectId": project_id,  # 目标project_id - required: True
        "issueIds": issueIds,  # 问题ID串 - required: True
        "state": state,  # issue状态 - required: False
        "type": type,  # 复制/移动[1：复制；2：移动] - required: True
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_project_issues(self):
    """
    接口名称：分页获取问题列表（项目下）
    接口地址：/issue/$VERSION$/issues
    """
    r = RequestService.call_get(apis.get("get_project_issues"), params={
        "ext": "",  # None - required: False
        "id": "",  # id - required: False
        "issueIds": "",  # None - required: False
        "labelId": "",  # 标签Id - required: False
        "memberId": "",  # 成员Id - required: False
        "name": "",  # 名称 - required: False
        "orderBy": "",  # 排序 - required: False
        "pageindex": "",  # 页码 - required: False
        "pagesize": "",  # 每页条数 - required: False
        "priority": "",  # 优先级列表 - required: False
        "projectId": "",  # 项目Id - required: False
        "sortBy": "",  # 分类 - required: False
        "startRow": "",  # 开始行 - required: False
        "state": "",  # 状态列表 - required: False
        "submitterId": "",  # 提交人Id - required: False
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delete_issue(self, eid):
    """
    接口名称：删除问题
    接口地址：/issue/$VERSION$/issues
    """
    r = RequestService.call_delete(apis.get("delete_issue"), json=[
        eid  # 问题列表 - required: False
    ])
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_issues_me(self):
    """
    接口名称：分页获取问题列表（个人工作台）
    接口地址：/issue/$VERSION$/issues/me
    """
    r = RequestService.call_get(apis.get("get_issues_me"), params={
        "ext": "",  # None - required: False
        "id": "",  # id - required: False
        "issueIds": "",  # None - required: False
        "labelId": "",  # 标签Id - required: False
        "memberId": "",  # 成员Id - required: False
        "name": "",  # 名称 - required: False
        "orderBy": "",  # 排序 - required: False
        "pageindex": "",  # 页码 - required: False
        "pagesize": "",  # 每页条数 - required: False
        "priority": "",  # 优先级列表 - required: False
        "projectId": "",  # 项目Id - required: False
        "sortBy": "",  # 分类 - required: False
        "startRow": "",  # 开始行 - required: False
        "state": "",  # 状态列表 - required: False
        "submitterId": "",  # 提交人Id - required: False
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_issue_by_id(self, eid):
    """
    接口名称：获取问题详细信息
    接口地址：/issue/$VERSION$/issues/{id}
    """
    r = RequestService.call_get(apis.get("get_issue_by_id", eid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_business_type_count(self, eid, cttType, itemList):
    """
    接口名称：获取问题的相关项的条目数
    接口地址：/issue/$VERSION$/item/count/{id}
    """
    r = RequestService.call_get(apis.get("get_business_type_count", eid), params={
        "cttType": cttType,  # 基线标识 - required: True
        "itemList": itemList,  # 业务条目:(discuss,relation,activity,check,attachment,elflow),逗号隔开 - required: True
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def query_list_by_ids(self, eid):
    """
    接口名称：根据ID列表查询对象列表
    接口地址：/issue/$VERSION$/list/{ids}
    """
    r = RequestService.call_get(apis.get("query_list_by_ids", eid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def care_issue(self, eid, name):
    """
    接口名称：收藏/取消收藏
    接口地址：/issue/$VERSION$/myCare
    """
    r = RequestService.call_post(apis.get("care_issue"), params={
        "id": eid,  # id - required: True
        "name": name,  # 名称 - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_state_flow_members(self, issue_id, checker=None, members=None):
    """
    接口名称：修改状态流程成员
    接口地址：/issue/$VERSION$/stateflow/members
    """
    r = RequestService.call_put(apis.get("update_state_flow_members"), json=[
        {"userId": "SYS_E39B20EA11E7A81AC85B767C89C1", "roleKey": "PROCESSOR",
         "objectId": issue_id}], )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

def export_business_template(self, businessType, exprotList, viewid, isFilter="false", mgReqFlag="false",
                             exportIdList=None):
    """
    接口名称：导出业务数据模板
    接口地址：/issue/$VERSION$/template/export
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
        with open(dir_document + r"\export_issue_tem_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def select_business_table(self, viewid):
    """
    接口名称：查询业务表格列
    接口地址：/issue/$VERSION$/{viewid}/businessTable
    """
    r = RequestService.call_post(apis.get("select_business_table", viewid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def select_business_list(self, viewid, mgReqFlag="true", page_index=1, page_size=20):
    """
    接口名称：查询业务数据
    接口地址：/issue/$VERSION$/{viewid}/businesslist
    """
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer " + commonServer.get_token()
    }
    r = RequestService.call_post(apis.get("select_business_list", "cb73735437c14de381294291bc1ee32d"), json={
        "mgReqFlag": mgReqFlag,
        "pageindex": page_index,
        "pagesize": page_size
    }, headers=headers)
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def select_filterlist(self, viewid, mgReqFlag="false", page_index=1, page_size=20):
    """
    接口名称：过滤业务数据
    接口地址：/issue/$VERSION$/{viewid}/filterlist
    """
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer " + commonServer.get_token()
    }
    r = RequestService.call_post(apis.get("select_filterlist", "cb73735437c14de381294291bc1ee32d"), json={
        "elConditionList": [
            {
                # "fieldType": "datetime",
                # "name": "createTime",
                # "oper": "between",
                # "value": "2014-05-30"
                "fieldType": "lifecycle",
                "name": "state",
                "oper": "in",
                "value": "DRAFT"

            }
        ],
        "elView": {
            "affiliation": "system",
            "businessType": "erd.cloud.issue.dto.EtIssue",
            "conditionRef": "and",
            "contextType": "3",
            "id": "cb73735437c14de381294291bc1ee32d",
            "selectedFields": "158,159,142,146,144,601,600,602,149,147,150,151,152,153",
        },
        "mgReqFlag": mgReqFlag,
        "pageindex": page_index,
        "pagesize": page_size
    }, headers=headers)
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def release_plan_comfirm(self, viewid):
    """
    接口名称：发布计划前判断是否可以发布
    接口地址：/issue/$VERSION$/{viewid}/releasePlanComfirm
    """
    r = RequestService.call_post(apis.get("release_plan_comfirm", viewid), json={
        "viewDto": ""  # 条件列表 - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

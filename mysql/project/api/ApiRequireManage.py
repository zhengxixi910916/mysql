import os
import time
from contextlib import closing

import requests
from erdcloud import CommonServer
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
from erdcloud.HttpClient import commonServer


"""
需求管理、需求管理-检查项|标签|成员
"""

# 获取上一级目录
dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dir_document = dir_path + r'/document'
dir_document1 = dir_path + r'/api/file'
times = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
file_name = dir_document + r"/export_require_tem" + times + ".xlsx"
file_name1 = dir_document1 + '/' + "project_requirement_import.xlsx"
apis = Api({
    "search_business": "/req/$VERSION$/api/list",  # 通用查询逻辑
    "select_business_export": "/req/$VERSION$/export",  # 导出业务数据
    "select_avlb_fieldlist": "/req/$VERSION$/extfields",  # 查询可用的扩展列名称
    "add_extfields": "/req/$VERSION$/extfields",  # 添加可扩展列
    "import_business": "/req/$VERSION$/import",  # 导入业务数据
    "get_business_type_count": "/req/$VERSION$/item/count/%s",  # 获取需求的相关项的条目数
    "query_list_by_ids": "/req/$VERSION$/list/%s",  # 根据ID列表查询对象列表
    "care_require": "/req/$VERSION$/myCare",  # 收藏/取消收藏
    "add_require": "/req/$VERSION$/require",  # 新增需求接口
    "get_baseline_reqchild_by_id": "/req/$VERSION$/require/baseline/%s/children",  # 基线获取子需求
    "get_require_me": "/req/$VERSION$/require/me",  # 获取需求列表数据-个人工作台
    "get_reqchild_by_id": "/req/$VERSION$/require/%s/children",  # 获取子需求
    "copy_requirements": "/req/$VERSION$/require/%s/copy",  # 复制|移动
    "get_require_by_id": "/req/$VERSION$/require/%s",  # 根据需求id获取需求详情
    "update_require": "/req/$VERSION$/require/%s",  # 更新需求详细信息
    "get_requires": "/req/$VERSION$/requires",  # 获取需求列表数据-需求管理列表
    "delete_require": "/req/$VERSION$/requires",  # 删除需求
    "get_editbatch_req_selectlist": "/req/$VERSION$/requires/editBatch/selectlist",  # 需求批量编辑树-selectlist
    "insertbatch_requires": "/req/$VERSION$/requires/insertbatch",  # 批量添加需求
    "get_reqs_by_projct_link": "/req/$VERSION$/requires/project/%s",  # 根据组合项目ID，获取需求列表数据
    "get_require_selectlist": "/req/$VERSION$/requires/selectlist",  # 需求树-selectlist
    "get_require_tree": "/req/$VERSION$/requires/tree",  # 需求树
    "get_require_tree_list": "/req/$VERSION$/requires/treelist",  # 需求树-list
    "updatebatch_requires": "/req/$VERSION$/requires/updatebatch",  # 需求批量编辑属性接口
    "get_require_type_list": "/req/$VERSION$/requiretypes",  # 需求类型列表
    "update_state_flow_members": "/req/$VERSION$/stateflow/members",  # 修改状态流程成员
    "get_states_by_type": "/req/$VERSION$/states/%s/%s",  # 项目需求统计
    "export_business_template": "/req/$VERSION$/template/export",  # 导出业务数据模板
    "update_req_state_by_id": "/req/$VERSION$/updateReqStateById/%s",  # 修改需求状态为已分配
    "select_business_table": "/req/$VERSION$/%s/businessTable",  # 查询业务表格列
    "select_business_list": "/req/$VERSION$/%s/businesslist",  # 查询业务数据
    "select_filterlist": "/req/$VERSION$/%s/filterlist",  # 过滤业务数据
    "release_plan_comfirm": "/req/$VERSION$/%s/releasePlanComfirm",  # 发布计划前判断是否可以发布
    "add_req_proj_link": "/req/$VERSION$/require/project/%s",  # 创建需求和项目关联关系
    "del_req_proj_link": "/req/$VERSION$/require/project/%s",  # 删除需求和项目关联关系
    "add_checklist": "/req/$VERSION$/require/%s/checklist",  # 添加检查项
    "update_checklist": "/req/$VERSION$/require/%s/checklist/%s",  # 修改检查项
    "delete_checklist": "/req/$VERSION$/require/%s/checklist/%s",  # 软删除检查项
    "add_labels": "/req/$VERSION$/require/%s/label",  # 需求-添加标签
    "delete_labels": "/req/$VERSION$/require/%s/label/%s",  # 需求删除标签
    "add_members": "/req/$VERSION$/require/%s/member",  # 添加需求成员
    "delete_members": "/req/$VERSION$/require/%s/member/%s",  # 需求-删除成员
    "requirementChangeTaskUsingPOST": "/req/$VERSION$/require/%s/changeTask",  # 需求转任务
    "compareChartUsingGET": "/plan/$VERSION$/task/compare",  # 计划进展对比报表API（这个是任务进度统计的，展示放这）

})


def requirementChangeTaskUsingPOST(self, project_id, parenttask_id, requireIds, type, checker=None):
    """
    接口名称：需求转任务
    接口地址：/req/$VERSION$/require/{project_id}/changeTask
    """
    r = RequestService.call_post(apis.get("requirementChangeTaskUsingPOST", project_id), params={
        "parentTaskId": parenttask_id,  # 父任务id - required: False
        "requireIds": requireIds,  # 需求ID串 - required: False
        "type": type,  # 责任人选择类型（1，原责任人，2，登录人） - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def search_business(self):
    """
    接口名称：通用查询逻辑
    接口地址：/req/$VERSION$/api/list
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


def select_business_export(self, businessType, exprotList, viewid, exportIdList, ):
    """
    接口名称：导出业务数据
    接口地址：/req/$VERSION$/export
    """
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
                                             "mgReqFlag": True,
                                             "businessType": businessType,
                                             "viewid": viewid,
                                             "exportIdList": exportIdList
                                         }
                                         )

    if r.status_code == 200:
        with open(file_name, "wb") as file:
            for data in r.iter_content(128):
                file.write(data)

    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def select_avlb_fieldlist(self):
    """
    接口名称：查询可用的扩展列名称
    接口地址：/req/$VERSION$/extfields
    """
    r = RequestService.call_get(apis.get("select_avlb_fieldlist"))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_extfields(self, attrKey, attrName, attrType, typeLength, defaultValue=None):
    """
    接口名称：添加可扩展列
    接口地址：/req/$VERSION$/extfields
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


def import_business(self, project_id, checker=None):
    """
    接口名称：导入业务数据
    接口地址：/req/$VERSION$/import
    """

    com = CommonServer()
    token = com.get_token()
    context = commonServer.get_context()
    api_path = commonServer.get_host() + context + apis.get("import_business")

    # self.book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # self.sheet = self.book.add_sheet('需求导入',cell_overwrite_ok=True)
    # col = ('编码', '名称', '提出人', '创建人')
    # for i in range(0, 4):
    #     self.sheet.write(0, i, col[i])
    # require_code = self.sheet.write(1, 0, str(random.randint(10000,99999)))
    # require_name = self.sheet.write(1, 1, "require"+times)
    # require_submitby = self.sheet.write(1, 2, "admin")
    # require_create_by = self.sheet.write(1, 3, "admin")
    # self.book.save(file_name2)
    #

    with open(file_name1, 'rb') as file:
        file = {'file': file}
        data = {
            "projectId": project_id,
            "businessType": "erd.cloud.require.dto.EtRequirement"
        }
        r = requests.post(url=api_path,
                          headers={
                              'Authorization': "Bearer " + token,
                          },
                          data=data,
                          files=file
                          )
    r = r.json()
    apis.check_success(self, r)
    return r

def get_business_type_count(self, requireid, cttType, itemList):
    """
    接口名称：获取需求的相关项的条目数
    接口地址：/req/$VERSION$/item/count/{id}
    """
    r = RequestService.call_get(apis.get("get_business_type_count", requireid), params={
        "cttType": cttType,  # 基线标识 - required: True
        "itemList": itemList,  # 业务条目:(child,discuss,relation,activity,check,attachment,elflow),逗号隔开 - required: True
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def query_list_by_ids(self, requireid):
    """
    接口名称：根据ID列表查询对象列表
    接口地址：/req/$VERSION$/list/{ids}
    """
    r = RequestService.call_get(apis.get("query_list_by_ids", requireid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def care_require(self, eid, name):
    """
    接口名称：收藏/取消收藏
    接口地址：/req/$VERSION$/myCare
    """
    r = RequestService.call_post(apis.get("care_require"), params={
        "id": eid,  # id - required: True
        "name": name,  # 名称 - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_require(self, name, project_id):
    """
    接口名称：新增需求接口
    接口地址：/req/$VERSION$/require
    """
    com = CommonServer()
    token = com.get_token()
    r = RequestService.call_post(apis.get("add_require"),
                                 data={
                                     "name": name,
                                     "state": "",
                                     "submitTime": "",
                                     "dueDate": '',
                                     "description": '',
                                     "ownerId":"",
                                     "parentId": '',
                                     "type": 2,
                                     "reqSource": "PLANNING",
                                     "priority": 1,
                                     "workLoad": '',
                                     "department": "SYS_2d28fff04a3da56f410a241528b4",
                                     "fileIds": '',
                                     "ownerType": 1,
                                     "submitterId": "SYS_E39B20EA11E7A81AC85B767C89C1",
                                     "labelLinkIds": ''

                                 },
                                 headers={
                                     'Authorization': "Bearer " + token,
                                     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                 }
                                 )
    apis.check_success(self, r)
    return r['res']["data"]


def get_baseline_req_child_by_id(self, eid):
    """
    接口名称：基线获取子需求
    接口地址：/req/$VERSION$/require/baseline/{id}/children
    """
    r = RequestService.call_get(apis.get("get_baseline_reqchild_by_id", eid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_require_me(self,label_id=None, member_id=None, order_by=None, page_index=1,
                   page_size=20, priority=None, project_id=None, require_name=None, sort_by=None, state=None,
                   submitter_id=None):
    """
    接口名称：获取需求列表数据-个人工作台
    接口地址：/req/$VERSION$/require/me
    """
    r = RequestService.call_get(apis.get("get_require_me"), params={
        "business_type": "erd.cloud.require.dto.EtRequirement",  # 需求类型 - required: False
        "label_id": label_id,  # 标签id - required: False
        "member_id": member_id,  # 责任人id - required: False
        "order_by": order_by,  # 排序字段，默认submitTime - required: False
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
        "priority": priority,  # 优先级 - required: False
        "projectId": project_id,  # 项目id - required: False
        "require_name": require_name,  # 需求名称 - required: False
        "sort_by": sort_by,  # 排序方式，默认倒序 - required: False
        "state": state,  # 需求状态 - required: False
        "submitter_id": submitter_id,  # 提出人id - required: False
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_reqchild_by_id(self, eid):
    """
    接口名称：获取子需求
    接口地址：/req/$VERSION$/require/{id}/children
    """
    r = RequestService.call_get(apis.get("get_reqchild_by_id", eid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def copy_requirements(self, eid, requireIds, project_id, type, state, createBy):
    """
    接口名称：复制|移动
    接口地址：/req/$VERSION$/require/{project_id}/copy
    """
    com = CommonServer()
    token = com.get_token()
    r = RequestService.call_post(apis.get("copy_requirements", eid),
                                 data={
                                     "createBy": createBy,  # 用户ID - required: False
                                     "projectId": project_id,  # 目标project_id - required: True
                                     "requireIds": requireIds,  # 需求ID串 - required: True
                                     "state": state,  # requirement状态 - required: False
                                     "type": type,  # 复制/移动[1：复制；2：移动] - required: True
                                 },
                                 headers={
                                     'Authorization': "Bearer " + token,
                                     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                 })
    apis.check_success(self, r)
    return r['res']["data"]


def get_require_by_id(self, eid):
    """
    接口名称：根据需求id获取需求详情
    接口地址：/req/$VERSION$/require/{require_id}
    """
    r = RequestService.call_get(apis.get("get_require_by_id", eid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_require(self, reqid, name, eid):
    """
    接口名称：更新需求详细信息
    接口地址：/req/$VERSION$/require/{require_id}
    """
    r = RequestService.call_put(apis.get("update_require", reqid), json={
        "state": "DRAFT",
        "name": name,
        "ownerId": eid
    })
    apis.check_success(self, r)
    return r


def get_requires(self, business_type=None, label_id=None, member_id=None, order_by=None, page_index=None,
                 page_size=None, priority=None, project_id=None, reqSource=None, require_name=None, sort_by=None,
                 state=None,
                 submitter_id=None):
    """
    接口名称：获取需求列表数据-需求管理列表
    接口地址：/req/$VERSION$/requires
    """
    r = RequestService.call_get(apis.get("get_requires"), params={
        "business_type": business_type,  # 需求类型 - required: False
        "label_id": label_id,  # 标签id - required: False
        "member_id": member_id,  # 责任人id - required: False
        "order_by": order_by,  # 排序字段，默认submitTime - required: False
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
        "priority": priority,  # 优先级 - required: False
        "projectId": project_id,  # 项目id - required: False
        "reqSource ": reqSource,  # 需求来源 - required: False
        "require_name": require_name,  # 需求名称 - required: False
        "sort_by": sort_by,  # 排序方式，默认倒序 - required: False
        "state": state,  # 需求状态 - required: False
        "submitter_id": submitter_id,  # 提出人id - required: False
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delete_require(self, reqIdList, checker=None):
    """
    接口名称：删除需求
    接口地址：/req/$VERSION$/requires
    """
    r = RequestService.call_delete(apis.get("delete_require"), json=[
        reqIdList  # 需求id列表 - required: False
    ])
    if checker is None:
        apis.check_success(self, r)
    else:
        apis.check(self, r, checker["code"], checker["success"])
    return r


def get_editbatch_req_selectlist(self):
    """
    接口名称：需求批量编辑树-selectlist
    接口地址：/req/$VERSION$/requires/editBatch/selectlist
    """
    r = RequestService.call_get(apis.get("get_editbatch_req_selectlist"), params={
        "projectId": "",  # 项目id - required: False
        "requireIds": "",  # 需求id - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def insertbatch_requires(self, name, ownerId, department, project_id, state, type, priority,
                         reqSource, description=None, parentId=None, workLoad=None, submitTime=None):
    """
    接口名称：批量添加需求
    接口地址：/req/$VERSION$/requires/insertbatch
    """
    r = RequestService.call_put(apis.get("insertbatch_requires"), json=[{
        "department": department,
        "description": description,
        "name": name,
        "ownerId": ownerId,
        "parentId": parentId,
        "priority": priority,
        "projectId": project_id,
        "reqSource": reqSource,
        "state": state,
        "submitTime": submitTime,
        "type": type,
        "workLoad": workLoad
    }])
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_reqs_by_projct_link(self, eid):
    """
    接口名称：根据组合项目ID，获取需求列表数据
    接口地址：/req/$VERSION$/requires/project/{project_id}
    """
    r = RequestService.call_get(apis.get("get_reqs_by_projct_link", eid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_require_selectlist(self):
    """
    接口名称：需求树-selectlist
    接口地址：/req/$VERSION$/requires/selectlist
    """
    r = RequestService.call_get(apis.get("get_require_selectlist"), params={
        "parent_id": "",  # 父节点id - required: False
        "projectId": "",  # 项目id - required: False
        "type": "",  # 需求类型 - required: False
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_require_tree(self, eid, parent_id=None):
    """
    接口名称：需求树
    接口地址：/req/$VERSION$/requires/tree
    """
    r = RequestService.call_get(apis.get("get_require_tree"), params={
        "parent_id": parent_id,  # 父节点id - required: False
        "project_id": eid,  # 项目id - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_require_tree_list(self, eid, parent_id=None):
    """
    接口名称：需求树-list
    接口地址：/req/$VERSION$/requires/treelist
    """
    r = RequestService.call_get(apis.get("get_require_tree_list"), params={
        "parent_id": parent_id,  # 父节点id - required: False
        "project_id": eid,  # 项目id - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updatebatch_requires(self, eid, project_id, type):
    """
    接口名称：需求批量编辑属性接口
    接口地址：/req/$VERSION$/requires/updatebatch
    """
    r = RequestService.call_put(apis.get("updatebatch_requires"), json=[{
        "id": eid,
        "projectId": project_id,
        "type": type
    }])
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_require_type_list(self):
    """
    接口名称：需求类型列表
    接口地址：/req/$VERSION$/requiretypes
    """
    r = RequestService.call_get(apis.get("get_require_type_list"), )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_state_flow_members(self):
    """
    接口名称：修改状态流程成员
    接口地址：/req/$VERSION$/stateflow/members
    """
    r = RequestService.call_put(apis.get("update_state_flow_members"), json={
        "members": ""  # members - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_states_by_type(self, project_id, statetype=None):
    """
    接口名称：项目需求统计
    接口地址：/req/$VERSION$/states/{project_id}/{state_type}
    """
    r = RequestService.call_get(apis.get("get_states_by_type", project_id, statetype))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def export_business_template(self, businessType, exprotList, project_id, viewid, isFilter="false", mgReqFlag="false",
                             exportIdList=None):
    """
    接口名称：导出业务数据模板
    接口地址：/req/$VERSION$/template/export
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("export_business_template"), params={
        "businessType": businessType,  # 业务对象 - required: True
        "exprotList": exprotList,  # 导出字段 - required: True
        "projectId": project_id,  # 项目ID - required: False
        "isFilter": isFilter,
        "mgReqFlag": mgReqFlag,
        "viewid": viewid,
        "exportIdList": exportIdList
    })) as response:
        with open(dir_document + r"\export_require_tem_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def update_req_state_by_id(self, requireid):
    """
    接口名称：修改需求状态为已分配
    接口地址：/req/$VERSION$/updateReqStateById/{require_ids}
    """
    r = RequestService.call_put(apis.get("update_req_state_by_id", requireid), params={
        "state": "PENDINGREVIEW"
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def select_business_table(self, viewid):
    """
    接口名称：查询业务表格列
    接口地址：/req/$VERSION$/{viewid}/businessTable
    """
    r = RequestService.call_post(apis.get("select_business_table", viewid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def select_business_list(self, viewid, mgReqFlag="true", page_index=1, page_size=20):
    """
    接口名称：查询业务数据
    接口地址：/req/$VERSION$/{viewid}/businesslist
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
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def select_filterlist(self, viewid, mgReqFlag="true", page_index=1, page_size=20):
    """
    接口名称：过滤业务数据
    接口地址：/req/$VERSION$/{viewid}/filterlist
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
            "businessType": "erd.cloud.require.dto.EtRequirement",
            "conditionRef": "and",
            "contextType": "3",
            "id": viewid,
            "selectedFields": "50f01335cfab40ad879923d6113a2054,213,194,191,201,193,196,803,"
                              "801,199,804,800,198,200,203",
        },
        "mgReqFlag": mgReqFlag,
        "pageindex": page_index,
        "pagesize": page_size
    }, headers=headers)
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def release_plan_comfirm(self, viewid):
    """
    接口名称：发布计划前判断是否可以发布
    接口地址：/req/$VERSION$/{viewid}/releasePlanComfirm
    """
    r = RequestService.call_post(apis.get("release_plan_comfirm", viewid), json={
        "viewDto": ""  # 条件列表 - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_req_proj_link(self, project_id, requireIds, checker=None):
    """
    接口名称：创建需求和项目关联关系
    接口地址：/req/$VERSION$/require/project/{project_id}
    """
    r = RequestService.call_put(apis.get("add_req_proj_link", project_id), params={
        "requireIds": requireIds  # 需求id串列表,英文逗号隔开 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def del_req_proj_link(self, project_id, requireIds, checker=None):
    """
    接口名称：删除需求和项目关联关系
    接口地址：/req/$VERSION$/require/project/{project_id}
    """
    r = RequestService.call_delete(apis.get("del_req_proj_link", project_id), params={
        "requireIds": requireIds  # 需求id串列表 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def add_checklist(self, eid, name, check_type, deliverable_flag, checker=None):
    """
    接口名称：添加检查项
    接口地址：/req/$VERSION$/require/{id}/checklist
    """
    r = RequestService.call_post(apis.get("add_checklist", eid), params={
        "check_type": check_type,  # 业务类型 计划[1];任务[2];问题[3]；需求[4];风险[5] - required: True
        "deliverable_flag": deliverable_flag,  # 是否交付件[0:否；1:是] - required: False
        "name": name,  # 检查项名称 - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_checklist(self, eid, checkid, state, checker=None):
    """
    接口名称：修改检查项
    接口地址：/req/$VERSION$/require/{id}/checklist/{cid}
    """
    r = RequestService.call_post(apis.get("update_checklist", eid, checkid), params={
        "state": state,  # 检查项状态 - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delete_checklist(self, eid, checkid, checker=None):
    """
    接口名称：软删除检查项
    接口地址：/req/$VERSION$/require/{id}/checklist/{cid}
    """
    r = RequestService.call_delete(apis.get("delete_checklist", eid, checkid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def add_labels(self, eid, label_id, checker=None):
    """
    接口名称：需求-添加标签
    接口地址：/req/$VERSION$/require/{id}/label
    """
    r = RequestService.call_post(apis.get("add_labels", eid), params={
        "label_id": label_id  # 标签ID多个用逗号或分号分隔 - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delete_labels(self, eid, labelIds, checker=None):
    """
    接口名称：需求删除标签
    接口地址：/req/$VERSION$/require/{id}/label/{label_id}
    """
    r = RequestService.call_delete(apis.get("delete_labels", eid, labelIds))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def add_members(self, requireid, objectId, roleKey, userid, checker=None):
    """
    接口名称：添加需求成员
    接口地址：/req/$VERSION$/require/{id}/member
    """
    r = RequestService.call_put(apis.get("add_members", requireid), json={
        "objectId": objectId,
        "roleKey": roleKey,
        "userId": userid
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delete_members(self, requireid, userid, checker=None):
    """
    接口名称：需求-删除成员
    接口地址：/req/$VERSION$/require/{id}/member/{member_id}
    """
    r = RequestService.call_delete(apis.get("delete_members", requireid, userid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def compare_chart(self, project_id, checker=None):
    """
    接口名称：计划进展对比报表API
    接口地址：/plan/$VERSION$/task/compare
    """
    r = RequestService.call_get(apis.get("compareChartUsingGET", None), params={
        "projectId": project_id,
        "version": -1,
        "startTime": "2022-01-01T00:00:00.000Z",
        "endTime": "2022-12-31T00:00:00.000Z"
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

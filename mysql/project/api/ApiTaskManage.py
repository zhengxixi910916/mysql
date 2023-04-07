import os
import time
from contextlib import closing

import requests
from erdcloud import CommonServer
from erdcloud.HttpClient import RequestService, commonServer
from erdcloud.erdApi import Api

from project.api.ApiIssueManage import delete_document_file


import random
'''
项目任务
'''
# 获取上一级目录
dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dir_document = dir_path + r'/document'
dir_document1 = dir_path + r'/api/file'

times = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
file_name = "task_" + times + ".xlsx"
file_path = dir_document + '/' + file_name
file_path1 = dir_document1 + '/'+'project_plan_import.xlsx'

apis = Api({
    "search_business": "/plan/$VERSION$/api/list",  # 通用查询逻辑
    "get_bdchart": "/plan/$VERSION$/bdchart/%s",  # 获取项目燃尽图
    "check_task_start_finish_time": "/plan/$VERSION$/checkTaskStartFinishTime",  # 校验任务的开始和结束时间
    "close_task_process": "/plan/$VERSION$/close",  # 流程配置调用任务关闭接口
    "cut_task_by_ids": "/plan/$VERSION$/cut",  # 裁剪计划
    "replace_check": "/plan/$VERSION$/deliver/replace",  # 替换交付件
    "get_duration_by_cal": "/plan/$VERSION$/duration",  # 根据日历配置计算工期或计划时间
    "execute_task": "/plan/$VERSION$/executetask/%s",  # 责任人开始执行任务
    "select_business_export": "/plan/$VERSION$/export",  # 导出业务数据
    "select_avlb_fieldlist": "/plan/$VERSION$/extfields",  # 查询可用的扩展列名称
    "add_extfields": "/plan/$VERSION$/extfields",  # 添加可扩展列
    "get_parent_task_by_id": "/plan/$VERSION$/getParentTaskById/%s",  # 通过任务id获取最顶层的父
    "import_business": "/plan/$VERSION$/import",  # 导入业务数据
    "get_business_type_count": "/plan/$VERSION$/item/count/%s",  # 获取计划的相关项的条目数
    "query_list_by_ids": "/plan/$VERSION$/list/%s",  # 根据ID列表查询对象列表
    "get_mchart": "/plan/$VERSION$/mchart/%s",  # 获取项目成员完成状况
    "export_mchart": "/plan/$VERSION$/mchartexport/%s",  # 导出项目概况统计报表
    "check_task_member": "/plan/$VERSION$/member/check",  # 计划成员修正
    "update_milestone": "/plan/$VERSION$/milestone",  # 里程碑变更
    "care_task": "/plan/$VERSION$/myCare",  # 收藏/取消收藏
    "sync_percent_task": "/plan/$VERSION$/percent/sync",  # 全局刷新计划百分比
    "get_predecessor_task_by_id": "/plan/$VERSION$/predecessor",  # 判断task及其子是否是其他task的前置任务
    "refresh_predecessor_link": "/plan/$VERSION$/predecessorLink/project/%s",  # 刷新项目下所有后置依赖任务计划时间
    "update_state_flow_members": "/plan/$VERSION$/stateflow/members",  # 修改状态流程成员
    "add_task": "/plan/$VERSION$/task",  # 创建任务
    "update_checklist": "/plan/$VERSION$/task/checklist",  # 修改检查项
    "delete_checklist": "/plan/$VERSION$/task/checklist/",  # 删除检查项批量删除检查项
    "update_checklist_folder": "/plan/$VERSION$/task/checklistFolder/%s",  # 修改检查项文件夹
    "editbatch_task": "/plan/$VERSION$/task/editBatch",  # 批量编辑任务,不支持跨项目编辑
    "insertbatch_task": "/plan/$VERSION$/task/insertBatch",  # 批量添加任务
    "get_milestone": "/plan/$VERSION$/task/milestone/%s",  # 获取里程碑数据
    "get_proj_tasks_statistics_detail": "/plan/$VERSION$/task/statistics/detail/%s",
    # 根据项目id获取项目任务统计数据详情
    "get_proj_tasks_statistics": "/plan/$VERSION$/task/statistics/%s",
    # 根据项目id获取项目任务统计数据（任务总数、完成数）
    "copy_template_task": "/plan/$VERSION$/task/template/copy",  # 拷贝项目模版任务数据
    "get_task_by_id": "/plan/$VERSION$/task/%s",  # 获取计划详细信息
    "update_task": "/plan/$VERSION$/task/%s",  # 修改任务
    "add_checklist": "/plan/$VERSION$/task/%s/checklist",  # 添加检查项
    "get_task_children": "/plan/$VERSION$/task/%s/children",  # 获取子任务
    "add_labels": "/plan/$VERSION$/task/%s/labels",  # 添加标签
    "delete_labels": "/plan/$VERSION$/task/%s/labels/%s",  # 删除标签
    "add_member": "/plan/$VERSION$/task/%s/members",  # 添加计划成员
    "delete_member": "/plan/$VERSION$/task/%s/members/%s",  # 删除计划成员
    "edit_sort_task": "/plan/$VERSION$/task/%s/order",  # 拖拽排序子任务
    "add_task_predecessorLink": "/plan/$VERSION$/task/%s/predecessorLink",  # 添加前置任务，不支持批量添加
    "sort_task": "/plan/$VERSION$/task/%s/sort",  # 任务排序
    "sync_task_handler": "/plan/$VERSION$/task/%s/all/members",  # 同步任务责任人
    "copy_task": "/plan/$VERSION$/task/%s/copy",  # 复制|移动
    "downgrade_task": "/plan/$VERSION$/task/%s/downgrade",  # 降级
    "upgrade_task": "/plan/$VERSION$/task/%s/upgrade",  # 升级
    "get_tasklist": "/plan/$VERSION$/taskList",  # 批量创建子任务时获取任务列表，来关联父任务
    "get_tasks": "/plan/$VERSION$/tasks",  # 获取任务列表（项目下）
    "get_all_task_doc": "/plan/$VERSION$/tasks/doc/%s",  # 获取项目下所有任务的交付件
    "get_first_tasklist": "/plan/$VERSION$/tasks/getOneTaskList",  # 根据项目id获取一级任务列表
    "get_task_me": "/plan/$VERSION$/tasks/me",  # 获取任务列表（个人工作台）
    "get_tasks_by_uid": "/plan/$VERSION$/tasks/member/%s",  # 获取责任人下的当前任务或要做任务
    "get_tasks_page": "/plan/$VERSION$/tasks/page",  # 获取项目任务列表（分页）
    "delete_task_by_id_list": "/plan/$VERSION$/tasks/projectId",  # 根据ids批量删除任务
    "get_tasks_by_source_id": "/plan/$VERSION$/tasks/source/%s",  # 根据来源ID获取任务
    "get_undone_task": "/plan/$VERSION$/tasks/undone/%s",  # 查询未完成任务
    "get_first_level_child_tasks": "/plan/$VERSION$/tasks/%s/children",  # 根据任务id获取第一层子任务列表
    "delete_task_predecessor_link": "/plan/$VERSION$/tasks/%s/predecessorLink",  # 删除任务前置依赖
    "delete_task_by_id": "/plan/$VERSION$/tasks/%s",  # 删除计划
    "export_business_template": "/plan/$VERSION$/template/export",  # 导出业务数据模板
    "query_tree_list_by_ids": "/plan/$VERSION$/tree/%s",  # 根据ID列表查询对象详细信息
    "close_task": "/plan/$VERSION$/%s/close",  # 任务关闭接口
    "close_validate": "/plan/$VERSION$/%s/close/validate",  # 任务关闭校验接口
    "get_critical_flag_task": "/plan/$VERSION$/%s/critical",  # 判断task及其子是否是其他task的前置任务
    "select_business_table": "/plan/$VERSION$/%s/businessTable",  # 查询业务表格列
    "select_business_list": "/plan/$VERSION$/%s/businesslist",  # 查询业务数据
    "select_filterlist": "/plan/$VERSION$/%s/filterlist",  # 过滤业务数据
    "release_plan_comfirm": "/plan/$VERSION$/%s/releasePlanComfirm",  # 发布计划前判断是否可以发布
    "getOneDurationrecordUsingGET": "/plan/$VERSION$/one/durationrecord/%s",  # 单个登记卡信息
    "updateDurationrecordUsingPUT": "/plan/$VERSION$/update/durationrecord",  # 更新工时选项卡登记
    "getDurationrecordUsingGET": "/plan/$VERSION$/durationrecord/%s",  # 获取工时选项卡
    "findUserDurationRecordsUsingGET": "/plan/$VERSION$/duration/record/%s/%s",  # 获取用户工时
    "addDurationrecordUsingPOST": "/plan/$VERSION$/durationrecord",  # 添加工时选项卡登记

})


def updateDurationrecordUsingPUT(self, record, checker=None):
    """
    接口名称：更新工时选项卡登记
    接口地址：/plan/$VERSION$/update/durationrecord
    """
    r = RequestService.call_put(apis.get("updateDurationrecordUsingPUT", None), json=record)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def addDurationrecordUsingPOST(self, workload, remainDuration, registeredTime, description, sumId, startDate,
                               checker=None):
    """
    接口名称：添加工时选项卡登记
    接口地址：/plan/$VERSION$/durationrecord
    """
    r = RequestService.call_post(apis.get("addDurationrecordUsingPOST", None), params={
        "workload": workload,
        "remainDuration": remainDuration,
        "registeredTime": registeredTime,
        "description": description,
        "sumId": sumId,
        "startDate": startDate
    },
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def findUserDurationRecordsUsingGET(self, startDate, endDate, userId=None, checker=None):
    """
    接口名称：获取用户工时
    接口地址：/plan/$VERSION$/duration/record/{startDate}/{endDate}
    """
    r = RequestService.call_get(apis.get("findUserDurationRecordsUsingGET", startDate, endDate), params={
        "userId": userId  # 用户id，可不填 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getDurationrecordUsingGET(self, id, checker=None):
    """
    接口名称：获取工时选项卡
    接口地址：/plan/$VERSION$/durationrecord/{id}
    """
    r = RequestService.call_get(apis.get("getDurationrecordUsingGET", id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def getOneDurationrecordUsingGET(self, id, checker=None):
    """
    接口名称：单个登记卡信息
    接口地址：/plan/$VERSION$/one/durationrecord/{id}
    """
    r = RequestService.call_get(apis.get("getOneDurationrecordUsingGET", id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def search_business(self, checker=None):
    """
    接口名称：通用查询逻辑
    接口地址：/plan/$VERSION$/api/list
    """
    r = RequestService.call_post(apis.get("search_business"), json={
        "elViewDto": ""  # 条件列表 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_bdchart(self, project_id, checker=None):
    """
    接口名称：获取项目燃尽图
    接口地址：/plan/$VERSION$/bdchart/{id}
    """
    r = RequestService.call_get(apis.get("get_bdchart", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def check_task_start_finish_time(self, task_id, checker=None):
    """
    接口名称：校验任务的开始和结束时间
    接口地址：/plan/$VERSION$/checkTaskStartFinishTime
    """
    r = RequestService.call_get(apis.get("check_task_start_finish_time"), params={
        "task_id": task_id,
        "finishTime": "2021-05-22",  # finishTime - required: False
        "startTime": "2021-05-22",  # startTime - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def close_task_process(self, params, checker=None):
    """
    接口名称：流程配置调用任务关闭接口
    接口地址：/plan/$VERSION$/close
    """
    r = RequestService.call_post(apis.get("close_task_process"), json=params)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def cut_task_by_ids(self, task_idList, checker=None):
    """
    接口名称：裁剪计划
    接口地址：/plan/$VERSION$/cut
    """
    r = RequestService.call_delete(apis.get("cut_task_by_ids"), json=[
        task_idList  # 任务Id列表 - required: False
    ])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def replace_check(self, checker=None):
    """
    接口名称：替换交付件
    接口地址：/plan/$VERSION$/deliver/replace
    """
    r = RequestService.call_post(apis.get("replace_check"), json={
        "params": ""  # params - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_duration_by_cal(self, project_id, startDate, finishDate, duration=None, checker=None):
    """
    接口名称：根据日历配置计算工期或计划时间
    接口地址：/plan/$VERSION$/duration
    """
    r = RequestService.call_get(apis.get("get_duration_by_cal"), params={
        "duration": duration,  # 工期 - required: False
        "finishDate": finishDate,  # 任务结束时间 - required: False
        "projectId": project_id,  # 项目id - required: False
        "startDate": startDate,  # 任务开始时间 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def execute_task(self, task_id,  project_id, checker=None):
    """
    接口名称：责任人开始执行任务
    接口地址：/plan/$VERSION$/executetask/{id}
    """
    r = RequestService.call_put(apis.put("execute_task", task_id),
                                json={"criticalFlag": 0, "flexAttrs": {"testAAA": "0", "testTest": None},
                                      "labelIds": [], "sop": "", "isCutted": 0,
                                      "id": task_id, "state": "PENDING", "leafNode": "false",
                                      "canBeCutted": 1, "taskCheckLists": [], "name": "Task_160800",
                                      "lifecycleTemplateId": "ac56c36a892d54fc626f191b9d12e3da",
                                      "projectId": project_id,
                                      "predecessorLink": "[{\"PredecessorUID\":\"135e0f82f1782cf07c67f7efdaf49d4c\",\"Type\":\"1\",\"LinkLag\":\"0\",\"_index\":\"0\",\"_uid\":\"e5e3bd22489dc377ec6439604a0e0959\"}]",
                                      "code": "1", "deliverVos": [], "description": "", "taskInput": "",
                                      "updateBy": "SYS_E39B20EA11E7A81AC85B767C89C1", "attachmentList": [],
                                      "favoritesFlag": "false", "responsibleIds": ["SYS_E39B20EA11E7A81AC85B767C89C1"],
                                      "milestoneFlag": 0, "workload": "", "percentComplete": "0", "taskOutput": "",
                                      "summaryFlag": "0", "parentId": -1,
                                      "createBy": "SYS_E39B20EA11E7A81AC85B767C89C1", "resAssignments": "MEMBER",
                                      "orderCode": "1001", "stageFlag": 0, "newRecord": "false", "taskLabelList": [],
                                      "testAAA": "0", "testTest": None})
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

def select_business_export(self, businessType, exprotList, project_id, viewid, exportIdList):
    """
    接口名称：导出业务数据
    接口地址：/plan/$VERSION$/export
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
    #     with open(dir_document + r"\export_task_" + times + ".xlsx", "wb") as file:
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
                                             "projectId": project_id,
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
    接口地址：/plan/$VERSION$/extfields
    """
    r = RequestService.call_get(apis.get("select_avlb_fieldlist"))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_extfields(self, attrKey, attrName, attrType, typeLength, defaultValue=None, checker=None):
    """
    接口名称：添加可扩展列
    接口地址：/plan/$VERSION$/extfields
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


def get_parent_task_by_id(self, task_id, checker=None):
    """
    接口名称：通过任务id获取最顶层的父
    接口地址：/plan/$VERSION$/getParentTaskById/{task_id}
    """
    r = RequestService.call_get(apis.get("get_parent_task_by_id", task_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def import_business(self, project_id=None, checker=None):
    """
    接口名称：导入业务数据
    接口地址：/plan/$VERSION$/import
    """
    com = CommonServer()
    token = com.get_token()
    context = com.get_context()
    api_path = com.get_host() + context + apis.get("import_business")

    # self.book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # self.sheet = self.book.add_sheet('计划导入', cell_overwrite_ok=True)
    # col = ('编码', '名称', '资源角色')
    # for i in range(0, 3):
    #     self.sheet.write(0, i, col[i])
    # task_code = self.sheet.write(1, 0, str(random.randint(10000,99999)))
    # task_name = self.sheet.write(1, 1, "task"+times)
    # task_role = self.sheet.write(1, 2, "项目成员")
    # self.book.save(file_path2)

    with open(file_path1, 'rb') as file:
        file = {'file': file}
        data = {
            "projectId": project_id,
            "businessType": "erd.cloud.plan.dto.EtTask"
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



def get_business_type_count(self, task_id, cttType, itemList, scence, checker=None):
    """
    接口名称：获取计划的相关项的条目数
    接口地址：/plan/$VERSION$/item/count/{id}
    """
    r = RequestService.call_get(apis.get("get_business_type_count", task_id), params={
        "cttType": cttType,
        "itemList": itemList,
        "scence": scence
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def query_list_by_ids(self, task_id, checker=None):
    """
    接口名称：根据ID列表查询对象列表
    接口地址：/plan/$VERSION$/list/{ids}
    """
    r = RequestService.call_get(apis.get("query_list_by_ids", task_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_mchart(self, project_id, month=time.strftime('%Y-%m', time.localtime()), checker=None):
    """
    接口名称：获取项目成员完成状况
    接口地址：/plan/$VERSION$/mchart/{id}
    """
    r = RequestService.call_get(apis.get("get_mchart", project_id), params={
        "month": month  # 月份(yyyy-MM) - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def export_mchart(self, project_id, month=time.strftime('%Y-%m', time.localtime())):
    """
    接口名称：导出项目概况统计报表
    接口地址：/plan/$VERSION$/mchartexport/{project_id}
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("export_mchart", project_id), params={
        "month": month  # 月份(yyyy-MM) - required: False
    })) as response:
        with open(dir_document + r"\export_mchart_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def check_task_member(self, checker=None):
    """
    接口名称：计划成员修正
    接口地址：/plan/$VERSION$/member/check
    """
    r = RequestService.call_get(apis.get("check_task_member", None), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def update_milestone(self, checker=None):
    """
    接口名称：里程碑变更
    接口地址：/plan/$VERSION$/milestone
    """
    r = RequestService.call_post(apis.get("update_milestone"), json={
        "params": ""  # 流程业务对象 - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def care_task(self, task_id, name, checker=None):
    """
    接口名称：收藏/取消收藏
    接口地址：/plan/$VERSION$/myCare
    """
    r = RequestService.call_post(apis.get("care_task"), params={
        "id": task_id,  # id - required: True
        "name": name,  # 名称 - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def sync_percent_task(self, checker=None):
    """
    接口名称：全局刷新计划百分比
    接口地址：/plan/$VERSION$/percent/sync
    """
    r = RequestService.call_put(apis.get("sync_percent_task"), )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def get_predecessor_task_by_id(self, task_ids, checker=None):
    """
    接口名称：判断task及其子是否是其他task的前置任务
    接口地址：/plan/$VERSION$/predecessor
    """
    r = RequestService.call_put(apis.get("get_predecessor_task_by_id"), json=[
        task_ids  # 计划Id - required: True
    ])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def refresh_predecessor_link(self, project_id, checker=None):
    """
    接口名称：刷新项目下所有后置依赖任务计划时间
    接口地址：/plan/$VERSION$/predecessorLink/project/{id}
    """
    r = RequestService.call_put(apis.get("refresh_predecessor_link", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def update_state_flow_members(self, checker=None):
    """
    接口名称：修改状态流程成员
    接口地址：/plan/$VERSION$/stateflow/members
    """
    r = RequestService.call_put(apis.get("update_state_flow_members"), json={
        "members": ""  # members - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_task(self, project_id, startDate=None,  finishDate=None,checker=None):
    """
    接口名称：创建任务
    接口地址：/plan/$VERSION$/task
    """
    r = RequestService.call_post(apis.get("add_task"), params={
        "name": "task_" + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()),
        "startDate": startDate,
        "finishDate": finishDate,
        "milestoneFlag": "0",
        "state": "",
        "criticalFlag": "0",
        "canBeCutted": "1",
        "description": "",
        "percentComplete": "",
        "projectId": project_id,
        "parentId": "",
        "actualFinishDate": "",
        "workload": "",
        "duration": "5",
        "resAssignments": "MEMBER",
        "sop": "",
        "taskInput": "",
        "taskOutput": "",
        "fileIds": "",
        "summaryFlag": "0",
        "taskMemberList[0].roleKey": "HANDLEPERSON",
        "taskMemberList[0].userId": "SYS_E39B20EA11E7A81AC85B767C89C1",
        "taskMemberList[1].roleKey": "IDENTIFY",
        "taskMemberList[1].userId": "",
        "labelLinkIds": "",
        "stageFlag": "1"
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_checklist(self, checkid, objectId, state, checker=None):
    """
    接口名称：修改检查项
    接口地址：/plan/$VERSION$/task/checklist
    """
    r = RequestService.call_put(apis.get("update_checklist"), json=[{
        "id": checkid,
        "objectId": objectId,
        "state": state
    }])
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_checklist(self, id, objectId, attachmentId=None, checker=None):
    """
    接口名称：删除检查项批量删除检查项
    接口地址：/plan/$VERSION$/task/checklist/
    """
    r = RequestService.call_put(apis.get("delete_checklist"), json=[{
        "attachmentId": attachmentId,
        "id": id,
        "objectId": objectId
    }])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def update_checklist_folder(self, checker=None):
    """
    接口名称：修改检查项文件夹
    接口地址：/plan/$VERSION$/task/checklistFolder/{id}
    """
    r = RequestService.call_put(apis.get("update_checklist_folder"), json={
        "checklist": ""  # 任务检查项列表 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def editbatch_task(self, eid, project_id, state, checker=None):
    """
    接口名称：批量编辑任务,不支持跨项目编辑
    接口地址：/plan/$VERSION$/task/editBatch
    """
    r = RequestService.call_put(apis.get("editbatch_task"), json=[{
        "id": eid,
        "projectId": project_id,
        "state": state
    }])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def insertbatch_task(self, tasks, checker=None):
    """
    接口名称：批量添加任务
    接口地址：/plan/$VERSION$/task/insertBatch
    """
    r = RequestService.call_put(apis.get("insertbatch_task"), json=tasks)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_milestone(self, project_id, checker=None):
    """
    接口名称：获取里程碑数据
    接口地址：/plan/$VERSION$/task/milestone/{project_id}
    """
    r = RequestService.call_get(apis.get("get_milestone", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_proj_tasks_statistics_detail(self, project_id, checker=None):
    """
    接口名称：根据项目id获取项目任务统计数据详情
    接口地址：/plan/$VERSION$/task/statistics/detail/{project_id}
    """
    r = RequestService.call_get(apis.get("get_proj_tasks_statistics_detail", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_proj_tasks_statistics(self, project_id, checker=None):
    """
    接口名称：根据项目id获取项目任务统计数据（任务总数、完成数）
    接口地址：/plan/$VERSION$/task/statistics/{project_id}
    """
    r = RequestService.call_get(apis.get("get_proj_tasks_statistics", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def copy_template_task(self, project_id,template_id, checker=None):
    """
    接口名称：拷贝项目模版任务数据
    接口地址：/plan/$VERSION$/task/template/copy
    """
    r = RequestService.call_post(apis.get("copy_template_task"), json={
        "parentID": "",
        "projectId": project_id,  # 项目ID - required: False
        "task_ids": "",
        "templateId": template_id,  # 项目模版ID - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']


def get_task_by_id(self, task_id, checker=None):
    """
    接口名称：获取计划详细信息
    接口地址：/plan/$VERSION$/task/{id}
    """
    r = RequestService.call_get(apis.get("get_task_by_id", task_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_task(self, name,task_id, project_id, checker=None):
    """
    接口名称：修改任务
    接口地址：/plan/$VERSION$/task/{id}
    """
    r = RequestService.call_put(apis.get("update_task", task_id),
                                json={"stageFlag": 0, "name": name, "startDate": "",
                                      "finishDate": "", "milestoneFlag": "0", "state": "PENDING", "criticalFlag": 0,
                                      "canBeCutted": 1, "belongStageName": "", "testAAA": "0",
                                      "flexAttrs": {"testAAA": "0", "testTest": None}, "description": "",
                                      "percentComplete": "0", "projectId": project_id,
                                      "parentId": "-1", "actualFinishDate": "", "workload": "40", "duration": "5",
                                      "resAssignments": "MEMBER", "sop": "", "taskInput": "", "taskOutput": "",
                                      "testTest": None, "taskMemberList": [{"roleKey": "PARTICIPANTS", "userId": ""},
                                                                           {"roleKey": "HANDLEPERSON",
                                                                            "userId": "SYS_E39B20EA11E7A81AC85B767C89C1"}],
                                      "summaryFlag": "0"})
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def add_checklist(self, objectId, name, source, auditingFlag, deliverableFlag, state, foldId=None, attachmentId=None,
                  processId=None, checker=None):
    """
    接口名称：添加检查项
    接口地址：/plan/$VERSION$/task/{id}/checklist
    """
    r = RequestService.call_post(apis.get("add_checklist", objectId), params={
        "attachmentId": attachmentId,  # 文档ID - required: False
        "auditingFlag": auditingFlag,
        "deliverableFlag": deliverableFlag,  # 是否交付件（0：否；1：是） - required: False
        "foldId": foldId,  # 附件所属文件夹 - required: False
        "name": name,  # 名称 - required: False
        "objectId": objectId,  # 检查项关联的对象id - required: False
        "processId": processId,  # 流程id - required: False
        "source": source,  # 来源 - required: False
        "state": state,  # 状态（ default[0];完成[1];关闭[2]） - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_task_children(self, task_id, checker=None):
    """
    接口名称：获取子任务
    接口地址：/plan/$VERSION$/task/{id}/children
    """
    r = RequestService.call_get(apis.get("get_task_children", task_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_labels(self, task_id, labelIds, checker=None):
    """
    接口名称：添加标签
    接口地址：/plan/$VERSION$/task/{id}/labels
    """
    r = RequestService.call_post(apis.get("add_labels", task_id), params={
        "labelIds": labelIds  # 标签ID串 - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delete_labels(self, task_id, labelIds, checker=None):
    """
    接口名称：删除标签
    接口地址：/plan/$VERSION$/task/{id}/labels/{labelIds}
    """
    r = RequestService.call_delete(apis.get("delete_labels", task_id, labelIds))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def add_member(self, task_id, userId, roleKey, checker=None):
    """
    接口名称：添加计划成员
    接口地址：/plan/$VERSION$/task/{id}/members
    """
    r = RequestService.call_put(apis.get("add_member", task_id), json=[
        {
            "roleKey": roleKey,
            "userId": userId,
        }
    ])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delete_member(self, task_id, userid, checker=None):
    """
    接口名称：删除计划成员
    接口地址：/plan/$VERSION$/task/{id}/members/{memberIds}
    """
    r = RequestService.call_delete(apis.get("delete_member", task_id, userid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def edit_sort_task(self, task_id, childtask_id1, childtask_id2, checker=None):
    """
    接口名称：拖拽排序子任务
    接口地址：/plan/$VERSION$/task/{id}/order
    """
    r = RequestService.call_put(apis.get("edit_sort_task", task_id), json=[
        childtask_id1, childtask_id2
    ])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def add_task_predecessorLink(self, task_id, task1id, checker=None):
    """
    接口名称：添加前置任务，不支持批量添加
    接口地址：/plan/$VERSION$/task/{id}/predecessorLink
    """
    r = RequestService.call_put(apis.get("add_task_predecessorLink", task_id), json={
        "predecessorLink": "{\"PredecessorUID\":\"" + task1id + "\",\"Type\":\"1\",\"LinkLag\":\"0\","
                                                                "\"_index\":\"0\",\"_uid\":\"" + task_id + "\"}",
        "task_id": task_id
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def sort_task(self, task_id, sortType, checker=None):
    """
    接口名称：任务排序
    接口地址：/plan/$VERSION$/task/{id}/sort
    """
    r = RequestService.call_put(apis.get("sort_task", task_id), params={
        "sortType": sortType  # 排序方式，取值：moveUp（上移）；moveDown（下移） - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def sync_task_handler(self, project_id, checker=None):
    """
    接口名称：同步任务责任人
    接口地址：/plan/$VERSION$/task/{project_id}/all/members
    """
    r = RequestService.call_put(apis.get("sync_task_handler", project_id), None)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def copy_task(self, eid, task_ids, project_id, type, state, createBy, parentId=None, checker=None):
    """
    接口名称：复制|移动
    接口地址：/plan/$VERSION$/task/{projectId}/copy
    """
    r = RequestService.call_post(apis.get("copy_task", eid), params={
        "createBy": createBy,  # 用户ID - required: False
        "parentId": parentId,  # 父任务ID - required: False
        "projectId": project_id,
        "state": state,  # task状态 - required: False
        "taskIds": task_ids,  # 任务ID串 - required: True
        "type": type,  # 复制/移动[1：复制；2：移动] - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def downgrade_task(self, task_ids, project_id, checker=None):
    """
    接口名称：降级
    接口地址：/plan/$VERSION$/task/{project_id}/downgrade
    """
    r = RequestService.call_post(apis.get("downgrade_task", project_id), params={
        "taskIds": task_ids,  # 任务ID串 - required: True
        "projectId": project_id
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def upgrade_task(self, task_ids, project_id, checker=None):
    """
    接口名称：升级
    接口地址：/plan/$VERSION$/task/{project_id}/upgrade
    """
    r = RequestService.call_post(apis.get("upgrade_task", project_id), params={
        "taskIds": task_ids,  # 任务ID串 - required: True
        "projectId": project_id
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_tasklist(self, project_id, checker=None):
    """
    接口名称：批量创建子任务时获取任务列表，来关联父任务
    接口地址：/plan/$VERSION$/taskList
    """
    r = RequestService.call_get(apis.get("get_tasklist"), params={
        "projectId": project_id  # 项目ID - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_tasks(self, project_id, page_size=10, page_index=1, isFirstFloor="true", sortBy=None, orderBy=None,
              checker=None):
    """
    接口名称：获取任务列表（项目下）
    接口地址：/plan/$VERSION$/tasks
    """
    r = RequestService.call_get(apis.get("get_tasks"), params={
        "orderBy": orderBy,  # 排序字段（默认order_code，要对所属项目名称排序时传project_name） - required: False
        "projectId": project_id,  # 项目ID - required: False
        "sortBy": sortBy,  # 排序方式（DESC或ASC，排序字段不是order_code时默认DESC） - required: False
        "pagesize": page_size,
        "pageindex": page_index,
        "isFirstFloor": isFirstFloor
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_all_task_doc(self, project_id, deliverableFlag, page_index=1, page_size=20, checker=None):
    """
    接口名称：获取项目下所有任务的交付件
    接口地址：/plan/$VERSION$/tasks/doc/{id}
    """
    r = RequestService.call_get(apis.get("get_all_task_doc", project_id), params={
        "deliverableFlag": deliverableFlag,
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 页大小 - required: False
        "projectId": project_id
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_first_tasklist(self, project_id, checker=None):
    """
    接口名称：根据项目id获取一级任务列表
    接口地址：/plan/$VERSION$/tasks/getOneTaskList
    """
    r = RequestService.call_get(apis.get("get_first_tasklist"), params={
        "projectId": project_id  # 项目ids,多个id用逗号分隔 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_task_me(self, project_id, page_index=1, page_size=20, checker=None):
    """
    接口名称：获取任务列表（个人工作台）
    接口地址：/plan/$VERSION$/tasks/me
    """
    r = RequestService.call_get(apis.get("get_task_me"), params={
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 页大小 - required: False
        "projectId": project_id,  # 项目ID - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_tasks_by_uid(self, userid, type, checker=None):
    """
    接口名称：获取责任人下的当前任务或要做任务
    接口地址：/plan/$VERSION$/tasks/member/{member}
    """
    r = RequestService.call_get(apis.get("get_tasks_by_uid", userid), params={
        "type": type  # 根据责任人id【0.获取任务列表(默认);1.获取当前任务列表;2.获取将要做的任务列表】 - required: True
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_tasks_page(self, project_id, page_index=1, page_size=20, checker=None):
    """
    接口名称：获取项目任务列表（分页）
    接口地址：/plan/$VERSION$/tasks/page
    """
    r = RequestService.call_get(apis.get("get_tasks_page"), params={
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 页大小 - required: False
        "projectId": project_id,  # 项目ID - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delete_task_by_id_list(self, project_id, task_id, checker=None):
    """
    接口名称：根据ids批量删除任务
    接口地址：/plan/$VERSION$/tasks/projectId
    """
    r = RequestService.call_delete(apis.get("delete_task_by_id_list"),
                                   json={"projectId": project_id,
                                         "taskIds": task_id})
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_tasks_by_source_id(self, sourceids, project_id, sourceObjName, checker=None):
    """
    接口名称：根据来源ID获取任务
    接口地址：/plan/$VERSION$/tasks/source/{sourceids}
    """
    r = RequestService.call_get(apis.get("get_tasks_by_source_id", sourceids), params={
        "projectId": project_id,  # 项目id - required: False
        "sourceObjName": sourceObjName,  # 来源名称 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_undone_task(self, project_id, checker=None):
    """
    接口名称：查询未完成任务
    接口地址：/plan/$VERSION$/tasks/undone/{project_id}
    """
    r = RequestService.call_get(apis.get("get_undone_task", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_first_level_child_tasks(self, task_id, checker=None):
    """
    接口名称：根据任务id获取第一层子任务列表
    接口地址：/plan/$VERSION$/tasks/{id}/children
    """
    r = RequestService.call_get(apis.get("get_first_level_child_tasks", task_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delete_task_predecessor_link(self, task_id, linkIdList, checker=None):
    """
    接口名称：删除任务前置依赖
    接口地址：/plan/$VERSION$/tasks/{id}/predecessorLink
    """
    r = RequestService.call_delete(apis.get("delete_task_predecessor_link", task_id), json=[
        linkIdList
    ])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def delete_task_by_id(self, project_id, task_id, checker=None):
    """
    接口名称：删除计划
    接口地址：/plan/$VERSION$/tasks/{project_id}
    """
    r = RequestService.call_delete(apis.get("delete_task_by_id", project_id), json=[
        task_id  # 任务Id列表 - required: False
    ])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def export_business_template(self, businessType, exprotList, viewid, isFilter="false", mgReqFlag="false",
                             exportIdList=None):
    """
    接口名称：导出业务数据模板
    接口地址：/plan/$VERSION$/template/export
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
        with open(dir_document + r"\export_task_tem_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def query_tree_list_by_ids(self, project_id, checker=None):
    """
    接口名称：根据ID列表查询对象详细信息
    接口地址：/plan/$VERSION$/tree/{ids}
    """
    r = RequestService.call_get(apis.get("query_tree_list_by_ids", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def close_task(self, task_id, checker=None):
    """
    接口名称：任务关闭接口
    接口地址：/plan/$VERSION$/{id}/close
    """
    r = RequestService.call_put(apis.get("close_task", task_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def close_validate(self, task_id, checker=None):
    """
    接口名称：任务关闭校验接口
    接口地址：/plan/$VERSION$/{id}/close/validate
    """
    r = RequestService.call_get(apis.get("close_validate", task_id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

def get_critical_flag_task(self, project_id, checker=None):
    """
    接口名称：判断task及其子是否是其他task的前置任务
    接口地址：/plan/$VERSION$/{project_id}/critical
    """
    r = RequestService.call_get(apis.get("get_critical_flag_task", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def select_business_table(self, viewid, project_id, mgReqFlag="false", page_index=1, page_size=20, checker=None):
    """
    接口名称：查询业务表格列
    接口地址：/plan/$VERSION$/{viewid}/businessTable
    """
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer " + commonServer.get_token()
    }
    r = RequestService.call_post(apis.get("select_business_table", viewid), json={
        "mgReqFlag": mgReqFlag,
        "pageindex": page_index,
        "pagesize": page_size,
        "projectId": project_id
    }, headers=headers)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def select_business_list(self, viewid, mgReqFlag="true", page_index=1, page_size=20, project_id=None, checker=None):
    """
    接口名称：查询业务数据
    接口地址：/plan/$VERSION$/{viewid}/businesslist
    """
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer " + commonServer.get_token()
    }
    r = RequestService.call_post(apis.get("select_business_list", viewid), json={
        "mgReqFlag": mgReqFlag,
        "pageindex": page_index,
        "pagesize": page_size,
        "projectId": project_id
    }, headers=headers)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def select_filterlist(self, viewid, mgReqFlag="true", page_index=1, page_size=20, project_id=None, checker=None):
    """
    接口名称：过滤业务数据
    接口地址：/plan/$VERSION$/{viewid}/filterlist
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
            "businessType": "erd.cloud.plan.dto.EtTask",
            "conditionRef": "and",
            "contextType": "3",
            "id": viewid,
            "selectedFields": "59,60,41,30,37,36,503,505,500,32,33,34,35,47,49,46",
        },
        "mgReqFlag": mgReqFlag,
        "pageindex": page_index,
        "pagesize": page_size,
        "projectId": project_id
    }, headers=headers)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def release_plan_comfirm(self, viewid, project_id, mgReqFlag="false", checker=None):
    """
    接口名称：发布计划前判断是否可以发布
    接口地址：/plan/$VERSION$/{viewid}/releasePlanComfirm
    """
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer " + commonServer.get_token()
    }
    r = RequestService.call_post(apis.get("release_plan_comfirm", viewid), json={
        "projectId": project_id,
        "mgReqFlag": mgReqFlag
    }, headers=headers)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

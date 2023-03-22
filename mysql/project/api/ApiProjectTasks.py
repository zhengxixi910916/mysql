from erdcloud.HttpClient import RequestService, commonServer
from erdcloud.erdApi import Api

apis = Api({
    "createDeliversUsingPOST": "/plan/$VERSION$/add/delivers",  # 添加交付物
    "batchOperateUsingPUT": "/plan/$VERSION$/batchOperate",  # 批量执行/完成任务
    "getBdchartUsingGET": "/plan/$VERSION$/bdchart/{id}",  # 获取项目燃尽图
    "checkTaskStartFinishTimeUsingGET": "/plan/$VERSION$/checkTaskStartFinishTime",  # 校验任务的开始和结束时间
    "closeUsingPOST_1": "/plan/$VERSION$/close",  # 流程配置调用任务关闭接口
    "cutTaskByIdsUsingDELETE": "/plan/$VERSION$/cut",  # 裁剪计划
    "deleteDurationrecordUsingDELETE": "/plan/$VERSION$/delete/record/{id}",  # 删除工时登记
    "deleteDeliverUsingDELETE": "/plan/$VERSION$/delete/taskdeliver/{id}",  # 删除交付物
    "replaceCheckUsingPOST": "/plan/$VERSION$/deliver/replace",  # 替换交付件
    "getDurationByConfigUsingGET": "/plan/$VERSION$/duration",  # 根据日历配置计算工期或计划时间
    "findUserDurationRecordsUsingGET": "/plan/$VERSION$/duration/record/{startDate}/{endDate}",  # 获取用户工时
    "addDurationrecordUsingPOST": "/plan/$VERSION$/durationrecord",  # 添加工时选项卡登记
    "getDurationrecordUsingGET": "/plan/$VERSION$/durationrecord/{id}",  # 获取工时选项卡
    "executeTaskUsingPUT": "/plan/$VERSION$/executetask/{id}",  # 责任人开始执行任务
    "getParentEtTaskByIdUsingGET": "/plan/$VERSION$/getParentTaskById/{taskId}",  # 通过任务id获取最顶层的父
    "getBusinessTypeCountUsingGET_3": "/plan/$VERSION$/item/count/{id}",  # 获取计划的相关项的条目数
    "queryListByIdsUsingGET_3": "/plan/$VERSION$/list/{ids}",  # 根据ID列表查询对象列表
    "getMchartUsingGET": "/plan/$VERSION$/mchart/{id}",  # 获取项目成员完成状况
    "exportMchartUsingGET": "/plan/$VERSION$/mchartexport/{projectId}",  # 导出项目概况统计报表
    "taskMemberCheckUsingGET": "/plan/$VERSION$/member/check",  # 计划成员修正
    "milestoneUpdateBatchUsingPOST": "/plan/$VERSION$/milestone",  # 里程碑变更
    "careMyProjectUsingPOST_4": "/plan/$VERSION$/myCare",  # 收藏/取消收藏
    "getOneDurationrecordUsingGET": "/plan/$VERSION$/one/durationrecord/{id}",  # 单个登记卡信息
    "syncPercentUsingPUT": "/plan/$VERSION$/percent/sync",  # 全局刷新计划百分比
    "getPredecessorTaskByTaskIdUsingPUT": "/plan/$VERSION$/predecessor",  # 判断task及其子是否是其他task的前置任务
    "predecessorLinkRefreshUsingPUT": "/plan/$VERSION$/predecessorLink/project/{id}",  # 刷新项目下所有后置依赖任务计划时间
    "updateStateFlowMembersUsingPUT_4": "/plan/$VERSION$/stateflow/members",  # 修改状态流程成员
    "addTaskUsingPOST_1": "/plan/$VERSION$/task",  # 创建任务
    "updateCheckListUsingPUT_2": "/plan/$VERSION$/task/checklist",  # 修改检查项
    "deleteCheckItemsUsingPUT": "/plan/$VERSION$/task/checklist/",  # 删除检查项批量删除检查项
    "updateTemplateAttachmentUsingPUT": "/plan/$VERSION$/task/checklist/templateAttachment",  # 修改检查项模板文件
    "updateCheckLisFolderUsingPUT": "/plan/$VERSION$/task/checklistFolder/{id}",  # 修改检查项文件夹
    "editBatchUsingPUT_2": "/plan/$VERSION$/task/editBatch",  # 批量编辑任务,不支持跨项目编辑
    "editBatchResponsibilityUsingPUT": "/plan/$VERSION$/task/editBatchResponsibility",  # 批量转责任人
    "insertBatchUsingPUT_3": "/plan/$VERSION$/task/insertBatch",  # 批量添加任务
    "milestoneUsingGET": "/plan/$VERSION$/task/milestone/{projectId}",  # 获取里程碑数据
    "getProjectTasksStatisticsDetailByProjectIdUsingGET": "/plan/$VERSION$/task/statistics/detail/{projectId}",
    # 根据项目id获取项目任务统计数据详情
    "getProjectTasksStatisticsByProjectIdUsingGET": "/plan/$VERSION$/task/statistics/{projectId}",
    # 根据项目id获取项目任务统计数据（任务总数、完成数）
    "copyTaskTemplateUsingPOST": "/plan/$VERSION$/task/template/copy",  # 拷贝项目模版任务数据
    "getTaskByIdUsingGET": "/plan/$VERSION$/task/%s",  # 获取计划详细信息
    "updateTaskUsingPUT": "/plan/$VERSION$/task/%s",  # 修改任务
    "searchBusinessUsingGET": "/plan/$VERSION$/task/{id}/businesses",  # 查询关联的需求、问题、风险列表
    "addBusinessUsingPOST": "/plan/$VERSION$/task/{id}/businesslink",  # 添加关联需求、问题、风险
    "removeBusinessUsingDELETE": "/plan/$VERSION$/task/{id}/businesslink",  # 删除关联需求、问题、风险
    "searchBusinessUsingGET_1": "/plan/$VERSION$/task/{id}/candidatebusinesses",  # 搜索可以关联的需求、问题、风险
    "addCheckItemUsingPOST_1": "/plan/$VERSION$/task/{id}/checklist",  # 添加检查项
    "getChildByIdUsingGET_1": "/plan/$VERSION$/task/{id}/children",  # 获取子任务
    "addLabelRelationUsingPOST": "/plan/$VERSION$/task/{id}/labels",  # 添加标签
    "deleteLabelRelationUsingDELETE": "/plan/$VERSION$/task/{id}/labels/{labelIds}",  # 删除标签
    "addMembersUsingPUT_2": "/plan/$VERSION$/task/{id}/members",  # 添加计划成员
    "deleteMemberUsingDELETE_2": "/plan/$VERSION$/task/{id}/members/{memberIds}",  # 删除计划成员
    "editSortUsingPUT": "/plan/$VERSION$/task/{id}/order",  # 拖拽排序子任务
    "updateTaskPredecessorLinkUsingPUT": "/plan/$VERSION$/task/{id}/predecessorLink",  # 添加前置任务，不支持批量添加
    "taskSortUsingPUT": "/plan/$VERSION$/task/{id}/sort",  # 任务排序
    "synchroTaskHandlerUsingPUT": "/plan/$VERSION$/task/{projectId}/all/members",  # 同步任务责任人
    "copyTaskUsingPOST_2": "/plan/$VERSION$/task/{projectId}/copy",  # 复制|移动
    "downgradeUsingPOST": "/plan/$VERSION$/task/{projectId}/downgrade",  # 降级
    "upgradeUsingPOST": "/plan/$VERSION$/task/{projectId}/upgrade",  # 升级
    "getTaskListUsingGET": "/plan/$VERSION$/taskList",  # 批量创建子任务时获取任务列表，来关联父任务
    "getTasksUsingGET_1": "/plan/$VERSION$/tasks",  # 获取任务列表（项目下）
    "getAllTaskDocUsingGET": "/plan/$VERSION$/tasks/doc/{id}",  # 获取项目下所有任务的交付件
    "getOneTaskListUsingGET": "/plan/$VERSION$/tasks/getOneTaskList",  # 根据项目id获取一级任务列表
    "getTasksMeUsingGET": "/plan/$VERSION$/tasks/me",  # 获取任务列表（个人工作台）
    "getTasksByUserIdUsingGET": "/plan/$VERSION$/tasks/member/{member}",  # 获取责任人下的当前任务或要做任务
    "getTasksPageUsingGET": "/plan/$VERSION$/tasks/page",  # 获取项目任务列表（分页）
    "deleteTaskByIdListUsingDELETE": "/plan/$VERSION$/tasks/projectId",  # 根据ids批量删除任务
    "getTasksBySourceIdUsingGET": "/plan/$VERSION$/tasks/source/{sourceids}",  # 根据来源ID获取任务
    "getPlanUndoneUsingGET": "/plan/$VERSION$/tasks/undone/{projectId}",  # 查询未完成任务
    "getFirstLevelChildrenTasksByTaskIdUsingGET_1": "/plan/$VERSION$/tasks/{id}/children",  # 根据任务id获取第一层子任务列表
    "deleteTaskPredecessorLinkUsingDELETE": "/plan/$VERSION$/tasks/{id}/predecessorLink",  # 删除任务前置依赖
    "deleteTaskByIdsUsingDELETE": "/plan/$VERSION$/tasks/{projectId}",  # 删除计划
    "queryTreeListByIdsUsingGET": "/plan/$VERSION$/tree/{ids}",  # 根据ID列表查询对象详细信息
    "updateDurationrecordUsingPUT": "/plan/$VERSION$/update/durationrecord",  # 更新工时选项卡登记
    "closeUsingPUT": "/plan/$VERSION$/{id}/close",  # 任务关闭接口
    "closeValidateUsingGET": "/plan/$VERSION$/{id}/close/validate",  # 任务关闭校验接口
    "getCriticalFlagTaskUsingGET": "/plan/$VERSION$/{projectId}/critical",  # 判断task及其子是否是其他task的前置任务
    "getRequireSelectListUsingGET": "/req/$VERSION$/baseline/requires/selectlist",  # 需求树-selectlist
    "getRequireTreeListUsingGET": "/req/$VERSION$/baseline/requires/treelist",  # 需求树-list
    "snapshotUsingGET": "/req/$VERSION$/baseline/snapshot/{id}",  # 快照需求对象基本信息详情查询
})


def create_delivers_using_post(self, checker=None):
    """
    接口名称：添加交付物
    接口地址：/plan/$VERSION$/add/delivers
    """
    r = RequestService.call_post(apis.get("createDeliversUsingPOST", None), json={
        "etTaskDeliverVos": ""  # 交付物id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def batch_operate_using_put(self, plan_id_list, operate_type, checker=None):
    """
    接口名称：批量执行/完成任务
    接口地址：/plan/$VERSION$/batchOperate
    """
    r = RequestService.call_put(apis.get("batchOperateUsingPUT", None),
                                json={
                                    "taskIdList": plan_id_list,
                                    "operateType": operate_type
                                })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_bdchart_using_get(self, checker=None):
    """
    接口名称：获取项目燃尽图
    接口地址：/plan/$VERSION$/bdchart/{id}
    """
    r = RequestService.call_get(apis.get("getBdchartUsingGET", None), path={
        "id": ""  # 项目ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def check_task_start_finish_time_using_get(self, checker=None):
    """
    接口名称：校验任务的开始和结束时间
    接口地址：/plan/$VERSION$/checkTaskStartFinishTime
    """
    r = RequestService.call_get(apis.get("checkTaskStartFinishTimeUsingGET", None), json={
        "taskId": ""  # taskId - required: False
    }, params={
        "finishTime": "",  # finishTime - required: False
        "startTime": "",  # startTime - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def close_using_post_1(self, checker=None):
    """
    接口名称：流程配置调用任务关闭接口
    接口地址：/plan/$VERSION$/close
    """
    r = RequestService.call_post(apis.get("closeUsingPOST_1", None), json={
        "params": ""  # params - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def cut_task_by_ids_using_delete(self, checker=None):
    """
    接口名称：裁剪计划
    接口地址：/plan/$VERSION$/cut
    """
    r = RequestService.call_delete(apis.get("cutTaskByIdsUsingDELETE", None), json={
        "taskIdList": ""  # 任务Id列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_durationrecord_using_delete(self, checker=None):
    """
    接口名称：删除工时登记
    接口地址：/plan/$VERSION$/delete/record/{id}
    """
    r = RequestService.call_delete(apis.get("deleteDurationrecordUsingDELETE", None), path={
        "id": ""  # 登记工时id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_deliver_using_delete(self, checker=None):
    """
    接口名称：删除交付物
    接口地址：/plan/$VERSION$/delete/taskdeliver/{id}
    """
    r = RequestService.call_delete(apis.get("deleteDeliverUsingDELETE", None), path={
        "id": ""  # 交付物id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def replace_check_using_post(self, checker=None):
    """
    接口名称：替换交付件
    接口地址：/plan/$VERSION$/deliver/replace
    """
    r = RequestService.call_post(apis.get("replaceCheckUsingPOST", None), json={
        "params": ""  # params - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_duration_by_config_using_get(self, checker=None):
    """
    接口名称：根据日历配置计算工期或计划时间
    接口地址：/plan/$VERSION$/duration
    """
    r = RequestService.call_get(apis.get("getDurationByConfigUsingGET", None), params={
        "duration": "",  # 工期 - required: False
        "finishDate": "",  # 任务结束时间 - required: False
        "projectId": "",  # 项目id - required: False
        "startDate": "",  # 任务开始时间 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def find_user_duration_records_using_get(self, checker=None):
    """
    接口名称：获取用户工时
    接口地址：/plan/$VERSION$/duration/record/{startDate}/{endDate}
    """
    r = RequestService.call_get(apis.get("findUserDurationRecordsUsingGET", None), params={
        "userId": ""  # 用户id，可不填 - required: False
    }, path={
        "endDate": "",  # 结束时间 - required: True
        "startDate": "",  # 开始时间 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_durationrecord_using_post(self, checker=None):
    """
    接口名称：添加工时选项卡登记
    接口地址：/plan/$VERSION$/durationrecord
    """
    r = RequestService.call_post(apis.get("addDurationrecordUsingPOST", None), params={
        "createBy": "",  # 创建者 - required: False
        "createTime": "",  # 创建时间 - required: False
        "delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "description": "",  # 工作内容 - required: False
        "difference": "",  # 登记偏差 - required: False
        "duration": "",  # 预估工时 - required: False
        "id": "",  # 对象Id - required: False
        "registeredTime": "",  # 登记时长 - required: False
        "remainDuration": "",  # 剩余工时 - required: False
        "startDate": "",  # 开始时间 - required: False
        "sumId": "",  # 关联业务对象的id - required: False
        "updateBy": "",  # 更新者 - required: False
        "updateTime": "",  # 更新时间 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_durationrecord_using_get(self, checker=None):
    """
    接口名称：获取工时选项卡
    接口地址：/plan/$VERSION$/durationrecord/{id}
    """
    r = RequestService.call_get(apis.get("getDurationrecordUsingGET", None), path={
        "id": ""  # 任务id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def execute_task_using_put(self, checker=None):
    """
    接口名称：责任人开始执行任务
    接口地址：/plan/$VERSION$/executetask/{id}
    """
    r = RequestService.call_put(apis.get("executeTaskUsingPUT", None), json={
        "task": ""  # 任务对象 - required: False
    }, path={
        "id": ""  # 任务id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_parent_et_task_by_id_using_get(self, checker=None):
    """
    接口名称：通过任务id获取最顶层的父
    接口地址：/plan/$VERSION$/getParentTaskById/{taskId}
    """
    r = RequestService.call_get(apis.get("getParentEtTaskByIdUsingGET", None), path={
        "taskId": ""  # taskId - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_business_type_count_using_get_3(self, checker=None):
    """
    接口名称：获取计划的相关项的条目数
    接口地址：/plan/$VERSION$/item/count/{id}
    """
    r = RequestService.call_get(apis.get("getBusinessTypeCountUsingGET_3", None), params={
        "cttType": "",  # 基线标识 - required: True
        "itemList": "",  # 业务条目:(task,discuss,relation,activity,check,attachment,property,elflow)，逗号隔开 - required: True
    }, path={
        "id": ""  # 业务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_list_by_ids_using_get_3(self, checker=None):
    """
    接口名称：根据ID列表查询对象列表
    接口地址：/plan/$VERSION$/list/{ids}
    """
    r = RequestService.call_get(apis.get("queryListByIdsUsingGET_3", None), path={
        "ids": ""  # ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_mchart_using_get(self, checker=None):
    """
    接口名称：获取项目成员完成状况
    接口地址：/plan/$VERSION$/mchart/{id}
    """
    r = RequestService.call_get(apis.get("getMchartUsingGET", None), params={
        "month": ""  # 月份(yyyy-MM) - required: False
    }, path={
        "id": ""  # 项目ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def export_mchart_using_get(self, checker=None):
    """
    接口名称：导出项目概况统计报表
    接口地址：/plan/$VERSION$/mchartexport/{projectId}
    """
    r = RequestService.call_get(apis.get("exportMchartUsingGET", None), params={
        "month": ""  # 月份(yyyy-MM) - required: False
    }, path={
        "projectId": ""  # 项目ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def task_member_check_using_get(self, checker=None):
    """
    接口名称：计划成员修正
    接口地址：/plan/$VERSION$/member/check
    """
    r = RequestService.call_get(apis.get("taskMemberCheckUsingGET", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def milestone_update_batch_using_post(self, checker=None):
    """
    接口名称：里程碑变更
    接口地址：/plan/$VERSION$/milestone
    """
    r = RequestService.call_post(apis.get("milestoneUpdateBatchUsingPOST", None), json={
        "params": ""  # 流程业务对象 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def care_my_project_using_post_4(self, checker=None):
    """
    接口名称：收藏/取消收藏
    接口地址：/plan/$VERSION$/myCare
    """
    r = RequestService.call_post(apis.get("careMyProjectUsingPOST_4", None), params={
        "id": "",  # id - required: True
        "name": "",  # 名称 - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_one_durationrecord_using_get(self, checker=None):
    """
    接口名称：单个登记卡信息
    接口地址：/plan/$VERSION$/one/durationrecord/{id}
    """
    r = RequestService.call_get(apis.get("getOneDurationrecordUsingGET", None), path={
        "id": ""  # 选项卡id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def sync_percent_using_put(self, checker=None):
    """
    接口名称：全局刷新计划百分比
    接口地址：/plan/$VERSION$/percent/sync
    """
    r = RequestService.call_put(apis.get("syncPercentUsingPUT", None), None)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_predecessor_task_by_task_id_using_put(self, checker=None):
    """
    接口名称：判断task及其子是否是其他task的前置任务
    接口地址：/plan/$VERSION$/predecessor
    """
    r = RequestService.call_put(apis.get("getPredecessorTaskByTaskIdUsingPUT", None), json={
        "taskIds": ""  # 计划Id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def predecessor_link_refresh_using_put(self, checker=None):
    """
    接口名称：刷新项目下所有后置依赖任务计划时间
    接口地址：/plan/$VERSION$/predecessorLink/project/{id}
    """
    r = RequestService.call_put(apis.get("predecessorLinkRefreshUsingPUT", None), path={
        "id": ""  # 项目id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_state_flow_members_using_put_4(self, checker=None):
    """
    接口名称：修改状态流程成员
    接口地址：/plan/$VERSION$/stateflow/members
    """
    r = RequestService.call_put(apis.get("updateStateFlowMembersUsingPUT_4", None), json={
        "members": ""  # members - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_task_using_post_1(self, data, checker=None):
    """
    接口名称：创建任务
    接口地址：/plan/$VERSION$/task
    """
    headers = commonServer.get_headers()
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
    r = RequestService.call_post(apis.get("addTaskUsingPOST_1", None),
                                 headers=headers,
                                 data=data
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r['res']['data']


def update_check_list_using_put_2(self, checker=None):
    """
    接口名称：修改检查项
    接口地址：/plan/$VERSION$/task/checklist
    """
    r = RequestService.call_put(apis.get("updateCheckListUsingPUT_2", None), json={
        "checkItems": ""  # 任务检查项列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_check_items_using_put(self, checker=None):
    """
    接口名称：删除检查项批量删除检查项
    接口地址：/plan/$VERSION$/task/checklist/
    """
    r = RequestService.call_put(apis.get("deleteCheckItemsUsingPUT", None), json={
        "list": ""  # 任务检查项列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_template_attachment_using_put(self, checker=None):
    """
    接口名称：修改检查项模板文件
    接口地址：/plan/$VERSION$/task/checklist/templateAttachment
    """
    r = RequestService.call_put(apis.get("updateTemplateAttachmentUsingPUT", None), json={
        "checkItems": ""  # 任务检查项列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_check_lis_folder_using_put(self, checker=None):
    """
    接口名称：修改检查项文件夹
    接口地址：/plan/$VERSION$/task/checklistFolder/{id}
    """
    r = RequestService.call_put(apis.get("updateCheckLisFolderUsingPUT", None), json={
        "checklist": ""  # 任务检查项列表 - required: False
    }, path={
        "id": ""  # 任务ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def edit_batch_using_put_2(self, checker=None):
    """
    接口名称：批量编辑任务,不支持跨项目编辑
    接口地址：/plan/$VERSION$/task/editBatch
    """
    r = RequestService.call_put(apis.get("editBatchUsingPUT_2", None), json={
        "taskList": ""  # 任务列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def edit_batch_responsibility_using_put(self, task_id1, task_id2, project_id,checker=None):
    """
    接口名称：批量修改责任人
    接口地址：/plan/$VERSION$/task/editBatchResponsibility
    """
    r = RequestService.call_put(apis.get("editBatchResponsibilityUsingPUT", None), json=
    [{"id": task_id1,
      "taskMemberList": [{"userId": "SYS_E39B20EA11E7A81AC85B767C89C1", "roleKey": "HANDLEPERSON"}],
      "projectId": project_id}, {"id": task_id2, "taskMemberList": [
        {"userId": "SYS_E39B20EA11E7A81AC85B767C89C1", "roleKey": "HANDLEPERSON"}],
                                                         "projectId": project_id}])
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def insert_batch_using_put_3(self, checker=None):
    """
    接口名称：批量添加任务
    接口地址：/plan/$VERSION$/task/insertBatch
    """
    r = RequestService.call_put(apis.get("insertBatchUsingPUT_3", None), json={
        "tasks": ""  # 任务列表 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def milestone_using_get(self, checker=None):
    """
    接口名称：获取里程碑数据
    接口地址：/plan/$VERSION$/task/milestone/{projectId}
    """
    r = RequestService.call_get(apis.get("milestoneUsingGET", None), path={
        "projectId": ""  # 项目id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_project_tasks_statistics_detail_by_project_id_using_get(self, checker=None):
    """
    接口名称：根据项目id获取项目任务统计数据详情
    接口地址：/plan/$VERSION$/task/statistics/detail/{projectId}
    """
    r = RequestService.call_get(apis.get("getProjectTasksStatisticsDetailByProjectIdUsingGET", None), path={
        "projectId": ""  # 项目id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_project_tasks_statistics_by_project_id_using_get(self, checker=None):
    """
    接口名称：根据项目id获取项目任务统计数据（任务总数、完成数）
    接口地址：/plan/$VERSION$/task/statistics/{projectId}
    """
    r = RequestService.call_get(apis.get("getProjectTasksStatisticsByProjectIdUsingGET", None), path={
        "projectId": ""  # 项目id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def copy_task_template_using_post(self, checker=None):
    """
    接口名称：拷贝项目模版任务数据
    接口地址：/plan/$VERSION$/task/template/copy
    """
    r = RequestService.call_post(apis.get("copyTaskTemplateUsingPOST", None), json={
        "taskCopyTemplateDto": ""  # 参数对象 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_task_by_id_using_get(self, task_id, checker=None):
    """
    接口名称：获取计划详细信息
    接口地址：/plan/$VERSION$/task/{id}
    """
    r = RequestService.call_get(apis.get("getTaskByIdUsingGET", task_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_task_using_put(self, plan_id, project_id, checker=None):
    """
    接口名称：修改任务
    接口地址：/plan/$VERSION$/task/{id}
    """

    r = RequestService.call_put(apis.get("updateTaskUsingPUT", plan_id),
                                json={
                                    "stageFlag": 0,
                                    "name": "AutoPlan_update",
                                    "startDate": "",
                                    "finishDate": "",
                                    "milestoneFlag": "0",
                                    "state": "PENDING",
                                    "criticalFlag": 0,
                                    "canBeCutted": 1,
                                    "belongStageName": "",
                                    "description": "",
                                    "percentComplete": "0",
                                    "projectId": project_id,
                                    "parentId": "-1",
                                    "actualFinishDate": "",
                                    "workload": "",
                                    "duration": "",
                                    "resAssignments": "PM",
                                    "sop": "",
                                    "taskInput": "",
                                    "taskOutput": "",
                                    "flexAttrs": {},
                                    "taskMemberList": [
                                        {
                                            "roleKey": "PARTICIPANTS",
                                            "userId": "SYS_E39B20EA11E7A81AC85B767C89C1"
                                        },
                                        {
                                            "roleKey": "HANDLEPERSON",
                                            "userId": "SYS_E39B20EA11E7A81AC85B767C89C1"
                                        }
                                    ],
                                    "summaryFlag": "0"
                                })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def search_business_using_get(self, checker=None):
    """
    接口名称：查询关联的需求、问题、风险列表
    接口地址：/plan/$VERSION$/task/{id}/businesses
    """
    r = RequestService.call_get(apis.get("searchBusinessUsingGET", None), path={
        "id": ""  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_business_using_post(self, checker=None):
    """
    接口名称：添加关联需求、问题、风险
    接口地址：/plan/$VERSION$/task/{id}/businesslink
    """
    r = RequestService.call_post(apis.get("addBusinessUsingPOST", None), json={
        "businessList": ""  # 关联对象 - required: False
    }, path={
        "id": ""  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def remove_business_using_delete(self, checker=None):
    """
    接口名称：删除关联需求、问题、风险
    接口地址：/plan/$VERSION$/task/{id}/businesslink
    """
    r = RequestService.call_delete(apis.get("removeBusinessUsingDELETE", None), params={
        "businessId": "",  # businessId - required: False
        "type": "",  # type,取值：requirement/issue/risk - required: True
    }, path={
        "id": ""  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def search_business_using_get_1(self, checker=None):
    """
    接口名称：搜索可以关联的需求、问题、风险
    接口地址：/plan/$VERSION$/task/{id}/candidatebusinesses
    """
    r = RequestService.call_get(apis.get("searchBusinessUsingGET_1", None), params={
        "name": "",  # name - required: False
        "type": "",  # type,取值：requirement/issue/risk - required: True
    }, path={
        "id": ""  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_check_item_using_post_1(self, checker=None):
    """
    接口名称：添加检查项
    接口地址：/plan/$VERSION$/task/{id}/checklist
    """
    r = RequestService.call_post(apis.get("addCheckItemUsingPOST_1", None), params={
        "attachmentId": "",  # 文档ID - required: False
        "attachmentName": "",  # 文档名称 - required: False
        "auditingFlag": "",  # 是否审核 - required: False
        "createBy": "",  # 创建者 - required: False
        "createTime": "",  # 创建时间 - required: False
        "delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "deliverableFlag": "",  # 是否交付件（0：否；1：是） - required: False
        "description": "",  # 描述 - required: False
        "flexAttrs": "",  # 其它扩展属性 - required: False
        "foldId": "",  # 附件所属文件夹 - required: False
        "id": "",  # 对象Id - required: False
        "members": "",  # 责任人 - required: False
        "name": "",  # 名称 - required: False
        "objectClassName": "",  # 检查项关联对象ClassName - required: False
        "objectId": "",  # 检查项关联的对象id - required: False
        "processDefinitionKey": "",  # 流程Key - required: False
        "processDefinitionName": "",  # 流程名称 - required: False
        "processId": "",  # 流程id - required: False
        "source": "",  # 来源 - required: False
        "state": "",  # 状态（ default[0];完成[1];关闭[2]） - required: False
        "templateAttachmentId": "",  # 检查项模板附件ID - required: False
        "templateId": "",  # task模板ID - required: False
        "updateBy": "",  # 更新者 - required: False
        "updateTime": "",  # 更新时间 - required: False
    }, path={
        "id": ""  # 任务ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_child_by_id_using_get_1(self, checker=None):
    """
    接口名称：获取子任务
    接口地址：/plan/$VERSION$/task/{id}/children
    """
    r = RequestService.call_get(apis.get("getChildByIdUsingGET_1", None), path={
        "id": ""  # 任务ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_label_relation_using_post(self, checker=None):
    """
    接口名称：添加标签
    接口地址：/plan/$VERSION$/task/{id}/labels
    """
    r = RequestService.call_post(apis.get("addLabelRelationUsingPOST", None), params={
        "labelIds": ""  # 标签ID串 - required: True
    }, path={
        "id": ""  # 任务ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_label_relation_using_delete(self, checker=None):
    """
    接口名称：删除标签
    接口地址：/plan/$VERSION$/task/{id}/labels/{labelIds}
    """
    r = RequestService.call_delete(apis.get("deleteLabelRelationUsingDELETE", None), path={
        "id": "",  # 任务ID - required: False
        "labelIds": "",  # 标签ID串 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_members_using_put_2(self, checker=None):
    """
    接口名称：添加计划成员
    接口地址：/plan/$VERSION$/task/{id}/members
    """
    r = RequestService.call_put(apis.get("addMembersUsingPUT_2", None), json={
        "taskMemberList": ""  # EtTaskMember对象列表 - required: True
    }, path={
        "id": ""  # 任务ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_member_using_delete_2(self, checker=None):
    """
    接口名称：删除计划成员
    接口地址：/plan/$VERSION$/task/{id}/members/{memberIds}
    """
    r = RequestService.call_delete(apis.get("deleteMemberUsingDELETE_2", None), path={
        "id": "",  # 任务ID - required: False
        "memberIds": "",  # 成员id串 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def edit_sort_using_put(self, checker=None):
    """
    接口名称：拖拽排序子任务
    接口地址：/plan/$VERSION$/task/{id}/order
    """
    r = RequestService.call_put(apis.get("editSortUsingPUT", None), json={
        "taskId": ""  # 拖拽子任务ID - required: False
    }, path={
        "id": ""  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_task_predecessor_link_using_put(self, checker=None):
    """
    接口名称：添加前置任务，不支持批量添加
    接口地址：/plan/$VERSION$/task/{id}/predecessorLink
    """
    r = RequestService.call_put(apis.get("updateTaskPredecessorLinkUsingPUT", None), json={
        "task": ""  # 任务对象 - required: False
    }, path={
        "id": ""  # 任务id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def task_sort_using_put(self, checker=None):
    """
    接口名称：任务排序
    接口地址：/plan/$VERSION$/task/{id}/sort
    """
    r = RequestService.call_put(apis.get("taskSortUsingPUT", None), params={
        "sortType": ""  # 排序方式，取值：moveUp（上移）；moveDown（下移） - required: False
    }, path={
        "id": ""  # 任务ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def synchro_task_handler_using_put(self, checker=None):
    """
    接口名称：同步任务责任人
    接口地址：/plan/$VERSION$/task/{projectId}/all/members
    """
    r = RequestService.call_put(apis.get("synchroTaskHandlerUsingPUT", None), path={
        "projectId": ""  # 项目id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def copy_task_using_post_2(self, checker=None):
    """
    接口名称：复制|移动
    接口地址：/plan/$VERSION$/task/{projectId}/copy
    """
    r = RequestService.call_post(apis.get("copyTaskUsingPOST_2", None), params={
        "createBy": "",  # 用户ID - required: False
        "parentId": "",  # 父任务ID - required: False
        "state": "",  # task状态 - required: False
        "taskIds": "",  # 任务ID串 - required: True
        "type": "",  # 复制/移动[1：复制；2：移动] - required: True
    }, path={
        "projectId": ""  # 项目ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def downgrade_using_post(self, checker=None):
    """
    接口名称：降级
    接口地址：/plan/$VERSION$/task/{projectId}/downgrade
    """
    r = RequestService.call_post(apis.get("downgradeUsingPOST", None), params={
        "taskIds": ""  # 任务ID串 - required: True
    }, path={
        "projectId": ""  # 项目id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def upgrade_using_post(self, checker=None):
    """
    接口名称：升级
    接口地址：/plan/$VERSION$/task/{projectId}/upgrade
    """
    r = RequestService.call_post(apis.get("upgradeUsingPOST", None), params={
        "taskIds": ""  # 任务ID串 - required: True
    }, path={
        "projectId": ""  # 项目id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_task_list_using_get(self, checker=None):
    """
    接口名称：批量创建子任务时获取任务列表，来关联父任务
    接口地址：/plan/$VERSION$/taskList
    """
    r = RequestService.call_get(apis.get("getTaskListUsingGET", None), params={
        "projectId": ""  # 项目ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_tasks_using_get_1(self, checker=None):
    """
    接口名称：获取任务列表（项目下）
    接口地址：/plan/$VERSION$/tasks
    """
    r = RequestService.call_get(apis.get("getTasksUsingGET_1", None), json={
        "procInstId": ""  # 流程实例ID - required: False
    }, params={
        "_type": "",  # 通过数量查询任务报表里面查看使用 - required: False
        "childFlag": "",  # 是否查询叶子节点[(默认)空或者1：全部；2：叶子节点数据] - required: False
        "endDate": "",  # 结束时间（yyyy-MM-dd 格式） - required: False
        "isFirstFloor": "",  # 是否只查询第一层 - required: False
        "labelId": "",  # 标签ID - required: False
        "name": "",  # 名称 - required: False
        "orderBy": "",  # 排序字段（默认order_code，要对所属项目名称排序时传project_name） - required: False
        "projectId": "",  # 项目ID - required: False
        "sortBy": "",  # 排序方式（DESC或ASC，排序字段不是order_code时默认DESC） - required: False
        "startDate": "",  # 开始时间（yyyy-MM-dd 格式） - required: False
        "state": "",  # 任务状态（多个状态用逗号分隔） - required: False
        "taskId": "",  # 任务id用来查询子任务 - required: False
        "userId": "",  # 责任人ID（多个ID以逗号分隔） - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_all_task_doc_using_get(self, checker=None):
    """
    接口名称：获取项目下所有任务的交付件
    接口地址：/plan/$VERSION$/tasks/doc/{id}
    """
    r = RequestService.call_get(apis.get("getAllTaskDocUsingGET", None), json={
        "deliverableFlag": ""  # 是否是交付件(1:是，0：否， null ：全部显示) - required: False
    }, params={
        "name": "",  # 名称 - required: False
        "orderBy": "",  # 排序字段（默认order_code - required: False
        "pageIndex": "",  # 页码 - required: False
        "pagesize": "",  # 页大小 - required: False
        "sortBy": "",  # 排序方式（DESC或ASC - required: False
    }, path={
        "id": ""  # 项目ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_one_task_list_using_get(self, checker=None):
    """
    接口名称：根据项目id获取一级任务列表
    接口地址：/plan/$VERSION$/tasks/getOneTaskList
    """
    r = RequestService.call_get(apis.get("getOneTaskListUsingGET", None), params={
        "projectId": ""  # 项目ids,多个id用逗号分隔 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_tasks_me_using_get(self, checker=None):
    """
    接口名称：获取任务列表（个人工作台）
    接口地址：/plan/$VERSION$/tasks/me
    """
    r = RequestService.call_get(apis.get("getTasksMeUsingGET", None), params={
        "childFlag": "",  # 是否查询叶子节点[(默认)空或者1：全部；2：叶子节点数据] - required: False
        "endDate": "",  # 结束时间（yyyy-MM-dd 格式） - required: False
        "labelId": "",  # 标签ID（多个ID以逗号分隔） - required: False
        "name": "",  # 名称 - required: False
        "orderBy": "",  # 排序字段（默认按状态指定规则排序，要对所属项目名称排序时传project_name） - required: False
        "pageIndex": "",  # 页码 - required: False
        "pagesize": "",  # 页大小 - required: False
        "projectId": "",  # 项目ID - required: False
        "sortBy": "",  # 排序方式（DESC或ASC，排序字段不是order_code时默认DESC） - required: False
        "startDate": "",  # 开始时间（yyyy-MM-dd 格式） - required: False
        "state": "",  # 任务状态（多个状态用逗号分隔） - required: False
        "userId": "",  # 责任人ID（多个ID以逗号分隔） - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_tasks_by_user_id_using_get(self, checker=None):
    """
    接口名称：获取责任人下的当前任务或要做任务
    接口地址：/plan/$VERSION$/tasks/member/{member}
    """
    r = RequestService.call_get(apis.get("getTasksByUserIdUsingGET", None), params={
        "type": ""  # 根据责任人id【0.获取任务列表(默认);1.获取当前任务列表;2.获取将要做的任务列表】 - required: True
    }, path={
        "member": ""  # 用户id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_tasks_page_using_get(self, checker=None):
    """
    接口名称：获取项目任务列表（分页）
    接口地址：/plan/$VERSION$/tasks/page
    """
    r = RequestService.call_get(apis.get("getTasksPageUsingGET", None), params={
        "labelId": "",  # 标签ID - required: False
        "milestoneFlag": "",  # 是否里程碑显示（Yes[1];NO[0]） - required: False
        "name": "",  # 名称 - required: False
        "orderBy": "",  # 排序字段（默认order_code - required: False
        "pageIndex": "",  # 页码 - required: False
        "pagesize": "",  # 页大小 - required: False
        "projectId": "",  # 项目ID - required: False
        "sortBy": "",  # 排序方式（DESC或ASC - required: False
        "state": "",  # 任务状态（多个状态用逗号分隔） - required: False
        "userId": "",  # 责任人ID（多个ID以逗号分隔） - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_task_by_id_list_using_delete(self, project_id, plan_list_id, checker=None):
    """
    接口名称：根据ids批量删除任务
    接口地址：/plan/$VERSION$/tasks/projectId
    """
    r = RequestService.call_delete(apis.get("deleteTaskByIdListUsingDELETE", None), json={
        "projectId": project_id,
         "taskIds": plan_list_id}, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_tasks_by_source_id_using_get(self, checker=None):
    """
    接口名称：根据来源ID获取任务
    接口地址：/plan/$VERSION$/tasks/source/{sourceids}
    """
    r = RequestService.call_get(apis.get("getTasksBySourceIdUsingGET", None), params={
        "projectId": "",  # 项目id - required: False
        "sourceObjName": "",  # 来源名称 - required: False
    }, path={
        "sourceids": ""  # 来源ids(逗号隔开) - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_plan_undone_using_get(self, checker=None):
    """
    接口名称：查询未完成任务
    接口地址：/plan/$VERSION$/tasks/undone/{projectId}
    """
    r = RequestService.call_get(apis.get("getPlanUndoneUsingGET", None), path={
        "projectId": ""  # 项目ID - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_first_level_children_tasks_by_task_id_using_get_1(self, checker=None):
    """
    接口名称：根据任务id获取第一层子任务列表
    接口地址：/plan/$VERSION$/tasks/{id}/children
    """
    r = RequestService.call_get(apis.get("getFirstLevelChildrenTasksByTaskIdUsingGET_1", None), json={
        "procInstId": ""  # 流程实例ID - required: False
    }, path={
        "id": ""  # 任务id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_task_predecessor_link_using_delete(self, checker=None):
    """
    接口名称：删除任务前置依赖
    接口地址：/plan/$VERSION$/tasks/{id}/predecessorLink
    """
    r = RequestService.call_delete(apis.get("deleteTaskPredecessorLinkUsingDELETE", None), json={
        "linkIdList": ""  # 关联Id列表 - required: False
    }, path={
        "id": ""  # 任务id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_task_by_ids_using_delete(self, checker=None):
    """
    接口名称：删除计划
    接口地址：/plan/$VERSION$/tasks/{projectId}
    """
    r = RequestService.call_delete(apis.get("deleteTaskByIdsUsingDELETE", None), json={
        "taskIds": ""  # 任务Id列表 - required: False
    }, path={
        "projectId": ""  # 项目Id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_tree_list_by_ids_using_get(self, checker=None):
    """
    接口名称：根据ID列表查询对象详细信息
    接口地址：/plan/$VERSION$/tree/{ids}
    """
    r = RequestService.call_get(apis.get("queryTreeListByIdsUsingGET", None), path={
        "ids": ""  # ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_durationrecord_using_put(self, checker=None):
    """
    接口名称：更新工时选项卡登记
    接口地址：/plan/$VERSION$/update/durationrecord
    """
    r = RequestService.call_put(apis.get("updateDurationrecordUsingPUT", None), json={
        "record": ""  # 选项卡对象 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def close_using_put(self, checker=None):
    """
    接口名称：任务关闭接口
    接口地址：/plan/$VERSION$/{id}/close
    """
    r = RequestService.call_put(apis.get("closeUsingPUT", None), path={
        "id": ""  # 任务id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def close_validate_using_get(self, checker=None):
    """
    接口名称：任务关闭校验接口
    接口地址：/plan/$VERSION$/{id}/close/validate
    """
    r = RequestService.call_get(apis.get("closeValidateUsingGET", None), path={
        "id": ""  # 任务id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_critical_flag_task_using_get(self, checker=None):
    """
    接口名称：判断task及其子是否是其他task的前置任务
    接口地址：/plan/$VERSION$/{projectId}/critical
    """
    r = RequestService.call_get(apis.get("getCriticalFlagTaskUsingGET", None), path={
        "projectId": ""  # 项目Id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_require_select_list_using_get(self, checker=None):
    """
    接口名称：需求树-selectlist
    接口地址：/req/$VERSION$/baseline/requires/selectlist
    """
    r = RequestService.call_get(apis.get("getRequireSelectListUsingGET", None), params={
        "parent_id": "",  # 父节点id - required: False
        "project_id": "",  # 项目id - required: False
        "type": "",  # 需求类型 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_require_tree_list_using_get(self, checker=None):
    """
    接口名称：需求树-list
    接口地址：/req/$VERSION$/baseline/requires/treelist
    """
    r = RequestService.call_get(apis.get("getRequireTreeListUsingGET", None), params={
        "baseline_id": "",  # 基线id - required: False
        "parent_id": "",  # 父节点id - required: False
        "project_id": "",  # 项目id - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def snapshot_using_get(self, checker=None):
    """
    接口名称：快照需求对象基本信息详情查询
    接口地址：/req/$VERSION$/baseline/snapshot/{id}
    """
    r = RequestService.call_get(apis.get("snapshotUsingGET", None), json={
        "type": ""  # 基线化类型 - required: False
    }, path={
        "id": ""  # 对象id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

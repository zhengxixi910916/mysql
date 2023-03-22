from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
项目群管理
'''
apis = Api({
    "create_program": "/portfolio/$VERSION$/program",  # 新增项目群
    "get_all_page_program": "/portfolio/$VERSION$/program/all/page",  # 查询所有项目群列表分页
    "archive_program": "/portfolio/$VERSION$/program/archive/%s",  # 项目群归档
    "get_archives_program": "/portfolio/$VERSION$/program/archives/%s",  # 查询用户归档项目群
    "add_attention": "/portfolio/$VERSION$/program/attention",  # 添加关注/收藏/打开对象
    "cancel_attention": "/portfolio/$VERSION$/program/attention",  # 取消关注/收藏/打开对象
    "get_attentions": "/portfolio/$VERSION$/program/attentions",  # 查询用户关注/收藏/打开对象
    "get_candidates": "/portfolio/$VERSION$/program/candidates/%s",  # 获取候选项目群、项目
    "get_dept_program_tree": "/portfolio/$VERSION$/program/depttree/%s",  # 获取用户部门项目群树
    "selectFilterListUsingPOST_3": "/portfolio/$VERSION$/program/filterlist",  # 过滤业务数据
    "get_milestones_by_progid": "/portfolio/$VERSION$/program/milestones/%s",  # 根据项目群ID获取子项目里程碑列表
    "get_overview_by_progid": "/portfolio/$VERSION$/program/overview/%s",  # 根据项目群ID获取子项目群、子项目信息概览列表
    "search_program": "/portfolio/$VERSION$/program/search/%s",  # 搜索项目群
    "add_sub_prog_proj": "/portfolio/$VERSION$/program/subs/%s",  # 添加/移除子项目群、子项目
    "get_sub_tree_by_progid": "/portfolio/$VERSION$/program/subtree/%s",  # 根据项目群ID查询子项目群、项目树
    "get_program_by_id": "/portfolio/$VERSION$/program/%s",  # 查询单个项目群
    "update_program_by_id": "/portfolio/$VERSION$/program/%s",  # 修改项目群
    "delete_program_by_id": "/portfolio/$VERSION$/program/%s",  # 删除项目群
    "get_program_member_by_id": "/portfolio/$VERSION$/program/%s/members",  # 项目群成员查询
    "get_proj_of_program": "/portfolio/$VERSION$/program/%s/projects",  # 查询项目群下所有项目
    "get_prog_milestone_baseline": "/portfolio/$VERSION$/programMilestoneBl",  # 查询项目群项目基线里程碑
    "get_prog_milestone_finished": "/portfolio/$VERSION$/programMilestoneCena",  # 查询项目群里程碑完成情况
    "get_programs_by_userid": "/portfolio/$VERSION$/user/programs/%s",  # 获取项目群经理所有项目群、子项目群
})


def create_program(self, name, departmentId, programManagerId, startTime, finishTime, workload, budget,
                   description, isArchived):
    """
    接口名称：新增项目群
    接口地址：/portfolio/$VERSION$/program
    """
    payload = {
        # "actualFinishTime": "",  # 实际结束时间 - required: False
        # "actualStartTime": "",  # 实际开始时间 - required: False
        "budget": budget,  # 预算 - required: True
        # "children[0].actualFinishTime": "",  # 实际结束时间 - required: False
        # "children[0].actualStartTime": "",  # 实际开始时间 - required: False
        # "children[0].budget": "",  # 预算 - required: False
        # "children[0].departmentId": "",  # 所属部门 (对应ELOrganization) - required: False
        # "children[0].finishTime": "",  # 计划结束时间 - required: False
        # "children[0].isArchived": "",  # 项目群是否归档 - required: False
        # "children[0].programManagerId": "",  # 项目群经理ID - required: False
        # "children[0].startTime": "",  # 计划开始时间 - required: False
        # "children[0].state": "",  # 项目群状态 - required: False
        # "children[0].type": "",  # 项目群类型  - required: False
        # "children[0].workload": "",  # 预计工作量 - required: False
        # "code": "",  # 编码 - required: False
        # "createBy": "",  # 创建者 - required: False
        # "createTime": "",  # 创建时间 - required: False
        # "delFlag": "",  # 删除标记（0：正常；1：删除；2：审核） - required: False
        "departmentId": departmentId,  # 所属部门 (对应ELOrganization) - required: True
        "description": description,  # 描述 - required: True
        "finishTime": finishTime,  # 计划结束时间 - required: True
        # "flexAttrs": "",  # 扩展属性 - required: False
        # "id": "",  # 对象Id - required: False
        "isArchived": isArchived,  # 项目群是否归档 - required: True
        "name": name,  # 名称 - required: True
        # "parent.actualFinishTime": "",  # 实际结束时间 - required: False
        # "parent.actualStartTime": "",  # 实际开始时间 - required: False
        # "parent.budget": "",  # 预算 - required: False
        # "parent.departmentId": "",  # 所属部门 (对应ELOrganization) - required: False
        # "parent.finishTime": "",  # 计划结束时间 - required: False
        # "parent.isArchived": "",  # 项目群是否归档 - required: False
        # "parent.programManagerId": "",  # 项目群经理ID - required: False
        # "parent.startTime": "",  # 计划开始时间 - required: False
        # "parent.state": "",  # 项目群状态 - required: False
        # "parent.type": "",  # 项目群类型  - required: False
        # "parent.workload": "",  # 预计工作量 - required: False
        # "parentId": "",  # 父节点Id - required: False
        # "parentIdPath": "",  # 父节点IdPath - required: False
        "programManagerId": programManagerId,  # 项目群经理ID - required: True
        "startTime": startTime,  # 计划开始时间 - required: True
        # "state": "",  # 项目群状态 - required: False
        # "type": "",  # 项目群类型  - required: False
        # "updateBy": "",  # 更新者 - required: False
        # "updateTime": "",  # 更新 - required: False
        "workload": workload,  # 预计工作量 - required: True
    }
    r = RequestService.call_post(apis.get("create_program"), payload)
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_all_page_program(self):
    """
    接口名称：查询所有项目群列表分页
    接口地址：/portfolio/$VERSION$/program/all/page
    """
    r = RequestService.call_get(apis.get("get_all_page_program"), params={
        "createBy": "",  # 项目群创建人ID - required: False
        "departmentId": "",  # 项目群所属部门ID - required: False
        "isArchived": "",  # 项目群是否归档0:未归档,1:已归档 - required: False
        "name": "",  # 项目群名称 - required: False
        "pageNo": 1,  # 页码 - required: True
        "pageSize": 10,  # 每页条数 - required: True
        "programManagerId": "",  # 项目群经理ID - required: False
        "sortField": "",  # 项目群排序字段 - required: False
        "sortMode": "",  # 项目群排序方式:asc,desc - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def select_filter_list_using_post_3(self, el_condition_list, checker=None):
    """
    接口名称：过滤业务数据
    接口地址：/portfolio/$VERSION$/program/filterlist
    """
    r = RequestService.call_post(apis.get("selectFilterListUsingPOST_3", None),
                                 json={
                                     "elConditionList": el_condition_list,
                                     "pageindex": 1,
                                     "pagesize": 20
                                 }
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def archive_program(self, eid):
    """
    接口名称：项目群归档
    接口地址：/portfolio/$VERSION$/program/archive/{id}
    """
    r = RequestService.call_put(apis.get("archive_program", eid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_archives_program(self, eid):
    """
    接口名称：查询用户归档项目群
    接口地址：/portfolio/$VERSION$/program/archives/{userId}
    """
    r = RequestService.call_get(apis.get("get_archives_program", eid))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_attention(self, programId, type):
    """
    接口名称：添加关注/收藏/打开对象
    接口地址：/portfolio/$VERSION$/program/attention
    """
    r = RequestService.call_post(apis.get("add_attention"), params={
        "programId": programId,  # 项目群ID - required: True
        "type": type,  # 类型，0:最近打开的;1:我关注的; 2:我收藏的 - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def cancel_attention(self, programId, type):
    """
    接口名称：取消关注/收藏/打开对象
    接口地址：/portfolio/$VERSION$/program/attention
    """
    r = RequestService.call_delete(apis.get("cancel_attention"), params={
        "programId": programId,  # 项目群ID - required: True
        "type": type,  # 类型，0:最近打开的;1:我关注的; 2:我收藏的 - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_attentions(self, type):
    """
    接口名称：查询用户关注/收藏/打开对象
    接口地址：/portfolio/$VERSION$/program/attentions
    """
    r = RequestService.call_get(apis.get("get_attentions"), params={
        "type": type  # 类型，0:最近打开的;1:我关注的; 2:我收藏的 - required: True
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_candidates(self, programId, type, code=None, name=None):
    """
    接口名称：获取候选项目群、项目
    接口地址：/portfolio/$VERSION$/program/candidates/{programId}
    """
    r = RequestService.call_get(apis.get("get_candidates", programId), params={
        "code": code,  # 编码 - required: False
        "name": name,  # 名称 - required: False
        "type": type,  # 类型 - required: True
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_dept_program_tree(self, userId):
    """
    接口名称：获取用户部门项目群树
    接口地址：/portfolio/$VERSION$/program/depttree/{userId}
    """
    r = RequestService.call_get(apis.get("get_dept_program_tree", userId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_milestones_by_progid(self, eid, type):
    """
    接口名称：根据项目群ID获取子项目里程碑列表
    接口地址：/portfolio/$VERSION$/program/milestones/{id}
    """
    r = RequestService.call_get(apis.get("get_milestones_by_progid", eid), params={
        "type": type  # ID类型（program 或 project） - required: True
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_overview_by_progid(self, eid, type):
    """
    接口名称：根据项目群ID获取子项目群、子项目信息概览列表
    接口地址：/portfolio/$VERSION$/program/overview/{id}
    """
    r = RequestService.call_get(apis.get("get_overview_by_progid", eid), params={
        "type": type  # ID类型（program 或 project） - required: True
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def search_program(self, userId, name):
    """
    接口名称：搜索项目群
    接口地址：/portfolio/$VERSION$/program/search/{userId}
    """
    r = RequestService.call_get(apis.get("search_program", userId), params={
        "name": name  # 项目群名称 - required: True
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def add_sub_prog_proj(self, programId, project_id, type, operation):
    """
    接口名称：添加/移除子项目群、子项目
    接口地址：/portfolio/$VERSION$/program/subs/{id}
    """
    r = RequestService.call_put(apis.get("add_sub_prog_proj", programId), json={
        "list": [
            {
                "id": project_id,
                "type": type
            }
        ],
        "operation": operation
        # 添加/移除子项目群、子项目参数实体对象 - required: False
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_sub_tree_by_progid(self, programId):
    """
    接口名称：根据项目群ID查询子项目群、项目树
    接口地址：/portfolio/$VERSION$/program/subtree/{programId}
    """
    r = RequestService.call_get(apis.get("get_sub_tree_by_progid", programId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_program_by_id(self, programId):
    """
    接口名称：查询单个项目群
    接口地址：/portfolio/$VERSION$/program/{id}
    """
    r = RequestService.call_get(apis.get("get_program_by_id", programId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_program_by_id(self, programId, name):
    """
    接口名称：修改项目群
    接口地址：/portfolio/$VERSION$/program/{id}
    """
    r = RequestService.call_put(apis.get("update_program_by_id", programId), json={
        "name": name,
    })
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def delete_program_by_id(self, programId):
    """
    接口名称：删除项目群
    接口地址：/portfolio/$VERSION$/program/{id}
    """
    r = RequestService.call_delete(apis.get("delete_program_by_id", programId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_program_member_by_id(self, programId):
    """
    接口名称：项目群成员查询
    接口地址：/portfolio/$VERSION$/program/{id}/members
    """
    r = RequestService.call_get(apis.get("get_program_member_by_id", programId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r


def get_proj_of_program(self, programId):
    """
    接口名称：查询项目群下所有项目
    接口地址：/portfolio/$VERSION$/program/{id}/projects
    """
    r = RequestService.call_get(apis.get("get_proj_of_program", programId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_prog_milestone_baseline(self):
    """
    接口名称：查询项目群项目基线里程碑
    接口地址：/portfolio/$VERSION$/programMilestoneBl
    """
    r = RequestService.call_get(apis.get("get_prog_milestone_baseline"))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_prog_milestone_finished(self):
    """
    接口名称：查询项目群里程碑完成情况
    接口地址：/portfolio/$VERSION$/programMilestoneCena
    """
    r = RequestService.call_get(apis.get("get_prog_milestone_finished"))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_programs_by_userid(self, userId):
    """
    接口名称：获取项目群经理所有项目群、子项目群
    接口地址：/portfolio/$VERSION$/user/programs/{userId}
    """
    r = RequestService.call_get(apis.get("get_programs_by_userid", userId))
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

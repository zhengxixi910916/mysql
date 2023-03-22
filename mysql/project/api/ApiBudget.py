import os
import time
from contextlib import closing

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
预算模板 API、预算科目 API、费用 API、预算 API、费用定时 API、
'''

# 获取上一级目录
dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dir_document = dir_path + r'/document'
times = time.strftime("%Y-%m-%d %H %M %S", time.localtime(time.time()))
file_name = "budget_" + times + ".xlsx"

apis = Api({
    "create_budget_tem": "/budget/$VERSION$/template/create",  # 新增预算模板
    "del_budget_tem": "/budget/$VERSION$/template/delete",  # 批量删除预算模板
    "page_budget_tem": "/budget/$VERSION$/template/search",  # 查询预算模板分页列表
    "get_budget_tem_by_id": "/budget/$VERSION$/template/%s/get",  # 根据ID查询预算模板对象信息
    "update_budget_tem": "/budget/$VERSION$/template/%s/update",  # 修改单条预算模板

    "create_budget_category": "/budget/$VERSION$/category/create",  # 新增预算科目或品名
    "add_budget_category_parts": "/budget/$VERSION$/category/%s/parts/save",  # 添加品名

    "del_budget_category": "/budget/$VERSION$/category/delete",  # 批量删除预算科目或品名
    "get_ERP_categorys": "/budget/$VERSION$/category/erp/query",  # 查询ERP所有预算科目（树形平铺）
    "create_budget_parts_by_tem": "/budget/$VERSION$/category/parts/create",  # 根据模板品名ID集合，批量新增品名
    "get_budget_category": "/budget/$VERSION$/category/search",  # 查询预算科目或品名列表
    "get_parts_for_tem": "/budget/$VERSION$/category/template/parts",  # 查询项目对应预算模板中的品名列表
    "sync_history_proj": "/budget/$VERSION$/category/template/sync",  # 同步历史项目的预算科目数据
    "get_budget_category_by_id": "/budget/$VERSION$/category/%s/get",  # 根据ID查询预算科目或品名对象信息
    "save_budget_parts": "/budget/$VERSION$/category/%s/parts/save",  # 批量保存单一预算科目下的品名列表
    "update_budget_category_by_id": "/budget/$VERSION$/category/%s/update",  # 根据ID修改预算科目或品名

    "query_proj_budget": "/budget/$VERSION$/project/budget/query",  # 查询项目预算
    "save_proj_budget": "/budget/$VERSION$/project/category/budget/save",  # 批量保存项目预算
    "get_proj_budget_config": "/budget/$VERSION$/project/%s/budget/config",  # 查询项目预算设置接口
    "view_proj_budget": "/budget/$VERSION$/project/%s/budget/html",  # 项目预算列表Html预览
    "search_proj_budget": "/budget/$VERSION$/project/%s/budget/list",  # 查询项目预算列表/查询项目预算费用概况
    "set_proj_budget": "/budget/$VERSION$/project/%s/config",  # 设置项目预算
    "get_budget_process_info": "/budget/$VERSION$/project/%s/process",  # 查询项目预算流程信息
    "get_stages_by_proj_id": "/budget/$VERSION$/project/%s/stage/list",  # 查询项目已使用的阶段
    "query_budget_state": "/budget/$VERSION$/project/%s/state/query",  # 查询预算审批状态(MAKING:编制 APPROVING：审批中RELEASED：已发布)

    "del_proj_cost_by_cids": "/budget/$VERSION$/cost/delete",  # 根据费用ID批量删除项目费用数据
    "export_cost": "/budget/$VERSION$/cost/export",  # 导出项目费用
    "insert_project_cost": "/budget/$VERSION$/cost/insert",  # 新增单条项目费用数据
    "search_proj_cost": "/budget/$VERSION$/cost/list",  # 查询项目费用
    "export_proj_budget": "/budget/$VERSION$/cost/project/export",  # 项目费用/预算导出
    "search_proj_cost_budget": "/budget/$VERSION$/cost/project/list",  # 查询项目费用/预算
    "updatebatch_proj_cost": "/budget/$VERSION$/cost/update/batch",  # 批量修改项目费用
    "get_proj_cost_by_id": "/budget/$VERSION$/cost/%s/get",  # 查询单条项目费用数据
    "update_project_cost_by_id": "/budget/$VERSION$/cost/%s/update",  # 修改单条项目费用数据

    "sync_category": "/budget/$VERSION$/scheduler/category/sync",  # 同步历史项目预算科目数据
    "sync_ERP_cost": "/budget/$VERSION$/scheduler/cost/sync",  # 费用从ERP系统同步

    "get_budget_cost": "/budget/$VERSION$/stastic/project/budget/compare",  # 预算费用报表--按部门统计预算费用
    "get_proj_budget_cost": "/budget/$VERSION$/stastic/project/%s/budget/compare",  # 单项目统计--统计各阶段预算和费用对比
    "get_proj_budget_by_category": "/budget/$VERSION$/stastic/project/%s/budget/show",  # 单项目统计--以最后一级子预算科目为统计维度
    "refreshTemplateUsingGET": "/budget/$VERSION$/category/%s/refreshTemplate",  # 刷新项目费用科目

})


def refreshTemplateUsingGET(self, project_id, checker=None):
    """
    接口名称：刷新项目费用科目
    接口地址：/budget/$VERSION$/category/{project_id}/refreshTemplate
    """
    r = RequestService.call_get(apis.get("refreshTemplateUsingGET", project_id), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def create_budget_tem(self, name, description, state, projectType, checker=None):
    """
    接口名称：新增预算模板
    接口地址：/budget/$VERSION$/template/create
    """
    r = RequestService.call_post(apis.get("create_budget_tem"), params={
        "description": description,  # 描述 - required: False
        "name": name,  # 名称 - required: False
        "projectType": projectType,  # 项目类型 - required: False
        "state": state,  # 状态：0 启用 1 停用 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def del_budget_tem(self, temid, checker=None):
    """
    接口名称：批量删除预算模板
    接口地址：/budget/$VERSION$/template/delete
    """
    r = RequestService.call_delete(apis.get("del_budget_tem"), json=[
        temid  # ids - required: True
    ])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def page_budget_tem(self, page_index=1, page_size=20, name=None, orderBy=None, projectType=None, sortBy=None,
                    state=None,
                    checker=None):
    """
    接口名称：查询预算模板分页列表
    接口地址：/budget/$VERSION$/template/search
    """
    r = RequestService.call_get(apis.get("page_budget_tem"), params={
        "name": name,  # 名称 - required: False
        "orderBy": orderBy,  # 排序字段，默认创建时间 - required: False
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页条数 - required: False
        "projectType": projectType,  # 项目类型 - required: False
        "sortBy": sortBy,  # 排序方式，默认倒序 - required: False
        "state": state,  # 状态:0:启用; 1:停用 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_budget_tem_by_id(self, temid, checker=None):
    """
    接口名称：根据ID查询预算模板对象信息
    接口地址：/budget/$VERSION$/template/{id}/get
    """
    r = RequestService.call_get(apis.get("get_budget_tem_by_id", temid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_budget_tem(self, temid, name, description, state, projectType, flexAttrs=None, checker=None):
    """
    接口名称：修改单条预算模板
    接口地址：/budget/$VERSION$/template/{id}/update
    """
    r = RequestService.call_put(apis.get("update_budget_tem", temid), json={
        "description": description,
        "flexAttrs": flexAttrs,
        "name": name,
        "projectType": projectType,
        "state": state
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def create_budget_category(self, templateId, name, description, type, code=None, parentId=-1, erpCode=None,
                           checker=None):
    """
    接口名称：新增预算科目
    接口地址：/budget/$VERSION$/category/create
    """
    r = RequestService.call_post(apis.get("create_budget_category"), params={
        "code": code,  # 编码 - required: False
        "description": description,  # 描述 - required: False
        "erpCode": erpCode,  # ERP系统预算科目编号 - required: False
        "name": name,  # 名称 - required: False
        "parentId": parentId,  # 父节点Id - required: False
        "templateId": templateId,  # 预算模板ID - required: False
        "type": type,  # 类型 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]
def add_budget_category_parts(self,budget_category_id, name, budget_template_id, checker=None):
    """
    接口名称：添加品名
    接口地址：/budget/$VERSION$/category/{budget_category_id}}/parts/save
    """
    r = RequestService.call_put(apis.put("add_budget_category_parts", budget_category_id), json=[
        {"name": name, "unit": "g", "unitPrice": "1", "application": "1212", "procedure": "1", "type": 1, "code": 1,
         "templateId": budget_template_id}], )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

def del_budget_category(self, budgetid, checker=None):
    """
    接口名称：批量删除预算科目或品名
    接口地址：/budget/$VERSION$/category/delete
    """
    r = RequestService.call_delete(apis.get("del_budget_category"), json=[
        budgetid  # ids - required: True
    ])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def get_ERP_categorys(self, checker=None):
    """
    接口名称：查询ERP所有预算科目（树形平铺）
    接口地址：/budget/$VERSION$/category/erp/query
    """
    r = RequestService.call_get(apis.get("get_ERP_categorys"), params={
        "categoryId": "",  # 预算科目ID - required: False
        "value": "",  # ERP预算编码 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def create_budget_parts_by_tem(self, categoryId, partIds, project_id, checker=None):
    """
    接口名称：根据模板品名ID集合，批量新增品名
    接口地址：/budget/$VERSION$/category/parts/create
    """
    r = RequestService.call_put(apis.get("create_budget_parts_by_tem"), json={
        "categoryId": categoryId,
        "partIds": [partIds],
        "projectId": project_id
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def get_budget_category(self, templateId, type, parentId=None, name=None, checker=None):
    """
    接口名称：查询预算科目或品名列表
    接口地址：/budget/$VERSION$/category/search
    """
    r = RequestService.call_get(apis.get("get_budget_category"), params={
        "name": name,  # 预算科目/品名 名称 - required: False
        "parentId": parentId,  # 父科目ID - required: False
        "templateId": templateId,  # 预算模板ID - required: False
        "type": type,  # 类型:0:预算科目; 1:品名 - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_parts_for_tem(self, code, project_id, checker=None):
    """
    接口名称：查询项目对应预算模板中的品名列表
    接口地址：/budget/$VERSION$/category/template/parts
    """
    r = RequestService.call_get(apis.get("get_parts_for_tem"), params={
        "code": code,  # 预算科目code - required: True
        "projectId": project_id,  # 项目Id - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']


def sync_history_proj(self, checker=None):
    """
    接口名称：同步历史项目的预算科目数据
    接口地址：/budget/$VERSION$/category/template/sync
    """
    r = RequestService.call_put(apis.get("sync_history_proj"))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def get_budget_category_by_id(self, budgetid, checker=None):
    """
    接口名称：根据ID查询预算科目或品名对象信息
    接口地址：/budget/$VERSION$/category/{id}/get
    """
    r = RequestService.call_get(apis.get("get_budget_category_by_id", budgetid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def save_budget_parts(self, budgetid, templateId, name, unit, unitPrice, application, procedure, type,
                      code="CODE" + time.strftime('%H%M%S', time.localtime()), checker=None):
    """
    接口名称：批量保存单一预算科目下的品名列表
    接口地址：/budget/$VERSION$/category/{id}/parts/save
    """
    r = RequestService.call_put(apis.get("save_budget_parts", budgetid), json=[{
        "application": application,
        "code": code,
        "name": name,
        "procedure": procedure,
        "templateId": templateId,
        "type": type,
        "unit": unit,
        "unitPrice": unitPrice
    }])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def update_budget_category_by_id(self, budgetid, name, parentId,
                                 code=None,
                                 flexAttrs=None, erpCode=None, description=None, checker=None):
    """
    接口名称：根据ID修改预算科目或品名
    接口地址：/budget/$VERSION$/category/{id}/update
    """
    r = RequestService.call_put(apis.get("update_budget_category_by_id", budgetid), json={
        "code": code,
        "description": description,
        "erpCode": erpCode,
        "flexAttrs": flexAttrs,
        "name": name,
        "parentId": parentId
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def query_proj_budget(self, categoryId, project_id, checker=None):
    """
    接口名称：查询项目预算
    接口地址：/budget/$VERSION$/project/budget/query
    """
    r = RequestService.call_get(apis.get("query_proj_budget"), params={
        "categoryId": categoryId,  # 预算科目ID - required: True
        "projectId": project_id,  # 项目ID - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def save_proj_budget(self, stagename, categoryId, partId, project_id, num, checker=None):
    """
    接口名称：批量保存项目预算
    接口地址：/budget/$VERSION$/project/category/budget/save
    """
    r = RequestService.call_put(apis.get("save_proj_budget"), json={
        "categoryId": categoryId,
        "entrys": [{
            "num": num,
            "partId": partId,
            "stage": stagename,
        }],
        "partId": "",
        "projectId": project_id,
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def get_proj_budget_config(self, project_id, checker=None):
    """
    接口名称：查询项目预算设置接口
    接口地址：/budget/$VERSION$/project/{id}/budget/config
    """
    r = RequestService.call_get(apis.get("get_proj_budget_config", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def view_proj_budget(self, checker=None):
    """
    接口名称：项目预算列表Html预览
    接口地址：/budget/$VERSION$/project/{id}/budget/html
    """
    r = RequestService.call_get(apis.get("view_proj_budget"), params={
        "department": ""  # 部门名 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def search_proj_budget(self, project_id, flag=None, checker=None):
    """
    接口名称：查询项目预算列表/查询项目预算费用概况
    接口地址：/budget/$VERSION$/project/{id}/budget/list
    """
    r = RequestService.call_get(apis.get("search_proj_budget", project_id), params={
        "flag": flag  # 是否查询费用 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def set_proj_budget(self, project_id, stagename, startTime, endTime, yieldRate, estimateNum, procedure, checker=None):
    """
    接口名称：设置项目预算
    接口地址：/budget/$VERSION$/project/{id}/config
    """
    r = RequestService.call_put(apis.get("set_proj_budget", project_id), json=[{
        "endTime": endTime,
        "estimateNum": estimateNum,
        "procedure": procedure,
        "stage": stagename,
        "startTime": startTime,
        "yieldRate": yieldRate
    }])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def get_budget_process_info(self, project_id, checker=None):
    """
    接口名称：查询项目预算流程信息
    接口地址：/budget/$VERSION$/project/{id}/process
    """
    r = RequestService.call_get(apis.get("get_budget_process_info", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_stages_by_proj_id(self, project_id, checker=None):
    """
    接口名称：查询项目已使用的阶段
    接口地址：/budget/$VERSION$/project/{id}/stage/list
    """
    r = RequestService.call_get(apis.get("get_stages_by_proj_id", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def query_budget_state(self, project_id, checker=None):
    """
    接口名称：查询预算审批状态(MAKING:编制 APPROVING：审批中RELEASED：已发布)
    接口地址：/budget/$VERSION$/project/{project_id}/state/query
    """
    r = RequestService.call_get(apis.get("query_budget_state", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def del_proj_cost_by_cids(self, costid, checker=None):
    """
    接口名称：根据费用ID批量删除项目费用数据
    接口地址：/budget/$VERSION$/cost/delete
    """
    r = RequestService.call_delete(apis.get("del_proj_cost_by_cids"), json=[
        costid  # ids - required: True
    ])
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


def export_cost(self, project_id, stage=None, occurrenceTimeStart=None, occurrenceTimeEnd=None, categoryId=None):
    """
    接口名称：导出项目费用
    接口地址：/budget/$VERSION$/cost/export
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("export_cost"), params={
        "categoryId": categoryId,  # 预算科目ID - required: False
        "occurrenceTimeEnd": occurrenceTimeEnd,  # 发生结束时间 - required: False
        "occurrenceTimeStart": occurrenceTimeStart,  # 发生开始时间 - required: False
        "projectId": project_id,  # 项目ID - required: False
        "stage": stage,  # 阶段 - required: False
    })) as response:
        with open(dir_document + r"\export_cost_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def insert_project_cost(self, name, project_id, categoryId, stage, costAmount, occurrenceTime, description=None,
                        checker=None):
    """
    接口名称：新增单条项目费用数据
    接口地址：/budget/$VERSION$/cost/insert
    """
    r = RequestService.call_post(apis.get("insert_project_cost"), params={
        "categoryId": categoryId,  # 预算科目ID - required: False
        "costAmount": costAmount,  # 总额 - required: False
        "description": description,  # 描述 - required: False
        "name": name,  # 名称 - required: False
        "occurrenceTime": occurrenceTime,  # 发生时间 - required: False
        "projectId": project_id,  # 项目ID - required: False
        "stage": stage,  # 阶段 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def search_proj_cost(self, project_id, page_size=20, page_index=1, categoryId=None, occurrenceTimeEnd=None,
                     occurrenceTimeStart=None, stage=None, checker=None):
    """
    接口名称：查询项目费用
    接口地址：/budget/$VERSION$/cost/list
    """
    r = RequestService.call_get(apis.get("search_proj_cost"), params={
        "categoryId": categoryId,  # 预算科目ID - required: False
        "occurrenceTimeEnd": occurrenceTimeEnd,  # 发生结束时间 - required: False
        "occurrenceTimeStart": occurrenceTimeStart,  # 发生开始时间 - required: False
        "pageindex": page_index,  # 页码 - required: False
        "pagesize": page_size,  # 每页数量 - required: False
        "projectId": project_id,  # 项目ID - required: False
        "stage": stage,  # 阶段 - required: False
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def export_proj_budget(self, department, projectCreateTime=",", overFlag="0"):
    """
    接口名称：项目费用/预算导出
    接口地址：/budget/$VERSION$/cost/project/export
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("export_proj_budget"), params={
        "department": department,  # 所属部门 - required: True
        "overFlag": overFlag,  # 超额：0：查询所有 1：只查询超额项目 2：只查询不超额项目 - required: False
        "projectCreateTime": projectCreateTime,  # 项目创建时间 - required: False
    })) as response:
        with open(dir_document + r"//export_proj_cost_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def search_proj_cost_budget(self, page_index=1, page_size=20, department=None, orderBy=None, overFlag=None,
                            projectCreateTime=None, sortBy=None, checker=None):
    """
    接口名称：查询项目费用/预算
    接口地址：/budget/$VERSION$/cost/project/list
    """
    r = RequestService.call_get(apis.get("search_proj_cost_budget"), params={
        "department": department,  # 所属部门 - required: False
        "orderBy": orderBy,  # 排序字段 - required: False
        "overFlag": overFlag,  # 是否超预算: 0:查询所有的，1:只查询超预算的, 2:只查询不超预算的 - required: False
        "pageindex": page_index,  # 页数 - required: False
        "pagesize": page_size,  # 每页数量 - required: False
        "projectCreateTime": projectCreateTime,  # 项目创建时间(区间，必须以逗号或分号隔开) - required: False
        "sortBy": sortBy,  # 排序规则: ASC: 升序, DESC: 降序 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def updatebatch_proj_cost(self, costs=None, checker=None):
    """
    接口名称：批量修改项目费用
    接口地址：/budget/$VERSION$/cost/update/batch
    """
    r = RequestService.call_put(apis.get("updatebatch_proj_cost"), json={
        "costs": costs  # costs - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_proj_cost_by_id(self, costid, checker=None):
    """
    接口名称：查询单条项目费用数据
    接口地址：/budget/$VERSION$/cost/{id}/get
    """
    r = RequestService.call_get(apis.get("get_proj_cost_by_id", costid))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def update_project_cost_by_id(self, costid, costname, categoryId, stage, flexAttrs=None, description=None,
                              checker=None):
    """
    接口名称：修改单条项目费用数据
    接口地址：/budget/$VERSION$/cost/{id}/update
    """
    r = RequestService.call_put(apis.get("update_project_cost_by_id", costid), json={
        "categoryId": categoryId,
        "description": description,
        "flexAttrs": flexAttrs,
        "name": costname,
        "stage": stage
    })
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def sync_category(self, checker=None):
    """
    接口名称：同步历史项目预算科目数据
    接口地址：/budget/$VERSION$/scheduler/category/sync
    """
    r = RequestService.call_post(apis.get("sync_category"), )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
        return r
    else:
        apis.check_success(self, r)
        return r


def sync_ERP_cost(self, checker=None):
    """
    接口名称：费用从ERP系统同步
    接口地址：/budget/$VERSION$/scheduler/cost/sync
    """
    r = RequestService.call_post(apis.get("sync_ERP_cost"), params={
        "costCacheTime": ""  # 起始时间 - required: False
    }, )
    apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    # return r['res']["data"]


def get_budget_cost(self, department_id, checker=None):
    """
    接口名称：预算费用报表--按部门统计预算费用
    接口地址：/budget/$VERSION$/stastic/project/budget/compare
    """
    r = RequestService.call_get(apis.get("get_budget_cost"), params={
        "department": department_id,  # 所属部门 - required: False
        "order": "0",  # 排序：0:按预算排序 1:按费用排序 2:按超额费用排序 3:按超额率排序 - required: False
        "projectCreateTime": "",  # 项目创建时间(区间，必须以逗号或分号隔开) - required: False
        "sort": "1",  # 排序规则: 0: 升序, 1: 降序 - required: False
        "productId": "0094d641626eb400e57d78583f5e5018"
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

def get_proj_budget_cost(self, project_id, checker=None):
    """
    接口名称：单项目统计--统计各阶段预算和费用对比
    接口地址：/budget/$VERSION$/stastic/project/{id}/budget/compare
    """
    r = RequestService.call_get(apis.get("get_proj_budget_cost", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def get_proj_budget_by_category(self, project_id, checker=None):
    """
    接口名称：单项目统计--以最后一级子预算科目为统计维度
    接口地址：/budget/$VERSION$/stastic/project/{id}/budget/show
    """
    r = RequestService.call_get(apis.get("get_proj_budget_by_category", project_id))
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r


if __name__ == '__main__':
    print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

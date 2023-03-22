from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

apis = Api({
    "projectChangeOrderCallbackUsingPOST": "/proj/$VERSION$/change/changeOrder/callback",  # 项目变更流程回调接口
    "addOrderUsingPOST": "/proj/$VERSION$/change/order",  # 项目变更新增
    "updateOrderUsingPUT": "/proj/$VERSION$/change/order",  # 项目变更编辑
    "deleteOrderUsingDELETE": "/proj/$VERSION$/change/order",  # 项目变更批量删除
    "calculateChangeBudgetUsingPOST": "/proj/$VERSION$/change/order/calculateChangeBudget",  # 前端修改更新后数量或者金额后修正数据
    "getOrderBudgetListUsingGET": "/proj/$VERSION$/change/order/getBudgetList/%s",  # 创建变更单的预算列表查询
    "getDealPlanTimeUsingPOST": "/proj/$VERSION$/change/order/getDealPlanTime",  # 批量计算延伸或缩短变更后时间
    "getIsRelatePlanUsingGET": "/proj/$VERSION$/change/order/getIsRelatePlan/%s",  # 查看关联任务的人员id
    "getOrderMemberListUsingGET": "/proj/$VERSION$/change/order/getMemberList/%s",  # 创建变更单的成员列表查询
    "getOrderPlanListUsingGET": "/proj/$VERSION$/change/order/getPlanList/%s",  # 创建变更单的计划列表查询
    "getOrderInfoByIdUsingGET": "/proj/$VERSION$/change/orderInfo",  # 项目变更详情
    "selectPageUsingGET": "/proj/$VERSION$/change/ordersPage",  # 项目变更列表查询
    "queryTodoTaskListByUserIdAndSystemIdUsingGET": "/workflow/$VERSION$/task/todotask",
    # queryTodoTaskListByUserIdAndSystemId
})


def project_change_order_callback(self, process_instance_id, process_definition_id, business_key, checker=None):
    """
    接口名称：项目变更流程回调接口
    接口地址：/proj/$VERSION$/change/changeOrder/callback
    """
    r = RequestService.call_post(apis.get("projectChangeOrderCallbackUsingPOST", None), json={
        "processInstanceId": process_instance_id,
        "processDefinitionId": process_definition_id,
        "routeFlag": "0",
        "trigger": "start",
        "flowState": "COMPLETE",
        "title": "项目变更流程模板",
        "processDefinitionKey": "PROJECT_CHANGE",
        "bussinessFormDataJson": "[]",
        "taskDefinitionKey": "COMPLETE_NODE",
        "startUserId": "b7785da599bd8b8301810c39642ee193",
        "businessKeys": [
            business_key
        ],
        "tenantId": "erdp",
        "customformJson": "{\"id\":\"c9c8085555384f4cc23755b5fce0efa9\"}"
    }
                                 )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def add_order(self, creat_data, checker=None):
    """
    接口名称：项目变更新增
    接口地址：/proj/$VERSION$/change/order
    """
    r = RequestService.call_post(apis.get("addOrderUsingPOST", None), json=creat_data)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def update_order(self, checker=None):
    """
    接口名称：项目变更编辑
    接口地址：/proj/$VERSION$/change/order
    """
    r = RequestService.call_put(apis.get("updateOrderUsingPUT", None), json={
        "projectChangeOrderEditDto": ""  # 变更列表查询实体 - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def delete_order(self, checker=None):
    """
    接口名称：项目变更批量删除
    接口地址：/proj/$VERSION$/change/order
    """
    r = RequestService.call_delete(apis.get("deleteOrderUsingDELETE", None), json={
        "ids": ""  # 变更单id - required: False
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def calculate_change_budget(self, budget_voList, checker=None):
    """
    接口名称：前端修改更新后数量或者金额后修正数据
    接口地址：/proj/$VERSION$/change/order/calculateChangeBudget
    """
    r = RequestService.call_post(apis.get("calculateChangeBudgetUsingPOST", None), json=budget_voList)
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_order_budget_list(self, project_id, checker=None):
    """
    接口名称：创建变更单的预算列表查询
    接口地址：/proj/$VERSION$/change/order/getBudgetList/{projectId}
    """
    r = RequestService.call_get(apis.get("getOrderBudgetListUsingGET", project_id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_deal_plan_time(self, project_id, checker=None):
    """
    接口名称：批量计算延伸或缩短变更后时间
    接口地址：/proj/$VERSION$/change/order/getDealPlanTime
    """
    r = RequestService.call_post(apis.get("getDealPlanTimeUsingPOST", None), json={
        "projectId": project_id,
        "dealPlanType": "1",
        "dealPlanDay": 1,
        "changePlanIdList": []
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_is_relate_plan(self, checker=None):
    """
    接口名称：查看关联任务的人员id
    接口地址：/proj/$VERSION$/change/order/getIsRelatePlan/{projectId}
    """
    r = RequestService.call_get(apis.get("getIsRelatePlanUsingGET", None), path={
        "projectId": ""  # 项目ID - required: True
    }, )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_order_member_list(self, project_id, checker=None):
    """
    接口名称：创建变更单的成员列表查询
    接口地址：/proj/$VERSION$/change/order/getMemberList/{projectId}
    """
    r = RequestService.call_get(apis.get("getOrderMemberListUsingGET", project_id))
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_order_plan_list(self, project_id, checker=None):
    """
    接口名称：创建变更单的计划列表查询
    接口地址：/proj/$VERSION$/change/order/getPlanList/{projectId}
    """
    r = RequestService.call_get(apis.get("getOrderPlanListUsingGET", project_id), params={
        "milestoneFlag": 1,
        "stateList": "PENDING,PROCESSION,DRAFT"
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def get_order_info_by_id(self, project_change_id, project_id, checker=None):
    """
    接口名称：项目变更详情
    接口地址：/proj/$VERSION$/change/orderInfo
    """
    r = RequestService.call_get(apis.get("getOrderInfoByIdUsingGET", None), params={
        "id": project_change_id,
        "projectId": project_id
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def select_page(self,project_id, change_order_code, checker=None):
    """
    接口名称：项目变更列表查询
    接口地址：/proj/$VERSION$/change/ordersPage
    """
    r = RequestService.call_get(apis.get("selectPageUsingGET", None), params={
        "projectId": project_id,
        "changeOrderCode": change_order_code,
        "changeType":"",
        "pageSize": 10,
        "pageIndex": 1
    })
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r


def query_todo_task_list_by_user_id_and_system_id(self, checker=None):
    """
    接口名称：queryTodoTaskListByUserIdAndSystemId
    接口地址：/workflow/$VERSION$/task/todotask
    """
    r = RequestService.call_get(apis.get("queryTodoTaskListByUserIdAndSystemIdUsingGET", None), params={
        "tenantId": "erdp",
        "pagesize": 20,
        "pageIndex": 1
    }
                                )
    if checker is not None:
        apis.check(self, r, checker["code"], checker["success"])
    else:
        apis.check_success(self, r)
    return r

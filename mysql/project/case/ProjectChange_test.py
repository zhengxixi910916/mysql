import time
import unittest
from project.api import ApiProjectChange, ApiProject


class ProjectChange(unittest.TestCase):
    user_id = "025CE39B20EA11E7A81AC85B767C89C1"
    org_id = "69a12d9d163fec76d208e957289d0c53"
    now_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    project_name = 'project_change_test_' + now_time
    project_id = ''
    # 項目变更的id
    project_change_id = ''
    # 项目变更单号
    project_change_order_code = ''
    # 预算的数据
    budget_voList = ''
    # 项目内成员的信息
    user_id_info_0 = ''
    user_id_info_1 = ''
    user_info = ''
    # 计划列表
    plan_list = ''

    process_instance_id = ''
    process_definition_id = ''
    business_key = ''

    def test_0100_get_order_member_list(self):
        """
        接口名称：创建变更单的成员列表查询
        接口地址：/proj/$VERSION$/change/order/getMemberList/{projectId}
        """
        # 创建项目
        r = ApiProject.addProjectUsingPOST_1(self, name=ProjectChange.project_name
                                             )
        ProjectChange.project_id = r.get('id')

        r = ApiProjectChange.get_order_member_list(self,
                                                   project_id=ProjectChange.project_id)
        ProjectChange.user_id_info_0 = r['res']['data'][0]
        ProjectChange.user_id_info_1 = r['res']['data'][1]
        ProjectChange.user_info = r['res']['people'][0]

    def test_0200_get_order_plan_list(self):
        """
        接口名称：创建变更单的计划列表查询
        接口地址：/proj/$VERSION$/change/order/getPlanList/{projectId}
        """
        ApiProjectChange.get_order_plan_list(self,
                                             project_id=ProjectChange.project_id)

    def test_0300_get_order_budget_list(self):
        """
        接口名称：创建变更单的预算列表查询
        接口地址：/proj/$VERSION$/change/order/getBudgetList/{projectId}
        """
        r = ApiProjectChange.get_order_budget_list(self,
                                                   project_id=ProjectChange.project_id)
        ProjectChange.budget_voList = r['res']['data']['budgetVoList']

    def test_0400_get_deal_plan_time(self):
        """
        接口名称：批量计算延伸或缩短变更后时间
        接口地址：/proj/$VERSION$/change/order/getDealPlanTime
        """
        r = ApiProjectChange.get_deal_plan_time(self,
                                                project_id=ProjectChange.project_id)
        ProjectChange.plan_list = r['res']['data']

    def test_0450_calculate_change_budget(self, checker=None):
        """
        接口名称：前端修改更新后数量或者金额后修正数据
        接口地址：/proj/$VERSION$/change/order/calculateChangeBudget
        """
        ApiProjectChange.calculate_change_budget(self,
                                                 budget_voList=ProjectChange.budget_voList
                                                 )

    def test_0500_add_order(self):
        """
        接口名称：项目变更新增
        接口地址：/proj/$VERSION$/change/order
        """
        # todo 优化里面的参数projectChangeMemberAddDtoList
        creat_data = {
            "projectId": ProjectChange.project_id,
            "changeType": "proj_plan,proj_member,proj_budget,proj_other",
            "changeState": "MAKING",
            "measures": "test",
            "changeReason": "test",
            "otherBefore": "before_test",
            "otherAfter": "under_test",
            "projectChangePlanAddDtoList": ProjectChange.plan_list,
            "projectChangeMemberAddDtoList": [
                {
                    "roleKey": "PM",
                    "isKeyMember": "0",
                    "name": "项目经理",
                    "oldUserIdList": [
                        "SYS_E39B20EA11E7A81AC85B767C89C1"
                    ],
                    "oldUserList": [
                        {
                            "id": "SYS_E39B20EA11E7A81AC85B767C89C1",
                            "orgId": "SYS_2d28fff04a3da56f410a241528b4",
                            "orgName": "组织部门",
                            "code": "1",
                            "name": "admin",
                            "displayName": "管理员",
                            "displayEn": "guanliyuan",
                            "mobile": "",
                            "email": "admin@domain.com",
                            "avatar": "./static/images/avatar/Avatar-3.png",
                            "type": "license",
                            "status": "1",
                            "active": "1",
                            "leader": "0"
                        }
                    ],
                    "newUserList": [
                        {
                            "id": "SYS_E39B20EA11E7A81AC85B767C89C1",
                            "orgId": "SYS_2d28fff04a3da56f410a241528b4",
                            "orgName": "组织部门",
                            "code": "1",
                            "name": "admin",
                            "displayName": "管理员",
                            "displayEn": "guanliyuan",
                            "mobile": "",
                            "email": "admin@domain.com",
                            "avatar": "./static/images/avatar/Avatar-3.png",
                            "type": "license",
                            "status": "1",
                            "active": "1",
                            "leader": "0"
                        }
                    ],
                    "roleName": "项目经理",
                    "newUserIdList": [
                        "SYS_E39B20EA11E7A81AC85B767C89C1"
                    ]
                },
                {
                    "roleKey": "MEMBER",
                    "isKeyMember": "0",
                    "name": "项目成员",
                    "oldUserIdList": [
                        "SYS_E39B20EA11E7A81AC85B767C89C1"
                    ],
                    "oldUserList": [
                        {
                            "id": "SYS_E39B20EA11E7A81AC85B767C89C1",
                            "orgId": "SYS_2d28fff04a3da56f410a241528b4",
                            "orgName": "组织部门",
                            "code": "1",
                            "name": "admin",
                            "displayName": "管理员",
                            "displayEn": "guanliyuan",
                            "mobile": "",
                            "email": "admin@domain.com",
                            "avatar": "./static/images/avatar/Avatar-3.png",
                            "type": "license",
                            "status": "1",
                            "active": "1",
                            "leader": "0"
                        }
                    ],
                    "newUserList": [
                        {
                            "id": "SYS_E39B20EA11E7A81AC85B767C89C1",
                            "orgId": "SYS_2d28fff04a3da56f410a241528b4",
                            "orgName": "组织部门",
                            "code": "1",
                            "name": "admin",
                            "displayName": "管理员",
                            "displayEn": "guanliyuan",
                            "mobile": "",
                            "email": "admin@domain.com",
                            "avatar": "./static/images/avatar/Avatar-3.png",
                            "type": "license",
                            "status": "1",
                            "active": "1",
                            "leader": "0"
                        }
                    ],
                    "roleName": "项目成员",
                    "newUserIdList": [
                        "SYS_E39B20EA11E7A81AC85B767C89C1"
                    ]
                }
            ],
            "projectChangeBudgetAddDtoList": ProjectChange.budget_voList
        }
        r = ApiProjectChange.add_order(self,
                                       creat_data=creat_data
                                       )
        ProjectChange.project_change_id = r['res']['data']['id']
        ProjectChange.project_change_order_code = r['res']['data']['changeOrderCode']
        print(ProjectChange.project_change_order_code)

    def test_0600_get_order_info_by_id(self):
        """
        接口名称：项目变更详情
        接口地址：/proj/$VERSION$/change/orderInfo
        """
        ApiProjectChange.get_order_info_by_id(self,
                                              project_change_id=ProjectChange.project_change_id,
                                              project_id=ProjectChange.project_id
                                              )

    def test_0600_select_page(self):
        """
        接口名称：项目变更列表查询
        接口地址：/proj/$VERSION$/change/ordersPage
        """
        ApiProjectChange.select_page(self, project_id=ProjectChange.project_id,
                                     change_order_code=ProjectChange.project_change_order_code)

    @unittest.skip('目前单个运行只能是project的接口')
    def test_0700_query_todo_task_list_by_user_id_and_system_id(self):
        """
        接口名称：获取待我处理 - 流程的信息
        接口地址：/workflow/$VERSION$/task/todotask
        """
        r = ApiProjectChange.query_todo_task_list_by_user_id_and_system_id(self)
        ProjectChange.process_instance_id = r['res']['data']['records'][0]['processInstanceId']
        ProjectChange.process_definition_id = r['res']['data']['records'][0]['processDefinitionId']
        ProjectChange.business_key = r['res']['data']['records'][0]['processInstanceDto']['businessKey']

    unittest.skip('目前单个运行只能是project的接口')

    @unittest.skip('该接口废弃')
    def test_0800_project_change_order_callback(self):
        """
        接口名称：项目变更流程回调接口
        接口地址：/proj/$VERSION$/change/changeOrder/callback
        """
        ApiProjectChange.project_change_order_callback(self,
                                                       process_instance_id=ProjectChange.process_instance_id,
                                                       process_definition_id=ProjectChange.process_definition_id,
                                                       business_key=ProjectChange.business_key
                                                       )

    def test_5000_delete_project(self):
        """
            接口名称：删除项目
            接口地址：/project/$VERSION$/{id}
        """
        ApiProject.deleteProjectUsingDELETE(self,
                                            project_id=ProjectChange.project_id,
                                            checker=None)


if __name__ == '__main__':
    unittest.main()

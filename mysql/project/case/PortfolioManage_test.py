# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 18:23
# @Author  : Liao
import random
import time
import unittest

from project.api import ApiStrategy
from project.api import ApiIndicatorElements, ApiPortfolioManage, ApiCombinationDecision
from project.case.file.runSql import db


class PortfolioManage(unittest.TestCase):
    """项目组合管理"""

    user_id = db.user_id
    department_id = db.org_id
    project_id = db.project_id
    strategy_goal_id = ""
    # 新增项目组合
    portfolio_name = "portfolio_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
    start_time = time.strftime('%Y-%m-%d', time.localtime())
    finish_time = time.strftime('%Y-%m-%d', time.localtime())
    budget = str(random.randint(1000, 9999))
    description = portfolio_name
    # 更新项目组合
    update_portfolio_name = ""

    portfolio_id = ""
    portfolio_code = ""
    role_bid1 = ""
    role_bid2 = ""
    parent_id = ""
    id1 = ""
    id2 = ""
    indicator_id = ""
    feature_id = ""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass

    def test_0100_create_portfolio(self):
        """
        新增组合
        """
        # /portfolio/$VERSION$/portfolio
        PortfolioManage.strategy_name = "strategy_" + time.strftime('%H%M%S', time.localtime())
        add_strategy = ApiStrategy.add_strategy(self,
                                                name=PortfolioManage.strategy_name,
                                                description=PortfolioManage.strategy_name
                                                )
        PortfolioManage.strategy_goal_id = str(add_strategy)
        print("strategy_goal_id：", PortfolioManage.strategy_goal_id)
        create_portfolio = ApiPortfolioManage.create_portfolio(self,
                                                               PortfolioManage.portfolio_name,
                                                               PortfolioManage.strategy_goal_id,
                                                 )
        PortfolioManage.portfolio_id = create_portfolio.get("id")
        PortfolioManage.portfolio_code = create_portfolio.get("code")

    def test_0200_add_attention(self):
        """
        添加关注/收藏/打开对象
        """
        # /portfolio/$VERSION$/portfolio/attention
        # type = 类型，0:最近打开的;1:我关注的; 2:我收藏的
        attention_type = "0"
        add_attention_result = ApiPortfolioManage.add_attention(self, PortfolioManage.portfolio_id, attention_type)
        print(add_attention_result)

    def test_0300_get_attentions(self):
        """
        查询用户关注/收藏/打开对象
        """
        # /portfolio/$VERSION$/portfolio/attentions
        # type = 类型，0:最近打开的;1:我关注的; 2:我收藏的
        attention_type = "0"
        get_attentions_result = ApiPortfolioManage.get_attentions(self, attention_type)
        print(get_attentions_result)

    def test_0400_cancel_attention(self):
        """
        取消关注/收藏/打开对象
        """
        # /portfolio/$VERSION$/portfolio/attention
        # type = 类型，0:最近打开的;1:我关注的; 2:我收藏的
        attention_type = "0"
        cancel_attention_result = ApiPortfolioManage.cancel_attention(self, PortfolioManage.portfolio_id,
                                                                      attention_type)
        print(cancel_attention_result)

    def test_0500_get_portfolio_by_id(self):
        """
        查询单个项目组合详情
        """
        # /portfolio/$VERSION$/portfolio/{id}
        get_portfolio_result = ApiPortfolioManage.get_portfolio_by_id(self, PortfolioManage.portfolio_id)
        print(get_portfolio_result)

    def test_0600_get_portfolio_list(self):
        """
        查询项目组合
        """
        # /portfolio/$VERSION$/portfolios
        get_portfolio_list_result = ApiPortfolioManage.get_portfolio_list(self)
        print(get_portfolio_list_result)

    def test_0700_get_all_portfolio(self):
        """
        查询所有项目组合
        """
        # /portfolio/$VERSION$/portfolios/all
        get_all_portfolio_result = ApiPortfolioManage.get_all_portfolio(self)
        print(get_all_portfolio_result)

    def test_0800_get_page_portfolio(self):
        """
        查询所有项目组合列表分页
        """
        # /portfolio/$VERSION$/portfolios/all/page
        get_page_portfolio_result = ApiPortfolioManage.get_page_portfolio(self)
        print(get_page_portfolio_result)

    def test_0900_update_portfolio(self):
        """
        修改组合基本信息
        """
        # /portfolio/$VERSION$/portfolio
        PortfolioManage.update_portfolio_name = "update_" + PortfolioManage.portfolio_name
        update_result = ApiPortfolioManage.update_portfolio(self, PortfolioManage.portfolio_id,
                                                            PortfolioManage.update_portfolio_name)
        print(update_result)

    def test_1000_add_subs_proj(self):
        """
        添加、移除项目
        """
        # /portfolio/$VERSION$/portfolio/subs/{id}
        operation = "add"
        add_type = "project"
        add_subs_proj_result = ApiPortfolioManage.add_subs_proj(self, PortfolioManage.portfolio_id,
                                                                PortfolioManage.project_id, add_type, operation)
        print(add_subs_proj_result)

    def test_1100_get_portfolio_proj(self):
        """
        查询组合名下所有项目列表
        """
        # /portfolio/$VERSION$/portfolio/{id}/projects
        get_portfolio_proj_result = ApiPortfolioManage.get_portfolio_proj(self, PortfolioManage.portfolio_id)
        print(get_portfolio_proj_result)

    def test_1200_search_proj_prog(self):
        """
        根据Code、名称查询项目群、项目
        """
        # /portfolio/$VERSION$/portfolio/paramsearch
        # type取值：program/project
        search_type = "project"
        search_proj_result = ApiPortfolioManage.search_proj_prog(self, PortfolioManage.portfolio_code,
                                                                 PortfolioManage.update_portfolio_name, search_type)
        print(search_proj_result)

    def test_1300_get_portfolio_tree(self):
        """
        查询组合树
        """
        # /portfolio/$VERSION$/portfolio/tree/{id}
        get_portfolio_tree_result = ApiPortfolioManage.get_portfolio_tree(self, PortfolioManage.portfolio_id)
        print(get_portfolio_tree_result)

    def test_1400_get_candidates(self):
        """
        查询候选项目
        """
        # /portfolio/$VERSION$/portfolio/candidates
        # type取值：program/project
        candidate_type = "project"
        get_candidates_result = ApiPortfolioManage.get_candidates(self, candidate_type)
        print(get_candidates_result)

    def test_1500_getAllProjectScoresUsingGET(self):
        """
        接口名称：获取项目组合下所有项目提案的评分
        接口地址：/decision/$VERSION$/all/project/{portfolioId}/score
        """
        r = ApiPortfolioManage.getAllProjectScoresUsingGET(self,
                                                           portfolioId=PortfolioManage.portfolio_id
                                                           )
        print("r:", r)

    def test_1600_getscoresUsingGET(self):
        """
        接口名称：获取项目机会评分
        接口地址：/decision/$VERSION$/project/{portfolioId}/score
        """
        ApiPortfolioManage.getscoresUsingGET(self,
                                             portfolioId=PortfolioManage.portfolio_id,
                                             procInstId="",
                                             project_id="",
                                             userId=""
                                             )

    def test_1700_getuserscoresUsingGET(self):
        """
        接口名称：获取当前登录人的项目机会评分
        接口地址：/decision/$VERSION$/project/{portfolioId}/userscore
        """
        ApiPortfolioManage.getuserscoresUsingGET(self,
                                                 portfolioId=PortfolioManage.portfolio_id,
                                                 project_id=db.project_id
                                                 )

    def test_1800_getScoreByproject_idUsingGET(self):
        """
        接口名称：获取单个项目机会评分
        接口地址：/decision/$VERSION$/project_id/score
        """
        ApiPortfolioManage.getScoreByproject_idUsingGET(self,
                                                        portfolioId=PortfolioManage.portfolio_id,
                                                        project_id=db.project_id
                                                        )

    def test_1900_projectsUsingGET_1(self):
        """
        接口名称：查询组合下项目机会列表
        接口地址：/decision/$VERSION$/{portfolioId}/projects
        """
        ApiPortfolioManage.projectsUsingGET_1(self,
                                              portfolioId=PortfolioManage.portfolio_id
                                              )

    def test_2000_getscorelistUsingGET(self):
        """
        接口名称：获取项目机会评分汇总
        接口地址：/decision/$VERSION$/{portfolioId}/score
        """
        ApiPortfolioManage.getscorelistUsingGET(self,
                                                portfolioId=PortfolioManage.portfolio_id,
                                                )

    def test_2100_editscoresUsingPUT(self):
        """
        接口名称：调整项目机会评分
        接口地址：/decision/$VERSION$/update/project/{portfolioId}/score
        """
        ApiPortfolioManage.editscoresUsingPUT(self,
                                              portfolioId="048e309b9fcf3e7da601e0650199911e",
                                              projectEvaluateScore=[
                                                  {"id": "1a852bd1dd8f3e4e95b9bc829945e7fb", "score": 11},
                                                  {"id": "f00700aac70aa22d2d43a823368c6d24", "score": 11}]
                                              )

    @unittest.skip('该接口已废弃不用')
    def test_2200_userEvaluateScoreStartNotifyUsingPOST(self):
        """
        接口名称：流程评分结束调用
        接口地址：/decision/$VERSION$/project/score/end
        """
        ApiPortfolioManage.userEvaluateScoreStartNotifyUsingPOST(self,
                                                                 params={
                                                                     "processInstanceId": "061b8ab0956011eca7d02e4fce3af5cb",
                                                                     "processDefinitionId": "PROJECT_SCORE:2:2e5aba24071811ec9c214a65b460b2ff",
                                                                     "serialNumber": "1",
                                                                     "trigger": "complete",
                                                                     "flowState": "",
                                                                     "processDefinitionKey": "PROJECT_SCORE",
                                                                     "bussinessFormDataJson": "[{\"flexAttrs\":{\"decisionMaking\":\"REANALYSIS\",\"decisionState\":\"PENDINGANALYSIS\"},\"code\":\"RDP20220224081\",\"templateInfo\":{},\"description\":\"<p>1</p>\",\"delFlag\":\"0\",\"type\":\"proposal\",\"startTime\":\"2022-02-20 00:00:00\",\"id\":\"12b01436d6381734364125d0e9446d9a\",\"state\":\"SKETCH\",\"finishTime\":\"2022-02-20 00:00:00\",\"pmIds\":[\"SYS_E39B20EA11E7A81AC85B767C89C1\"],\"updateTime\":\"2022-02-24 18:52:48\",\"parentId\":\"-1\",\"createBy\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"createTime\":\"2022-02-24 09:27:28\",\"isTemplate\":0,\"name\":\"122\",\"lifecycleTemplateId\":\"da92b41ba14a1eea50752ce6fd792557\",\"portfolioId\":\"6684fe697391d9d302db7c6d0bef077d\",\"_createByUser\":[],\"submitter\":[],\"_state\":\"提案\",\"_type\":\"proposal\",\"pmId\":[{\"id\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"orgId\":\"SYS_2d28fff04a3da56f410a241528b4\",\"orgName\":\"组织部门\",\"code\":\"1\",\"name\":\"admin\",\"displayName\":\"管理员\",\"displayEn\":\"guanliyuan\",\"mobile\":\"\",\"email\":\"admin@domain.com\",\"avatar\":\"./static/images/avatar/Avatar-3.png\",\"type\":\"license\",\"status\":\"1\",\"active\":\"1\",\"leader\":\"0\"}]}]",
                                                                     "taskDefinitionKey": "user1",
                                                                     "startUserId": "SYS_E39B20EA11E7A81AC85B767C89C1",
                                                                     "businessKeys": [
                                                                         "12b01436d6381734364125d0e9446d9a"
                                                                     ],
                                                                     "candidateUsers": "SYS_E39B20EA11E7A81AC85B767C89C1",
                                                                     "candidateGroups": "",
                                                                     "roleKey": "",
                                                                     "tenantId": "erdp",
                                                                     "assignee": "SYS_E39B20EA11E7A81AC85B767C89C1",
                                                                     "userTaskFormDataList": [
                                                                         {
                                                                             "userTaskFormDatas": "[{\"procInstId\":\"061b8ab0956011eca7d02e4fce3af5cb\",\"portfolioId\":\"6684fe697391d9d302db7c6d0bef077d\",\"project_id\":\"12b01436d6381734364125d0e9446d9a\",\"projectName\":\"122\",\"scoreUserId\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"scoreUserName\":\"admin\",\"score\":[{\"elem_id\":\"1462c851b1b5b3f4c943f3550eff113e\",\"score\":\"00011\"},{\"elem_id\":\"02dcac02fde0382fefff3fc30cc788e9\",\"score\":\"11\"},{\"elem_id\":\"12b01436d6381734364125d0e9446d9a\",\"score\":\"11\"}]}]",
                                                                             "lastUpdatedTime": 1645700034047
                                                                         }
                                                                     ],
                                                                     "historyUserTaskList": [],
                                                                     "task_id": "06430ff9956011eca7d02e4fce3af5cb"
                                                                 })

    def test_2300_updateProposalDecisionUsingPUT(self):
        """
        接口名称：设置决策结论
        接口地址：/decision/$VERSION$/project
        """
        ApiPortfolioManage.updateProposalDecisionUsingPUT(self,
                                                          project={
                                                              "flexAttrs": {
                                                                  "decisionMaking": "SUSPENSION"
                                                              },
                                                              "id": "12b01436d6381734364125d0e9446d9a"
                                                          }
                                                          )

    def test_2400_addUsingPOST_1(self):
        """
        接口名称：添加项目组合关联关系
        接口地址：/decision/$VERSION$/project/{portfolioId}
        """
        ApiPortfolioManage.addUsingPOST_1(self,
                                          portfolioId=PortfolioManage.portfolio_id
                                          )

    def test_2500_deleteLinkUsingDELETE(self):
        """
        接口名称：删除项目组合关联关系
        接口地址：/decision/$VERSION$/project/{portfolioId}/{project_id}
        """
        ApiPortfolioManage.deleteLinkUsingDELETE(self,
                                                 portfolioId=PortfolioManage.portfolio_id,
                                                 project_id=db.project_id
                                                 )

    def test_2600_archive_portfolio(self):
        """
        项目组合归档
        """
        #  /portfolio/$VERSION$/portfolio/archive/{id}
        archive_result = ApiPortfolioManage.archive_portfolio(self, PortfolioManage.portfolio_id)
        print(archive_result)

    def test_2700_get_archives(self):
        """
        查询用户归档项目组合
        """
        # /portfolio/$VERSION$/portfolio/archives/{userId}
        get_archives_result = ApiPortfolioManage.get_archives(self, PortfolioManage.user_id)
        print(get_archives_result)

    # def test_2800_delete_portfolio(self):
    #     """
    #     删除组合
    #     """
    #     # /portfolio/$VERSION$/portfolio/{id}
    #
    #     delete_result = ApiPortfolioManage.delete_portfolio(self, PortfolioManage.portfolio_id)
    #     print(delete_result)

        # #删除指标要素(该处存在一个bug--指标要素已在项目组合中使用，项目组合删除后，该指标要素仍删除不了，bug修复后将以下代码取消注释即可)
        # ApiIndicatorElements.deleteUsingDELETE_1(self,
        #                                          ids=PortfolioManage.feature_id
        #                                          )

    def test_2900_update(self):
        """
        接口名称：添加/修改组合决策指标要素关系
        接口地址：/decision/$VERSION$/portindelemlinks
        """
        # 新增指标要素定义
        r1 = ApiIndicatorElements.addUsingPOST(self)
        PortfolioManage.indicator_id = r1
        # 查询指标要素定义
        r2 = ApiIndicatorElements.queryOneUsingGET(self,
                                                   IndicatorId=PortfolioManage.indicator_id
                                                   )
        print(r2)
        PortfolioManage.feature_id = r2[0].get("id"), r2[1].get("id"), r2[0].get("id")
        print(PortfolioManage.feature_id)
        PortfolioManage.role_bid1 = r2[0].get("id")
        PortfolioManage.parent_id = r2[-1].get("parentId")
        PortfolioManage.role_bid2 = r2[-1].get("parentId")

        update = ApiCombinationDecision.updateUsingPUT_2(self,
                                                         portfolioId=PortfolioManage.portfolio_id,
                                                         role_bid1=PortfolioManage.role_bid1,
                                                         parent_id=PortfolioManage.parent_id,
                                                         role_bid2=PortfolioManage.role_bid2)

    def test_3000_query_one(self):
        """
        接口名称：查询组合决策指标要素关系
        接口地址：/decision/$VERSION$/portindelemlinks/{portfolioId}
        """
        query_one = ApiCombinationDecision.queryOneUsingGET_1(self,
                                                              portfolioId=PortfolioManage.portfolio_id)
        print(query_one)
        PortfolioManage.id1 = query_one[0].get("id")
        PortfolioManage.id2 = query_one[1].get("id")
        PortfolioManage.parent_id = query_one[1].get("parentId")

    def test_3100_save_weight(self):
        """
        接口名称：分配组合下的指标权重
        接口地址：/decision/$VERSION$/portindelemlinks/{portfolioId}/weight
        """
        save_weight = ApiCombinationDecision.saveWeightUsingPUT(self,
                                                                id1=PortfolioManage.id1,
                                                                portfolioId=PortfolioManage.portfolio_id,
                                                                role_bid1=PortfolioManage.role_bid1,
                                                                id2=PortfolioManage.id2,
                                                                role_bid2=PortfolioManage.role_bid2,
                                                                parent_id=PortfolioManage.parent_id
                                                                )
        print(save_weight)

    def test_3200_update_state(self):
        """
        接口名称：修改组合决策指标要素关系状态
        接口地址：/decision/$VERSION$/portindelemlinkstate/{portfolioId}
        """
        update_state = ApiCombinationDecision.updatestateUsingPUT(self, portfolioId=PortfolioManage.portfolio_id)
        print(update_state)


if __name__ == '__main__':
    unittest.main()

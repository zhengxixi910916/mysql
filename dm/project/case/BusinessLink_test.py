# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 15:04
# @Author  : Liao

import unittest
import time
from project.api import ApiProject, ApiProjectBaseline
from project.api import ApiBusinessLink, ApiUrgeMail

from project.case.file.runSql import db


class BusinessLink(unittest.TestCase):
    """
    任务、需求、问题、风险关联对象，计划、需求、问题、风险跟催
    """
    project_id = ""
    user_id = "025CE39B20EA11E7A81AC85B767C89C1"
    org_id = "69a12d9d163fec76d208e957289d0c53"
    task1_name = ""
    task_id1 = ""
    task_id2 = ""
    issue_id1 = ""
    issue_id2 = ""
    require_id1 = ""
    require_id2 = ""
    risk_id1 = ""
    risk_id2 = ""
    baseline_id1 = ""
    parentsId = ""
    baseline_snapshot_id = ""
    baseline_task1_id = ""
    @classmethod
    def setUpClass(cls):
        print(__name__)

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass

    def test_0101_search_task_business_linked(self):
        """
        接口名称：查询已经做关联的需求、任务、问题、风险列表
        接口地址：/plan/$VERSION$/{id}/businesslink
        """
        # 创建项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        project_add = ApiProject.addProjectUsingPOST_1(self,name=project_name)
        BusinessLink.project_id = project_add.get("id")
        print("project_id:", project_add.get("id"))

        # 创建任务
        BusinessLink.task1_name = "task1_" + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
        t1 = ApiBusinessLink.add_task(self,
                                      data={
                                          "name": BusinessLink.task1_name,
                                          "startDate": "",
                                          "finishDate": "",
                                          "milestoneFlag": "1",
                                          "state": "DRAFT",
                                          "criticalFlag": "1",
                                          "canBeCutted": "1",
                                          "description": "",
                                          "percentComplete": "",
                                          "projectId": BusinessLink.project_id,
                                          "parentId": "",
                                          "actualFinishDate": "",
                                          "workload": "",
                                          "duration": "",
                                          "resAssignments": "PM",
                                          "sop": "",
                                          "taskInput": "",
                                          "taskOutput": "",
                                          "fileIds": "",
                                          "summaryFlag": "0",
                                          "taskMemberList[0].roleKey": "IDENTIFY",
                                          "taskMemberList[0].userId": BusinessLink.user_id,
                                          "taskMemberList[1].roleKey": "HANDLEPERSON",
                                          "taskMemberList[1].userId": BusinessLink.user_id,
                                          "labelLinkIds": ""
                                      })
        t2 = ApiBusinessLink.add_task(self,
                                      data={
                                          "name": "task2_" + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()),
                                          "startDate": "",
                                          "finishDate": "",
                                          "milestoneFlag": "1",
                                          "state": "DRAFT",
                                          "criticalFlag": "1",
                                          "canBeCutted": "1",
                                          "description": "",
                                          "percentComplete": "",
                                          "projectId": BusinessLink.project_id,
                                          "parentId": "",
                                          "actualFinishDate": "",
                                          "workload": "",
                                          "duration": "",
                                          "resAssignments": "PM",
                                          "sop": "",
                                          "taskInput": "",
                                          "taskOutput": "",
                                          "fileIds": "",
                                          "summaryFlag": "0",
                                          "taskMemberList[0].roleKey": "IDENTIFY",
                                          "taskMemberList[0].userId": BusinessLink.user_id,
                                          "taskMemberList[1].roleKey": "HANDLEPERSON",
                                          "taskMemberList[1].userId": BusinessLink.user_id,
                                          "labelLinkIds": ""
                                      })
        BusinessLink.task_id1 = t1.get("id")
        BusinessLink.task_id2 = t2.get("id")
        print("task_id:", BusinessLink.task_id1, BusinessLink.task_id2)

        # 创建需求
        re1 = ApiBusinessLink.add_require(self,
                                          data={"department": BusinessLink.org_id,  # 需求提出部门 - required: False
                                                "description": "description_" + time.strftime('%Y_%m_%d_%H_%M_%S',
                                                                                              time.localtime()),
                                                # 描述 - required: False
                                                "dueDate": "",  # 结束时间 - required: False
                                                "labelLinkIds": "",  # 标签 - required: False
                                                "name": "require1_" + time.strftime('%Y_%m_%d_%H_%M_%S',
                                                                                    time.localtime()),
                                                # 名称 - required: False
                                                "ownerId": BusinessLink.project_id,  # 项目id或者用户id - required: False
                                                "ownerType": "2",  # 需求所属类型,1:个人,2:项目 - required: False
                                                "parentId": "",  # 父节点Id - required: False
                                                "priority": "1",  # 优先级，数据字典 - required: False
                                                "reqSource": "PLANNING",  # 需求来源 - required: False
                                                "state": "DRAFT",  # 状态 - required: False
                                                "submitTime": time.strftime('%Y-%m-%d', time.localtime()),
                                                # 需求提出时间 - required: False
                                                "submitterId": BusinessLink.user_id,  # 需求提出人 - required: False
                                                "type": type,  # 需求类型，来自数据字典 - required: False
                                                "workLoad": "",  # 工作量 - required: False}
                                                })
        re2 = ApiBusinessLink.add_require(self,
                                          data={"department": BusinessLink.org_id,  # 需求提出部门 - required: False
                                                "description": "description_" + time.strftime('%Y_%m_%d_%H_%M_%S',
                                                                                              time.localtime()),
                                                # 描述 - required: False
                                                "dueDate": "",  # 结束时间 - required: False
                                                "labelLinkIds": "",  # 标签 - required: False
                                                "name": "require2_" + time.strftime('%Y_%m_%d_%H_%M_%S',
                                                                                    time.localtime()),
                                                # 名称 - required: False
                                                "ownerId": BusinessLink.project_id,  # 项目id或者用户id - required: False
                                                "ownerType": "2",  # 需求所属类型,1:个人,2:项目 - required: False
                                                "parentId": "",  # 父节点Id - required: False
                                                "priority": "1",  # 优先级，数据字典 - required: False
                                                "reqSource": "PLANNING",  # 需求来源 - required: False
                                                "state": "DRAFT",  # 状态 - required: False
                                                "submitTime": time.strftime('%Y-%m-%d', time.localtime()),
                                                # 需求提出时间 - required: False
                                                "submitterId": BusinessLink.user_id,  # 需求提出人 - required: False
                                                "type": type,  # 需求类型，来自数据字典 - required: False
                                                "workLoad": "",  # 工作量 - required: False}
                                                })
        BusinessLink.require_id1 = re1.get("id")
        BusinessLink.require_id2 = re2.get("id")
        print("requirement_id:", BusinessLink.require_id1, BusinessLink.require_id2)

        # 创建问题
        i1 = ApiBusinessLink.add_issue(self,
                                       {"actualFinishDate": "",  # 实际完成时间  - required: False
                                        "actualStartDate": "",  # 实际开始时间 - required: False
                                        "description": "description",  # 描述 - required: False
                                        "finishDate": "",  # 计划完成时间 - required: False
                                        "labelLinkIds": "",  # 标签 - required: False
                                        "name": "issue1_" + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()),
                                        # 名称 - required: False
                                        "priority": "1",  # 优先级 - required: False
                                        "projectId": BusinessLink.project_id,  # 项目ID - required: False
                                        "state": "DRAFT",  # 问题状态（待处理[0];已处理[1];已过期[2]） - required: False
                                        "type": "1",  # 类型 - required: False
                                        "workload": "",  # 工作量 - required: False
                                        "submitter[id]": BusinessLink.user_id,
                                        "submitter[displayName]": "name",
                                        "submitter[code]": time.strftime('%H%M%S', time.localtime()),
                                        "submitter[name]": "name",
                                        "submitter[avatar]": "./img/downLoad/d0e47e26b1e84170ab995cc2de5fb310?_=1620804962106"}
                                       )
        i2 = ApiBusinessLink.add_issue(self,
                                       {"actualFinishDate": "",  # 实际完成时间  - required: False
                                        "actualStartDate": "",  # 实际开始时间 - required: False
                                        "description": "description",  # 描述 - required: False
                                        "finishDate": "",  # 计划完成时间 - required: False
                                        "labelLinkIds": "",  # 标签 - required: False
                                        "name": "issue2_" + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()),
                                        # 名称 - required: False
                                        "priority": "1",  # 优先级 - required: False
                                        "projectId": BusinessLink.project_id,  # 项目ID - required: False
                                        "state": "DRAFT",  # 问题状态（待处理[0];已处理[1];已过期[2]） - required: False
                                        "type": "1",  # 类型 - required: False
                                        "workload": "",  # 工作量 - required: False
                                        "submitter[id]": BusinessLink.user_id,
                                        "submitter[displayName]": "name",
                                        "submitter[code]": time.strftime('%H%M%S', time.localtime()),
                                        "submitter[name]": "name",
                                        "submitter[avatar]": "./img/downLoad/d0e47e26b1e84170ab995cc2de5fb310?_=1620804962106"})
        BusinessLink.issue_id1 = i1.get("id")
        BusinessLink.issue_id2 = i2.get("id")
        print("issue_id:", BusinessLink.issue_id1, BusinessLink.issue_id2)

        # 创建风险
        ri1 = ApiBusinessLink.add_risk(self,
                                       name="risk1_" + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()),
                                       project_id=BusinessLink.project_id,
                                       )
        ri2 = ApiBusinessLink.add_risk(self,
                                       name="risk2_" + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()),
                                       project_id=BusinessLink.project_id,
                                       )

        BusinessLink.risk_id1 = ri1.get("id")
        BusinessLink.risk_id1 = ri2.get("id")
        print("risk_id:", BusinessLink.risk_id1, BusinessLink.risk_id2)

        # 查询已经做关联的需求、任务、问题、风险列表
        search_task_business_linked = ApiBusinessLink.search_task_business_linked(self, task_id=BusinessLink.task_id1)
        print(search_task_business_linked)

    def test_0102_search_task_avl_business_Link(self):
        """
        接口名称：搜索可以做关联的需求、问题、风险
        接口地址：/plan/$VERSION$/{id}/businesslink/{type}
        """
        search_task_avl_business_link0 = ApiBusinessLink.search_task_avl_business_link(self,
                                                                                       task_id=BusinessLink.task_id1,
                                                                                       project_id=BusinessLink.project_id,
                                                                                       type_="ELTask"
                                                                                       )
        search_task_avl_business_link1 = ApiBusinessLink.search_task_avl_business_link(self,
                                                                                       task_id=BusinessLink.task_id1,
                                                                                       project_id=BusinessLink.project_id,
                                                                                       type_="ELRequire"
                                                                                       )
        search_task_avl_business_link2 = ApiBusinessLink.search_task_avl_business_link(self,
                                                                                       task_id=BusinessLink.task_id1,
                                                                                       project_id=BusinessLink.project_id,
                                                                                       type_="ELIssue"
                                                                                       )
        search_task_avl_business_link3 = ApiBusinessLink.search_task_avl_business_link(self,
                                                                                       task_id=BusinessLink.task_id1,
                                                                                       project_id=BusinessLink.project_id,
                                                                                       type_="ELRisk"
                                                                                       )
        search_task_avl_business_link4 = ApiBusinessLink.search_task_avl_business_link(self,
                                                                                       task_id=BusinessLink.task_id1,
                                                                                       project_id=BusinessLink.project_id,
                                                                                       type_="ELDocument"
                                                                                       )
        print(search_task_avl_business_link0, search_task_avl_business_link1, search_task_avl_business_link2,
              search_task_avl_business_link3, search_task_avl_business_link4)

    def test_0103_add_task_business_link(self):
        """
        接口名称：添加业务对象关联
        接口地址：/plan/$VERSION$/{id}/businesslink/{type}
        """
        add_task_business_link0 = ApiBusinessLink.add_task_business_link(self,
                                                                         role_a_id=BusinessLink.task_id1,
                                                                         type_="ELTask",
                                                                         role_b_id=BusinessLink.task_id2
                                                                         )
        add_task_business_link1 = ApiBusinessLink.add_task_business_link(self,
                                                                         role_a_id=BusinessLink.task_id1,
                                                                         type_="ELRequire",
                                                                         role_b_id=BusinessLink.require_id1
                                                                         )
        add_task_business_link2 = ApiBusinessLink.add_task_business_link(self,
                                                                         role_a_id=BusinessLink.task_id1,
                                                                         type_="ELIssue",
                                                                         role_b_id=BusinessLink.issue_id1
                                                                         )
        add_task_business_link3 = ApiBusinessLink.add_task_business_link(self,
                                                                         role_a_id=BusinessLink.task_id1,
                                                                         type_="ELRisk",
                                                                         role_b_id=BusinessLink.risk_id1
                                                                         )
        add_task_business_link4 = ApiBusinessLink.add_task_business_link(self,
                                                                         role_a_id=BusinessLink.task_id1,
                                                                         type_="ELDocument",
                                                                         role_b_id=db.document_id
                                                                         )
        print(add_task_business_link0, add_task_business_link1, add_task_business_link2,
              add_task_business_link3, add_task_business_link4)

    def test_0104_delete_task_business_link(self):
        """
        接口名称：删除关联
        接口地址：/plan/$VERSION$/{id}/businesslink/{type}
        """
        delete_task_business_link0 = ApiBusinessLink.delete_task_business_link(self,
                                                                               task_id=BusinessLink.task_id1,
                                                                               type_="ELTask",
                                                                               business_id=BusinessLink.task_id2
                                                                               )
        delete_task_business_link1 = ApiBusinessLink.delete_task_business_link(self,
                                                                               task_id=BusinessLink.task_id1,
                                                                               type_="ELRequire",
                                                                               business_id=BusinessLink.require_id1
                                                                               )
        delete_task_business_link2 = ApiBusinessLink.delete_task_business_link(self,
                                                                               task_id=BusinessLink.task_id1,
                                                                               type_="ELIssue",
                                                                               business_id=BusinessLink.issue_id1
                                                                               )
        delete_task_business_link3 = ApiBusinessLink.delete_task_business_link(self,
                                                                               task_id=BusinessLink.task_id1,
                                                                               type_="ELRisk",
                                                                               business_id=BusinessLink.risk_id1
                                                                               )
        # todo 先不测试，后面看看为什么传的是文档id
        # delete_task_business_link4 = ApiBusinessLink.delete_task_business_link(self,
        #                                                                        task_id=BusinessLink.task_id1,
        #                                                                        type_="ELDocument",
        #                                                                        business_id=db.document_id
        #                                                                        )

    def test_0105_search_task_business(self):
        """
        查询关联的需求、问题、风险列表
        """
        # /plan/$VERSION$/task/{id}/businesses
        search_task_business = ApiBusinessLink.search_task_business(self, task_id=BusinessLink.task_id1)
        print(search_task_business)

    def test_0106_search_task_business_1(self):
        """
        搜索可以关联的需求、问题、风险
        """
        # /plan/v1/task/{id}/candidatebusinesses
        search_task_business_1 = ApiBusinessLink.search_task_business_1(self, task_id=BusinessLink.task_id1,
                                                                        type_="issue")
        print(search_task_business_1)

    def test_0201_search_req_business_linked(self):
        """
        查询已经做关联的需求、任务、问题、风险列表
        """
        # /req/$VERSION$/{id}/businesslink
        search_req_business_linked = ApiBusinessLink.search_req_business_linked(self,
                                                                                requireid=BusinessLink.require_id1)
        print(search_req_business_linked)

    def test_0202_search_req_avl_business_link(self):
        """
        接口名称：搜索可以做关联的任务、问题、风险
        接口地址：/req/$VERSION$/{id}/businesslink/{type}
        """
        search_req_avl_business_link0 = ApiBusinessLink.search_req_avl_business_link(self,
                                                                                     require_id=BusinessLink.require_id1,
                                                                                     project_id=BusinessLink.project_id,
                                                                                     type_="ELTask"
                                                                                     )
        search_req_avl_business_link1 = ApiBusinessLink.search_req_avl_business_link(self,
                                                                                     require_id=BusinessLink.require_id1,
                                                                                     project_id=BusinessLink.project_id,
                                                                                     type_="ELRequire"
                                                                                     )
        search_req_avl_business_link2 = ApiBusinessLink.search_req_avl_business_link(self,
                                                                                     require_id=BusinessLink.require_id1,
                                                                                     project_id=BusinessLink.project_id,
                                                                                     type_="ELIssue"
                                                                                     )
        search_req_avl_business_link3 = ApiBusinessLink.search_req_avl_business_link(self,
                                                                                     require_id=BusinessLink.require_id1,
                                                                                     project_id=BusinessLink.project_id,
                                                                                     type_="ELRisk"
                                                                                     )
        search_req_avl_business_link4 = ApiBusinessLink.search_req_avl_business_link(self,
                                                                                     require_id=BusinessLink.require_id1,
                                                                                     project_id=BusinessLink.project_id,
                                                                                     type_="ELDocument"
                                                                                     )

        print(search_req_avl_business_link0, search_req_avl_business_link1, search_req_avl_business_link2,
              search_req_avl_business_link3, search_req_avl_business_link4)

    def test_0203_add_req_business_link(self):
        """
        接口名称：添加业务对象关联
        接口地址：/req/$VERSION$/{id}/businesslink/{type}
        """
        add_req_business_link0 = ApiBusinessLink.add_req_business_link(self,
                                                                       role_a_id=BusinessLink.require_id1,
                                                                       type_="ELTask",
                                                                       role_b_id=BusinessLink.task_id1
                                                                       )
        add_req_business_link1 = ApiBusinessLink.add_req_business_link(self,
                                                                       role_a_id=BusinessLink.require_id1,
                                                                       type_="ELRequire",
                                                                       role_b_id=BusinessLink.require_id2
                                                                       )
        add_req_business_link2 = ApiBusinessLink.add_req_business_link(self,
                                                                       role_a_id=BusinessLink.require_id1,
                                                                       type_="ELIssue",
                                                                       role_b_id=BusinessLink.issue_id1
                                                                       )
        add_req_business_link3 = ApiBusinessLink.add_req_business_link(self,
                                                                       role_a_id=BusinessLink.require_id1,
                                                                       type_="ELRisk",
                                                                       role_b_id=BusinessLink.risk_id1
                                                                       )
        add_req_business_link4 = ApiBusinessLink.add_req_business_link(self,
                                                                       role_a_id=BusinessLink.require_id1,
                                                                       type_="ELDocument",
                                                                       role_b_id=db.document_id
                                                                       )

        print(add_req_business_link0, add_req_business_link1, add_req_business_link2,
              add_req_business_link3, add_req_business_link4)

    def test_0204_delete_req_business_link(self):
        """
        接口名称：删除关联
        接口地址：/req/$VERSION$/{id}/businesslink/{type}
        """
        delete_req_business_link0 = ApiBusinessLink.delete_req_business_link(self,
                                                                             require_id=BusinessLink.require_id1,
                                                                             type_="ELTask",
                                                                             business_id=BusinessLink.task_id1
                                                                             )
        delete_req_business_link1 = ApiBusinessLink.delete_req_business_link(self,
                                                                             require_id=BusinessLink.require_id1,
                                                                             type_="ELRequire",
                                                                             business_id=BusinessLink.require_id2
                                                                             )
        delete_req_business_link2 = ApiBusinessLink.delete_req_business_link(self,
                                                                             require_id=BusinessLink.require_id1,
                                                                             type_="ELIssue",
                                                                             business_id=BusinessLink.issue_id1
                                                                             )
        delete_req_business_link3 = ApiBusinessLink.delete_req_business_link(self,
                                                                             require_id=BusinessLink.require_id1,
                                                                             type_="ELRisk",
                                                                             business_id=BusinessLink.risk_id1
                                                                             )
        delete_req_business_link4 = ApiBusinessLink.delete_req_business_link(self,
                                                                             require_id=BusinessLink.require_id1,
                                                                             type_="ELDocument",
                                                                             business_id=db.document_id
                                                                             )
        print(delete_req_business_link0, delete_req_business_link1, delete_req_business_link2,
              delete_req_business_link3, delete_req_business_link4)

    def test_0301_search_issue_business_linked(self):
        """
        接口名称：查询已经做关联的需求、任务、问题、风险列表
        接口地址：/issue/$VERSION$/{id}/businesslink
        """
        search_issue_business_linked = ApiBusinessLink.search_issue_business_linked(self,
                                                                                    issue_id=BusinessLink.issue_id1)
        print(search_issue_business_linked)

    def test_0302_search_issue_avl_business_link(self):
        """
        接口名称：搜索可以做关联的需求、任务、风险、问题
        接口地址：/issue/$VERSION$/{id}/businesslink/{type}
        """
        search_issue_avl_business_link0 = ApiBusinessLink.search_issue_avl_business_link(self,
                                                                                         issue_id=BusinessLink.issue_id1,
                                                                                         project_id=BusinessLink.project_id,
                                                                                         type_="ELTask"
                                                                                         )
        search_issue_avl_business_link1 = ApiBusinessLink.search_issue_avl_business_link(self,
                                                                                         issue_id=BusinessLink.issue_id1,
                                                                                         project_id=BusinessLink.project_id,
                                                                                         type_="ELRequire"
                                                                                         )
        search_issue_avl_business_link2 = ApiBusinessLink.search_issue_avl_business_link(self,
                                                                                         issue_id=BusinessLink.issue_id1,
                                                                                         project_id=BusinessLink.project_id,
                                                                                         type_="ELIssue"
                                                                                         )
        search_issue_avl_business_link3 = ApiBusinessLink.search_issue_avl_business_link(self,
                                                                                         issue_id=BusinessLink.issue_id1,
                                                                                         project_id=BusinessLink.project_id,
                                                                                         type_="ELRisk"
                                                                                         )
        search_issue_avl_business_link4 = ApiBusinessLink.search_issue_avl_business_link(self,
                                                                                         issue_id=BusinessLink.issue_id1,
                                                                                         project_id=BusinessLink.project_id,
                                                                                         type_="ELDocument"
                                                                                         )
        print(search_issue_avl_business_link0, search_issue_avl_business_link1, search_issue_avl_business_link2,
              search_issue_avl_business_link3, search_issue_avl_business_link4)

    def test_0303_issue_business_link(self):
        """
        接口名称：添加业务对象关联
        接口地址：/issue/$VERSION$/{id}/businesslink/{type}
        """
        add_issue_business_link0 = ApiBusinessLink.add_issue_business_link(self,
                                                                           role_a_id=BusinessLink.issue_id1,
                                                                           type_="ELTask",
                                                                           role_b_id=BusinessLink.task_id1
                                                                           )
        add_issue_business_link1 = ApiBusinessLink.add_issue_business_link(self,
                                                                           role_a_id=BusinessLink.issue_id1,
                                                                           type_="ELRequire",
                                                                           role_b_id=BusinessLink.require_id1
                                                                           )
        add_issue_business_link2 = ApiBusinessLink.add_issue_business_link(self,
                                                                           role_a_id=BusinessLink.issue_id1,
                                                                           type_="ELIssue",
                                                                           role_b_id=BusinessLink.issue_id2
                                                                           )
        add_issue_business_link3 = ApiBusinessLink.add_issue_business_link(self,
                                                                           role_a_id=BusinessLink.issue_id1,
                                                                           type_="ELRisk",
                                                                           role_b_id=BusinessLink.risk_id1
                                                                           )
        add_issue_business_link4 = ApiBusinessLink.add_issue_business_link(self,
                                                                           role_a_id=BusinessLink.issue_id1,
                                                                           type_="ELDocument",
                                                                           role_b_id=db.document_id
                                                                           )
        print(add_issue_business_link0, add_issue_business_link1, add_issue_business_link2,
              add_issue_business_link3, add_issue_business_link4)

    def test_0304_delete_issue_business_link(self):
        """
        接口名称：删除关联
        接口地址：/issue/$VERSION$/{id}/businesslink/{type}
        """
        delete_issue_business_link0 = ApiBusinessLink.delete_issue_business_link(self,
                                                                                 issue_id=BusinessLink.issue_id1,
                                                                                 type_="ELTask",
                                                                                 business_id=BusinessLink.task_id1
                                                                                 )
        delete_issue_business_link1 = ApiBusinessLink.delete_issue_business_link(self,
                                                                                 issue_id=BusinessLink.issue_id1,
                                                                                 type_="ELRequire",
                                                                                 business_id=BusinessLink.require_id1
                                                                                 )
        delete_issue_business_link2 = ApiBusinessLink.delete_issue_business_link(self,
                                                                                 issue_id=BusinessLink.issue_id1,
                                                                                 type_="ELIssue",
                                                                                 business_id=BusinessLink.issue_id2
                                                                                 )
        delete_issue_business_link3 = ApiBusinessLink.delete_issue_business_link(self,
                                                                                 issue_id=BusinessLink.issue_id1,
                                                                                 type_="ELRisk",
                                                                                 business_id=BusinessLink.risk_id1
                                                                                 )
        # delete_issue_business_link4 = ApiBusinessLink.delete_issue_business_link(self,
        #                                                                          issue_id=BusinessLink.issue_id1,
        #                                                                          type_="ELDocument",
        #                                                                          business_id=db.document_id
        #                                                                          )

    def test_0401_search_risk_business_linked(self):
        """
        查询已经做关联的需求、任务、问题、风险列表
        """
        # /risk/$VERSION$/{id}/businesslink
        search_risk_business_linked = ApiBusinessLink.search_risk_business_linked(self, risk_id=BusinessLink.risk_id1)
        print(search_risk_business_linked)

    def test_0402_search_risk_avl_business_link(self):
        """
        接口名称：搜索可以做关联的需求、问题、任务
        接口地址：/risk/$VERSION$/{id}/businesslink/{type}
        """
        search_risk_avl_business_link0 = ApiBusinessLink.search_risk_avl_business_link(self,
                                                                                       risk_id=BusinessLink.risk_id1,
                                                                                       project_id=BusinessLink.project_id,
                                                                                       type_="ELTask"
                                                                                       )
        search_risk_avl_business_link1 = ApiBusinessLink.search_risk_avl_business_link(self,
                                                                                       risk_id=BusinessLink.risk_id1,
                                                                                       project_id=BusinessLink.project_id,
                                                                                       type_="ELRequire"
                                                                                       )
        search_risk_avl_business_link2 = ApiBusinessLink.search_risk_avl_business_link(self,
                                                                                       risk_id=BusinessLink.risk_id1,
                                                                                       project_id=BusinessLink.project_id,
                                                                                       type_="ELIssue"
                                                                                       )
        search_risk_avl_business_link3 = ApiBusinessLink.search_risk_avl_business_link(self,
                                                                                       risk_id=BusinessLink.risk_id1,
                                                                                       project_id=BusinessLink.project_id,
                                                                                       type_="ELRisk"
                                                                                       )
        search_risk_avl_business_link4 = ApiBusinessLink.search_risk_avl_business_link(self,
                                                                                       risk_id=BusinessLink.risk_id1,
                                                                                       project_id=BusinessLink.project_id,
                                                                                       type_="ELDocument"
                                                                                       )
        print(search_risk_avl_business_link0, search_risk_avl_business_link1, search_risk_avl_business_link2,
              search_risk_avl_business_link3, search_risk_avl_business_link4)

    def test_0403_risk_business_link(self):
        """
        接口名称：添加业务对象关联
        接口地址：/risk/$VERSION$/{id}/businesslink/{type}
        """
        add_risk_business_link0 = ApiBusinessLink.add_risk_business_link(self,
                                                                         role_a_id=BusinessLink.risk_id1,
                                                                         type_="ELTask",
                                                                         role_b_id=BusinessLink.task_id1
                                                                         )
        add_risk_business_link1 = ApiBusinessLink.add_risk_business_link(self,
                                                                         role_a_id=BusinessLink.risk_id1,
                                                                         type_="ELRequire",
                                                                         role_b_id=BusinessLink.require_id1
                                                                         )
        add_risk_business_link2 = ApiBusinessLink.add_risk_business_link(self,
                                                                         role_a_id=BusinessLink.risk_id1,
                                                                         type_="ELIssue",
                                                                         role_b_id=BusinessLink.issue_id1
                                                                         )
        add_risk_business_link3 = ApiBusinessLink.add_risk_business_link(self,
                                                                         role_a_id=BusinessLink.risk_id1,
                                                                         type_="ELRisk",
                                                                         role_b_id=BusinessLink.risk_id2
                                                                         )
        add_risk_business_link4 = ApiBusinessLink.add_risk_business_link(self,
                                                                         role_a_id=BusinessLink.risk_id1,
                                                                         type_="ELDocument",
                                                                         role_b_id=db.document_id
                                                                         )
        print(add_risk_business_link0, add_risk_business_link1, add_risk_business_link2,
              add_risk_business_link3, add_risk_business_link4)

    def test_0404_delete_risk_business_link(self):
        """
        接口名称：删除关联
        接口地址：/risk/$VERSION$/{id}/businesslink/{type}
        """
        delete_risk_business_link0 = ApiBusinessLink.delete_risk_business_link(self,
                                                                               risk_id=BusinessLink.risk_id1,
                                                                               type_="ELTask",
                                                                               business_id=BusinessLink.task_id1
                                                                               )
        delete_risk_business_link1 = ApiBusinessLink.delete_risk_business_link(self,
                                                                               risk_id=BusinessLink.risk_id1,
                                                                               type_="ELRequire",
                                                                               business_id=BusinessLink.require_id1
                                                                               )
        delete_risk_business_link2 = ApiBusinessLink.delete_risk_business_link(self,
                                                                               risk_id=BusinessLink.risk_id1,
                                                                               type_="ELIssue",
                                                                               business_id=BusinessLink.issue_id1
                                                                               )
        delete_risk_business_link3 = ApiBusinessLink.delete_risk_business_link(self,
                                                                               risk_id=BusinessLink.risk_id1,
                                                                               type_="ELRisk",
                                                                               business_id=BusinessLink.risk_id2
                                                                               )
        # todo 先不测试，后面看看为什么传的是文档id
        # delete_risk_business_link4 = ApiBusinessLink.delete_risk_business_link(self,
        #                                                                        risk_id=BusinessLink.risk_id1,
        #                                                                        type_="ELDocument",
        #                                                                        business_id=db.document_id
        #                                                                        )

    def test_0501_baseline_add(self):
        """
        接口名称：添加基线
        接口地址：/proj/$VERSION$/baseline/add
        """
        pro_r1 = ApiProjectBaseline.baseline_add(self,
                                            name="test_" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()),
                                            baseline_type="project",
                                            baseline_date="",
                                            description="123456",
                                            project_id=BusinessLink.project_id,
                                            )
        task_r1 = ApiProjectBaseline.baseline_add(self,
                                                  name="\t "+BusinessLink.task1_name,
                                                  baseline_type="task",
                                                  baseline_date="",
                                                  description="123456",
                                                  project_id=BusinessLink.project_id
                                                )
        BusinessLink.baseline_id1 = pro_r1.get("id")
        BusinessLink.baseline_task1_id = task_r1.get("id")

    def test_0502_get_project_by_base_line(self):
        """
        接口名称： 根据基线ID查询项目基本信息
        接口地址：/proj/$VERSION$/baseline/project/{id}
        """
        ApiProjectBaseline.get_project_by_baseline_id_using_get(self,
                                                                baseline_id=BusinessLink.baseline_id1)

    def test_0503_baseline_compare(self):
        """
        接口名称：基线对比
        接口地址：/proj/$VERSION$/baseline/compare
        """
        ApiProjectBaseline.baseline_compare(self,
                                            baseline_id1=BusinessLink.baseline_id1,
                                            baseline_id2="-1",
                                            project_id=BusinessLink.project_id,
                                            fields="name",
                                            )

    def test_0504_Baseline_Page_List(self):
        """
        接口名称：基线分页列表
        接口地址：/proj/$VERSION$/baseline/list/page
        """
        r = ApiProjectBaseline.baseline_page_list(self,
                                                  name="",
                                                  baseline_type="",
                                                  pager_name="10",
                                                  sort_by="",
                                                  order_by="",
                                                  page_size="10",
                                                  page_index="1",
                                                  project_id=BusinessLink.project_id,
                                                  )
        print(r)

    def test_0505_Baseline_List(self):
        """
        接口名称：基线列表
        接口地址：/proj/$VERSION$/baseline/snapshot/list
        """
        r = ApiProjectBaseline.baseline_list(self,
                                             project_id=BusinessLink.project_id,
                                             baseline_type="task"
                                             )
        BusinessLink.baseline_snapshot_id = r[0]['id']
        print(r)

    def test_0506_Baseline_Type_List(self):
        """基线类型列表"""
        ApiProjectBaseline.baseline_type_list(self)

    # @unittest.skip('未用到')
    def test_0507_select_Business_List_Using_POST_5(self):
        """
        接口名称：查询业务数据
        接口地址：/plan/$VERSION$/baseline/{viewid}/businesslist
        """
        r = ApiProjectBaseline.select_business_list_using_post_5(self,
                                                                 view_id=db.task_view_id,
                                                                 view_dto={"pageindex": 1, "pagesize": 20,
                                                                           "mgReqFlag": "false"}
                                                                 )
        BusinessLink.parentsId = r["res"]["data"]["records"][0]["id"]

    def test_0508_snapshot_Using_GET_1(self):
        """
        接口名称：快照任务对象基本信息详情查询
        接口地址：/plan/$VERSION$/baseline/snapshot/{id}
        """
        ApiProjectBaseline.snapshot_using_get_1(self, task_id1=BusinessLink.parentsId)

    def test_0509_get_Tasks_Using_GET(self):
        """
        接口名称：通过基线获取任务列表（项目下）
        接口地址：/plan/$VERSION$/baseline/tasks
        """
        ApiProjectBaseline.get_tasks_using_get(self,
                                               project_id=BusinessLink.project_id,
                                               baseline_id=BusinessLink.baseline_id1
                                               )

    def test_0510_get_First_Level_Children_Tasks_By_Task_Id_Using_GET(self):
        """
        接口名称：根据任务id获取第一层子基线任务列表
        接口地址：/plan/$VERSION$/baseline/tasks/{id}/children
        """
        ApiProjectBaseline.get_first_level_children_tasks_by_task_id_using_get(self,
                                                                               task_id=BusinessLink.parentsId,
                                                                               baseline_id=BusinessLink.baseline_id1
                                                                               )

    def test_0511_Baseline_Delete(self):
        """
        接口名称：清除基线
        接口地址：/proj/$VERSION$/baseline/delete
        """
        ApiProjectBaseline.baseline_delete(self,
                                           baseline_id=BusinessLink.baseline_id1
                                           )

    def test_0601_task_urge_mail_using_post(self):
        """
        接口名称：计划跟催邮件发送
        接口地址：/plan/$VERSION$/urge/mail
        """
        ApiUrgeMail.task_urge_mail_using_post(self,
                                              copy_mails="",
                                              description="测试计划跟催。",
                                              task_id=BusinessLink.task_id1,
                                              title="计划跟催",
                                              to_mails="admin@domain.com"
                                              )

    def test_0602_req_urge_mail_using_post(self):
        """
        接口名称：需求跟催邮件发送
        接口地址：/req/$VERSION$/urge/mail
        """
        ApiUrgeMail.req_urge_mail_using_post(self,
                                             copy_mails="",
                                             description="测试需求跟催。",
                                             req_id=BusinessLink.require_id1,
                                             title="需求跟催",
                                             to_mails="admin@domain.com"
                                             )

    def test_0603_issue_urge_mail_using_post(self):
        """
        接口名称：问题跟催邮件发送
        接口地址：/issue/$VERSION$/urge/mail
        """
        ApiUrgeMail.issue_urge_mail_using_post(self,
                                               copy_mails="",
                                               description="测试问题跟催。",
                                               issue_id=BusinessLink.issue_id1,
                                               title="问题跟催",
                                               to_mails="chenguangda@e-lead.cn"
                                               )

    def test_0604_risk_urge_mail_using_post(self):
        """
        接口名称：风险跟催邮件发送
        接口地址：/risk/$VERSION$/urge/mail
        """
        ApiUrgeMail.risk_urge_mail_using_post(self,
                                              copy_mails="",
                                              description='<div class="ps__scrollbar-x-rail" style="left: 0px; bottom: 0px;"><div tabindex="0" class="ps__scrollbar-x" style="left: 0px; width: 0px;"></div></div><div class="ps__scrollbar-y-rail" style="top: 0px; right: 0px;"><div tabindex="0" class="ps__scrollbar-y" style="top: 0px; height: 0px;"></div></div>',
                                              risk_id=BusinessLink.risk_id1,
                                              title="风险跟催",
                                              to_mails="chenguangda@e-lead.cn"
                                              )

        # 删除项目
        project_delete = ApiProject.deleteProjectUsingDELETE(self, project_id=BusinessLink.project_id)
        print(project_delete)


if __name__ == '__main__':
    unittest.main(verbosity=2)

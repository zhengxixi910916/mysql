# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 15:04
# @Author  : Liao
import random
import time
import unittest

from project.api import ApiIssueManage, ApiRiskManage, ApiProject
from project.case.file.runSql import db


class IssueManage(unittest.TestCase):
    """问题基础信息操作"""

    user_id = db.user_id
    project_id = db.project_id
    org_id = db.org_id
    # 问题视图-所有的
    view_id = db.issue_view_id

    static_date = time.strftime('%Y-%m', time.localtime())
    issue_id = ""
    copy_issue_id = ""
    issue_name = ""
    insertbatch_id = ""
    checklist_id = ""
    labels_id = ""
    attr_id = ""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass

        # if IssueManage.issue_id != "":
        #     DB.instance().clear_condition(section="project",
        #                                   table="issue_elissue",
        #                                   condition={"id": IssueManage.issue_id}
        #                                   )
        # if IssueManage.copy_issue_id != "":
        #     DB.instance().clear_condition(section="project",
        #                                   table="issue_elissue",
        #                                   condition={"id": IssueManage.copy_issue_id}
        #                                   )
        # if IssueManage.insertbatch_id != "":
        #     DB.instance().clear_condition(section="project",
        #                                   table="issue_elissue",
        #                                   condition={"id": IssueManage.insertbatch_id}
        #                                   )
        # if IssueManage.labels_id != "":
        #     DB.instance().clear_condition(section="system",
        #                                   table="sys_eldictionary",
        #                                   condition={"id": IssueManage.labels_id}
        #                                   )
        # if IssueManage.attr_id != "":
        #     DB.instance().clear_condition(section="system",
        #                                   table="sys_elview_basefield",
        #                                   condition={"id": IssueManage.attr_id}
        #                                   )
        # if IssueManage.checklist_id != "":
        #     DB.instance().clear_condition(section="project",
        #                                   table="issue_elissuechecklist",
        #                                   condition={"id": IssueManage.checklist_id}
        #                                   )
        # if __name__ == '__main__':
        #     print("delete sql")
        #     db.delete_sql()

        pass

    # def test_0100_search_business(self):
    #     """
    #     通用查询逻辑
    #     """
    #     # /issue/v1/api/list (erdcloud 1.2.0.ga 没有此接口)
    #     search_business_result = ApiIssueManage.search_business(self)
    #     print(search_business_result)

    def test_0200_select_business_export(self):
        """
        导出业务数据
        """
        # /issue/v1/export
        export_business_result = ApiIssueManage.select_business_export(self,
                                                                       businessType="erd.cloud.issue.dto.EtIssue",
                                                                       exprotList="code,name",
                                                                       viewid=IssueManage.view_id
                                                                       )
        print(export_business_result)

    def test_0300_select_avlb_fieldlist(self):
        """
        查询可用的扩展列名称
        """
        # /issue/v1/extfields
        search_avlb_fieldlist_result = ApiIssueManage.select_avlb_fieldlist(self)
        print(search_avlb_fieldlist_result)

    @unittest.skip('因为超出行的大小')
    def test_0400_add_extfields(self):
        """
        添加可扩展列
        """
        # /issue/v1/extfields
        attrKey = "ext_test_" + time.strftime('%H%M%S', time.localtime())
        attrName = "test_" + time.strftime('%H%M%S', time.localtime())
        attrType = "varchar"
        typeLength = "1"
        add_extfields_result = ApiIssueManage.add_extfields(self, attrKey, attrName, attrType, typeLength)
        print(add_extfields_result)
        # 强制删除数据
        result = ApiIssueManage.select_avlb_fieldlist(self)
        print(result)
        if result:
            for t in result:
                if t['displayName'] == attrName:
                    IssueManage.attr_id = t['id']

    # def test_0500_import_business(self):
    #     """
    #     导入业务数据(导入接口放到最后写
    #     """
    #     # /issue/v1/import
    #     import_business_result = ApiIssueManage.import_business(self)
    #     print(import_business_result)

    def test_0600_add_issue(self):
        """
        新增问题
        """
        # /issue/v1/issue
        # 新增项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        addProjectUsingPOST_1 = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        print(addProjectUsingPOST_1)
        IssueManage.project_id = addProjectUsingPOST_1.get("id")
        IssueManage.issue_name = "issue_" + time.strftime('%H%M%S', time.localtime())
        add_issue_result = ApiIssueManage.add_issue(self,
                                                    name=IssueManage.issue_name,
                                                    project_id=IssueManage.project_id,
                                                    submitid=IssueManage.user_id,
                                                    priority="1",
                                                    state="DRAFT",
                                                    type="1"
                                                    )
        print(add_issue_result)
        IssueManage.issue_id = add_issue_result.get("id")
        print("issue_id:", IssueManage.issue_id)

    def test_0700_insertbatch_issue(self):
        """
        批量添加问题
        """
        # /issue/v1/issue/insertbatch
        insertbatch_name = "insertbatch_issue_" + time.strftime('%H%M%S', time.localtime())
        insertbatch_issue_result = ApiIssueManage.insertbatch_issue(self,
                                                                    insertbatch_name,
                                                                    IssueManage.project_id,
                                                                    IssueManage.user_id,
                                                                    "PROCESSOR",
                                                                    "0", "DRAFT", "0"
                                                                    )
        print(insertbatch_issue_result)
        IssueManage.insertbatch_id = "".join(insertbatch_issue_result)
        print("insertbatch_issue_id:", IssueManage.insertbatch_id)

    def test_0800_editbatch_issue(self):
        """
        批量修改问题
        """
        # /issue/v1/issue/editBatch
        editbatch_issue_result = ApiIssueManage.editbatch_issue(self,
                                                                IssueManage.insertbatch_id,
                                                                IssueManage.project_id,
                                                                "1"
                                                                )
        print(editbatch_issue_result)

    def test_0900_update_issue(self):
        """
        修改问题信息
        """
        # /issue/v1/issue/{id}
        update_issue_name = "update_" + IssueManage.issue_name
        update_issue_result = ApiIssueManage.update_issue(self,
                                                          IssueManage.issue_id,
                                                          update_issue_name,
                                                          IssueManage.user_id,
                                                          IssueManage.project_id,
                                                          "0", "0", "DRAFT"
                                                          )
        print(update_issue_result)

    def test_0900_get_labels_list(self):
        """
        获取系统标签列表
        """
        # /issue/v1/issue/labels
        get_labels_list = ApiIssueManage.get_labels_list(self)
        print(get_labels_list)

    def test_1000_add_checklist(self):
        """
        添加检查项
        """
        # /issue/v1/issue/{id}/checklist
        checklist_name = "check_" + time.strftime('%H%M%S', time.localtime())
        add_checklist_result = ApiIssueManage.add_checklist(self, IssueManage.issue_id, checklist_name, "1")
        print(add_checklist_result)
        IssueManage.checklist_id = add_checklist_result.get("id")
        print("checklist_id:", IssueManage.checklist_id)

    def test_1100_update_checklist(self):
        """
        修改检查项
        """
        # /issue/v1/issue/{id}/checklist
        update_checklist_result = ApiIssueManage.update_checklist(self,
                                                                  IssueManage.issue_id,
                                                                  IssueManage.checklist_id,
                                                                  "1"
                                                                  )
        print(update_checklist_result)

    def test_1200_delete_checklist(self):
        """
        删除检查项
        """
        # /issue/v1/issue/{id}/checklist/{checkListIds}
        delete_checklist_result = ApiIssueManage.delete_checklist(self,
                                                                  IssueManage.issue_id,
                                                                  IssueManage.checklist_id
                                                                  )
        print(delete_checklist_result)

    @unittest.skip('测试project不能有平台的接口')
    def test_1300_add_labels(self):
        """
        添加标签，标签ID多个用逗号或分号分隔
        """
        # /issue/v1/issue/{id}/labels
        colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""
        for i in range(6):
            color += colorArr[random.randint(0, 14)]
        add_dict_result = ApiRiskManage.add_dict(self,
                                                 name="common_lable",
                                                 typename="common",
                                                 attribute="lable",
                                                 value="#" + color,
                                                 sort=random.randint(10, 99),
                                                 display_cn="标签",
                                                 display_en="labels"
                                                 )
        IssueManage.labels_id = add_dict_result.get("id")
        add_labels_result = ApiIssueManage.add_labels(self, IssueManage.issue_id, IssueManage.labels_id)
        print(add_labels_result)

    @unittest.skip('因为上面的那个接口')
    def test_1400_delete_labels(self):
        """
        删除标签，标签ID多个用逗号或分号分隔
        """
        # /issue/v1/issue/{id}/labels/{labelIds}
        delete_labels_result = ApiIssueManage.delete_labels(self, IssueManage.issue_id, IssueManage.labels_id)
        print(delete_labels_result)

    def test_1500_copy_issue(self):
        """
        复制|移动
        """
        # /req/v1/require/{project_id}/copy
        # type=1 复制 type=2 移动
        copy_type = "1"
        copy_issue_result = ApiIssueManage.copy_issue(self,
                                                      IssueManage.project_id,
                                                      IssueManage.issue_id,
                                                      IssueManage.project_id,
                                                      copy_type,
                                                      "original",
                                                      " "
                                                      )
        print(copy_issue_result)
        IssueManage.copy_issue_id = "".join(copy_issue_result)
        print("copy_issue_id:", IssueManage.copy_issue_id)

    # def test_1600_get_project_issues(self):
    #     """
    #     分页获取问题列表（项目下）
    #     """
    #     # /issue/v1/issues（erdcloud1.2.0.ga没有此接口）
    #     get_project_issues = ApiIssueManage.get_project_issues(self)
    #     print(get_project_issues)

    # def test_1610_add_members(self):
    #     """
    #     添加责任人，责任人ID多个用逗号或分号分隔
    #     """
    #     # /issue/v1/issue/{id}/members（erdcloud1.2.0.ga没有此接口）
    #     add_members_result = ApiIssueManage.add_members(self,

    # )

    # def test_1620_delete_members(self):
    #     """
    #     删除责任人，责任人ID多个用逗号或分号分隔
    #     """
    #     # /issue/v1/issue/{id}/members/{memberIds}（erdcloud1.2.0.ga没有此接口）
    #     delete_members_result = ApiIssueManage.delete_members(self)
    #     print(delete_members_result)

    # def test_1630_get_issues_me(self):
    #     """
    #     分页获取问题列表（个人工作台）
    #     """
    #     # /issue/v1/issues/me(该接口已被弃用）
    #     get_issues_me_result = ApiIssueManage.get_issues_me(self)
    #     print(get_issues_me_result)

    def test_1700_get_issue_by_id(self):
        """
        获取问题详细信息
        """
        # /issue/v1/issues/{id}
        get_issue_by_id = ApiIssueManage.get_issue_by_id(self, IssueManage.issue_id)
        print(get_issue_by_id)

    def test_1800_get_business_type_count(self):
        """
        获取问题的相关项的条目数
        """
        # /issue/v1/item/count/{id}
        get_business_type_count = ApiIssueManage.get_business_type_count(self,
                                                                         IssueManage.issue_id,
                                                                         "0",
                                                                         "discuss,relation,activity,check,attachment,"
                                                                         "elflow "
                                                                         )
        print(get_business_type_count)

    def test_1900_query_list_by_ids(self):
        """
        根据ID列表查询对象列表
        """
        # /issue/v1/list/{ids}
        query_list_by_ids = ApiIssueManage.query_list_by_ids(self, IssueManage.issue_id)
        print(query_list_by_ids)

    def test_2500_care_issue(self):
        """
        收藏/取消收藏
        """
        # /issue/v1/myCare
        care_issue_result = ApiIssueManage.care_issue(self,
                                                      IssueManage.issue_id,
                                                      IssueManage.issue_name
                                                      )
        print(care_issue_result)

    # todo 需要已经加入项目的成员id，要先将成员加入项目
    def test_2600_update_state_flow_members(self):
        """
        修改状态流程成员
        """
        ApiIssueManage.update_state_flow_members(self,issue_id=IssueManage.issue_id)

    def test_2700_export_business_template(self):
        """
        导出业务数据模板
        """
        # /issue/v1/template/export
        export_business_template = ApiIssueManage.export_business_template(self,
                                                                           "erd.cloud.issue.dto.EtIssue",
                                                                           "code,name,state,type,priority,finishDate,"
                                                                           "actualFinishDate,submitterId,member",
                                                                           IssueManage.view_id
                                                                           )
        print(export_business_template)

    # def test_2900_select_business_table(self):
    #     """
    #     查询业务表格列
    #     """
    #     # /issue/v1/{viewid}/businessTable(erdcloud1.2.0.ga没有此接口）
    #     select_business_table = ApiIssueManage.select_business_table(self, IssueManage.view_id)
    #     print(select_business_table)

    def test_3000_select_business_list(self):
        """
        查询业务数据
        """
        # /issue/v1/{viewid}/businesslist
        select_business_list = ApiIssueManage.select_business_list(self, IssueManage.view_id)
        print(select_business_list)

    def test_3100_select_filterlist(self):
        """
        过滤业务数据
        """
        # /issue/v1/{viewid}/filterlist
        select_filterlist_result = ApiIssueManage.select_filterlist(self, IssueManage.view_id)
        print(select_filterlist_result)

    # def test_3200_release_plan_comfirm(self):
    #     """
    #     发布计划前判断是否可以发布(erdcloud1.2.0.ga没有此接口）
    #     """
    #     # /issue/v1/{viewid}/releasePlanComfirm
    #     release_plan_comfirm_result = ApiIssueManage.release_plan_comfirm(self, IssueManage.view_id)
    #     print(release_plan_comfirm_result)

    def test_3500_delete_issue(self):
        """
        删除问题
        """
        # /issue/v1/issue
        delete_issue_result = ApiIssueManage.delete_issue(self, IssueManage.issue_id)
        print(delete_issue_result)

        # 删除项目
        deleteProjectUsingDELETE = ApiProject.deleteProjectUsingDELETE(self, project_id=IssueManage.project_id)
        print(deleteProjectUsingDELETE)

if __name__ == '__main__':
    unittest.main(verbosity=2)

# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 15:04
# @Author  : Liao
import random
import time
import unittest

from project.api import ApiRiskManage, ApiProject

from project.case.file.runSql import db

class RiskManage(unittest.TestCase):
    """风险基础信息操作"""

    user_id = db.user_id
    project_id = ''
    org_id = db.org_id
    # 风险视图-所有的
    view_id = db.risk_view_id

    static_date = time.strftime('%Y-%m', time.localtime())
    risk_id = ""
    copy_risk_id = ""
    risk_name = ""
    insert_batch_id = ""
    checklist_id = ""
    labels_id = ""
    attr_id = ""

    @classmethod
    def setUpClass(cls) -> None:
        pass

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     db.delete_sql()
    # if RiskManage.risk_id != "":
    #     DB.instance().clear_condition(section="project",
    #                                   table="risk_elrisk",
    #                                   condition={"id": RiskManage.risk_id}
    #                                   )
    # if RiskManage.copy_risk_id != "":
    #     DB.instance().clear_condition(section="project",
    #                                   table="risk_elrisk",
    #                                   condition={"id": RiskManage.copy_risk_id}
    #                                   )
    # if RiskManage.insertbatch_id != "":
    #     DB.instance().clear_condition(section="project",
    #                                   table="risk_elrisk",
    #                                   condition={"id": RiskManage.insertbatch_id}
    #                                   )
    # if RiskManage.labels_id != "":
    #     DB.instance().clear_condition(section="system",
    #                                   table="sys_eldictionary",
    #                                   condition={"id": RiskManage.labels_id}
    #                                   )
    # if RiskManage.attr_id != "":
    #     DB.instance().clear_condition(section="system",
    #                                   table="sys_elview_basefield",
    #                                   condition={"id": RiskManage.attr_id}
    #                                   )
    # if RiskManage.checklist_id != "":
    #     DB.instance().clear_condition(section="project",
    #                                   table="risk_elriskchecklist",
    #                                   condition={"id": RiskManage.checklist_id}
    #                                   )
    # if __name__ == '__main__':
    #     print("delete sql")
    #     db.delete_sql()

    def test_0100_add_risk(self):
        """
        新增风险
        """
        # 新增项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        addProjectUsingPOST_1 = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        print(addProjectUsingPOST_1)
        RiskManage.project_id = addProjectUsingPOST_1.get("id")

        # /risk/v1/risk
        RiskManage.risk_name = "risk_" + time.strftime('%H%M%S', time.localtime())
        add_risk_result = ApiRiskManage.add_risk(self,
                                                 name=RiskManage.risk_name,
                                                 project_id=RiskManage.project_id,
                                                 grade="3",
                                                 state="DRAFT",
                                                 type="1"
                                                 )
        print(add_risk_result)
        RiskManage.risk_id = add_risk_result.get("id")
        print("risk_id:", RiskManage.risk_id)

    def test_0200_update_risk(self):
        """
        修改风险
        """
        # /risk/v1
        update_risk_name = "update_" + RiskManage.risk_name
        update_risk_result = ApiRiskManage.update_risk(self,
                                                       RiskManage.risk_id,
                                                       update_risk_name,
                                                       RiskManage.user_id,
                                                       RiskManage.project_id,
                                                       "3", "1", "DRAFT"
                                                       )
        print(update_risk_result)

    # def test_0300_search_business(self):
    #     """
    #     通用查询逻辑
    #     """
    #     # /risk/v1/api/list (erdcloud 1.2.0.ga 没有此接口)
    #     search_business_result = ApiRiskManage.search_business(self)
    #     print(search_business_result)

    def test_0400_get_risk_chart(self):
        """
        风险报表
        """
        # /risk/v1/chart/{project_id}
        get_risk_chart_result = ApiRiskManage.get_risk_chart(self, RiskManage.project_id)
        print(get_risk_chart_result)

    def test_0500_export_risk_chart(self):
        """
        导出项目风险报表
        """
        # /risk/v1/chartexport/{project_id}
        export_risk_chart = ApiRiskManage.export_risk_chart(self, RiskManage.project_id)
        print(export_risk_chart)

    def test_0600_select_business_export(self):
        """
        导出业务数据
        """
        # /risk/v1/export
        export_business_result = ApiRiskManage.select_business_export(self,
                                                                      businessType="erd.cloud.risk.dto.EtRisk",
                                                                      exprotList="code,name",
                                                                      viewid=RiskManage.view_id,
                                                                      exportIdList=None
                                                                      )
        print(export_business_result)

    def test_0700_select_avlb_fieldlist(self):
        """
        查询可用的扩展列名称
        """
        # /risk/v1/extfields
        search_avlb_fieldlist_result = ApiRiskManage.select_avlb_fieldlist(self)
        print(search_avlb_fieldlist_result)

    @unittest.skip('因为超出行的大小')
    def test_0800_add_extfields(self):
        """
        添加可扩展列
        """
        # /risk/v1/extfields
        attrKey = "ext_test_" + time.strftime('%H%M%S', time.localtime())
        attrName = "test_" + time.strftime('%H%M%S', time.localtime())
        attrType = "varchar"
        typeLength = "255"
        add_extfields_result = ApiRiskManage.add_extfields(self, attrKey, attrName, attrType, typeLength)
        print("add_extfields_result:", add_extfields_result)
        # 查询添加的数据
        result = ApiRiskManage.select_avlb_fieldlist(self)
        print(result)
        if result:
            for t in result:
                if t['displayName'] == attrName:
                    RiskManage.attr_id = t.get("id")
        print("attr_id：", RiskManage.attr_id)

    # def test_0900_import_business(self):
    #     """
    #     导入业务数据(导入接口放到最后写
    #     """
    #     # /risk/v1/import
    #     import_business_result = ApiRiskManage.import_business(self)
    #     print(import_business_result)

    def test_1000_get_business_type_count(self):
        """
        获取风险的相关项的条目数
        """
        # /risk/v1/item/count/{id}
        get_business_type_count = ApiRiskManage.get_business_type_count(self,
                                                                        RiskManage.risk_id,
                                                                        "0",
                                                                        "discuss,relation,activity,check,attachment,"
                                                                        "elflow",
                                                                        "project"
                                                                        )
        print(get_business_type_count)

    def test_1100_query_list_by_ids(self):
        """
        根据ID列表查询对象列表
        """
        # /risk/v1/list/{ids}
        query_list_by_ids = ApiRiskManage.query_list_by_ids(self, RiskManage.risk_id)
        print(query_list_by_ids)

    def test_1200_insertbatch_risk(self):
        """
        批量添加风险
        """
        # /risk/v1/risk/insertbatch
        insertbatch_name = "insertbatch_risk_" + time.strftime('%H%M%S', time.localtime())
        insertbatch_risk_result = ApiRiskManage.insertbatch_risk(self,
                                                                 insertbatch_name,
                                                                 RiskManage.project_id,
                                                                 "3", "1", "DRAFT"
                                                                 )
        print(insertbatch_risk_result)
        RiskManage.insert_batch_id = "".join(insertbatch_risk_result)
        print("insertbatch_risk_id:", RiskManage.insert_batch_id)

    def test_1300_editbatch_risk(self):
        """
        批量修改风险
        """
        # /risk/v1/risk/editBatch
        editbatch_risk_result = ApiRiskManage.editbatch_risk(self,
                                                             RiskManage.insert_batch_id,
                                                             RiskManage.project_id,
                                                             "1"
                                                             )
        print(editbatch_risk_result)

    def test_1400_add_checklist(self):
        """
        添加规避措施
        """
        # /risk/v1/risk/{id}/checklist
        checklist_name = "check_" + time.strftime('%H%M%S', time.localtime())
        add_checklist_result = ApiRiskManage.add_checklist(self, RiskManage.risk_id, checklist_name, "1")
        print(add_checklist_result)
        RiskManage.checklist_id = add_checklist_result.get("id")
        print("checklist_id:", RiskManage.checklist_id)

    def test_1500_get_checklist_by_id(self):
        """
        根据风险id查询规避措施
        """
        # /risk/v1/risk/{id}/checklist
        get_checklist_by_id = ApiRiskManage.get_checklist_by_id(self, RiskManage.risk_id)
        print(get_checklist_by_id)

    def test_1600_update_checklist(self):
        """
        修改规避措施
        """
        # /risk/v1/risk/checklist
        update_checklist_result = ApiRiskManage.update_checklist(self,
                                                                 RiskManage.checklist_id,
                                                                 RiskManage.risk_id,
                                                                 "1"
                                                                 )
        print(update_checklist_result)

    def test_1700_delete_checklist(self):
        """
        删除规避措施
        """
        # /risk/v1/risk/{id}/checklist/{cid}
        delete_checklist_result = ApiRiskManage.delete_checklist(self,
                                                                 RiskManage.risk_id,
                                                                 RiskManage.checklist_id
                                                                 )
        print(delete_checklist_result)

    @unittest.skip('测试project不能有平台的接口')
    def test_1800_add_labels(self):
        """
        添加标签，标签ID多个用逗号或分号分隔
        """
        # /risk/v1/risk/{id}/labels
        colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""
        for _ in range(6):
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
        RiskManage.labels_id = add_dict_result.get("id")
        ApiRiskManage.add_labels(self, RiskManage.risk_id, RiskManage.labels_id)

    def test_1900_get_labels_list_by_id(self):
        """
        根据风险id查询标签
        """
        # /risk/v1/risk/{id}/labels
        ApiRiskManage.get_labels_list_by_id(self, RiskManage.risk_id)

    @unittest.skip('因为test_1800的原因')
    def test_2000_delete_labels(self):
        """
        删除标签，标签ID多个用逗号或分号分隔
        """
        # /risk/v1/risk/{id}/labels/{labelIds}
        ApiRiskManage.delete_labels(self, RiskManage.risk_id, RiskManage.labels_id)

    def test_2100_copy_risk(self):
        """
        复制|移动
        """
        # /risk/v1/risk/{project_id}/copy
        # type=1 复制 type=2 移动
        copy_type = "1"
        copy_risk_result = ApiRiskManage.copy_risk(self,
                                                   RiskManage.project_id,
                                                   RiskManage.risk_id,
                                                   RiskManage.project_id,
                                                   copy_type,
                                                   "original",
                                                   " "
                                                   )
        print(copy_risk_result)
        RiskManage.copy_risk_id = copy_risk_result
        print("copy_risk_id:", RiskManage.copy_risk_id)

    def test_2200_get_risk_by_id(self):
        """
        获取风险详细信息
        """
        # /risk/v1/{id}
        get_risk_by_id = ApiRiskManage.get_risk_by_id(self, RiskManage.risk_id)
        print(get_risk_by_id)

    # def test_2300_get_project_risks(self):
    #     """
    #     分页获取风险列表（项目下）
    #     """
    #     # /risk/v1/risks（erdcloud1.2.0.ga没有此接口）
    #     get_project_risks = ApiRiskManage.get_project_risks(self)
    #     print(get_project_risks)

    # def test_2400_get_risks_me(self):
    #     """
    #     分页获取风险列表（个人工作台）
    #     """
    #     # /risk/v1/risks/me(该接口已被弃用）
    #     get_risks_me_result = ApiRiskManage.get_risks_me(self)
    #     print(get_risks_me_result)

    def test_2500_get_risk_by_id(self):
        """
        获取风险详细信息
        """
        # /risk/v1/risks/{id}
        get_risk_by_id = ApiRiskManage.get_risk_by_id(self, RiskManage.risk_id)
        print(get_risk_by_id)

    def test_2600_care_risk(self):
        """
        收藏/取消收藏
        """
        # /risk/v1/myCare
        care_risk_result = ApiRiskManage.care_risk(self,
                                                   RiskManage.risk_id,
                                                   RiskManage.risk_name
                                                   )
        print(care_risk_result)

    # def test_2700_update_state_flow_members(self):
    #     """
    #     修改状态流程成员
    #     """
    #     # /risk/v1/stateflow/members （erdcloud1.2.0.ga没有此接口）
    #     update_state_flow_members = ApiRiskManage.update_state_flow_members(self)
    #     print(update_state_flow_members)

    def test_2800_export_business_template(self):
        """
        导出业务数据模板
        """
        # /risk/v1/template/export
        export_business_template = ApiRiskManage.export_business_template(self,
                                                                          "erd.cloud.risk.dto.Etrisk",
                                                                          "code,name,state,type,priority,finishDate,"
                                                                          "actualFinishDate,submitterId,member",
                                                                          RiskManage.view_id
                                                                          )
        print(export_business_template)

    # def test_2900_select_business_table(self):
    #     """
    #     查询业务表格列
    #     """
    #     # /risk/v1/{viewid}/businessTable(erdcloud1.2.0.ga没有此接口）
    #     select_business_table = ApiRiskManage.select_business_table(self, RiskManage.view_id)
    #     print(select_business_table)

    def test_3000_select_business_list(self):
        """
        查询业务数据
        """
        # /risk/v1/{viewid}/businesslist
        select_business_list = ApiRiskManage.select_business_list(self, RiskManage.view_id)
        print(select_business_list)

    def test_3100_select_filterlist(self):
        """
        过滤业务数据
        """
        # /risk/v1/{viewid}/filterlist
        select_filterlist_result = ApiRiskManage.select_filterlist(self, RiskManage.view_id)
        print(select_filterlist_result)

    # def test_3200_release_plan_comfirm(self):
    #     """
    #     发布计划前判断是否可以发布(erdcloud1.2.0.ga没有此接口）
    #     """
    #     # /risk/v1/{viewid}/releasePlanComfirm
    #     release_plan_comfirm_result = ApiRiskManage.release_plan_comfirm(self, RiskManage.view_id)
    #     print(release_plan_comfirm_result)

    def test_3300_delete_risk(self):
        """
        删除风险
        """
        # /risk/v1/risks
        delete_risk_result = ApiRiskManage.delete_risk(self, RiskManage.risk_id)
        print(delete_risk_result)

        # 删除项目
        deleteProjectUsingDELETE = ApiProject.deleteProjectUsingDELETE(self, project_id=RiskManage.project_id)
        print(deleteProjectUsingDELETE)

if __name__ == '__main__':
    unittest.main(verbosity=2)

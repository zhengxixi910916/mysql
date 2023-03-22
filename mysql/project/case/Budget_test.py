# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 15:04
# @Author  : Liao
import random
import time
import unittest

from erdcloud.mysql_db import DB
from project.api import ApiBudget, ApiProject
from project.case.file.runSql import db


class Budget(unittest.TestCase):
    """预算模板 API、预算科目 API、费用 API、预算API"""
    project_id = ""
    org_id = db.org_id

    budget_tem_name = ""
    budget_name = ""
    stage_name = ""
    cost_name = ""
    budget_code = ""
    budget_template_id = ""
    budget_category_id = ""
    parts_id = ""
    stage_id = ""
    cost_id = ""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        if Budget.budget_template_id != "":
            DB.instance().clear(section="project", table="budget_elbudget_template", eid=Budget.budget_template_id)
        if Budget.budget_category_id != "":
            DB.instance().clear(section="project", table="budget_elbudget_category", eid=Budget.budget_template_id)
        if Budget.parts_id != "":
            DB.instance().clear(section="project", table="budget_elbudget_category", eid=Budget.parts_id)
        if Budget.stage_id != "":
            DB.instance().clear(section="project", table="budget_elbudget_project_entry", eid=Budget.stage_id)
        if Budget.cost_id != "":
            DB.instance().clear(section="project", table="budget_elbudget_project_cost", eid=Budget.cost_id)


    def test_0100_create_budget_tem(self):
        """
        新增预算模板
        """
        # 新增项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        addProjectUsingPOST_1 = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        print(addProjectUsingPOST_1)
        Budget.project_id = addProjectUsingPOST_1.get("id")

        # /budget/$VERSION$/template/create
        Budget.budget_tem_name = "budget_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        create_budget_tem = ApiBudget.create_budget_tem(self,
                                                        name=Budget.budget_tem_name,
                                                        description=Budget.budget_tem_name,
                                                        state="0",
                                                        projectType="ITProject"
                                                        )

        Budget.budget_template_id = create_budget_tem.get("id")
        print(Budget.budget_template_id)
        print(create_budget_tem)

    def test_0200_page_budget_tem(self):
        """
        查询预算模板分页列表
        """
        # /budget/$VERSION$/template/search
        page_budget_tem = ApiBudget.page_budget_tem(self)
        print(page_budget_tem)

    def test_0300_get_budget_tem_by_id(self):
        """
        根据ID查询预算模板对象信息
        """
        # /budget/$VERSION$/template/{id}/get
        get_budget_tem_by_id = ApiBudget.get_budget_tem_by_id(self, temid=Budget.budget_template_id)
        print(get_budget_tem_by_id)

    def test_0400_create_budget_category(self):
        """
        新增预算科目或品名
        """
        # /budget/$VERSION$/category/create
        # 新增预算科目
        Budget.budget_name = "budget_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        create_budget_category = ApiBudget.create_budget_category(self,
                                                                  templateId=Budget.budget_template_id,
                                                                  name=Budget.budget_name,
                                                                  description=Budget.budget_name,
                                                                  type="0")
        Budget.budget_category_id = create_budget_category.get("id")
        Budget.budget_code = create_budget_category.get("code")
        print(Budget.budget_code)
        # 添加品名
        Budget.budget_parts_name = "budget_parts" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        add_budget_category_pars = ApiBudget.add_budget_category_parts(self,
                                                                       budget_category_id=Budget.budget_category_id,
                                                                       name=Budget.budget_parts_name,
                                                                       budget_template_id=Budget.budget_template_id)

        print(add_budget_category_pars)

    def test_0500_update_budget_tem(self):
        """
        修改单条预算模板
        """
        # /budget/$VERSION$/template/{id}/update
        update_budget_tem_name = "update_" + Budget.budget_tem_name
        update_budget_tem = ApiBudget.update_budget_tem(self,
                                                        temid=Budget.budget_template_id,
                                                        name=update_budget_tem_name,
                                                        description=update_budget_tem_name,
                                                        state="0",
                                                        projectType="ITProject"
                                                        )
        print(update_budget_tem)


    def test_0600_get_ERP_categorys(self):
        """
        查询ERP所有预算科目（树形平铺）
        """
        # /budget/$VERSION$/category/erp/query
        get_ERP_categorys = ApiBudget.get_ERP_categorys(self)
        print(get_ERP_categorys)

    def test_0700_get_budget_category(self):
        """
        查询预算科目或品名列表
        """
        # /budget/$VERSION$/category/search
        get_budget_category = ApiBudget.get_budget_category(self,
                                                            templateId=Budget.budget_template_id,
                                                            type="1"
                                                            )
        print(get_budget_category)

    def test_0800_get_budget_category_by_id(self):
        """
        根据ID查询预算科目或品名对象信息
        """
        # /budget/$VERSION$/category/{id}/get
        get_budget_category_by_id = ApiBudget.get_budget_category_by_id(self, budgetid=Budget.budget_category_id)
        print(get_budget_category_by_id)

    def test_0900_update_budget_category_by_id(self):
        """
        根据ID修改预算科目或品名
        """
        # /budget/$VERSION$/category/{id}/update
        update_budget_name = "update_" + Budget.budget_name
        update_budget_category_by_id = ApiBudget.update_budget_category_by_id(self,
                                                                              budgetid=Budget.budget_category_id,
                                                                              name=update_budget_name,
                                                                              parentId="-1",
                                                                              code=Budget.budget_code
                                                                              )
        print(update_budget_category_by_id)

    def test_1100_save_budget_parts(self):
        parts_name = "part_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        save_budget_parts = ApiBudget.save_budget_parts(self,
                                                        budgetid=Budget.budget_category_id,
                                                        templateId=Budget.budget_template_id,
                                                        name=parts_name,
                                                        unit="个",
                                                        unitPrice=str(random.randint(1000, 9999)),
                                                        application="用途",
                                                        procedure="1",
                                                        type="1"
                                                        )
        print(save_budget_parts)
        # 查询并返回品名id
        search_parts = ApiBudget.get_budget_category(self,
                                                     parentId=Budget.budget_category_id,
                                                     templateId=Budget.budget_template_id,
                                                     type="1"
                                                     )
        print(search_parts)
        if search_parts:
            for t in search_parts:
                if t['name'] == parts_name:
                    Budget.parts_id = t['id']
        print("parts_id:", Budget.parts_id)

    def test_1300_get_parts_for_tem(self):
        """
        查询项目对应预算模板中的品名列表
        """
        # /budget/$VERSION$/category/template/parts
        get_parts_for_tem = ApiBudget.get_parts_for_tem(self,
                                                        code=Budget.budget_code,
                                                        project_id=Budget.project_id
                                                        )
        print(get_parts_for_tem)

    def test_1400_create_budget_parts_by_tem(self):
        """
        根据模板品名ID集合，批量新增品名
        """
        # /budget/$VERSION$/category/parts/create
        create_bdget_parts_by_tem = ApiBudget.create_budget_parts_by_tem(self,
                                                                         categoryId=Budget.budget_category_id,
                                                                         partIds=Budget.parts_id,
                                                                         project_id=Budget.project_id
                                                                         )
        print(create_bdget_parts_by_tem)

    def test_1500_query_proj_budget(self):
        """
        查询项目预算
        """
        # /budget/$VERSION$/project/budget/query
        query_proj_budget = ApiBudget.query_proj_budget(self, categoryId=Budget.budget_category_id, project_id=Budget.project_id)
        print(query_proj_budget)

    def test_1600_get_proj_budget_config(self):
        """
        查询项目预算设置接口
        """
        # /budget/$VERSION$/project/{id}/budget/config
        get_proj_budget_config = ApiBudget.get_proj_budget_config(self, project_id=Budget.project_id)
        print(get_proj_budget_config)

    def test_1700_search_proj_budget(self):
        """
        查询项目预算列表/查询项目预算费用概况
        """
        # /budget/$VERSION$/project/{id}/budget/list
        search_proj_budget = ApiBudget.search_proj_budget(self, project_id=Budget.project_id)
        print(search_proj_budget)

    def test_1800_get_budget_process_info(self):
        """
        查询项目预算流程信息
        """
        # /budget/$VERSION$/project/{id}/process
        get_budget_process_info = ApiBudget.get_budget_process_info(self, project_id=Budget.project_id)
        print(get_budget_process_info)

    def test_1900_get_stages_by_proj_id(self):
        """
        查询项目已使用的阶段
        """
        # /budget/$VERSION$/project/{id}/stage/list
        get_stages_by_proj_id = ApiBudget.get_stages_by_proj_id(self, project_id=Budget.project_id)
        print(get_stages_by_proj_id)

    def test_2000_query_budget_state(self):
        """
        查询预算审批状态(MAKING:编制 APPROVING：审批中RELEASED：已发布)
        """
        # /budget/$VERSION$/project/{project_id}/state/query
        query_budget_state = ApiBudget.query_budget_state(self, project_id=Budget.project_id)
        print(query_budget_state)

    def test_2100_set_proj_budget(self):
        """
        设置项目预算
        """
        # /budget/$VERSION$/project/{id}/config
        Budget.stage_name = "stage_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        set_proj_budget = ApiBudget.set_proj_budget(self,
                                                    project_id=Budget.project_id,
                                                    stagename=Budget.stage_name,
                                                    startTime=time.strftime('%Y-%m-%d', time.localtime()),
                                                    endTime=time.strftime('%Y-%m-%d', time.localtime()),
                                                    yieldRate="100",
                                                    estimateNum="1",
                                                    procedure="1"
                                                    )
        print(set_proj_budget)
        # 查询添加的数据
        search_stage = ApiBudget.get_proj_budget_config(self, project_id=Budget.project_id)
        if search_stage:
            for t in search_stage:
                if t['stage'] == Budget.stage_name:
                    Budget.stage_id = t['id']
        print("stage_id:", Budget.stage_id)

    @unittest.skip('接口未使用')
    def test_2200_save_proj_budget(self):
        """
        批量保存项目预算
        """
        # /budget/$VERSION$/project/category/budget/save
        save_proj_budget = ApiBudget.save_proj_budget(self,
                                                      stagename=Budget.stage_name,
                                                      categoryId=Budget.budget_category_id,
                                                      partId=Budget.parts_id,
                                                      project_id=Budget.project_id,
                                                      num=random.randint(100, 999)
                                                      )
        print(save_proj_budget)

    def test_2400_search_proj_cost(self):
        """
        查询项目费用
        """
        # /budget/$VERSION$/cost/list
        search_proj_cost = ApiBudget.search_proj_cost(self, project_id=Budget.project_id)
        print(search_proj_cost)

    def test_2500_search_proj_cost_budget(self):
        """
        查询项目费用/预算
        """
        # /budget/$VERSION$/cost/project/list
        search_proj_cost_budget = ApiBudget.search_proj_cost_budget(self)
        print(search_proj_cost_budget)

    def test_2600_insert_project_cost(self):
        """
        新增单条项目费用数据
        """
        # /budget/$VERSION$/cost/insert
        Budget.cost_name = "cost_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime())
        insert_project_cost = ApiBudget.insert_project_cost(self,
                                                            name=Budget.cost_name,
                                                            project_id=Budget.project_id,
                                                            categoryId=Budget.budget_category_id,
                                                            stage=Budget.stage_name,
                                                            costAmount=random.randint(1000, 9999),
                                                            occurrenceTime=time.strftime('%Y-%m-%d', time.localtime())
                                                            )
        print(insert_project_cost)
        # 查询添加的数据
        search_cost = ApiBudget.search_proj_cost(self, project_id=Budget.project_id)
        print(search_cost)
        if search_cost:
            for t in search_cost['records']:
                if t['name'] == Budget.cost_name:
                    Budget.cost_id = t['id']
        print("cost_id:", Budget.cost_id)

    def test_2700_get_proj_cost_by_id(self):
        """
        查询单条项目费用数据
        """
        # /budget/$VERSION$/cost/{id}/get
        get_proj_cost_by_id = ApiBudget.get_proj_cost_by_id(self, costid=Budget.cost_id)
        print(get_proj_cost_by_id)

    def test_2800_update_project_cost_by_id(self):
        """
        修改单条项目费用数据
        """
        # /budget/$VERSION$/cost/{id}/update
        update_cost_name = "update_" + Budget.cost_name
        update_project_cost_by_id = ApiBudget.update_project_cost_by_id(self,
                                                                        costid=Budget.cost_id,
                                                                        costname=update_cost_name,
                                                                        categoryId=Budget.budget_category_id,
                                                                        stage=Budget.stage_name
                                                                        )
        print(update_project_cost_by_id)

    # def test_2900_updatebatch_proj_cost(self):
    #     """
    #     批量修改项目费用
    #     """
    #     # /budget/$VERSION$/cost/update/batch(找不到此接口)
    #     updatebatch_proj_cost = ApiBudget.updatebatch_proj_cost(self)
    #     print(updatebatch_proj_cost)

    def test_3000_export_cost(self):
        """
        导出项目费用
        """
        # /budget/$VERSION$/cost/export
        export_cost = ApiBudget.export_cost(self, project_id=Budget.project_id)
        print(export_cost)

    def test_3100_export_proj_budget(self):
        """
        项目费用/预算导出
        """
        # /budget/$VERSION$/cost/project/export
        export_proj_budget = ApiBudget.export_proj_budget(self, department=Budget.org_id)
        print(export_proj_budget)

    def test_3200_sync_category(self):
        """
        接口名称：同步历史项目预算科目数据
        接口地址：/budget/$VERSION$/scheduler/category/sync
        """
        sync_category = ApiBudget.sync_category(self)
        print(sync_category)

    def test_3300_sync_ERP_cost(self):
        """
        费用从ERP系统同步
        """
        # /budget/$VERSION$/scheduler/cost/sync
        sync_ERP_cost = ApiBudget.sync_ERP_cost(self)
        print(sync_ERP_cost)

    def test_3400_get_budget_cost(self):
        """
        预算费用报表--按部门统计预算费用
        """
        # /budget/$VERSION$/stastic/project/budget/compare
        get_budget_cost = ApiBudget.get_budget_cost(self, department_id=Budget.org_id)
        print(get_budget_cost)

    def test_3500_get_proj_budget_cost(self):
        """
        单项目统计--统计各阶段预算和费用对比
        """
        # /budget/$VERSION$/stastic/project/{id}/budget/compare
        get_proj_budget_cost = ApiBudget.get_proj_budget_cost(self, project_id=Budget.project_id)
        print(get_proj_budget_cost)

    def test_3600_get_proj_budget_by_category(self):
        """
        单项目统计--以最后一级子预算科目为统计维度
        """
        # /budget/$VERSION$/stastic/project/{id}/budget/show
        get_proj_budget_by_category = ApiBudget.get_proj_budget_by_category(self, project_id=Budget.project_id)
        print(get_proj_budget_by_category)
    def test_3800_refreshTemplateUsingGET(self):
        """
        接口名称：刷新项目费用科目
        接口地址：/budget/$VERSION$/category/{project_id}/refreshTemplate
        """
        ApiBudget.refreshTemplateUsingGET(self,
                                          Budget.project_id
                                          )
    def test_3900_del_proj_cost_by_cids(self):
        """
        根据费用ID批量删除项目费用数据
        """
        # /budget/$VERSION$/cost/delete
        del_proj_cost_by_cids = ApiBudget.del_proj_cost_by_cids(self, costid=Budget.cost_id)
        print(del_proj_cost_by_cids)

    def test_4100_del_budget_category(self):
        """
        批量删除预算科目或品名
        """
        # /budget/$VERSION$/category/delete
        del_budget_category = ApiBudget.del_budget_category(self, budgetid=Budget.budget_category_id)
        print(del_budget_category)

    def test_4200_del_budget_tem(self):
        """
        批量删除预算模板
        """
        # /budget/$VERSION$/template/delete
        del_budget_tem = ApiBudget.del_budget_tem(self, temid=Budget.budget_template_id)
        print(del_budget_tem)




if __name__ == '__main__':
    unittest.main(verbosity=2)

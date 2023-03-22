# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 15:04
# @Author  : Liao
import random
import time
import unittest

from project.api import ApiRequireManage, ApiRiskManage, ApiProject

from project.case.file.runSql import db


class RequireManage(unittest.TestCase):
    """需求管理、需求管理-检查项|标签|成员"""

    user_id = db.user_id
    project_id = ""
    project_name = db.project_name
    org_id = db.org_id
    # 需求视图-所有的
    view_id = db.require_view_id

    static_date = time.strftime('%Y-%m', time.localtime())
    require_id = ""
    copy_require_id = ""
    require_name = ""
    insertbatch_id = ""
    checklist_id = ""
    labels_id = ""
    attr_id = ""
    import_name_id_list = ''

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass

    def test_0100_add_require(self):
        """
        新增需求接口
        """
        # 新增项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        r = ApiProject.addProjectUsingPOST_1(self,name=project_name,)
        print(r)
        RequireManage.project_id = r["id"]
        # /req/v1/require
        RequireManage.require_name = "require_" + time.strftime('%H%M%S', time.localtime())
        # require_description = RequireManage.require_name
        # submit_time = time.strftime('%Y-%m-%d', time.localtime())
        add_require_result = ApiRequireManage.add_require(self,
                                                          name=RequireManage.require_name,
                                                          project_id=RequireManage.project_id
                                                          )
        print(add_require_result)
        RequireManage.require_id = add_require_result.get("id")
        print("requirement_id:", RequireManage.require_id)

    def test_0200_select_business_export(self):
        """
        接口名称：导出业务数据
        接口地址：/req/$VERSION$/export
        """
        # /req/v1/export
        # 导出
        ApiRequireManage.select_business_export(self,
                                                businessType="erd.cloud.require.dto.EtRequirement",
                                                exprotList="code,name",
                                                exportIdList=RequireManage.require_id,
                                                viewid=RequireManage.view_id
                                                )

    def test_0210_import_business(self):
        """
        接口名称：导入业务数据
        接口地址：/req/$VERSION$/import
        """
        ApiRequireManage.import_business(self, project_id=RequireManage.project_id
                                         )

    def test_0300_select_avlb_fieldlist(self):
        """
        查询可用的扩展列名称
        """
        # /req/v1/extfields
        search_avlb_fieldlist_result = ApiRequireManage.select_avlb_fieldlist(self)
        print(search_avlb_fieldlist_result)

    @unittest.skip('因为超出行的大小')
    def test_0400_add_extfields(self):
        """
        添加可扩展列
        """
        # /req/v1/extfields
        attrKey = "ext_test_" + time.strftime('%H%M%S', time.localtime())
        attrName = "test_" + time.strftime('%H%M%S', time.localtime())
        attrType = "varchar"
        typeLength = "255"
        add_extfields_result = ApiRequireManage.add_extfields(self, attrKey, attrName, attrType, typeLength)
        print(add_extfields_result)
        # 查询添加的数据
        result = ApiRequireManage.select_avlb_fieldlist(self)
        print(result)
        if result:
            for t in result:
                if t['displayName'] == attrName:
                    RequireManage.attr_id = t['id']

    # def test_0500_import_business(self):
    #     """
    #     导入业务数据(导入接口放到最后写
    #     """
    #     # /req/v1/import
    #     import_business_result = ApiRequireManage.import_business(self)
    #     print(import_business_result)

    def test_0700_get_business_type_count(self):
        """
        获取需求的相关项的条目数
        """
        # /req/v1/item/count/{id}
        get_business_type_count = ApiRequireManage.get_business_type_count(self,
                                                                           RequireManage.require_id,
                                                                           "0",
                                                                           "discuss,child,relation,activity,check,"
                                                                           "attachment,elflow")
        print(get_business_type_count)

    def test_0800_query_list_by_ids(self):
        """
        根据ID列表查询对象列表
        """
        # /req/v1/list/{ids}
        query_list_by_ids_result = ApiRequireManage.query_list_by_ids(self, RequireManage.require_id)
        print(query_list_by_ids_result)

    def test_0900_care_require(self):
        """
        收藏/取消收藏
        """
        # /req/v1/myCare
        care_my_project_result = ApiRequireManage.care_require(self,
                                                               RequireManage.require_id,
                                                               RequireManage.require_name
                                                               )
        print(care_my_project_result)

    def test_1000_get_baseline_reqchild_by_id(self):
        """
        基线获取子需求
        """
        # /req/v1/require/baseline/{id}/children
        get_baseline_reqchild_by_id = ApiRequireManage.get_baseline_req_child_by_id(self, RequireManage.require_id)
        print(get_baseline_reqchild_by_id)

    @unittest.skip('此接口未调用')
    def test_1100_get_require_me(self):
        """
        获取需求列表数据-个人工作台
        """
        # /req/v1/require/me
        get_require_me_result = ApiRequireManage.get_require_me(self)
        print(get_require_me_result)

    def test_1200_get_reqchild_by_id(self):
        """
        获取子需求
        """
        # /req/v1/require/{id}/children
        get_reqchild_by_id = ApiRequireManage.get_reqchild_by_id(self, RequireManage.require_id)
        print(get_reqchild_by_id)

    def test_1300_copy_requirements(self):
        """
        复制|移动
        """
        # /req/v1/require/{project_id}/copy
        # type=1 复制 type=2 移动
        copy_type = '1'

        copy_requirements_result = ApiRequireManage.copy_requirements(self,
                                                                      eid=RequireManage.project_id,
                                                                      requireIds=RequireManage.require_id,
                                                                      project_id=RequireManage.project_id,
                                                                      type=copy_type,
                                                                      state="original",
                                                                      createBy=""
                                                                      )
        RequireManage.copy_require_id = copy_requirements_result

    def test_1400_get_require_by_id(self):
        """
        根据需求id获取需求详情
        """
        # /req/v1/require/{require_id}
        get_require_by_id_result = ApiRequireManage.get_require_by_id(self, RequireManage.require_id)
        print(get_require_by_id_result)

    def test_1500_update_require(self):
        """
        更新需求详细信息
        """
        # /req/v1/require/{require_id}
        update_require_name = "update_" + RequireManage.require_name
        update_require_result = ApiRequireManage.update_require(self,
                                                                RequireManage.require_id,
                                                                update_require_name,
                                                                RequireManage.project_id
                                                                )
        print(update_require_result)

    def test_1600_get_requires(self):
        """
        获取需求列表数据-需求管理列表
        """
        # /req/v1/requires
        get_requires_result = ApiRequireManage.get_requires(self)
        print(get_requires_result)

    def test_1700_get_editbatch_req_selectlist(self):
        """
        需求批量编辑树-selectlist
        """
        # /req/v1/requires/editBatch/selectlist
        get_editbatch_req_selectlist = ApiRequireManage.get_editbatch_req_selectlist(self)
        print(get_editbatch_req_selectlist)

    def test_1800_insertbatch_requires(self):
        """
        批量添加需求
        """
        # /req/v1/requires/insertbatch
        insertbatch_name = "insertbatch_require_" + time.strftime('%H%M%S', time.localtime())
        insertbatch_requires_result = ApiRequireManage.insertbatch_requires(self,
                                                                            insertbatch_name,
                                                                            RequireManage.project_id,
                                                                            RequireManage.org_id,
                                                                            RequireManage.project_id,
                                                                            "DRAFT", "0", "0", "PLANNING"
                                                                            )
        print(insertbatch_requires_result)
        RequireManage.insertbatch_id = "".join(insertbatch_requires_result)
        print("insertbatch_requires_id:", RequireManage.insertbatch_id)

    def test_1900_get_reqs_by_projct_link(self):
        """
        根据组合项目ID，获取需求列表数据
        """
        # /req/v1/requires/project/{project_id}
        get_reqs_by_projct_link = ApiRequireManage.get_reqs_by_projct_link(self, RequireManage.project_id)
        print(get_reqs_by_projct_link)

    def test_2000_get_require_selectlist(self):
        """
        需求树-selectlist
        """
        # /req/v1/requires/selectlist
        get_require_selectlist = ApiRequireManage.get_require_selectlist(self)
        print(get_require_selectlist)

    def test_2100_get_require_tree(self):
        """
        需求树
        """
        # /req/v1/requires/tree
        get_require_tree_result = ApiRequireManage.get_require_tree(self, RequireManage.project_id)
        print(get_require_tree_result)

    def test_2200_get_require_tree_list(self):
        """
        需求树-list
        """
        # /req/v1/requires/treelist
        get_require_tree_list_result = ApiRequireManage.get_require_tree_list(self, RequireManage.project_id)
        print(get_require_tree_list_result)

    def test_2300_updatebatch_requires(self):
        """
        需求批量编辑属性接口
        """
        # /req/v1/requires/updatebatch
        updatebatch_requires_result = ApiRequireManage.updatebatch_requires(self,
                                                                            RequireManage.insertbatch_id,
                                                                            RequireManage.project_id,
                                                                            "0"
                                                                            )
        print(updatebatch_requires_result)

    def test_2400_get_require_type_list(self):
        """
        需求类型列表
        """
        # /req/v1/requiretypes
        get_require_type_list_result = ApiRequireManage.get_require_type_list(self)
        print(get_require_type_list_result)

    def test_2500_add_req_proj_link(self):
        """
        创建需求和项目关联关系
        """
        # /req/v1/require/project/{project_id}
        add_req_proj_link = ApiRequireManage.add_req_proj_link(self, RequireManage.project_id, RequireManage.require_id)
        print(add_req_proj_link)

    def test_2600_del_req_proj_link(self):
        """
        删除需求和项目关联关系
        """
        # /req/v1/require/project/{project_id}
        del_req_proj_link = ApiRequireManage.del_req_proj_link(self, RequireManage.project_id, RequireManage.require_id)
        print(del_req_proj_link)

    def test_2700_add_checklist(self):
        """
        添加检查项
        """
        # /req/v1/require/{id}/checklist
        checklist_name = "check_" + time.strftime('%H%M%S', time.localtime())
        add_checklist_result = ApiRequireManage.add_checklist(self, RequireManage.require_id, checklist_name, "4", "1")
        print(add_checklist_result)
        RequireManage.checklist_id = add_checklist_result.get("id")
        print("checklist_id:", RequireManage.checklist_id)

    def test_2800_update_checklist(self):
        """
        修改检查项
        """
        # /req/v1/require/{id}/checklist/{cid}
        update_checklist_result = ApiRequireManage.update_checklist(self,
                                                                    RequireManage.require_id,
                                                                    RequireManage.checklist_id,
                                                                    "1"
                                                                    )
        print(update_checklist_result)

    def test_2900_delete_checklist(self):
        """
        软删除检查项
        """
        # /req/v1/require/{id}/checklist/{cid}
        delete_checklist_result = ApiRequireManage.delete_checklist(self,
                                                                    RequireManage.require_id,
                                                                    RequireManage.checklist_id
                                                                    )
        print(delete_checklist_result)

    @unittest.skip('测试project不能有平台的接口')
    def test_3000_add_labels(self):
        """
        需求-添加标签
        """
        # /req/v1/require/{id}/label
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
        RequireManage.labels_id = add_dict_result.get("id")
        add_labels_result = ApiRequireManage.add_labels(self, RequireManage.require_id, RequireManage.labels_id)
        print(add_labels_result)

    @unittest.skip('因为上面一个接口的原因')
    def test_3100_delete_labels(self):
        """
        需求删除标签
        """
        # /req/v1/require/{id}/label/{label_id}
        delete_labels_result = ApiRequireManage.delete_labels(self, RequireManage.require_id, RequireManage.labels_id)
        print(delete_labels_result)

    def test_3200_add_members(self):
        """
        添加需求成员
        """
        # /req/v1/require/{id}/member
        add_members_result = ApiRequireManage.add_members(self,
                                                          RequireManage.require_id,
                                                          RequireManage.require_id,
                                                          "DEVELOP",
                                                          RequireManage.user_id
                                                          )
        print(add_members_result)

    def test_3300_delete_members(self):
        """
        需求-删除成员
        """
        # /req/v1/require/{id}/member/{member_id}
        delete_members_result = ApiRequireManage.delete_members(self, RequireManage.require_id, RequireManage.user_id)
        print(delete_members_result)

    # def test_3400_update_state_flow_members(self):
    #     """
    #     修改状态流程成员
    #     """
    #     # /req/v1/stateflow/members （erdcloud1.2.0.ga没有此接口）
    #     update_state_flow_members = ApiRequireManage.update_state_flow_members(self)
    #     print(update_state_flow_members)

    def test_3500_get_states_by_type(self):
        """
        项目需求统计
        """
        # /req/v1/states/{project_id}/{state_type}
        get_states_by_type_result = ApiRequireManage.get_states_by_type(self, RequireManage.project_id)
        print(get_states_by_type_result)

    def test_3600_export_business_template(self):
        """
        接口名称：导出业务数据模板
        接口地址：/req/$VERSION$/template/export
        """
        export_business_template = ApiRequireManage.export_business_template(self,
                                                                             "erd.cloud.require.dto.EtRequirement",
                                                                             "code,name,type,state,submitterId,"
                                                                             "department,submitTime,member,reqSource,"
                                                                             "priority",
                                                                             RequireManage.project_id,
                                                                             RequireManage.view_id
                                                                             )
        print(export_business_template)

    def test_3700_update_req_state_by_id(self):
        """
        修改需求状态为已分配
        """
        # /req/v1/updateReqStateById/{require_ids}
        update_req_state_by_id = ApiRequireManage.update_req_state_by_id(self, RequireManage.require_id)
        print(update_req_state_by_id)

    # def test_3800_select_business_table(self):
    #     """
    #     查询业务表格列
    #     """
    #     # /req/v1/{viewid}/businessTable(erdcloud1.2.0.ga没有此接口）
    #     select_business_table = ApiRequireManage.select_business_table(self, RequireManage.view_id)
    #     print(select_business_table)

    def test_3900_select_business_list(self):
        """
        查询业务数据
        """
        # /req/v1/{viewid}/businesslist
        import_name_id_list = []
        select_business_list = ApiRequireManage.select_business_list(self, RequireManage.view_id)
        records = select_business_list['res']['data']['records']
        try:
            for i in range(len(records)):
                if 'require' in records[i]['name']:
                    import_name_id_list.append(records[i]['id'])
        except Exception as e:
            print(e)
            pass
        RequireManage.import_name_id_list = import_name_id_list
        print(RequireManage.import_name_id_list)

    def test_4000_select_filterlist(self):
        """
        过滤业务数据
        """
        # /req/v1/{viewid}/filterlist
        select_filterlist_result = ApiRequireManage.select_filterlist(self, RequireManage.view_id)
        print(select_filterlist_result)

    def test_4300_requirementChangeTaskUsingPOST(self):
        """
        接口名称：需求转任务
        接口地址：/req/$VERSION$/require/{project_id}/changeTask
        """
        ApiRequireManage.requirementChangeTaskUsingPOST(self,
                                                        project_id=RequireManage.project_id,
                                                        parenttask_id="",
                                                        requireIds=RequireManage.require_id,
                                                        type="2"
                                                        )

    def test_4400_compare_chart(self):
        """
        接口名称：计划进展对比报表API
        接口地址：/plan/$VERSION$/task/compare
        """
        ApiRequireManage.compare_chart(self,
                                       project_id=RequireManage.project_id)

    def test_4500_delete_require(self):
        """
        删除需求
        """
        # # /req/v1/requires
        # for require_id in RequireManage.import_name_id_list:
        #     ApiRequireManage.delete_require(self,
        #                                     # checker={
        #                                     #     "code": "10000",
        #                                     #     "success": False
        #                                     # }
        #                                     )
        print(RequireManage.require_id)
        ApiRequireManage.delete_require(self, reqIdList=RequireManage.require_id)

        # 删除项目
        ApiProject.deleteProjectUsingDELETE(self, project_id=RequireManage.project_id)


if __name__ == '__main__':
    unittest.main(verbosity=2)

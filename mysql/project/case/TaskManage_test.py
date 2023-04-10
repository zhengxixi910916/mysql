# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 15:04
# @Author  : Liao
import random
import time
import unittest

from project.api import ApiProject, ApiRiskManage, ApiTaskManage,ApiProjectTemplate,ApiProjectTasks

from project.case.file.runSql import db


class TaskManage(unittest.TestCase):
    """项目计划"""

    user_id = db.user_id
    project_id = ''
    org_id = db.org_id
    # 计划视图-所有的
    view_id = db.task_view_id
    plan_id_list = ''
    task_id = ""
    child_task_id1 = ""
    child_task_id2 = ""
    copy_task_id = ""
    task_name = ""
    checklist_id = ""
    labels_id = ""
    attr_id = ""
    sum_id = ""
    working_hour_id = ""
    project_template_id = ""
    plan_data = ''
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass

    def test_0100_add_task(self):
        """
        接口名称：创建任务
        接口地址：/plan/$VERSION$/task
        """

        # 新增项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        r = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        print(r)
        TaskManage.project_id = r["id"]


        TaskManage.plan_data = {
            "name": "AutoPlan",
            "startDate": "",
            "finishDate": "",
            "milestoneFlag": "0",
            "state": "",
            "criticalFlag": "0",
            "canBeCutted": "1",
            "stageFlag": "0",
            "description": "",
            "percentComplete": "",
            "projectId": TaskManage.project_id,
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
            "taskMemberList[0].roleKey": "HANDLEPERSON",
            "taskMemberList[0].userId": "SYS_E39B20EA11E7A81AC85B767C89C1",
            "taskMemberList[1].roleKey": "IDENTIFY",
            "taskMemberList[1].userId":"",
            "labelLinkIds": ""
        }

        TaskManage.plan_data['projectId'] = TaskManage.project_id
        add_task_result = ApiProjectTasks.add_task_using_post_1(self, data=TaskManage.plan_data)
        print(add_task_result)
        TaskManage.task_id = add_task_result.get("id")
        print("task_id:", TaskManage.task_id)

    def test_0150_copy_task(self):
        """
        复制|移动
        """
        # /task/v1/task/{project_id}/copy
        # type=1 复制 type=2 移动
        copy_type = "1"
        copy_task_result = ApiTaskManage.copy_task(self,
                                                   TaskManage.project_id,
                                                   TaskManage.task_id,
                                                   TaskManage.project_id,
                                                   copy_type,
                                                   "original",
                                                   " "
                                                   )
        print(copy_task_result)
        TaskManage.copy_task_id = "".join(copy_task_result['res']['taskIdList'])

    def test_0200_update_task(self):
        """
        修改计划
        """
        # /task/v1
        update_task_name = "update_" + TaskManage.task_name
        ApiTaskManage.update_task(self,name=update_task_name,task_id=TaskManage.task_id, project_id=TaskManage.project_id)


    def test_0300_select_business_export(self):
        """
        接口名称：导出业务数据
        接口地址：/plan/$VERSION$/export
        """
        ApiTaskManage.select_business_export(self,
                                             businessType="erd.cloud.plan.dto.EtTask",
                                             exprotList="code,name,resAssignments",
                                             project_id=TaskManage.project_id,
                                             viewid=TaskManage.view_id,
                                             exportIdList=TaskManage.task_id
                                             )

    def test_1000_get_business_type_count(self):
        """
        获取计划的相关项的条目数
        """
        # /task/v1/item/count/{id}
        get_business_type_count = ApiTaskManage.get_business_type_count(self,
                                                                        task_id=TaskManage.task_id,
                                                                        cttType="0",
                                                                        itemList="",
                                                                        scence=""
                                                                        )
        print(get_business_type_count)

    def test_1100_query_list_by_ids(self):
        """
        根据ID列表查询对象列表
        """
        # /task/v1/list/{ids}
        query_list_by_ids = ApiTaskManage.query_list_by_ids(self, TaskManage.task_id)
        print(query_list_by_ids)

    def test_1200_insertbatch_task(self):
        """
        批量添加计划
        """
        # /task/v1/task/insertbatch
        insertbatch_name = "insertbatch_task_" + time.strftime('%H%M%S', time.localtime())
        add_child_task_result = ApiTaskManage.insertbatch_task(self,
                                                               [{
                                                                   "description": "",
                                                                   "finishDate": "",
                                                                   "name": insertbatch_name + "1",
                                                                   "parentId": "",
                                                                   "projectId": TaskManage.project_id,
                                                                   "resAssignments": "PM",
                                                                   "startDate": "",
                                                                   "state": "DRAFT",
                                                                   "taskMemberList": [{
                                                                       "roleKey": "HANDLEPERSON",
                                                                       "userId": TaskManage.user_id
                                                                   }]
                                                               }, {
                                                                   "description": "",
                                                                   "finishDate": "",
                                                                   "name": insertbatch_name + "2",
                                                                   "parentId": TaskManage.task_id,
                                                                   "projectId": TaskManage.project_id,
                                                                   "resAssignments": "PM",
                                                                   "startDate": "",
                                                                   "state": "DRAFT",
                                                                   "taskMemberList": [{
                                                                       "roleKey": "HANDLEPERSON",
                                                                       "userId": TaskManage.user_id
                                                                   }]
                                                               }]
                                                               )
        print(add_child_task_result)
        TaskManage.child_task_id1 = add_child_task_result[0]
        TaskManage.child_task_id2 = add_child_task_result[1]

        print("child_task_id1:", TaskManage.child_task_id1)
        print("child_task_id2:", TaskManage.child_task_id2)

    def test_1300_editbatch_task(self):
        """
        批量修改计划
        """
        # /task/v1/task/editBatch
        editbatch_task_result = ApiTaskManage.editbatch_task(self,
                                                             TaskManage.child_task_id1,
                                                             TaskManage.project_id,
                                                             "PENDING"
                                                             )
        print(editbatch_task_result)


    def test_1500_add_checklist(self):
        """
        添加规避措施
        """
        # /task/v1/task/{id}/checklist
        checklist_name = "check_" + time.strftime('%H%M%S', time.localtime())
        add_checklist_result = ApiTaskManage.add_checklist(self,
                                                           TaskManage.task_id,
                                                           checklist_name,
                                                           "RDP", "0", "1", "0")
        print(add_checklist_result)
        TaskManage.checklist_id = add_checklist_result.get("id")
        print("checklist_id:", TaskManage.checklist_id)

    def test_1600_update_checklist(self):
        """
        修改规避措施
        """
        # /task/v1/task/checklist
        update_checklist_result = ApiTaskManage.update_checklist(self,
                                                                 TaskManage.checklist_id,
                                                                 TaskManage.task_id,
                                                                 "1"
                                                                 )
        print(update_checklist_result)

    def test_1700_delete_checklist(self):
        """
        删除规避措施
        """
        # /task/v1/task/{id}/checklist/{cid}
        delete_checklist_result = ApiTaskManage.delete_checklist(self,
                                                                 objectId=TaskManage.task_id,
                                                                 id=TaskManage.checklist_id
                                                                 )
        print(delete_checklist_result)

    @unittest.skip('测试project不能有平台的接口')
    def test_1800_add_labels(self):
        """
        添加标签，标签ID多个用逗号或分号分隔
        """
        # /task/v1/task/{id}/labels
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
        TaskManage.labels_id = add_dict_result.get("id")
        add_labels_result = ApiTaskManage.add_labels(self, TaskManage.task_id, TaskManage.labels_id)
        print(add_labels_result)

    @unittest.skip('因为test_1800的原因')
    def test_2000_delete_labels(self):
        """
        删除标签，标签ID多个用逗号或分号分隔
        """
        # /task/v1/task/{id}/labels/{labelIds}
        delete_labels_result = ApiTaskManage.delete_labels(self, TaskManage.task_id, TaskManage.labels_id)
        print(delete_labels_result)

    def test_2300_get_project_tasks(self):
        """
        分页获取计划列表（项目下）
        """
        # /task/v1/tasks
        get_project_tasks = ApiTaskManage.get_tasks(self, TaskManage.project_id)
        print(get_project_tasks)

    def test_2500_get_task_by_id(self):
        """
        获取计划详细信息
        """
        # /task/v1/tasks/{id}
        get_task_by_id = ApiTaskManage.get_task_by_id(self, TaskManage.task_id)
        print(get_task_by_id)

    def test_2600_get_bdchart(self):
        """
        获取项目燃尽图
        """
        # /plan/$VERSION$/bdchart/{id}
        get_bdchart = ApiTaskManage.get_bdchart(self, TaskManage.project_id)
        print(get_bdchart)

    def test_2700_get_mchart(self):
        """
        获取项目成员完成状况
        """
        # /plan/$VERSION$/mchart/{id}
        get_mchart = ApiTaskManage.get_mchart(self, TaskManage.project_id)
        print(get_mchart)

    def test_2800_get_tasks_page(self):
        """
        获取项目任务列表（分页）
        """
        # /plan/$VERSION$/tasks/page
        get_tasks_page = ApiTaskManage.get_tasks_page(self, TaskManage.project_id)
        print(get_tasks_page)

    @unittest.skip('接口未使用')
    def test_2900_get_undone_task(self):
        """
        接口名称：查询未完成任务
        接口地址：/plan/$VERSION$/tasks/undone/{project_id}
        """
        get_undone_task = ApiTaskManage.get_undone_task(self, TaskManage.project_id)
        print(get_undone_task)

    def test_3000_sync_percent_task(self):
        """
        全局刷新计划百分比
        """
        # /plan/$VERSION$/percent/sync
        sync_percent_task = ApiTaskManage.sync_percent_task(self)
        print(sync_percent_task)

    def test_3100_get_task_children(self):
        """
        获取子任务
        """
        # /plan/$VERSION$/task/{id}/children
        get_task_children = ApiTaskManage.get_task_children(self, TaskManage.task_id)
        print(get_task_children)

    def test_3200_get_milestone(self):
        """
        获取里程碑数据
        """
        # /plan/$VERSION$/task/milestone/{project_id}
        get_milestone = ApiTaskManage.get_milestone(self, TaskManage.project_id)
        print(get_milestone)

    def test_3300_get_first_tasklist(self):
        """
        根据项目id获取一级任务列表
        """
        # /plan/$VERSION$/tasks/getOneTaskList
        get_first_tasklist = ApiTaskManage.get_first_tasklist(self, TaskManage.project_id)
        print(get_first_tasklist)

    @unittest.skip('接口未使用')
    def test_3400_get_proj_tasks_statistics(self):
        """
        根据项目id获取项目任务统计数据（任务总数、完成数）
        """
        # /plan/$VERSION$/task/statistics/{project_id}
        get_proj_tasks_statistics = ApiTaskManage.get_proj_tasks_statistics(self, TaskManage.project_id)
        print(get_proj_tasks_statistics)

    def test_3500_get_critical_flag_task(self):
        """
        判断task及其子是否是其他task的前置任务
        """
        # /plan/$VERSION$/{project_id}/critical
        get_critical_flag_task = ApiTaskManage.get_critical_flag_task(self, TaskManage.project_id)
        print(get_critical_flag_task)

    def test_3600_get_all_task_doc(self):
        """
        获取项目下所有任务的交付件
        """
        # /plan/$VERSION$/tasks/doc/{id}
        get_all_task_doc = ApiTaskManage.get_all_task_doc(self, TaskManage.project_id, "1")
        print(get_all_task_doc)

    def test_3700_query_tree_list_by_ids(self):
        """
        根据ID列表查询对象详细信息
        """
        # /plan/$VERSION$/tree/{ids}
        query_tree_list_by_ids = ApiTaskManage.query_tree_list_by_ids(self, TaskManage.project_id)
        print(query_tree_list_by_ids)

    def test_3800_refresh_predecessor_link(self):
        """
        刷新项目下所有后置依赖任务计划时间
        """
        # /plan/$VERSION$/predecessorLink/project/{id}
        refresh_predecessor_link = ApiTaskManage.refresh_predecessor_link(self, TaskManage.project_id)
        print(refresh_predecessor_link)

    @unittest.skip('接口未使用')
    def test_3900_get_proj_tasks_statistics_detail(self):
        """
        根据项目id获取项目任务统计数据详情
        """
        # /plan/$VERSION$/task/statistics/detail/{project_id}
        get_proj_tasks_statistics_detail = ApiTaskManage.get_proj_tasks_statistics_detail(self, TaskManage.project_id)
        print(get_proj_tasks_statistics_detail)

    def test_4000_get_predecessor_task_by_id(self):
        """
        判断task及其子是否是其他task的前置任务(task_id)
        """
        # /plan/$VERSION$/predecessor
        get_predecessor_task_by_id = ApiTaskManage.get_predecessor_task_by_id(self, TaskManage.task_id)
        print(get_predecessor_task_by_id)

    def test_4100_add_task_predecessorLink(self):
        """
        添加前置任务，不支持批量添加
        """
        # /plan/$VERSION$/task/{id}/predecessorLink
        ApiTaskManage.add_task_predecessorLink(self,
                                               TaskManage.copy_task_id,
                                               TaskManage.task_id,

                                               )

    def test_4150_delete_task_predecessor_link(self):
        """
        删除任务前置依赖
        """
        # /plan/$VERSION$/tasks/{id}/predecessorLink
        ApiTaskManage.delete_task_predecessor_link(self,
                                                   TaskManage.task_id,
                                                   TaskManage.copy_task_id
                                                   )

    def test_4200_get_duration_by_cal(self):
        """
        根据日历配置计算工期或计划时间
        """
        # /plan/$VERSION$/duration
        get_duration_by_cal = ApiTaskManage.get_duration_by_cal(self,
                                                                TaskManage.project_id,
                                                                time.strftime('%Y-%m-%d', time.localtime()),
                                                                time.strftime('%Y-%m-%d', time.localtime())
                                                                )
        print(get_duration_by_cal)

    def test_4500_get_first_level_child_tasks(self):
        """
        根据任务id获取第一层子任务列表
        """
        # /plan/$VERSION$/tasks/{id}/children
        ApiTaskManage.get_first_level_child_tasks(self, TaskManage.task_id)

    def test_4600_export_mchart(self):
        """
        导出项目概况统计报表
        """
        # /plan/$VERSION$/mchartexport/{project_id}
        ApiTaskManage.export_mchart(self, TaskManage.project_id)

    def test_4700_get_tasks_by_uid(self):
        """
        获取责任人下的当前任务或要做任务
        """
        # /plan/$VERSION$/tasks/member/{member}
        get_tasks_by_uid = ApiTaskManage.get_tasks_by_uid(self, TaskManage.user_id, "0")
        print(get_tasks_by_uid)

    def test_4800_get_parent_task_by_id(self):
        """
        通过任务id获取最顶层的父
        """
        # /plan/$VERSION$/getParentTaskById/{task_id}
        get_parent_task_by_id = ApiTaskManage.get_parent_task_by_id(self, TaskManage.task_id)
        print(get_parent_task_by_id)

    def test_4900_sync_task_handler(self):
        """
        同步任务责任人
        """
        # /plan/$VERSION$/task/{project_id}/all/members
        sync_task_handler = ApiTaskManage.sync_task_handler(self, project_id="bd9868623b25a64f77c134c5073ac66b")
        print(sync_task_handler)

    def test_5000_check_task_start_finish_time(self):
        """
        校验任务的开始和结束时间
        """
        # /plan/$VERSION$/checkTaskStartFinishTime
        check_task_start_finish_time = ApiTaskManage.check_task_start_finish_time(self, TaskManage.task_id)
        print(check_task_start_finish_time)

    def test_5100_get_tasklist(self):
        """
        批量创建子任务时获取任务列表，来关联父任务
        """
        # /plan/$VERSION$/taskList
        ApiTaskManage.get_tasklist(self, TaskManage.project_id)

    def test_5300_care_task(self):
        """
        收藏/取消收藏
        """
        # /task/v1/myCare
        care_task_result = ApiTaskManage.care_task(self,
                                                   TaskManage.task_id,
                                                   "AutoPlan"
                                                   )
        print(care_task_result)

    def test_5400_pgrade_task(self):
        """
        升级
        """
        # /plan/$VERSION$/task/{project_id}/upgrade
        upgrade_task = ApiTaskManage.upgrade_task(self, TaskManage.child_task_id1, TaskManage.project_id)
        print(upgrade_task)

    def test_5500_downgrade_task(self):
        """
        降级
        """
        # /plan/$VERSION$/task/{project_id}/downgrade
        downgrade_task = ApiTaskManage.downgrade_task(self, TaskManage.child_task_id1, TaskManage.project_id)
        print(downgrade_task)

    def test_5600_sort_task(self):
        """
        任务排序
        """
        # /plan/$VERSION$/task/{id}/sort
        sort_task = ApiTaskManage.sort_task(self, TaskManage.task_id, "moveDown")
        print(sort_task)

    def test_5650_edit_sort_task(self):
        """
        拖拽排序子任务
        """
        # /plan/$VERSION$/task/{id}/order
        edit_sort_task = ApiTaskManage.edit_sort_task(self,
                                                      TaskManage.task_id,
                                                      TaskManage.child_task_id1,
                                                      TaskManage.child_task_id2
                                                      )
        print(edit_sort_task)

    def test_6600_add_member(self):
        """
        添加计划成员
        """
        # /plan/$VERSION$/task/{id}/members
        add_member = ApiTaskManage.add_member(self, TaskManage.task_id, TaskManage.user_id, "HANDLEPERSON")
        print(add_member)

    def test_6700_delete_member(self):
        """
        删除计划成员
        """
        # /plan/$VERSION$/task/{id}/members/{memberIds}
        delete_member = ApiTaskManage.delete_member(self, TaskManage.task_id, TaskManage.user_id)
        print(delete_member)

    def test_6900_export_business_template(self):
        """
        接口名称：导出业务数据模板
        接口地址：/plan/$VERSION$/template/export
        """
        export_business_template = ApiTaskManage.export_business_template(self,
                                                                          "erd.cloud.plan.dto.EtTask",
                                                                          "code,name,milestoneFlag,state,"
                                                                          "resAssignments,member,startDate,finishDate,"
                                                                          "duration,workload,percentComplete,"
                                                                          "predecessorLink,createBy",
                                                                          TaskManage.view_id
                                                                          )
        print(export_business_template)

    def test_7000_select_business_table(self):
        """
        查询业务表格列
        """
        # /task/v1/{viewid}/businessTable
        select_business_table = ApiTaskManage.select_business_table(self,
                                                                    TaskManage.view_id,
                                                                    TaskManage.project_id
                                                                    )
        print(select_business_table)

    def test_7100_select_filterlist(self):
        """
        过滤业务数据
        """
        # /task/v1/{viewid}/filterlist
        select_filterlist_result = ApiTaskManage.select_filterlist(self, TaskManage.view_id)
        print(select_filterlist_result)

    def test_7200_cut_task_by_ids(self):
        """
        裁剪计划
        """
        # /plan/$VERSION$/cut
        cut_task_by_ids = ApiTaskManage.cut_task_by_ids(self, TaskManage.task_id)
        print(cut_task_by_ids)

    def test_7300_select_business_list(self):
        """
        查询业务数据
        """
        # /task/v1/{viewid}/businesslist
        plan_id_list = []
        select_business_list = ApiTaskManage.select_business_list(self,
                                                                  TaskManage.view_id,
                                                                  TaskManage.project_id
                                                                  )
        plan_list_records = select_business_list['res']['data']['records']
        for i in range(len(plan_list_records)):
            plan_id_list.append(plan_list_records[i]['id'])
        TaskManage.plan_id_list = plan_id_list


    def test_7600_copy_template_task(self):
        """
        接口名称：拷贝项目模版任务数据
        接口地址：/plan/$VERSION$/task/template/copy
        """
        r = ApiProjectTemplate.addProjectTemplateUsingPOST(self,"创建项目模板XXX",
                                                       project_id=TaskManage.project_id,
                                                       name="Project_Template_" + time.strftime('%H%M%S', time.localtime()))
        TaskManage.project_template_id = r["id"]
        ApiTaskManage.copy_template_task(self, project_id=TaskManage.project_id,template_id=TaskManage.project_template_id)


    def test_7700_execute_task(self):
        """
        接口名称：责任人开始执行任务
        接口地址：/plan/$VERSION$/executetask/{id}
        """
        ApiTaskManage.execute_task(self,
                                   task_id=TaskManage.task_id,
                                   project_id=TaskManage.project_id)

    def test_7800_close_validate(self):
        """
        接口名称：任务关闭校验接口
        接口地址：/plan/$VERSION$/{id}/close/validate
        """
        ApiTaskManage.close_validate(self,
                                     task_id=TaskManage.task_id
                                     )

    def test_7900_close_task(self):
        """
        接口名称：任务关闭接口
        接口地址：/plan/$VERSION$/{id}/close
        """
        ApiTaskManage.close_task(self,
                                 task_id=db.task_view_id
                                 )

    def test_8000_close_task_process(self):
        """
        接口名称：流程配置调用任务关闭接口
        接口地址：/plan/$VERSION$/close
        """
        ApiTaskManage.close_task_process(self,
                                         params={
                                             "processInstanceId": "c90c19c295e711eca7d02e4fce3af5cb",
                                             "processDefinitionId": "TASK_CLOSE:2:0ace2de7954c11eca7d02e4fce3af5cb",
                                             "routeFlag": "0",
                                             "trigger": "start",
                                             "flowState": "COMPLETE",
                                             "processDefinitionKey": "TASK_CLOSE",
                                             "bussinessFormDataJson": "[{\"id\":\"ad229b43d06fdb2e1d8a5902f22cd980\",\"createBy\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"createTime\":\"2022-02-24 14:47:25\",\"updateBy\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"updateTime\":\"2022-02-24 16:05:39\",\"delFlag\":\"0\",\"code\":\"1\",\"name\":\"测试1\",\"description\":\"\",\"flexAttrs\":{},\"parentId\":\"-1\",\"project_id\":\"c59c0b2a0d83629651b9e8bf82887007\",\"priority\":0,\"actualStartDate\":\"2022-02-24\",\"state\":\"PROCESSION\",\"workload\":0,\"percentComplete\":0,\"criticalFlag\":0,\"summaryFlag\":0,\"milestoneFlag\":0,\"resAssignments\":\"PM\",\"orderCode\":\"1001\",\"taskMemberList\":[{\"id\":\"1047e3d9489e16b28154191eeff74779\",\"objectClassName\":\"erd.cloud.project.common.po.EtTaskPo\",\"objectId\":\"ad229b43d06fdb2e1d8a5902f22cd980\",\"roleKey\":\"HANDLEPERSON\",\"userId\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"active\":\"2\"},{\"id\":\"525dcb70c73932cc5d5c09cf4559b7ff\",\"objectClassName\":\"erd.cloud.plan.dto.EtTask\",\"objectId\":\"ad229b43d06fdb2e1d8a5902f22cd980\",\"roleKey\":\"SUBMITTER\",\"userId\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"sort\":0,\"active\":\"1\"}],\"sop\":\"\",\"taskInput\":\"\",\"taskOutput\":\"\",\"isCutted\":0,\"canBeCutted\":1,\"lifecycleTemplateId\":\"0afdb2d446b2ef0c3d089456db0aa64a\",\"leafNode\":false,\"newRecord\":false,\"responsibles\":[],\"checkLists\":[],\"_checked\":true,\"project\":{\"id\":\"c59c0b2a0d83629651b9e8bf82887007\",\"createBy\":\"SYS_E39B20EA11E7A81AC85B767C89C1\",\"createTime\":\"2022-02-24 12:22:01\",\"updateTime\":\"2022-02-24 12:22:01\",\"delFlag\":\"0\",\"code\":\"RDP20220224101\",\"name\":\"345345\",\"description\":\"1\",\"flexAttrs\":{\"extStringValue15\":\"0\"},\"parentId\":\"-1\",\"isTemplate\":0,\"templateId\":\"\",\"type\":\"STANDARD\",\"pmIds\":[\"SYS_E39B20EA11E7A81AC85B767C89C1\"],\"state\":\"PLANNING\",\"departmentId\":\"0cfa58e9c985f0525e2444377fbbebb4\",\"startTime\":\"2022-02-24\",\"finishTime\":\"2022-02-28\",\"lifecycleTemplateId\":\"da92b41ba14a1eea50752ce6fd792557\",\"projCategory\":\"category\",\"projectMemberList\":[],\"acl\":{\"acls\":{\"ELPortfolio\":{\"ALL\":63},\"ELRisk\":{\"NEW\":31,\"ALL\":63,\"COMPLETE\":31,\"DRAFT\":31,\"CANCEL\":31,\"CLOSE\":31,\"SKETCH\":31,\"OPEN\":31},\"role\":{\"ALL\":63},\"ELEied\":{\"ALL\":63},\"auth\":{\"ALL\":63},\"ELBudget\":{\"ALL\":63,\"RELEASED\":31,\"APPROVING\":31,\"MAKING\":31},\"ELProject\":{\"ALL\":63,\"Draft\":31,\"CLOSED\":31,\"ONGOING\":31,\"SETTEDUP\":31,\"PENDING\":31,\"SKETCH\":31,\"PLANNING\":31},\"ELIssue\":{\"SUSPENDING\":31,\"ALL\":63,\"PENDINGVERIFICATION\":31,\"CLOSED\":31,\"DRAFT\":31,\"CANCEL\":31,\"SKETCH\":31},\"ELRequire\":{\"PENDINGREVIEW\":31,\"TODO\":31,\"ALL\":63,\"PENDINGTEST\":31,\"REALIZED\":31,\"DRAFT\":31,\"CANCELED\":31,\"PENDINGANALYSE\":31,\"DEVELOP\":31,\"SKETCH\":31},\"ELProgram\":{\"ALL\":63},\"ELDocument\":{\"ALL\":31},\"ELTask\":{\"NEW\":31,\"ALL\":63,\"COMPLETE\":31,\"DRAFT\":31,\"CANCEL\":31,\"VALIDATION\":31,\"APPROVE\":31,\"PENDING\":31,\"PREPARING\":31,\"PROCESSION\":31,\"SKETCH\":31},\"ELStrategy\":{\"ALL\":63},\"department\":{\"ALL\":18},\"user\":{\"ALL\":18},\"ELDoc\":{\"ALL\":63}},\"project_id\":\"c59c0b2a0d83629651b9e8bf82887007\"}}}]",
                                             "taskDefinitionKey": "end1",
                                             "startUserId": "SYS_E39B20EA11E7A81AC85B767C89C1",
                                             "businessKeys": [
                                                 "ad229b43d06fdb2e1d8a5902f22cd980"
                                             ],
                                             "tenantId": "erdp"
                                         }
                                         )



    def test_8001_getDurationrecordUsingGET(self):
        """
        接口名称：获取工时选项卡
        接口地址：/plan/$VERSION$/durationrecord/{id}
        """
        # print(update_task_result)
        r = ApiTaskManage.getDurationrecordUsingGET(self,
                                                    id=TaskManage.task_id
                                                    )
        print(r)
        TaskManage.sum_id = r["res"]["data"]["id"]
        print(r["res"]["data"]["id"])

    def test_8002_findUserDurationRecordsUsingGET(self):
        """
        接口名称：获取用户工时
        接口地址：/plan/$VERSION$/duration/record/{startDate}/{endDate}
        """
        ApiTaskManage.findUserDurationRecordsUsingGET(self,
                                                      startDate="2022-01-01",
                                                      endDate=time.strftime("%Y-%m-%d", time.localtime()),
                                                      userId=db.user_id
                                                      )

    def test_8003_addDurationrecordUsingPOST(self):
        """
        接口名称：添加工时选项卡登记
        接口地址：/plan/$VERSION$/durationrecord
        """
        r = ApiTaskManage.addDurationrecordUsingPOST(self,
                                                     workload="10",
                                                     remainDuration="0.00",
                                                     registeredTime="1",
                                                     description="",
                                                     sumId=TaskManage.sum_id,
                                                     startDate=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                                                     )
        print(r)
        TaskManage.working_hour_id = r["res"]["data"]["id"]
        print(r["res"]["data"]["id"])

    def test_8004_getOneDurationrecordUsingGET(self):
        """
        接口名称：单个登记卡信息
        接口地址：/plan/$VERSION$/one/durationrecord/{id}
        """
        ApiTaskManage.getOneDurationrecordUsingGET(self,
                                                   id=TaskManage.working_hour_id
                                                   )

    def test_8005_updateDurationrecordUsingPUT(self):
        """
        接口名称：更新工时选项卡登记
        接口地址：/plan/$VERSION$/update/durationrecord
        """
        ApiTaskManage.updateDurationrecordUsingPUT(self,
                                                   record={"id": TaskManage.working_hour_id,
                                                           "createBy": TaskManage.user_id,
                                                           "createTime": time.strftime('%Y-%m-%d %H:%M:%S',
                                                                                       time.localtime()),
                                                           "updateTime": time.strftime('%Y-%m-%d %H:%M:%S',
                                                                                       time.localtime()),
                                                           "delFlag": "0",
                                                           "sumId": TaskManage.sum_id,
                                                           "startDate": time.strftime('%Y-%m-%d ',
                                                                                      time.localtime()) + "00:00:00",
                                                           "duration": 0,
                                                           "remainDuration": "0.00",
                                                           "registeredTime": "1",
                                                           "description": "测试",
                                                           "difference": -728})






    def test_9900_import_business(self):
        """
        接口名称：导入业务数据
        接口地址：/plan/$VERSION$/import
        """

        # 导入计划
        ApiTaskManage.import_business(self,
                                      project_id=TaskManage.project_id)

    def test_9910_delete_task_by_id_list(self):
        """
        接口名称：根据ids批量删除任务
        接口地址：/plan/$VERSION$/tasks/{projectId}
        """
        ApiTaskManage.delete_task_by_id_list(self,project_id=TaskManage.project_id, task_id=TaskManage.plan_id_list)


    def test_9920_delete_project(self):
        # 删除项目
        ApiProject.deleteProjectUsingDELETE(self, project_id=TaskManage.project_id)


if __name__ == '__main__':
    unittest.main(verbosity=2)

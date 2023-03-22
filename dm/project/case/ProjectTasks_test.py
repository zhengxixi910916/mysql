import time
import unittest
from project.api import ApiProjectTasks, ApiProject
from project.case.file.runSql import db

class ProjectTasks(unittest.TestCase):
    user_id = db.user_id
    org_id = db.org_id
    project_id = ''
    plan_id_list = []
    task_id = ''
    plan_data = {
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
        "projectId": "",
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
        "taskMemberList[1].userId": "SYS_E39B20EA11E7A81AC85B767C89C1",
        "labelLinkIds": ""
    }

    def test_0100_add_task_using_post_1(self):
        """
        接口名称：创建任务
        接口地址：/plan/$VERSION$/task
        """
        # 新增项目
        project_name = "project_task_" + time.strftime('%Y%m%d %H%M%S', time.localtime())
        project_ = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        # 获取项目id
        ProjectTasks.project_id = project_.get("id")
        # 创建计划
        ProjectTasks.plan_data['projectId'] = ProjectTasks.project_id
        for _ in range(2):
            r = ApiProjectTasks.add_task_using_post_1(self,
                                                      data=ProjectTasks.plan_data)
            ProjectTasks.plan_id_list.append(r['id'])

    def test_0200_update_task_using_put(self):
        """
        接口名称：修改任务
        接口地址：/plan/$VERSION$/task/{id}
        """

        for plan_id in ProjectTasks.plan_id_list:
            ApiProjectTasks.update_task_using_put(self,
                                                  plan_id=plan_id,
                                                  project_id=ProjectTasks.project_id
                                                  )
    def test_0250_get_task_by_id_using_get(self):
        """
        接口名称：获取计划详细信息
        接口地址：/plan/$VERSION$/task/{id}
        """

        r = ApiProjectTasks.get_task_by_id_using_get(self, task_id=ProjectTasks.plan_id_list[0])

    def test_0300_batch_operate_using_put(self):
        """
        接口名称：批量执行/完成任务
        接口地址：/plan/$VERSION$/batchOperate
        """
        # 批量执行
        r1 = ApiProjectTasks.batch_operate_using_put(self, plan_id_list=ProjectTasks.plan_id_list, operate_type=1)
        print(r1)

        # 批量完成任务
        r2 = ApiProjectTasks.batch_operate_using_put(self, plan_id_list=ProjectTasks.plan_id_list, operate_type=2)
        print(r2)

    def test_0400_edit_batch_responsibility_using_put(self):
        """
        接口名称：批量修改责任人
        接口地址：/plan/$VERSION$/task/editBatchResponsibility
        """

        ApiProjectTasks.edit_batch_responsibility_using_put(self,
                                                            task_id1=ProjectTasks.plan_id_list[0],
                                                            task_id2=ProjectTasks.plan_id_list[1],
                                                            project_id=ProjectTasks.project_id
                                                            )

    def test_0500_delete_task_by_id_list_using_delete(self):
        """
        接口名称：根据ids批量删除任务
        接口地址：/plan/$VERSION$/tasks/projectId
        """

        ApiProjectTasks.delete_task_by_id_list_using_delete(self, ProjectTasks.project_id,
                                                            plan_list_id=ProjectTasks.plan_id_list)

    def test_5000_deleteProjectUsingDELETE(self):
        """
        接口名称：删除项目
        接口地址：/proj/$VERSION$/{id}
        """
        ApiProject.deleteProjectUsingDELETE(self, project_id=ProjectTasks.project_id)


if __name__ == '__main__':
    unittest.main()

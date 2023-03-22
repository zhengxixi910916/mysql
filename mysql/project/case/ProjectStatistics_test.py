# -*- coding: utf-8 -*-
# @Time    : 2022/02/21
# @Author  : Chen
import time
import unittest
from project.api import ApiProjectStatistics,ApiProject
from project.case.file.runSql import db


class CustomProject(unittest.TestCase):
    """项目、项目群统计信息"""
    project_id = ''
    orgId = db.org_id


    def setUp(self) -> None:

        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        addProjectUsingPOST_1 = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        print(addProjectUsingPOST_1)
        CustomProject.project_id = addProjectUsingPOST_1.get('id')
        pass


    def test_0100_Statistics(self):
        """项目管理-统计"""
        ApiProjectStatistics.Statistics(self,
                                        project_id=CustomProject.project_id
                                        )

    def test_0200_Overview(self):
        """项目管理-统计-概况"""
        ApiProjectStatistics.Overview(self,
                                      project_id=CustomProject.project_id,
                                      month="2021-07",
                                      )

    def test_0300_PlanReport(self):
        """项目管理-统计-计划报表"""
        ApiProjectStatistics.PlanReport(self,
                                        project_id=CustomProject.project_id,
                                        ymonth="2021-07"
                                        )

    def test_0400_MilestoneReport(self):
        """项目管理-统计-里程碑情况"""
        ApiProjectStatistics.MilestoneReport(self,
                                             Id=CustomProject.project_id,
                                             project_id=CustomProject.project_id
                                             )

    def test_0500_ProblemReport(self):
        """项目管理-统计-问题报表"""
        ApiProjectStatistics.PlanReport(self,
                                        project_id=CustomProject.project_id,
                                        ymonth="2021-07"
                                        )

    def test_0600_RiskReport(self):
        """项目管理-统计-风险报表"""
        ApiProjectStatistics.RiskReport(self,
                                        project_id=CustomProject.project_id,
                                        ymonth="2021-07"
                                        )

    def test_0700_CustomReport(self):
        """项目管理-统计-自定义报表"""
        ApiProjectStatistics.CustomReport(self,
                                          project_id=CustomProject.project_id
                                          )

    def test_0800_Hrview(self):
        """项目管理-统计-人力视图报表"""
        ApiProjectStatistics.Hrview(self,
                                    project_id=CustomProject.project_id,
                                    memberIds="",
                                    startDate="2021/05/01",
                                    endDate="2021/09/30",
                                    dimension="monthly"
                                    )

    def test_0900_ProjectReport(self):
        """项目管理-统计-项目报告"""
        ApiProjectStatistics.ProjectReport(self,
                                           name="",
                                           type="0",
                                           status="",
                                           createBy="",
                                           dateFor="",
                                           startTime="",
                                           endTime="",
                                           page_size="20",
                                           page_index="1",
                                           updateBy="",
                                           project_id=CustomProject.project_id,
                                           orderBy="createTime",
                                           sortBy="DESC",
                                           )

    def test_1000_TaskCompletionStatistics(self):
        """项目管理-统计-任务完成统计情况"""
        ApiProjectStatistics.TaskCompletionStatistics(self,
                                                      userId="",
                                                      project_ids=CustomProject.project_id,
                                                      taskName="",
                                                      orgId="",
                                                      startDate="2021-07-27",
                                                      endDate="2021-07-27",
                                                      orgid=CustomProject.orgId
                                                      )

    def test_1100_getManpowerViewdepartUsingGET(self):
        """
        接口名称：人力视图报表
        接口地址：/proj/$VERSION$/statistic/hrviewdepart
        """
        #
        ApiProjectStatistics.getManpowerViewdepartUsingGET(self,
                                                           project_id="",
                                                           memberIds="",
                                                           departmentId="SYS_2d28fff04a3da56f410a241528b4",
                                                           startDate="2001/01/01",
                                                           endDate=time.strftime('%Y/%m/%d', time.localtime()),
                                                           dimension="monthly",
                                                           page_index="1",
                                                           page_size="20"
                                                           )

    def test_1500_get_project_process(self):
        """
        接口名称：项目进展统计报表
        接口地址：/proj/$VERSION$/statistic/progress
        """
        ApiProjectStatistics.get_project_process(self)

    def test_1200_getManpowerViewPageUsingGET(self):
        """
        接口名称：分页查询人力Loading视图
        接口地址：/proj/$VERSION$/statistic/hrview/page
        """
        ApiProjectStatistics.getManpowerViewPageUsingGET(self,
                                                         project_id=CustomProject.project_id,
                                                         memberIds='',
                                                         startDate="2001/01/01",
                                                         endDate=time.strftime('%Y/%m/%d', time.localtime()),
                                                         dimension="monthly",
                                                         page_index="1",
                                                         page_size="20"
                                                         )

    def test_1300_getTopProjectUsingGET(self):
        """
        接口名称：TOP项目清单报表
        接口地址：/proj/$VERSION$/statistic/topProject
        """
        ApiProjectStatistics.getTopProjectUsingGET(self,
                                                   departmentId=db.org_id,
                                                   page_index="1",
                                                   page_size="10"
                                                   )

    def test_1400_getManpowerViewUsingGET_2(self):
        """
        接口名称：项目状态统计
        接口地址：/proj/$VERSION$/statistic/status/report
        """
        ApiProjectStatistics.getManpowerViewUsingGET_2(self,
                                                       departmentId="",
                                                       pmId=db.user_id,
                                                       startDateA="2001-01-01",
                                                       starDateB=time.strftime('%Y-%m-%d', time.localtime())
                                                       )

    def test_1500_pageProjectUsingGET_1(self):
        """
        接口名称：根据项目id查询项目分页列表
        接口地址：/proj/$VERSION$/statistic/page/projects
        """
        ApiProjectStatistics.pageProjectUsingGET_1(self,
                                                   page_index="1",
                                                   page_size="10",
                                                   project_ids=CustomProject.project_id
                                                   )


if __name__ == "__main__":
    unittest.main()

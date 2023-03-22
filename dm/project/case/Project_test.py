# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 15:04
# @Author  : Liao

import time
import unittest

from project.api import ApiProject
from erdcloud.dm_db import DB
from project.case.file.runSql import db


class Project(unittest.TestCase):
    """项目信息"""
    project_id = ""
    user_id = db.user_id
    org_id = db.org_id
    project_name = ""
    project_name2 = ""
    children_ids = ""
    ABC_id = ""  # Application basic configuration id
    project_code = ''
    @classmethod
    def setUpClass(cls):
        pass

        # @classmethod
        # def tearDownClass(cls) -> None:
        #     db.delete_sql()
        DB.instance().clear(section="project",
                            table='proj_elproject',
                            eid=Project.project_id
                            )

    def test_0100_addProjectUsingPOST_1(self):
        """
        保存项目基本信息
        """
        # /proj/$VERSION$/project
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        addProjectUsingPOST_1 = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        print(addProjectUsingPOST_1)
        Project.project_id = addProjectUsingPOST_1.get("id")
        Project.project_code = addProjectUsingPOST_1.get('code')
        print("project_id:", Project.project_id)
        Project.project_name = addProjectUsingPOST_1.get("name")
        Project.project_name2 = Project.project_name + "归档"

    def test_0110_get_projectlist(self):
        """
        接口名称：根据当前用户查询项目信息列表
        接口地址：/proj/$VERSION$/projects
        """
        get_projectlist = ApiProject.getProjectListUsingGET(self)

    def test_0120_care_myproject(self):
        """
        接口名称：收藏项目/取消收藏
        接口地址：/proj/$VERSION$/addMyCareProject
        """
        care_myproject = ApiProject.careMyProjectUsingPOST_1(self,
                                                             project_id=Project.project_id,
                                                             project_name=Project.project_name)

    def test_0130_get_mycareproject(self):
        """
        接口名称：获取我收藏的项目
        接口地址：/proj/$VERSION$/getMyCareProject
        """
        ApiProject.getMyCareProjectUsingGET(self,
                                            project_name=Project.project_name)

    def test_0140_get_projecbyid(self):
        """
        接口名称： 根据项目ID查询项目基本信息
        接口地址：/proj/$VERSION$/project/{id}
        """
        ApiProject.getProjecByIdUsingGET(self,
                                         project_id=Project.project_id)

    def test_0150_update_project(self):
        """
        接口名称：更新项目信息
        接口地址：/proj/$VERSION$/project
        """

        ApiProject.updateProjectUsingPUT(self, project_code=Project.project_code,
                                         project_id=Project.project_id,
                                         project_name=Project.project_name)

    def test_0160_add_children(self):
        """
        接口名称：批量添加子项目
        接口地址：/proj/$VERSION$/projects/{id}/children
        """
        # 新增子项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        children_project = ApiProject.addProjectUsingPOST_1(self,
                                                            name=project_name,
                                                            )
        Project.children_ids = children_project.get("id")

        # 添加子项目
        ApiProject.addChildrenUsingPOST(self,
                                        project_id=Project.project_id,
                                        children_ids=Project.children_ids)

    def test_0170_delete_parentlink(self):
        """
        接口名称：根据子项目ID解除父子关系
        接口地址：/proj/$VERSION$/project/{id}/link
        """
        ApiProject.deleteParentLinkUsingPUT(self,
                                            children_ids=Project.children_ids)

    def test_0180_update_projectfile(self):
        """
        接口名称：项目归档
        接口地址：/proj/$VERSION$/project/{id}/archived
        """
        update_projectfile = ApiProject.updateProjectFileUsingPUT(self,
                                                                  project_id=Project.project_id)
        print(update_projectfile)

    def test_0190_getUserAclUsingGET(self):
        """
        接口名称：获取用户项目权限
        接口地址：/proj/$VERSION$/acl/sys/{userId}
        """
        ApiProject.getUserAclUsingGET(self,
                                      userId=db.user_id,
                                      project_id=db.project_id
                                      )

    def test_0200_getBascDataByTypeUsingGET(self):
        """
        接口名称：获取数据字典
        接口地址：/proj/$VERSION$/project/dict
        """
        ApiProject.getBascDataByTypeUsingGET(self,
                                             attribute="lable",
                                             type="common"
                                             )

    def test_0210_selectAvlbFieldListUsingGET_2(self):
        """
        接口名称：查询可用的扩展列名称
        接口地址：/proj/$VERSION$/avlbfields
        """
        ApiProject.selectAvlbFieldListUsingGET_2(self)

    def test_0220_getPorjectInfoByProcessInstanceIdUsingGET(self):
        """
        接口名称：根据流程的id查询实体对象的详情
        接口地址：/proj/$VERSION$/project_id/{processInstanceId}
        """
        ApiProject.getPorjectInfoByProcessInstanceIdUsingGET(self,
                                                             processInstanceId=Project.project_id,
                                                             )

    def test_0230_getProjectProgressByIdUsingGET(self):
        """
        接口名称：项目进度(已完成任务/总任务数)
        接口地址：/proj/$VERSION$/project/{id}/progress
        """
        ApiProject.getProjectProgressByIdUsingGET(self,
                                                  project_id=db.project_id
                                                  )

    def test_0240_selectAvlbFieldListUsingGET_3(self):
        """
        接口名称：查询可用的扩展列名称
        接口地址：/proj/$VERSION$/extfields
        """
        ApiProject.selectAvlbFieldListUsingGET_3(self,
                                                 active=""  # 列状态1已使用0未使用，空所有
                                                 )

    def test_0250_getProjectCloseAccessUsingGET(self):
        """
        接口名称： 根据项目ID判断项目是否支持关闭
        接口地址：/proj/$VERSION$/{id}/close/validate
        """
        ApiProject.getProjectCloseAccessUsingGET(self,
                                                 project_id=db.project_id
                                                 )

    def test_0260_getProjectByNameOrCodeUsingGET(self):
        """
        接口名称：根据项目名称或编码查询项目详情列表
        接口地址：/proj/$VERSION$/project/{id}/keyword
        """
        ApiProject.getProjectByNameOrCodeUsingGET(self,
                                                  project_id=db.project_id,
                                                  hasParent="2",  # 有无父项目（0：无父项目，1：有父项目，2：不限，其它：非法）
                                                  keyword="test"  # 查询关键字
                                                  )

    def test_0270_getMemberByNameUsingGET(self):
        """
        接口名称：查询成员
        接口地址：/proj/$VERSION$/members
        """
        ApiProject.getMemberByNameUsingGET(self,
                                           condition=""
                                           )

    def test_0280_pageProjectUsingGET(self):
        """
        接口名称：根据条件查询项目信息列表（不权限控制）
        接口地址：/proj/$VERSION$/pageProject
        """
        ApiProject.pageProjectUsingGET(self,name="",
                                       project_ids=Project.project_id,
                                       state="",
                                       type=""
                                       )

    def test_0290_searchProjectListUsingGET(self):
        """
        接口名称：根据当前用户高级查询项目信息列表
        接口地址：/proj/$VERSION$/searchProjects
        """
        ApiProject.searchProjectListUsingGET(self,
                                             condition="",
                                             conditionRef="",
                                             order_by="create_time",
                                             page_size="10",
                                             page_index="1",
                                             sort_by="desc"
                                             )

    def test_0300_getTempFirstNodeStateByIdUsingGET(self):
        """
        接口名称：根据模板ID获取项目模板的第一个节点状态
        接口地址：/proj/$VERSION$/{type}/state/firststate
        """
        ApiProject.getTempFirstNodeStateByIdUsingGET(self,
                                                     type="ELProject"
                                                     )

    def test_0310_addProjectMyOpenUsingPOST(self):
        """
        接口名称：添加项目查看记录（用于导航栏查看项目）
        接口地址：/proj/$VERSION$/addProjectMyOpen/{project_id}
        """
        ApiProject.addProjectMyOpenUsingPOST(self,
                                             project_id=Project.project_id
                                             )

    def test_0320_updateChildrenLinkUsingPUT(self):
        """
        接口名称：根据项目ID、子项目ID串更新项目父子关系
        接口地址：/proj/$VERSION$/projects/{id}/children
        """
        ApiProject.updateChildrenLinkUsingPUT(self,
                                              projectsId=db.project_id,
                                              childrenIds=Project.project_id
                                              )

    def test_0330_businessTableUsingPOST_2(self):
        """
        接口名称：查询业务表格列
        接口地址：/proj/$VERSION$/{viewid}/businessTable
        """
        ApiProject.businessTableUsingPOST_2(self,
                                            viewid=db.viewid_id
                                            )

    # def test_0200_getIsFileProjectUsingGET(self):
    #     """
    #     获取归档项目
    #     """
    #     # /proj/$VERSION$/projects/archived
    #     getIsFileProjectUsingGET = ApiProject.getIsFileProjectUsingGET(self)
    #     print(getIsFileProjectUsingGET)
    #
    # def test_0300_getAllProjectListUsingGET(self):
    #     """
    #     获取所有项目详细信息列表
    #     """
    #     # /proj/$VERSION$/projects/all
    #     getAllProjectListUsingGET = ApiProject.getAllProjectListUsingGET(self)
    #     print(getAllProjectListUsingGET)
    #
    # def test_0400_getMyAdministrationProjectUsingGET(self):
    #     """
    #     获取我最近打开的项目
    #     """
    #     # /proj/$VERSION$/getMyAdministrationProject
    #     getMyAdministrationProjectUsingGET = ApiProject.getMyAdministrationProjectUsingGET(self)
    #     print(getMyAdministrationProjectUsingGET)
    #
    # def test_0500_getDelayTaskByproject_idUsingGET(self):
    #     """
    #     延误率(延误率=延误任务数/计划完成任务数)
    #     """
    #     # /proj/$VERSION$/project/{id}/delay
    #     getDelayTaskByproject_idUsingGET = ApiProject.getDelayTaskByproject_idUsingGET(self, project_id=Project.project_id)
    #     print(getDelayTaskByproject_idUsingGET)
    #

    #
    # def test_0700_getProjectTreeUsingGET(self):
    #     """
    #     根据项目id获取树形子孙项目详情数据
    #     """
    #     # /proj/$VERSION$/projects/{id}/tree
    #     getProjectTreeUsingGET = ApiProject.getProjectTreeUsingGET(self, project_id=Project.project_id)
    #     print(getProjectTreeUsingGET)
    #
    # def test_0800_getChildrenByIdUsingGET(self):
    #     """
    #     根据项目ID获取下一层子项目
    #     """
    #     # /proj/$VERSION$/project/{id}/children
    #     getChildrenByIdUsingGET = ApiProject.getChildrenByIdUsingGET(self, project_id=Project.project_id)
    #     print(getChildrenByIdUsingGET)
    #
    # def test_6900_exportTemplateUsingGET(self):
    #     """
    #     导出数据模板
    #     """
    #     # /proj/$VERSION$/project/export/template
    #     exportTemplateUsingGET = ApiProject.exportTemplateUsingGET(self)
    #     print(exportTemplateUsingGET)
    #
    def test_6901_exportProjectListUsingGET(self):
        """
        导出项目列表数据
        """
        # /proj/$VERSION$/project/export
        exportProjectListUsingGET = ApiProject.exportProjectListUsingGET(self, exprotList="type")
        print(exportProjectListUsingGET)

    def test_6902_projAppBasicConfigUsingGET(self):
        """
        接口名称：查询单个系统应用基础配置
        接口地址：/proj/$VERSION$/basic/config/one
        """
        r = ApiProject.projAppBasicConfigUsingGET(self,
                                                  project_id=Project.project_id
                                                  )
        print(r["res"]["data"][0]["id"])
        Project.ABC_id = r["res"]["data"][0]["id"]

    def test_6903_pageProjAppBasicConfigUsingGET(self):
        """
        接口名称：分页查询系统应用基础配置
        接口地址：/proj/$VERSION$/basic/config/page
        """
        ApiProject.pageProjAppBasicConfigUsingGET(self)

    def test_6904_getProjectListByExtUsingPOST(self):
        """
        接口名称：根据当前用户查询项目信息列表支持扩展字段
        接口地址：/proj/$VERSION$/projects/ext
        """
        ApiProject.getProjectListByExtUsingPOST(self,
                                                viewDto={"name": "", "state": "", "type": "", "pmId": "",
                                                         "createBy": "", "archivedFlag": "", "sort_by": "",
                                                         "order_by": "", "pagesize": "20", "pageindex": "1",
                                                         "contextType": "", "elConditionList": []}
                                                )

    def test_6905_getChangeMemberLogConfigUsingGET(self):
        """
        接口名称：根据项目ID查询更换成员的配置
        接口地址：/proj/$VERSION$/changeMemberLogConfig/{project_id}
        """
        ApiProject.getChangeMemberLogConfigUsingGET(self,
                                                    project_id=Project.project_id
                                                    )

    def test_6906_getProjectByNameOrCodePageUsingGET(self):
        """
        接口名称：根据项目名称或编码查询项目详情列表
        接口地址：/proj/$VERSION$/project/{id}/keyword
        """
        ApiProject.getProjectByNameOrCodePageUsingGET(self,
                                                      project_id=Project.project_id,
                                                      hasParent="0",
                                                      keyword="",
                                                      page_index="1",
                                                      page_size="50"
                                                      )

    def test_6907_updateApplicationConfigUsingPUT(self):
        """
        接口名称：修改系统应用配置
        接口地址：/proj/$VERSION$/basic/config/{project_id}/update
        """
        ApiProject.updateApplicationConfigUsingPUT(self,
                                                   project_id=Project.project_id,
                                                   basicConfig={"id": Project.ABC_id,
                                                                "createBy": Project.user_id,
                                                                "createTime": "2020-05-19 16:20:51",
                                                                "updateBy": "SYS_E39B20EA11E7A81AC85B767C89C1",
                                                                "updateTime": time.strftime('%Y-%m-%d',
                                                                                            time.localtime()),
                                                                "delFlag": "0",
                                                                "name": "项目成员日志记录配置", "contextId": "all",
                                                                "config": "[{\"isRecord\":\"1\",\"type\":\"2\",\"value\":\"PROJECT_PUBLISH\"}]",
                                                                "type": "member", "description": "项目成员日志记录配置"}
                                                   )

    def test_7000_deleteProjectUsingDELETE(self):
        """
        删除项目
        """
        # /proj/$VERSION$/{id}
        deleteProjectUsingDELETE = ApiProject.deleteProjectUsingDELETE(self, project_id=Project.children_ids)
        print(deleteProjectUsingDELETE)


if __name__ == '__main__':
    unittest.main()

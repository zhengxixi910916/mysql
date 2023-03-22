# -*- coding: utf-8 -*-
# @Time    : 2022/2/21
# @Author  : zhihuimin

import unittest
from project.api import ApiReportItemInformation, ApiProject
from project.api import ApiProjectReportTemplate, ApiRequireManage, ApiProjectBasicInformationConfiguration, ApiProjectFolder
import time


class Project(unittest.TestCase):
    project_id = ""
    user_id = "025CE39B20EA11E7A81AC85B767C89C1"
    org_id = "69a12d9d163fec76d208e957289d0c53"
    require_name = ''
    projectreport_id = ''
    uu_id = ""
    template_id = ''
    context_type = ''
    folder_id = ''
    task_patternid = ""
    requirement_patternid = ""
    issue_patternid = ""
    risk_patternid = ""
    project_patternid = ""

    def test_0100_get_projectreports(self):
        """
        接口名称：查询所有项目报表
        接口地址：/proj/$VERSION$/project/report/all
        """
        # 新增项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        addProjectUsingPOST_1 = ApiProject.addProjectUsingPOST_1(self, name=project_name,)
        print(addProjectUsingPOST_1)
        Project.project_id = addProjectUsingPOST_1.get("id")
        Project.context_type = addProjectUsingPOST_1.get("name")
        print("project_id:", Project.project_id)

        # 新增需求
        Project.require_name = "require_" + time.strftime('%H%M%S', time.localtime())
        require_description = Project.require_name
        submit_time = time.strftime('%Y-%m-%d', time.localtime())
        add_require_result = ApiRequireManage.add_require(self,
                                                          name=Project.require_name,
                                                          project_id=Project.project_id
                                                          )
        print(add_require_result)
        Project.require_id = add_require_result.get("id")
        print("requirement_id:", Project.require_id)

        # 查询所有项目报表
        get_projectreports = ApiReportItemInformation.getProjectReportsUsingGET(self,
                                                                                project_id=Project.project_id,
                                                                                )
        print(get_projectreports)

    def test_0200_get_reportconfig(self):
        """
        接口名称：获取报表配置数据
        接口地址：/proj/$VERSION$/project/report/config
        """
        get_reportconfig = ApiReportItemInformation.getReportConfigUsingGET(self)
        print(get_reportconfig)

    def test_0300_show_report(self):
        """
        接口名称：查看项目自定义报表
        接口地址：/proj/$VERSION$/project/report
        """
        show_report = ApiReportItemInformation.showReportUsingGET(self,
                                                                  project_id=Project.project_id)
        print(show_report)

    def test_0400_add_projectreport(self):
        """
        接口名称：保存项目报表基本信息
        接口地址：/proj/$VERSION$/project/report
        """
        add_projectreport = ApiReportItemInformation.addProjectReportUsingPOST(self,
                                                                               project_id=Project.project_id)
        print(add_projectreport)
        Project.projectreport_id = add_projectreport.get("id")
        print(Project.projectreport_id)

    def test_0500_update_projectreport(self):
        """
        接口名称：修改项目报表
        接口地址：/proj/$VERSION$/project/report/{id}
        """
        update_projectreport = ApiReportItemInformation.updateProjectReportUsingPUT(self,
                                                                                    projectreport_id=Project.projectreport_id,
                                                                                    project_id=Project.project_id)

    def test_0600_get_singleprojectreport(self):
        """
        接口名称：根据ID查询单个项目报表
        接口地址：/proj/$VERSION$/project/report/{id}
        """
        get_singleprojectreport = ApiReportItemInformation.getSingleProjectReportUsingGET(self,
                                                                                          projectreport_id=Project.projectreport_id)

    def test_0700_delete_projectreport(self):
        """
        接口名称：删除项目报表
        接口地址：/proj/$VERSION$/project/report/{id}
        """
        delete_projectreport = ApiReportItemInformation.deleteProjectReportUsingDELETE(self,
                                                                                       projectreport_id=Project.projectreport_id)

    def test_0800_get_uuid(self):
        """
        接口名称：获取UUID
        接口地址：/rpt/$VERSION$/uuid
        """
        get_uuid = ApiProjectReportTemplate.getUuIdUsingGET(self)
        print(get_uuid)
        Project.uu_id = get_uuid[-1]

    def test_0900_add_template(self):
        """
        接口名称：创建项目报告模板
        接口地址：/rpt/$VERSION$/template
        """
        add_template = ApiProjectReportTemplate.addTemplateUsingPOST(self,
                                                                     uu_id=Project.uu_id,
                                                                     project_id=Project.project_id)

    def test_1000_get_templates(self):
        """
        接口名称：获取项目报告模板分页列表
        接口地址：/rpt/$VERSION$/templates
        """
        get_templates = ApiProjectReportTemplate.getTemplatesUsingGET(self,
                                                                      project_id=Project.project_id)
        print(get_templates)
        Project.template_id = get_templates[0]['id']

    def test_1100_get_template(self):
        """
        接口名称：获取项目报告模板信息
        接口地址：/rpt/$VERSION$/template/{id}
        """
        get_template = ApiProjectReportTemplate.getTemplateUsingGET(self,
                                                                    template_id=Project.template_id)

    def test_1200_update_template(self):
        """
        接口名称：更新项目报告模板
        接口地址：/rpt/$VERSION$/template/{id}
        """
        update_template = ApiProjectReportTemplate.updateTemplateUsingPUT(self,
                                                                          template_id=Project.template_id,
                                                                          project_id=Project.project_id)

    def test_1300_del_template(self):
        """
        接口名称：删除项目报告模板,支持多个删除
        接口地址：/rpt/$VERSION$/template
        """
        del_template = ApiProjectReportTemplate.delTemplateUsingDELETE(self,
                                                                       template_id=Project.template_id)

    def test_1400_create_folder(self):
        """
        接口名称：创建文件夹
        接口地址：/proj/$VERSION$/doc/folder
        """
        create_folder = ApiProjectFolder.createFolderUsingPOST(self,
                                                               context_id=Project.project_id,
                                                               context_type=Project.context_type,
                                                               parent_id=Project.project_id)
        print(create_folder)
        Project.folder_id = create_folder.get('id')

    def test_1500_update_folder(self):
        """
        接口名称：修改文件夹
        接口地址：/proj/$VERSION$/doc/folder/{id}
        """
        update_folder = ApiProjectFolder.updateFolderUsingPUT(self,
                                                              folder_id=Project.folder_id)

    def test_1600_folder_teelist(self):
        """
        接口名称：根据根节点获取文件夹树
        接口地址：/proj/$VERSION$/doc/folder/tree
        """
        folder_teelist = ApiProjectFolder.folderTeeListUsingGET(self,
                                                                tree_id=Project.project_id)

    def test_1700_folder_isnull(self):
        """
        接口名称：根据ID判断文件夹是否为空
        接口地址：/proj/$VERSION$/doc/folder/{id}/isnull
        """
        folder_isnull = ApiProjectFolder.folderIsNullUsingGET(self,
                                                              folder_id=Project.folder_id)

    def test_1800_folderTeeAllListUsingGET(self):
        """
        接口名称：根据父ID查询子文件夹
        接口地址：/proj/$VERSION$/doc/folder/{parentid}/children
        """
        ApiProjectFolder.folderTeeAllListUsingGET(self,
                                                  parentid=Project.folder_id
                                                  )

    def test_1900_delete_folder(self):
        """
        接口名称：根据ID删除文件夹
        接口地址：/proj/$VERSION$/doc/folder/{id}
        """
        delete_folder = ApiProjectFolder.deleteFolderUsingDELETE(self,
                                                                 folder_id=Project.folder_id)

    def test_2000_show_noticeconfig(self):
        """
        接口名称：显示基础配置信息
        接口地址：/proj/$VERSION$/notice/get
        """
        show_noticeconfig = ApiProjectBasicInformationConfiguration.showNoticeConfigUsingPOST(self,
                                                                                              project_id=Project.project_id)
        print(show_noticeconfig)
        for one in show_noticeconfig:
            if one["notiType"] == "ELTask":
                Project.task_patternid = one["patternId"]
                print(Project.task_patternid)
            if one["notiType"] == "ELRisk":
                Project.risk_patternid = one["patternId"]
                print(Project.risk_patternid)
            if one["notiType"] == "ELProject":
                Project.project_patternid = one["patternId"]
                print(Project.project_patternid)
            if one["notiType"] == "ELIssue":
                Project.issue_patternid = one["patternId"]
                print(Project.issue_patternid)
            if one["notiType"] == "ELRequirement":
                Project.requirement_patternid = one["patternId"]
                print(Project.requirement_patternid)

    def test_2100_add_noticeconfig(self):
        """
        接口名称：配置基础信息
        接口地址：/proj/$VERSION$/notice/{project_id}/add
        """
        add_noticeconfig = ApiProjectBasicInformationConfiguration.addNoticeConfigUsingPUT(self,
                                                                                           project_id=Project.project_id,
                                                                                           task_patternid=Project.task_patternid,
                                                                                           requirement_patternid=Project.requirement_patternid,
                                                                                           issue_patternid=Project.issue_patternid,
                                                                                           risk_patternid=Project.risk_patternid,
                                                                                           project_patternid=Project.project_patternid)
        print(add_noticeconfig)

        # 删除项目
        deleteProject = ApiProject.deleteProjectUsingDELETE(self, project_id=Project.project_id)


if __name__ == '__main__':
    unittest.main()

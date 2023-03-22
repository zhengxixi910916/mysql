import unittest, time
from project.api import ApiProjectTemplate,ApiProject
from project.case.file.runSql import db


class ProjectTemplate(unittest.TestCase):
    """项目模板"""
    TemplateId = ""
    project_id = ""
    user_id = db.user_id
    org_id = db.org_id
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_allTemplatesUsingGET(self):
        """
        接口名称：查询所有的模板
        接口地址：/proj/$VERSION$/alltemplates
        """
        ApiProjectTemplate.allTemplatesUsingGET(self)

    # def test_0200_mytemplatesUsingGET(self):
    #     """
    #     接口名称：查询所有我创建的模板
    #     接口地址：/proj/$VERSION$/mytemplates
    #     """
    def test_0300_addProjectTemplateUsingPOST(self):
        """
        接口名称：保存项目模板基本信息并根据配置表和项目类型生成相应计划类型
        接口地址：/proj/$VERSION$/template
        """
        # 新增项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        r1 = ApiProject.addProjectUsingPOST_1(self, name=project_name)

        ProjectTemplate.project_id = r1["id"]
        r2 = ApiProjectTemplate.addProjectTemplateUsingPOST(self, description="2222", project_id=ProjectTemplate.project_id, name="test_" + time.strftime('%Y-%m-%d %H%M%S'))

        ProjectTemplate.TemplateId = r2["id"]


    def test_0400_getAllProjecTemplatetListUsingGET(self):
        """
        接口名称：获取所有项目模板详细信息列表
        接口地址：/proj/$VERSION$/projects/all/template
        """
        r = ApiProjectTemplate.getAllProjecTemplatetListUsingGET(self,
                                                                 project_id=ProjectTemplate.project_id,
                                                                 type=""
                                                                 )



    def test_0500_replaceProjectTemplateUsingPOST(self):
        """
        接口名称：替换项目模板内容
        接口地址：/proj/$VERSION$/template/information/{project_id}
        """
        ApiProjectTemplate.replaceProjectTemplateUsingPOST(self,
                                                           project_id=ProjectTemplate.project_id,
                                                           description="test",
                                                           items="plan,projectRole,risk,folder",
                                                           )

    def test_0600_getProjectTemplateListUsingGET(self):
        """
        接口名称：项目模板列表接口
        接口地址：/proj/$VERSION$/template/list
        """
        ApiProjectTemplate.getProjectTemplateListUsingGET(self,
                                                          createBy="",
                                                          name="",
                                                          order_by="",
                                                          page_index="1",
                                                          page_size="20",
                                                          pmId="",
                                                          sort_by="",
                                                          type=""
                                                          )

    def test_0601_updateDefaultTemplateUsingPUT(self):
        """
        接口名称：更新项目默认模板
        接口地址：/proj/$VERSION$/project/defaultTemplate
        """
        ApiProjectTemplate.updateDefaultTemplateUsingPUT(self,
                                                         project={"departmentId": "281fa3c6e91b46d1bb7f961081376e7b",
                                                                  "description": "项目模板",
                                                                  "finishTime": "2019-04-30 00:00:00",
                                                                  "startTime": "2017-11-04 00:00:00",
                                                                  "id": "2916d30f05b94248b0e620002b44e3fd",
                                                                  "name": "机械产品开发项目模板",
                                                                  "pmId": "025CE39B20EA11E7A81AC85B767C89C1",
                                                                  "templateId": "1badffd2087d4af29031b729c7997fae",
                                                                  "type": "STANDARD",
                                                                  "isDefaultTemplate": "1"}
                                                         )

    def test_0700_deleteTemplateUsingDELETE(self):
        """
        接口名称：删除项目模板
        接口地址：/proj/$VERSION$/template/{id}
        """
        ApiProjectTemplate.deleteTemplateUsingDELETE(self,
                                                     id=ProjectTemplate.TemplateId
                                                     )


if __name__ == '__main__':
    unittest.main()

import unittest
from project.api import ApiProjectRole, ApiProject
from project.case.file.runSql import db
import time

class ProjectRole(unittest.TestCase):
    """项目角色"""
    new_project_id = db.project_id
    old_project_id = ''
    userId = db.user_id

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    # def test_0100
    # “”“高级查询角色树”“”     找不到这个接口

    def test_0200_copyProjectMembersRolesUsingGET(self):
        """根据项目ID复制人员角色"""
        # 新增项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        r = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        ProjectRole.old_project_id = r['id']
        ApiProjectRole.copyProjectMembersRolesUsingGET(self,
                                                       oldproject_id=ProjectRole.old_project_id,  # 这是旧的项目id
                                                       newproject_id=ProjectRole.new_project_id)  # 这是插入的新的项目id

        # def test_0300_deleteMemberRolesUsingDELETE(self):
        #     """删除当前项目下所有成员和角色"""
        #     ApiProjectRole.deleteMemberRolesUsingDELETE(self,
        #                                                 memberIds=["ba3cf49f42fadf61489dfd62d1d4e839","10a4048d3f421caa809095a13f241da2"],  # 这是角色id
        #                                                 project_id=db.project_id
        #                                                 )

    def test_0400_addProjectRoleUsingPOST(self):
        """新增项目角色"""
        ApiProjectRole.addProjectRoleUsingPOST(self,
                                               isKeyMember="1",
                                               objectId=ProjectRole.new_project_id,  # 这个id是对象标识
                                               roleKey="FR")

    def test_0500_editProjectRoleUsingPUT(self):
        """修改项目角色"""
        ApiProjectRole.editProjectRoleUsingPUT(self,
                                               isKeyMember="0",
                                               objectId=ProjectRole.new_project_id,  # 这个id是对象标识
                                               roleKey="PRODUCTION"
                                               )

    def test_0600_delProjectRoleUsingDELETE(self):
        """删除项目角色"""
        ApiProjectRole.delProjectRoleUsingDELETE(self,
                                                 HE="HE",
                                                 project_id=ProjectRole.new_project_id
                                                 )

    def test_0700_getProjectRoleMembersUsingGET(self):
        """查询当前项目角色下的项目成员"""
        ApiProjectRole.getProjectRoleMembersUsingGET(self,
                                                     roleKey="TE",
                                                     orderBy="joinTime",
                                                     project_id=ProjectRole.new_project_id,
                                                     sortBy="ASC",
                                                     page_size="10",
                                                     page_index="1"
                                                     )

    # def test_0800_(self):
    # """删除项目角色成员"""
    # 接口未找到

    def test_0900_SelectProjectRoleMembersUsingGET(self):
        """查询当前项目下所有成员和角色"""
        ApiProjectRole.SelectProjectRoleMembersUsingGET(self,
                                                        project_id=ProjectRole.new_project_id)

    # def test_1000(self):
    # """修改项目成员角色"""
    # 接口未找到

    def test_1100_addProjectRoleMemberUsingPUT(self):
        """新增项目角色成员"""
        ApiProjectRole.addProjectRoleMemberUsingPUT(self,
                                                    project_id=ProjectRole.new_project_id,
                                                    userId=ProjectRole.userId,
                                                    roleKey="FR"
                                                    )

    def test_1200_getProjectRoleTreeUsingGET(self):
        ApiProjectRole.getProjectRoleTreeUsingGET(self,
                                                  project_id=ProjectRole.new_project_id
                                                  )

    def test_1300_getProjectRoleUsingGET(self):
        """查询系统配置的项目角色"""
        ApiProjectRole.getProjectRoleUsingGET(self,
                                              project_id=ProjectRole.new_project_id
                                              )

    def test_7000_deleteProjectUsingDELETE(self):
        """
        删除项目
        """
        # /proj/$VERSION$/{id}
        r = ApiProject.deleteProjectUsingDELETE(self, project_id=ProjectRole.old_project_id)


if __name__ == '__main__':
    unittest.main()

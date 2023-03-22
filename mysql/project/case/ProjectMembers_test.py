import unittest

from project.api import ApiProjectMembers, ApiProject,ApiProjectRole
from project.case.file.runSql import db
import time

class ProjectMenbers(unittest.TestCase):
    """项目成员"""

    project_id = ''
    role_id = ''

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass

        pass

    def test_0100_addMembersUsingPUT(self):
        """
        接口名称：添加项目成员
        接口地址：/proj/$VERSION$/project/{id}/role/members
        """
        # 新增项目
        # /proj/$VERSION$/project
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        r = ApiProject.addProjectUsingPOST_1(self, name=project_name)
        print(r)
        ProjectMenbers.project_id = r['id']
        ApiProjectMembers.addMembersUsingPUT(self, project_id=ProjectMenbers.project_id, roleKey='Member')

    def test_0200_replaceMemberUsingGET(self):
        """
        接口名称：替换项目成员
        接口地址：/proj/$VERSION$/project/replace/member
        """
        # 新增项目角色
        r = ApiProjectRole.addProjectRoleUsingPOST(self,
                                               isKeyMember="1",
                                               objectId=ProjectMenbers.project_id,  # 这个id是对象标识
                                               roleKey="FR")
        ProjectMenbers.role_id = r['data']['id']

        ApiProjectMembers.replaceMemberUsingGET(self,
                                                id=ProjectMenbers.role_id,  # 角色id
                                                newMemberId=db.user_id,
                                                )

    def test_7000_deleteProjectUsingDELETE(self):
        """
        删除项目
        """
        # /proj/$VERSION$/{id}
        r = ApiProject.deleteProjectUsingDELETE(self, project_id=ProjectMenbers.project_id)



if __name__ == '__main__':
    unittest.main()

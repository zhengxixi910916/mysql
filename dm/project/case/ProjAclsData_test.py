# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 17:00
# @Author  : Liao

import unittest
from project.api import ApiProjAclsData
from project.case.file.runSql import db


class ProjAclsData(unittest.TestCase):
    """项目权限信息"""

    user_id = db.user_id

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_get_proj_acl_system_role(self):
        """
        获取用户系统角色 对项目的操作权限
        """
        # /proj/v1/acl/sys
        proj_sys = ApiProjAclsData.get_proj_acl_system_role(self)
        print(proj_sys)

    def test_0200_get_all_acl_system_roles(self):
        """
        获取用户系统角色 对所有对象的操作权限
        """
        # /proj/v1/acls/sys
        all_sys = ApiProjAclsData.get_all_acl_system_roles(self)
        print(ProjAclsData.user_id)
        print(all_sys)

    def test_0300_get_obj_acl_proj_role(self):
        """
        获取用户项目角色 对对象的操作权限
        """
        # /proj/v1/{id}/acl
        obj_type = "ELTask"
        obj_proj = ApiProjAclsData.get_obj_acl_proj_role(self, ProjAclsData.user_id, obj_type)
        print(obj_proj)

    def test_0400_get_all_acl_proj_roles(self):
        """
        获取用户项目角色 所有对象的操作权限
        """
        # /proj/v1/{id}/acls
        all_proj = ApiProjAclsData.get_all_acl_proj_roles(self, ProjAclsData.user_id)
        print(all_proj)


if __name__ == '__main__':
    unittest.main()

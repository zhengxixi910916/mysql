# -*- coding: utf-8 -*-#
# Author: YANGJIONG
# Date:   2022/7/5

import unittest
from project.api import ApiProjectTemplate, ApiDataAuthorizationManagement, ApiProject, ApiProjectRole
import time
from project.case.file.runSql import db

class DataAuthorizationManagement(unittest.TestCase):
    user_id = db.user_id
    org_id = db.org_id
    project_id = db.project_id
    template_id = ''
    aci_list = ''
    judge_creat_project = False

    def test_0100_get_object_acls_using_get(self):
        """
        接口名称：根据用户id或者角色id获取授权列表
        接口地址：/proj/$VERSION$/acl/list
        """
        aci_list = ApiDataAuthorizationManagement.get_object_acls_using_get(self,
                                                                            template_id=DataAuthorizationManagement.template_id)
        DataAuthorizationManagement.aci_list = aci_list['res']['data']

    def test_0200_create_object_acl_using_post(self):
        """
        接口名称：新增权限（授权）
        接口地址：/proj/$VERSION$/acl
        """

        # 设置项目为模板
        ApiProjectTemplate.addProjectTemplateUsingPOST(self,
                                                       description="2222",
                                                       project_id=DataAuthorizationManagement.project_id,
                                                       name="DataAuthorizationManagement_" + time.strftime(
                                                           '%Y-%m-%d %H%M%S')
                                                       )

        while True:
            # 访问项目模板列表
            template_list = ApiProjectTemplate.getProjectTemplateListUsingGET(self,
                                                                              createBy="",
                                                                              name="",
                                                                              order_by="",
                                                                              page_index="1",
                                                                              page_size="20",
                                                                              pmId="",
                                                                              sort_by="",
                                                                              type=""
                                                                              )
            try:
                DataAuthorizationManagement.template_id = template_list['records'][0]['id']
                break
            except Exception as e:
                print(e)
                DataAuthorizationManagement.judge_creat_project = True

        # 新增项目角色
        ApiProjectRole.addProjectRoleUsingPOST(self,
                                               objectId=DataAuthorizationManagement.template_id,
                                               roleKey='MARKETING',
                                               isKeyMember=1)

        # 新增权限
        ApiDataAuthorizationManagement.create_object_acl_using_post(self,
                                                                    template_id=DataAuthorizationManagement.template_id)

    def test_0300_update_object_acl_using_put(self):
        """
        接口名称：修改权限（授权）
        接口地址：/proj/$VERSION$/acl
        """
        ApiDataAuthorizationManagement.update_object_acl_using_put(self,
                                                                   template_id=DataAuthorizationManagement.template_id,
                                                                   acl_list=DataAuthorizationManagement.aci_list
                                                                   )

    def test_0400_del_object_acl_using_delete(self):
        """
        接口名称：删除权限（授权）
        接口地址：/proj/$VERSION$/acl
        """
        ApiProjectRole.delProjectRoleUsingDELETE(self,
                                                 project_id=DataAuthorizationManagement.project_id,
                                                 HE='MARKETING')
        ApiDataAuthorizationManagement.del_object_acl_using_delete(self,
                                                                   template_id=DataAuthorizationManagement.template_id)


    @unittest.skip('单个执行通过，批量执行报错')
    def test_0500_ac_user_using_get(self):
        """
        接口名称：统一获取用户信息，包括基本信息、角色信息、权限信息
        接口地址：/proj/$VERSION$/user/me
        """
        ApiDataAuthorizationManagement.ac_user_using_get(self)


if __name__ == '__main__':
    unittest.main()

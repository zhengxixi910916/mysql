# -*- coding: utf-8 -*-
# @Time    : 2022/02/18
# @Author  : Chen

import unittest
from project.api import ApiDocumentDataPermissions
from project.case.file.runSql import db


class DocumentDataPermissions(unittest.TestCase):
    """项目文档数据权限接口"""
    objectId = db.object_id

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_getUserAclsUsingGET(self):
        """
        接口名称：获取当前用户的数据操作权限
        接口地址：/proj/$VERSION$/doc/user/{objectId}/acls
        """
        ApiDocumentDataPermissions.getUserAclsUsingGET(self,
                                                       project_id=db.document_id,
                                                       type="ELFolder"  # ELFolder文件夹  ELDocument文档
                                                       )

    def test_0200_getAclsUsingGET(self):
        """
        接口名称：获取数据操作权限
        接口地址：/proj/$VERSION$/doc/{objectId}/acls
        """
        ApiDocumentDataPermissions.getAclsUsingGET(self,
                                                   objectId=db.document_id,
                                                   type="ELFolder"  # ELFolder文件夹  ELDocument文档
                                                   )


    def test_0300_setAclUsingPOST(self):
        """
        接口名称：设置数据操作权限
        接口地址：/proj/$VERSION$/doc/{objectId}/acls
        """
        ApiDocumentDataPermissions.setAclUsingPOST(self,
                                                   objectId=db.document_id,
                                                   type="ELFolder",
                                                   accessLimit0="0",
                                                   accessType0="+",
                                                   contextId0=db.document_id,
                                                   contextType0="ELFolder",
                                                   objectId0="ALL",
                                                   objectState0="ALL",
                                                   objectType0="ELDocument",
                                                   principalId0="PM",
                                                   principalType0="role",
                                                   accessLimit1="0",
                                                   accessType1="+",
                                                   contextId1=db.document_id,
                                                   contextType1="ELFolder",
                                                   objectId1="ALL",
                                                   objectState1="ALL",
                                                   objectType1="ELDocument",
                                                   principalId1="MEMBER",
                                                   principalType1="role",
                                                   )




if __name__ == '__main__':
    unittest.main()

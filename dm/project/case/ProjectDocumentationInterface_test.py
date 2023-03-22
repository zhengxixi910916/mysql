# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/3/8

import unittest
from project.api import ApiProjectDocumentationInterface
from project.case.file.runSql import db


class ProjectDocuments(unittest.TestCase):
    """项目文档接口"""
    doc_id = ''
    file_id = ''
    folder_id = ''
    project_id = db.project_id
    project_name = db.project_name

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass

    def test_0100_search_list(self):
        """
        接口名称：项目文档搜索分页
        接口地址：/proj/$VERSION$/doc/searchlist
        """
        ApiProjectDocumentationInterface.search_list(self,
                                                     context_id=ProjectDocuments.project_id,
                                                     page_no=1,
                                                     page_size=10,
                                                     name="",
                                                     order="ASC",
                                                     order_by_field="title"
                                                     )

    def test_0200_page(self):
        """
        接口名称：查询文档分页
        接口地址：/proj/$VERSION$/doc/list
        """
        ApiProjectDocumentationInterface.page(self,
                                              context_id=ProjectDocuments.project_id,
                                              page_size=10,
                                              page_no=1,
                                              name="",
                                              folder_id="",
                                              order="ASC",
                                              order_by_field="title"
                                              )

    def test_0300_query_attlist(self):
        """
        接口名称：查询历史版本文件list
        接口地址：/proj/$VERSION$/doc/{cid}/list
        """
        ApiProjectDocumentationInterface.query_attlist(self,
                                                       cid=ProjectDocuments.project_id)

    def test_0400_create_doc(self):
        """
        接口名称：创建文档
        接口地址：/proj/$VERSION$/doc/doc
        """
        create_doc = ApiProjectDocumentationInterface.create_doc(self,
                                                                 context_id=ProjectDocuments.project_id,
                                                                 context_type=ProjectDocuments.project_name)

        ProjectDocuments.doc_id = create_doc['id']

    def test_0500_upload_attach(self):
        """
        接口名称：上传文件，支持批量
        接口地址：/proj/$VERSION$/doc/upload
        """
        upload_attach = ApiProjectDocumentationInterface.upload_attach(self,
                                                                       doc_id=ProjectDocuments.doc_id)
        print(upload_attach)

    def test_0600_create_attach_doc(self):
        """
        接口名称：批量创建文档
        接口地址：/proj/$VERSION$/doc/docs
        """
        ApiProjectDocumentationInterface.create_attach_doc(self,
                                                           context_id=ProjectDocuments.project_id,
                                                           folder_id=ProjectDocuments.project_id)

    def test_0700_doc_detail(self):
        """
        接口名称：查询文档详情
        接口地址：/proj/$VERSION$/doc/doc/{id}
        """
        doc_detail = ApiProjectDocumentationInterface.doc_detail(self,
                                                                 doc_id=ProjectDocuments.doc_id)
        print(doc_detail)
        ProjectDocuments.file_id = doc_detail.get('fileDataId')
        print(ProjectDocuments.file_id)

    def test_0800_history_doc_detail(self):
        """
        接口名称：查询历史文档详情
        接口地址：/proj/$VERSION$/doc/doc/{id}/history
        """
        history_doc_detail = ApiProjectDocumentationInterface.history_doc_detail(self,
                                                                                 doc_id=ProjectDocuments.doc_id
                                                                                 )
        print(history_doc_detail)

    def test_0900_update_doc(self):
        """
        接口名称：修改文档
        接口地址：/proj/$VERSION$/doc/doc/{id}
        """
        ApiProjectDocumentationInterface.update_doc(self,
                                                    doc_id=ProjectDocuments.doc_id,
                                                    folder_id=ProjectDocuments.project_id
                                                    )

    def test_1000_doc_history_list(self):
        """
        接口名称：根据文档id查询该文档历史记录
        接口地址：/proj/$VERSION$/doc/{id}/histories
        """
        ApiProjectDocumentationInterface.doc_history_list(self,
                                                          doc_id=ProjectDocuments.doc_id)

    def test_1100_move_document(self):
        """
        接口名称：移动文件夹（文档）
        接口地址：/proj/$VERSION$/doc/move
        """
        ApiProjectDocumentationInterface.move_document(self,
                                                       df_id=ProjectDocuments.doc_id,
                                                       folder_id=ProjectDocuments.project_id)

    """
    可能是创建文档时上传附件未成功，故获取不到文件ID
    """
    @unittest.skip('暂时跳过')
    def test_1500_upload_cover_attach(self):
        """
        接口名称：修改文件
        接口地址：/proj/$VERSION$/doc/upload/cover
        """

        upload_cover_attach = ApiProjectDocumentationInterface.upload_cover_attach(self,
                                                                                   doc_id=ProjectDocuments.doc_id,
                                                                                   file_id=ProjectDocuments.file_id)
        print(upload_cover_attach)

    @unittest.skip('暂时跳过')
    def test_1600_delete_attach(self):
        """
        接口名称：删除文件附件
        接口地址：/proj/$VERSION$/doc/doc/{docid}/{fid}
        """
        ApiProjectDocumentationInterface.delete_attach(self,
                                                       doc_id=ProjectDocuments.doc_id,
                                                       file_id=ProjectDocuments.file_id)

    def test_1700_delete_doc(self):
        """
        接口名称：删除文档
        接口地址：/proj/$VERSION$/doc/doc/{id}
        """
        ApiProjectDocumentationInterface.delete_doc(self,
                                                    doc_id=ProjectDocuments.doc_id)


if __name__ == '__main__':
    unittest.TestCase()

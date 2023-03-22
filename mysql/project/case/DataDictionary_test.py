# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/3/3

import unittest
import time
from project.api import ApiProject
from project.api import ApiDataDictionary
from project.case.file.runSql import db


class DataDictionary(unittest.TestCase):
    """数据字典"""
    dictionary_id1 = ""
    dictionary_id2 = ""

    @classmethod
    def setUpClass(cls):
        pass

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     db.delete_sql()

    def test_0100_createUsingPOST_1(self):
        """
        接口名称：新增字典定义
        接口地址：/proj/$VERSION$/dictionary
        """
        r1 = ApiDataDictionary.createUsingPOST_1(self,
                                                 typeName="ResourcePackage",
                                                 attribute="active",
                                                 parentId="",
                                                 value="test" + time.strftime("%H%M%S", time.localtime()),
                                                 sort="0",
                                                 displayCn="test" + time.strftime("%H%M%S", time.localtime()),
                                                 displayEn="test" + time.strftime("%H%M%S", time.localtime()),
                                                 description="test" + time.strftime("%H%M%S", time.localtime()),
                                                 contextType="Project",
                                                 contextId=db.project_id,
                                                 name="ResourcePackage_active"
                                                 )
        r2 = ApiDataDictionary.createUsingPOST_1(self,
                                                 typeName="ResourcePackage",
                                                 attribute="active",
                                                 parentId="",
                                                 value="test_" + time.strftime("%H%M%S", time.localtime()),
                                                 sort="0",
                                                 displayCn="test_" + time.strftime("%H%M%S", time.localtime()),
                                                 displayEn="test_" + time.strftime("%H%M%S", time.localtime()),
                                                 description="test_" + time.strftime("%H%M%S", time.localtime()),
                                                 contextType="Project",
                                                 contextId=db.project_id,
                                                 name="ResourcePackage_active"
                                                 )

    def test_0200_importDictionaryUsingPOST(self):
        """
        接口名称：导入项目数据字典
        接口地址：/proj/$VERSION$/dictionary/import
        """
        # 新增项目
        project_name = "project_" + time.strftime('%Y%m%d', time.localtime())
        r1 = ApiProject.addProjectUsingPOST_1(self,
                                              name=project_name)
        print(r1)
        project_id = r1["id"]

        # 导入项目数据字典
        ApiDataDictionary.importDictionaryUsingPOST(self,
                                                    contextType="Project",
                                                    contextId=project_id,
                                                    typeName="agenda",
                                                    attribute=""
                                                    )

        # 删除项目

        deleteProjectUsingDELETE = ApiProject.deleteProjectUsingDELETE(self,
                                                                       project_id=project_id
                                                                       )
        print(deleteProjectUsingDELETE)

    def test_0300_queryListUsingGET(self):
        """
        接口名称：获取字典列表数据-分页
        接口地址：/proj/$VERSION$/dictionarys
        """
        ApiDataDictionary.queryListUsingGET(self,
                                            page_size="20",
                                            page_index="1",
                                            contextType="Project",
                                            contextId=db.project_id
                                            )

    def test_0400_selectListUsingGET(self):
        """
        接口名称：获取字典列表数据,根据context相关参数规则获取
        接口地址：/proj/$VERSION$/dictionarys/context
        """
        r = ApiDataDictionary.selectListUsingGET(self,
                                                 contextType="Project",
                                                 contextId=db.project_id
                                                 )
        print(r["res"]["data"])
        DataDictionary.dictionary_id1 = r["res"]["data"][0]["id"]
        print("DataDictionary.dictionary_id1 =", r["res"]["data"][0]["id"])
        DataDictionary.dictionary_id2 = r["res"]["data"][-1]["id"]
        print("DataDictionary.dictionary_id2 =", r["res"]["data"][-1]["id"])

    def test_0401_getUsingGET(self):
        """
        接口名称：获取字典详情
        接口地址：/proj/$VERSION$/dictionary/{id}
        """
        ApiDataDictionary.getUsingGET(self,
                                      id=DataDictionary.dictionary_id1
                                      )

    def test_0402_queryTypeListUsingGET(self):
        """
        接口名称：获取字典类型列表数据
        接口地址：/proj/$VERSION$/dictionary/types
        """
        ApiDataDictionary.queryTypeListUsingGET(self,
                                                contextId=db.project_id
                                                )

    def test_0403_updateUsingPUT_3(self):
        """
        接口名称：更新字典定义
        接口地址：/proj/$VERSION$/dictionary/{id}
        """
        ApiDataDictionary.updateUsingPUT_3(self,
                                           id=DataDictionary.dictionary_id1,
                                           dict={
                                               "id": DataDictionary.dictionary_id1,
                                               "parentId": "-1",
                                               "contextType": "Project",
                                               "contextId": db.project_id,
                                               "typeName": "ResourcePackage",
                                               "attribute": "active",
                                               "name": "ResourcePackage_active",
                                               "value": "1",
                                               "displayCn": "1",
                                               "displayEn": "1",
                                               "description": "",
                                               "sort": 0,
                                               "active": "0",
                                               "systemConfig": 0,
                                               "createTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                               "updateTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                               "delFlag": "0"
                                           }
                                           )

    def test_0500_deleteUsingDELETE_3(self):
        """
        接口名称：删除字典定义
        接口地址：/proj/$VERSION$/dictionary/{id}
        """
        ApiDataDictionary.deleteUsingDELETE_3(self,
                                              id=DataDictionary.dictionary_id1
                                              )

    def test_0600_deleteUsingDELETE_4(self):
        """
        接口名称：删除多个字典定义
        接口地址：/proj/$VERSION$/dictionary
        """
        ApiDataDictionary.deleteUsingDELETE_4(self,
                                              listIds=[DataDictionary.dictionary_id2]
                                              )


if __name__ == '__main__':
    unittest.TestCase()

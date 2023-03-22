# -*- coding: utf-8 -*-
# @Time    : 2022/02/22
# @Author  : Chen

import unittest, time, random
from project.api import ApiProductClassificationInformation
from project.case.file.runSql import db


class ProductClassificationInformation(unittest.TestCase):
    """产品分类信息"""
    CategoryId = ""
    CategoryName = ""
    CategoryCode = ""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_addProductCategoryUsingPOST(self):
        """
        接口名称：创建分类信息
        接口地址：/product/$VERSION$/category
        """
        r = ApiProductClassificationInformation.addProductCategoryUsingPOST(self,
                                                                            name=time.strftime("%Y%m%d %H%M%S"),
                                                                            categoryCode=random.randint(0, 9999999),
                                                                            majorType="",
                                                                            minorType="",
                                                                            description="test",
                                                                            parentId=""
                                                                            )
        print(r)
        ProductClassificationInformation.CategoryId = r["id"]
        print("ProductClassificationInformation.CategoryId:", ProductClassificationInformation.CategoryId)
        ProductClassificationInformation.CategoryName = r["name"]
        print("ProductClassificationInformation.CategoryName:", ProductClassificationInformation.CategoryName)
        ProductClassificationInformation.CategoryCode = r["categoryCode"]
        print("ProductClassificationInformation.CategoryCode:", ProductClassificationInformation.CategoryCode)

    def test_0200_updateProductCategoryUsingPUT(self):
        """
        接口名称：修改分类信息
        接口地址：/product/$VERSION$/category
        """
        ApiProductClassificationInformation.updateProductCategoryUsingPUT(self,
                                                                          category={
                                                                              "name": "大类1",
                                                                              "categoryCode": "",
                                                                              "majorType": "",
                                                                              "minorType": "null",
                                                                              "description": "",
                                                                              "flexAttrs": {},
                                                                              "id": ProductClassificationInformation.CategoryId,
                                                                              "parentId": ""
                                                                          }
                                                                          )

    def test_0300_getAllProductCategoryListUsingGET(self):
        """
        接口名称：查询所有产品分类信息
        接口地址：/product/$VERSION$/category/all
        """
        ApiProductClassificationInformation.getAllProductCategoryListUsingGET(self,
                                                                              )

    def test_0400_getAllMajorMinorsUsingGET(self):
        """
        接口名称：查询所有大类小类
        接口地址：/product/$VERSION$/category/all/majorminors
        """
        ApiProductClassificationInformation.getAllMajorMinorsUsingGET(self,
                                                                      )

    def test_0500_getProductCategoryUsingGET(self):
        """
        接口名称：查询单个分类信息
        接口地址：/product/$VERSION$/category/{id}
        """
        ApiProductClassificationInformation.getProductCategoryUsingGET(self,
                                                                       CategoryId=ProductClassificationInformation.CategoryId
                                                                       )

    def test_0600_getProductCategoryListUsingGET(self):
        """
        接口名称：查询多个分类信息
        接口地址：/product/$VERSION$/category/list
        """
        ApiProductClassificationInformation.getProductCategoryListUsingGET(self,
                                                                           code=ProductClassificationInformation.CategoryCode,
                                                                           name=ProductClassificationInformation.CategoryName
                                                                           )

    def test_0700_getNextLevelProductCategoryListUsingGET(self):
        ApiProductClassificationInformation.getNextLevelProductCategoryListUsingGET(self,
                                                                                    CategoryId=ProductClassificationInformation.CategoryId

                                                                                    )

    def test_0800_deleteProductCategoryUsingDELETE(self):
        """
        接口名称：删除分类信息
        接口地址：/product/$VERSION$/category/{id}
        """
        ApiProductClassificationInformation.deleteProductCategoryUsingDELETE(self,
                                                                             CategoryId=ProductClassificationInformation.CategoryId
                                                                             )


if __name__ == '__main__':
    unittest.main()

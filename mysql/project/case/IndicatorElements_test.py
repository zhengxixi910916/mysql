# -*- coding: utf-8 -*-
# @Time    : 2022/02/17
# @Author  : Chen

import unittest, time
from project.api import ApiIndicatorElements
from project.case.file.runSql import db


class IndicatorElements(unittest.TestCase):
    """指标要素定义"""
    IndicatorId = ""
    Indicator_id = ""
    name = ""
    FeatureId = ""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_addUsingPOST(self):
        """
        接口名称：新增指标要素定义
        接口地址：/decision/$VERSION$/indelemdef
        """
        IndicatorElements.Indicator_id = ApiIndicatorElements.addUsingPOST(self)
        print(IndicatorElements.Indicator_id)

    def test_0200_queryTreeUsingGET(self):
        """
        接口名称：查询指标要素定义树
        接口地址：/decision/$VERSION$/indelemdef/tree
        """
        r = ApiIndicatorElements.queryTreeUsingGET(self,
                                                   name=""
                                                   )
        print(r)
        IndicatorElements.IndicatorId = r[0].get("id")
        print("IndicatorElements.IndicatorId:", IndicatorElements.IndicatorId)

    def test_0300_isRepeatUsingGET(self):
        """
        接口名称：判断名称是否重复
        接口地址：/decision/$VERSION$/indicatorelem/exist
        """
        ApiIndicatorElements.isRepeatUsingGET(self,
                                              flag="1",
                                              name="测试"
                                              )

    def test_0400_queryOneUsingGET(self):
        """
        接口名称：查询指标要素定义
        接口地址：/decision/$VERSION$/indelemdef/{id}
        """
        r = ApiIndicatorElements.queryOneUsingGET(self,
                                                  IndicatorId=IndicatorElements.IndicatorId
                                                  )
        print(r)
        IndicatorElements.FeatureId = r[-1].get("id")
        print("IndicatorElements.FeatureId:", IndicatorElements.FeatureId)

    def test_0500_updateUsingPUT(self):
        """
        接口名称：修改指标要素定义
        接口地址：/decision/$VERSION$/indelemdef
        """
        ApiIndicatorElements.updateUsingPUT(self,
                                            elIndElemDef={
                                                "indicatorElementDef": [
                                                    {
                                                        "id": IndicatorElements.IndicatorId,
                                                        "name": "test_" + time.strftime('%Y-%m-%d %H %M %S',
                                                                                        time.localtime()),
                                                        "description": "12",
                                                        "evaluateAlgorithm": "",
                                                        "evaluateMethod": "math",
                                                        "type": 1
                                                    },
                                                    {
                                                        "id": IndicatorElements.FeatureId,
                                                        "name": "1",
                                                        "description": "1",
                                                        "type": 2
                                                    }
                                                ]
                                            }
                                            )


    def test_0600_deleteUsingDELETE_1(self):
        """
        接口名称：批量删除指标要素定义
        接口地址：/decision/$VERSION$/indelemdef/{ids}
        """
        ApiIndicatorElements.deleteUsingDELETE_1(self,ids=IndicatorElements.Indicator_id)


if __name__ == '__main__':
    unittest.main()

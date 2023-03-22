# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/3/4
import random
import time
import unittest
from project.api import ApiTaskViewController, \
    ApiRequireViewController, ApiRequireBaselineViewController, \
    ApiIssueViewController, ApiIssueBaselineViewController, \
    ApiProjectBaseline
from project.api import ApiProjectViewController
from project.case.file.runSql import db


class Controller(unittest.TestCase):
    """Controller"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass

    def test_0101_selectAvlbFieldListUsingGET_4(self):
        """
        接口名称：查询可用的扩展列名称
        接口地址：/proj/$VERSION$/extfields
        """
        ApiProjectViewController.selectAvlbFieldListUsingGET_4(self,
                                                               active=""  # 1已使用0未使用，空所有
                                                               )

    def test_0102_addExtfieldsUsingPOST_3(self):
        """
        接口名称：添加可扩展列
        接口地址：/proj/$VERSION$/extfields
        """
        ApiProjectViewController.addExtfieldsUsingPOST_3(self,
                                                         attrName="test_" + time.strftime("%H%M%S", time.localtime()),
                                                         attrKey="ext_" + time.strftime("%H%M%S", time.localtime()),
                                                         attrType="varchar",
                                                         typeLength="32",
                                                         defaultValue=""
                                                         )

    def test_0103_businessTableUsingPOST_3(self):
        """
        接口名称：查询业务表格列
        接口地址：/proj/$VERSION$/{viewid}/businessTable
        """
        ApiProjectViewController.businessTableUsingPOST_3(self,
                                                          viewid=db.task_view_id
                                                          )

    def test_1001_select_filter_list_using_post_6(self):
        """
        接口名称：过滤业务数据
        接口地址：/plan/$VERSION$/baseline/{viewid}/filterlist
        """
        ApiProjectBaseline.select_filter_list_using_post_6(self,
                                                           view_id=db.risk_view_id,
                                                           view_dto={"pageindex": 1, "pagesize": 20,
                                                                     "elConditionList": [
                                                                         {"name": "state", "value": "DRAFT",
                                                                          "oper": "in",
                                                                          "fieldType": "lifecycle"}],
                                                                     "elView": {"id": db.risk_view_id,
                                                                                "code": "", "name": "所有的",
                                                                                "description": "",
                                                                                "businessType": "erd.cloud.risk.dto.EtRisk",
                                                                                "affiliation": "system",
                                                                                "conditionRef": "and", "enabled": "0",
                                                                                "viewDefault": "1", "projectId": "",
                                                                                "contextType": "3",
                                                                                "selectedFields": "168,179,180,171,174,169,176,702,704,700,168,701,175,703,181"},
                                                                     "mgReqFlag": "false"}
                                                           )

    def test_0201_selectAvlbFieldListUsingGET_8(self):
        """
        接口名称：查询可用的扩展列名称
        接口地址：/plan/$VERSION$/extfields
        """
        ApiTaskViewController.selectAvlbFieldListUsingGET_8(self,
                                                            active=""
                                                            )

    def test_0202_addExtfieldsUsingPOST_7(self):
        """
        接口名称：添加可扩展列
        接口地址：/plan/$VERSION$/extfields
        """
        ApiTaskViewController.addExtfieldsUsingPOST_7(self,
                                                      attrName="test_" + time.strftime("%H%M%S", time.localtime()),
                                                      attrKey="ext_" + time.strftime("%H%M%S", time.localtime()),
                                                      attrType="varchar",
                                                      typeLength="16",
                                                      defaultValue=""
                                                      )

    def test_0203_businessTableUsingPOST_7(self):
        """
        接口名称：查询业务表格列
        接口地址：/plan/$VERSION$/{viewid}/businessTable
        """
        ApiTaskViewController.businessTableUsingPOST_7(self,
                                                       viewid=db.task_view_id
                                                       )

    def test_0204_selectBusinessListUsingPOST_6(self):
        """
        接口名称：查询业务数据
        接口地址：/plan/$VERSION$/{viewid}/businesslist
        """
        ApiTaskViewController.selectBusinessListUsingPOST_6(self,
                                                            view_id=db.viewid_id,
                                                            viewDto={
                                                                "mgReqFlag": "false",
                                                                "pageindex": 1, "pagesize": 20,
                                                                "projectid": db.project_id
                                                            }
                                                            )

    def test_0205_selectFilterListUsingPOST_7(self):
        """
        接口名称：过滤业务数据
        接口地址：/issue/$VERSION$/baseline/{viewid}/filterlist
        """
        ApiTaskViewController.selectFilterListUsingPOST_7(self,
                                                          viewid=db.task_view_id,
                                                          viewDto={"pageindex": 1, "pagesize": 20, "elConditionList": [
                                                              {"name": "state", "value": "PREPARING", "oper": "in",
                                                               "fieldType": "lifecycle"}],
                                                                   "elView": {"id": db.task_view_id,
                                                                              "code": "", "name": "所有的",
                                                                              "description": "",
                                                                              "businessType": "erd.cloud.plan.dto.EtTask",
                                                                              "affiliation": "system",
                                                                              "conditionRef": "and", "enabled": "0",
                                                                              "viewDefault": "1", "projectId": "",
                                                                              "contextType": "3",
                                                                              "selectedFields": "501,59,60,41,30,37,36,503,505,500,32,33,34,35,47,49,46"},
                                                                   "mgReqFlag": "false"}
                                                          )

    def test_0301_selectAvlbFieldListUsingGET_6(self):
        """
        接口名称：查询可用的扩展列名称
        接口地址：/req/$VERSION$/extfields
        """
        ApiRequireViewController.selectAvlbFieldListUsingGET_6(self,
                                                               active=""
                                                               )

    @unittest.skip('因为超出行的大小')
    def test_0302_addExtfieldsUsingPOST_5(self):
        """
        接口名称：添加可扩展列
        接口地址：/req/$VERSION$/extfields
        """
        ApiRequireViewController.addExtfieldsUsingPOST_5(self,
                                                         attrName="test_" + time.strftime("%H%M%S", time.localtime()),
                                                         attrKey="ext_" + time.strftime("%H%M%S", time.localtime()),
                                                         attrType="varchar",
                                                         typeLength=random.randint(50, 100),
                                                         defaultValue=""
                                                         )

    def test_0303_businessTableUsingPOST_5(self):
        """
        接口名称：查询业务表格列
        接口地址：/req/$VERSION$/{viewid}/businessTable
        """
        ApiRequireViewController.businessTableUsingPOST_5(self,
                                                          viewid=db.require_view_id
                                                          )

    def test_0304_selectBusinessListUsingPOST_3(self):
        """
        接口名称：查询业务数据
        接口地址：/req/$VERSION$/{viewid}/businesslist
        """
        ApiRequireViewController.selectBusinessListUsingPOST_3(self,
                                                               viewid=db.require_view_id,
                                                               viewDto={"pageindex": 1, "pagesize": 20,
                                                                        "mgReqFlag": "false"}
                                                               )

    def test_0305_selectFilterListUsingPOST_3(self):
        """
        接口名称：过滤业务数据
        接口地址：/req/$VERSION$/{viewid}/filterlist
        """
        ApiRequireViewController.selectFilterListUsingPOST_3(self,
                                                             viewid=db.require_view_id,
                                                             viewDto={"pageindex": 1, "pagesize": 20,
                                                                      "elConditionList": [
                                                                          {"name": "state", "value": "DRAFT",
                                                                           "oper": "in", "fieldType": "lifecycle"}],
                                                                      "elView": {
                                                                          "id": db.require_view_id,
                                                                          "code": "", "name": "所有的", "description": "",
                                                                          "businessType": "erd.cloud.require.dto.EtRequirement",
                                                                          "affiliation": "system",
                                                                          "conditionRef": "and", "enabled": "0",
                                                                          "viewDefault": "1", "projectId": "",
                                                                          "contextType": "3",
                                                                          "selectedFields": "885,50f01335cfab40ad879923d6113a2054,213,194,191,201,193,196,803,801,199,804,800,198,200,203"},
                                                                      "mgReqFlag": "false"}
                                                             )

    def test_3001_selectAvlbFieldListUsingGET_5(self):
        """
        接口名称：查询可用的扩展列名称
        接口地址：/req/$VERSION$/baseline/extfields
        """
        ApiRequireBaselineViewController.selectAvlbFieldListUsingGET_5(self,
                                                                       active=""
                                                                       )

    @unittest.skip('因为超出行的大小')
    def test_3002_addExtfieldsUsingPOST_4(self):
        """
        接口名称：添加可扩展列
        接口地址：/req/$VERSION$/baseline/extfields
        """
        ApiRequireBaselineViewController.addExtfieldsUsingPOST_4(self,
                                                                 attrName="test_" + time.strftime("%H%M%S",
                                                                                                  time.localtime()),
                                                                 attrKey="ext_" + time.strftime("%H%M%S",
                                                                                                time.localtime()),
                                                                 attrType="varchar",
                                                                 typeLength=random.randint(1, 30),
                                                                 defaultValue=""
                                                                 )

    def test_3003_businessTableUsingPOST_4(self):
        """
        接口名称：查询业务表格列
        接口地址：/req/$VERSION$/baseline/{viewid}/businessTable
        """
        ApiRequireBaselineViewController.businessTableUsingPOST_4(self,
                                                                  viewid=db.require_view_id
                                                                  )

    def test_3004_selectBusinessListUsingPOST_2(self):
        """
        接口名称：查询业务数据
        接口地址：/req/$VERSION$/baseline/{viewid}/businesslist
        """
        ApiRequireBaselineViewController.selectBusinessListUsingPOST_2(self,
                                                                       viewid=db.require_view_id,
                                                                       viewDto={"pageindex": 1, "pagesize": 20,
                                                                                "mgReqFlag": "false"}
                                                                       )

    def test_3005_selectFilterListUsingPOST_2(self):
        """
        接口名称：过滤业务数据
        接口地址：/req/$VERSION$/baseline/{viewid}/filterlist
        """
        ApiRequireBaselineViewController.selectFilterListUsingPOST_2(self,
                                                                     viewid=db.require_view_id,
                                                                     viewDto={"pageindex": 1, "pagesize": 20,
                                                                              "elConditionList": [
                                                                                  {"name": "state", "value": "DRAFT",
                                                                                   "oper": "in",
                                                                                   "fieldType": "lifecycle"}],
                                                                              "elView": {
                                                                                  "id": db.require_view_id,
                                                                                  "code": "", "name": "所有的",
                                                                                  "description": "",
                                                                                  "businessType": "erd.cloud.require.dto.EtRequirement",
                                                                                  "affiliation": "system",
                                                                                  "conditionRef": "and", "enabled": "0",
                                                                                  "viewDefault": "1", "projectId": "",
                                                                                  "contextType": "3",
                                                                                  "selectedFields": "885,50f01335cfab40ad879923d6113a2054,213,194,191,201,193,196,803,801,199,804,800,198,200,203"},
                                                                              "mgReqFlag": "false"}
                                                                     )

    def test_0401_selectAvlbFieldListUsingGET_1(self):
        """
        接口名称：查询可用的扩展列名称
        接口地址：/req/$VERSION$/extfields
        """
        ApiIssueViewController.selectAvlbFieldListUsingGET_1(self,
                                                             active=""
                                                             )

    @unittest.skip('因为超出行的大小')
    def test_0402_addExtfieldsUsingPOST_1(self):
        """
        接口名称：添加可扩展列
        接口地址：/issue/$VERSION$/extfields
        """
        ApiIssueViewController.addExtfieldsUsingPOST_1(self,
                                                       attrName="test_" + time.strftime("%H%M%S", time.localtime()),
                                                       attrKey="ext_" + time.strftime("%H%M%S", time.localtime()),
                                                       attrType="varchar",
                                                       typeLength=random.randint(1, 30),
                                                       defaultValue=""
                                                       )

    def test_0403_businessTableUsingPOST_1(self):
        """
        接口名称：查询业务表格列
        接口地址：/issue/$VERSION$/{viewid}/businessTable
        """
        ApiIssueViewController.businessTableUsingPOST_1(self,
                                                        viewid=db.issue_view_id
                                                        )

    def test_0404_selectBusinessListUsingPOST_1(self):
        """
        接口名称：查询业务数据
        接口地址：/issue/$VERSION$/{viewid}/businesslist
        """
        ApiIssueViewController.selectBusinessListUsingPOST_1(self,
                                                             viewid=db.issue_view_id,
                                                             viewDto={"pageindex": 1, "pagesize": 20,
                                                                      "mgReqFlag": "false"}
                                                             )

    def test_4001_selectAvlbFieldListUsingGET(self):
        """
        接口名称：查询可用的扩展列名称
        接口地址：/issue/$VERSION$/baseline/extfields
        """
        ApiIssueBaselineViewController.selectAvlbFieldListUsingGET(self,
                                                                   active=""
                                                                   )

    @unittest.skip('因为超出行的大小')
    def test_4002_addExtfieldsUsingPOST(self):
        """
        接口名称：添加可扩展列
        接口地址：/issue/$VERSION$/baseline/extfields
        """
        ApiIssueBaselineViewController.addExtfieldsUsingPOST(self,
                                                             attrName="test_" + time.strftime("%H%M%S",
                                                                                              time.localtime()),
                                                             attrKey="ext_" + time.strftime("%H%M%S", time.localtime()),
                                                             attrType="varchar",
                                                             typeLength=random.randint(1, 30),
                                                             defaultValue=""
                                                             )

    def test_4003_businessTableUsingPOST(self):
        """
        接口名称：查询业务表格列
        接口地址：/issue/$VERSION$/baseline/{viewid}/businessTable
        """
        ApiIssueBaselineViewController.businessTableUsingPOST(self,
                                                              viewid=db.issue_view_id
                                                              )

    def test_4004_selectBusinessListUsingPOST(self):
        """
        接口名称：查询业务数据
        接口地址：/issue/$VERSION$/baseline/{viewid}/businesslist
        """
        ApiIssueBaselineViewController.selectBusinessListUsingPOST(self,
                                                                   viewid=db.issue_view_id,
                                                                   viewDto={
                                                                       "mgReqFlag": "false",
                                                                       "pageindex": 1, "pagesize": 20,
                                                                       "projectid": db.project_id
                                                                   }
                                                                   )


if __name__ == '__main__':
    unittest.main()

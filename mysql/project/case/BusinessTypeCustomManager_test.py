# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/3/8

import unittest
import time
from project.api import ApiBusinessTypeCustomManager


class BusinessTypeCustomManager(unittest.TestCase):
    """业务类型自定义管理器"""
    TypelayoutID = ""
    active = ""
    contextId = ""
    contextType = ""
    createTime = ""
    delFlag = ""
    name = ""
    projectType = ""
    tplType = ""
    typedefId = ""
    typedefName = ""
    updateTime = ""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_0100_saveLayoutUsingPOST(self):
        """
        接口名称：创建类型布局
        接口地址：/proj/$VERSION$/type/layout
        """
        r = ApiBusinessTypeCustomManager.saveLayoutUsingPOST(self,
                                                             name="测试" + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                       time.localtime()),
                                                             projectType="-1",
                                                             tplType="create",
                                                             template="",
                                                             contextId="",
                                                             contextType="system",
                                                             active=0,
                                                             typedefId=3,
                                                             typedefName="erd.cloud.plan.dto.EtTask",
                                                             typeDef_createTime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                              time.localtime()),
                                                             typeDef_updateTime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                                              time.localtime())
                                                             )

        print(r)
        BusinessTypeCustomManager.TypelayoutID = r["res"]["data"]["id"]
        BusinessTypeCustomManager.active = r["res"]["data"]["active"]
        BusinessTypeCustomManager.contextId = r["res"]["data"]["contextId"]
        BusinessTypeCustomManager.contextType = r["res"]["data"]["contextType"]
        BusinessTypeCustomManager.createTime = r["res"]["data"]["createTime"]
        BusinessTypeCustomManager.delFlag = r["res"]["data"]["delFlag"]
        BusinessTypeCustomManager.name = r["res"]["data"]["name"]
        BusinessTypeCustomManager.projectType = r["res"]["data"]["projectType"]
        BusinessTypeCustomManager.tplType = r["res"]["data"]["tplType"]
        BusinessTypeCustomManager.typedefId = r["res"]["data"]["typedefId"]
        BusinessTypeCustomManager.typedefName = r["res"]["data"]["typedefName"]
        BusinessTypeCustomManager.updateTime = r["res"]["data"]["updateTime"]

    def test_0200_enableLayoutUsingPOST(self):
        """
        接口名称：启用类型布局
        接口地址：/proj/$VERSION$/type/layout/{id}
        """
        ApiBusinessTypeCustomManager.enableLayoutUsingPOST(self,
                                                           # TypelayoutID=BusinessTypeCustomManager.TypelayoutID
                                                           TypelayoutID="43dc7789d93142788e3043bf9f0a2cc1"  # 任务更新布局调整
                                                           # 启用一个布局时，页面初始化的布局就会被停用，容易引起功能故障；而初始化的布局ID只能通过sys接口获取，所以，在这里将需要启用的布局的ID写死。
                                                           )

    def test_0300_updateLayoutUsingPUT(self):
        """
        接口名称：更新类型布局
        接口地址：/proj/$VERSION$/type/layout/{id}
        """
        ApiBusinessTypeCustomManager.updateLayoutUsingPUT(self,
                                                          TypelayoutID=BusinessTypeCustomManager.TypelayoutID,
                                                          layout={"tplJson": "{}",
                                                                  "typedefId": BusinessTypeCustomManager.typedefId,
                                                                  "typedefName": BusinessTypeCustomManager.typedefName,
                                                                  "active": BusinessTypeCustomManager.active,
                                                                  "contextType": BusinessTypeCustomManager.contextType,
                                                                  "typeDef.id": BusinessTypeCustomManager.typedefId,
                                                                  "typeDef.createBy": "1",
                                                                  "typeDef.createTime": "2017-09-26 12:08:23",
                                                                  "typeDef.updateBy": "1",
                                                                  "typeDef.updateTime": "2017-09-26 12:08:23",
                                                                  "typeDef.delFlag": "0",
                                                                  "typeDef.name": "erd.cloud.plan.dto.EtTask",
                                                                  "typeDef.paramName": "ELTask",
                                                                  "typeDef.displayCn": "任务",
                                                                  "typeDef.displayEn": "Task",
                                                                  "typeDef.description": "任务定义",
                                                                  "typeDef.icon": "",
                                                                  "typeDef.instantiable": 1,
                                                                  "name": BusinessTypeCustomManager.name}
                                                          )

    def test_0400_delLayoutUsingDELETE(self):
        """
        接口名称：删除类型布局
        接口地址：/proj/$VERSION$/type/layout/{id}
        """
        ApiBusinessTypeCustomManager.delLayoutUsingDELETE(self,
                                                          TypelayoutID=BusinessTypeCustomManager.TypelayoutID
                                                          )


if __name__ == '__main__':
    unittest.TestCase()

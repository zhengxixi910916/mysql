# -*- coding: utf-8 -*-
# @Time    : 2021/7/15
# @Author  : Chen

import json
import unittest
from project.api import ApiRequireExport
from project.case.file.runSql import db


class RequireExportExcel(unittest.TestCase):
    """需求管理-导入导出"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    # def test_1000_Require_Export_Excel(self):
    #     """导出需求数据"""
    #     elConditionList = [{"name": "createTime", "value": "2021-06-29,", "oper": "between", "fieldType": "datetime"},
    #                        {"name": "submitterId", "value": "025CE39B20EA11E7A81AC85B767C89C1", "oper": "eq",
    #                         "fieldType": "user"}]
    #
    #     get_export_excel = ApiRequireExport.RequireExportExcel(self,
    #                                                              elConditionList=json.dumps(elConditionList),
    #                                                              exprotList="createBy,createTime",
    #                                                              isFilter="true",
    #                                                              relationship="and",
    #                                                              mgReqFlag="true",
    #                                                              businessType="com.elead.ppm.require.domain.entity.ELRequirement",
    #                                                              viewid="6e8741e2e55f44dd88a98933cbebbecd",
    #                                                              exportIdList="")
    #     print(get_export_excel)
    #
    # def test_2000_Require_Export_Template(self):
    #     """导入导出模板下载"""
    #     get_export_template = ApiRequireExport.RequireExportTemplate(self,
    #                                                                    project_id="",
    #                                                                    businessType="com.elead.ppm.require.domain.entity.ELRequirement",
    #                                                                    exprotList="code,name,workLoad,stateTemplateId,ownerId,priority,"
    #                                                                         "busiValue,acceptanceStandard,submitTime,state,reqSource,"
    #                                                                         "department,type,startDate,dueDate,reqValue,description,"
    #                                                                         "createTime,submitterId,labelLinkIds,member,createBy")


    def test_3000_Require_Export_Word(self):
        """导出到word 文档"""
        pass

    def test_4000_Require_Import_Excel(self):
        """导入需求数据"""
        post_import_excel = ApiRequireExport.RequireImportExcel(self,
                                                                file="(binary)",
                                                                project_id="",
                                                                businessType="m.elead.ppm.require.domain.entity.ELRequirement"
                                                                )


if __name__ == '__main__':
    unittest.main(verbosity=2)

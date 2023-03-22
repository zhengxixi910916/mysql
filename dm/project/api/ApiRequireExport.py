import os
import time
from contextlib import closing

from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api
'''
需求管理-导入导出
'''
apis = Api({
    "RequireExportExcel": "/req/$VERSION$/require/export/excel",  # 导出需求数据
    "RequireExportTemplate": "/req/$VERSION$/require/export/template",  # 导入导出模板下载
    "RequireExportWord": "/req/$VERSION$/require/export/word/%s",  # 导出到word 文档
    "RequireImportExcel": "/req/$VERSION$/require/import/excel",  # 导入需求数据
})
def RequireExportExcel(self,elConditionList,exprotList,isFilter,relationship,mgReqFlag,businessType,viewid,exportIdList):
    """
    接口名称：导出需求数据
    接口地址：/req/$VERSION$/require/export/excel
    """
    r = RequestService.call_get(apis.get("RequireExportExcel"),params = {
                    "elConditionList":elConditionList,
                    "exprotList": exprotList,
                    "isFilter": isFilter,  # true
                    "relationship":relationship,
                    "mgReqFlag": mgReqFlag,    # true
                    "businessType":businessType,
                    "viewid": viewid,
                    "exportIdList": exportIdList,
                },)
    # apis.check_success(self, r)
    # # if checker is not None:
    # #     self.assertEqual(checker, r["res"]["data"])
    # return r['res']["data"]


def RequireExportTemplate(self,project_id,businessType,exprotList):
    """
    接口名称：导入导出模板下载
    接口地址：/req/$VERSION$/require/export/template
    """
    r = RequestService.call_get(apis.get("RequireExportTemplate"),params = {
                "projectId":project_id,
                "businessType":businessType,
                "exprotList":exprotList,
                },)
    # apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    # return r['res']["data"]


def RequireExportWord(self):
    """
    接口名称：导出到word 文档
    接口地址：/req/$VERSION$/require/export/word/{project_id}
    """
    r = RequestService.call_get(apis.get("RequireExportWord"))
    # apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    # return r['res']["data"]


def RequireImportExcel(self,file,project_id=None,businessType=None):
    """
    接口名称：导入需求数据
    接口地址：/req/$VERSION$/require/import/excel
    """
    r = RequestService.call_post(apis.get("RequireImportExcel"),data= {
                    "file": file  # file - required: True
                },params= {
                    "projectId": project_id , # 项目ID如果不填，查询的是符合条件的需求 - required: False
                    "businessType":businessType,
                },)
    # apis.check_success(self, r)
    # if checker is not None:
    #     self.assertEqual(checker, r["res"]["data"])
    # return r['res']["data"]


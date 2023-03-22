# -*- coding: utf-8 -*-
# @Time    : 2022/02/24
# @Author  : Chen
import os
import time
from contextlib import closing
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

'''
导出
'''

# 获取上一级目录
dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dir_document = dir_path + r'/document'
times = time.strftime("%Y-%m-%d %H %M %S", time.localtime(time.time()))
file_name = "budget_" + times + ".xlsx"

apis = Api({
    "ExportProject": "/proj/$VERSION$/export",  # 导出项目
    "ExportProjectMembers": "/proj/$VERSION$/exportProjectMember",  # 导出项目成员
})


def ExportProject(self, exprotList, exportIdList=None):
    """
    接口名称：导出项目
    接口地址：/proj/v2/export
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("ExportProject"), params={
        "exprotList": exprotList,
        "exportIdList": exportIdList,
    })) as response:
        with open(dir_document + r"//ExportProject_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def ExportProjectMembers(self, project_id):
    """
    接口名称：导出项目成员
    接口地址：/proj/v2/exportProjectMember
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("ExportProjectMembers"), params={
        "projectId": project_id,
    })) as response:
        with open(dir_document + r"//ExportProjectMembers_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)

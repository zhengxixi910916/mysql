import os
import time
from contextlib import closing
from erdcloud.HttpClient import RequestService
from erdcloud.erdApi import Api

# 获取上一级目录
dir_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dir_document = dir_path + r'/document'
times = time.strftime("%Y-%m-%d %H %M %S", time.localtime(time.time()))
file_name = "budget_" + times + ".xlsx"


'''
项目任务excel
'''
apis = Api({
    "batchImportMilestoneUsingPOST": "/plan/$VERSION$/excel/task/import/batch",  # 批量导入计划里程碑
    "batchUpdateImportMilestoneUsingPOST": "/plan/$VERSION$/excel/task/import/update/batch",  # 批量导入更新计划里程碑
    "exportTaskTemplateUsingGET": "/plan/$VERSION$/excel/task/template/export",  # 下载计划里程碑导入模板
    "exportTaskUpdateTemplateUsingGET": "/plan/$VERSION$/excel/task/update/template/export",  # 下载计划里程碑导入更新模板
    "getTaskExcelListUsingGET": "/plan/$VERSION$/excel/tasks",  # 获取导出任务清单
    "exportTaskExeclUsingGET_1": "/plan/$VERSION$/excel/tasks/export/excel",  # 导出任务
    "exportTaskExeclTemplateUsingGET": "/plan/$VERSION$/excel/tasks/export/excel/template",  # 导出任务模板
    "exportToMppUsingGET": "/plan/$VERSION$/excel/tasks/export/mpp",  # 导出任务清单Mpp
    "uploadTaskExcelUsingPOST": "/plan/$VERSION$/excel/tasks/import/excel",  # 导入任务
})


def batchImportMilestoneUsingPOST(self, checker):
    """
    接口名称：批量导入计划里程碑
    接口地址：/plan/$VERSION$/excel/task/import/batch
    """
    r = RequestService.call_post(apis.get("batchImportMilestoneUsingPOST", None), data={
        "file": ""  # file - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def batchUpdateImportMilestoneUsingPOST(self, checker):
    """
    接口名称：批量导入更新计划里程碑
    接口地址：/plan/$VERSION$/excel/task/import/update/batch
    """
    r = RequestService.call_post(apis.get("batchUpdateImportMilestoneUsingPOST", None), data={
        "file": ""  # file - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def exportTaskTemplateUsingGET(self, checker):
    """
    接口名称：下载计划里程碑导入模板
    接口地址：/plan/$VERSION$/excel/task/template/export
    """
    r = RequestService.call_get(apis.get("exportTaskTemplateUsingGET", None), None)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def exportTaskUpdateTemplateUsingGET(self, checker):
    """
    接口名称：下载计划里程碑导入更新模板
    接口地址：/plan/$VERSION$/excel/task/update/template/export
    """
    r = RequestService.call_get(apis.get("exportTaskUpdateTemplateUsingGET", None), None)
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def getTaskExcelListUsingGET(self, project_id):
    """
    接口名称：获取导出任务清单
    接口地址：/plan/$VERSION$/excel/tasks
    """
    old_count = len(os.listdir(dir_document))
    with closing(RequestService.call_get_download(apis.get("getTaskExcelListUsingGET"), params={
        "projectId": project_id,
    })) as response:
        with open(dir_document + r"//getTaskExcelListUsingGET_" + times + ".xlsx", "wb") as file:
            for data in response.iter_content(128):
                file.write(data)
    new_count = len(os.listdir(dir_document))
    self.assertTrue(new_count > old_count)


def exportTaskExeclUsingGET_1(self, project_id, checker=None):
    """
    接口名称：导出任务
    接口地址：/plan/$VERSION$/excel/tasks/export/excel
    """
    r = RequestService.call_get(apis.get("exportTaskExeclUsingGET_1", None), params={
        "projectId": project_id  # project_id - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def exportTaskExeclTemplateUsingGET(self, checker):
    """
    接口名称：导出任务模板
    接口地址：/plan/$VERSION$/excel/tasks/export/excel/template
    """
    r = RequestService.call_get(apis.get("exportTaskExeclTemplateUsingGET", None), params={
        "fields": ""  # 导出字段名称集合 - required: False
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def exportToMppUsingGET(self, checker):
    """
    接口名称：导出任务清单Mpp
    接口地址：/plan/$VERSION$/excel/tasks/export/mpp
    """
    r = RequestService.call_get(apis.get("exportToMppUsingGET", None), params={
        "projectId": ""  # project_id - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]


def uploadTaskExcelUsingPOST(self, checker):
    """
    接口名称：导入任务
    接口地址：/plan/$VERSION$/excel/tasks/import/excel
    """
    r = RequestService.call_post(apis.get("uploadTaskExcelUsingPOST", None), data={
        "file": ""  # file - required: True
    }, params={
        "projectId": ""  # 项目id - required: True
    }, )
    apis.check_success(self, r)
    if checker is not None:
        self.assertEqual(checker, r["res"]["data"])
    return r['res']["data"]

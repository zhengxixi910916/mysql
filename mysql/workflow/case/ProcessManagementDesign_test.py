import unittest

from workflow.api import ApiProcessTemplateManagement
from workflow.api.WF24NewApi import *
from workflow.api.ApiProcessManagementDesign import *


class process_design(unittest.TestCase):
    """流程管理-流程设计"""

    # def test_0001_process_design(self):
    #     """
    #     接口名称：模板保存或更新接口;
    #     接口地址：/workflow/v1/dynamic/api/model/saveOrUpdate；
    #     """
    #     # 创建流程分类
    #     add_category()
    #     # 创建流程模板
    #     r = saveOrUpdate_model()
    #     self.assertEqual('200', r['code'])
#    接口地址更改
    # def test_0002_process_design(self):
    #     """
    #     接口名称：模板详情接口;
    #     接口地址：/workflow/v1/dynamic/api/model/view/{templateId}；
    #     """
    #     # 查询模板列表获取模板id
    #     id = 'e57e463812e01db7c00727d7c74dd22f'
    #     r = model_view(id)
    #     self.assertEqual('200', r['code'])
    #
    # def test_0003_process_design(self):
    #     """
    #     接口名称:分页查询流程模板;接口地址：/workflow/$VERSION$/dynamic/api/common/pageQuery/launchRecord/pageSize/pageIndex;
    #     """
    #     r = pageQuery_model()
    #     print(r)
    #     self.assertEqual('200', r['code'])
    #
    # def test_0004_process_design(self):
    #     """
    #     接口名称:检出模板;接口地址:/workflow/v1/procmodel/checkedout/model/%s;
    #     """
    #     r = checkedout_model('e57e463812e01db7c00727d7c74dd22f')
    #     print(r)
    #     self.assertEqual('200', r['code'])


if __name__ == '__main__':
    unittest.main()

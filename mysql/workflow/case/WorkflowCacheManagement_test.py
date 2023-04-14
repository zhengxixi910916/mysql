# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/4/7

import unittest
from workflow.api import ApiWorkflowCacheManagement


class WorkflowCacheManagement(unittest.TestCase):
    """工作流-缓存管理"""
    region = ""
    key = ""

    def test_0100_get_cache_regions_using_get_1(self):
        """
        接口名称：获取空间;        接口地址：/wf/$VERSION$/cache/regions;     调用位置：系统管理-缓存管理-服务列表-erdcloud-workflow-app
        """
        r = ApiWorkflowCacheManagement.get_cache_regions_using_get_1(self,
                                                                     service="workflow"
                                                                     )
        print(r)
        WorkflowCacheManagement.region = r["res"]["data"]["records"][0]["name"]
        print("WorkflowCacheManagement.region:", WorkflowCacheManagement.region)

    # def test_0100_get_cache_regions_using_get(self):
    #     """
    #     接口名称：获取空间;        接口地址：/$VERSION$/cache/regions;
    #     """
    #     ApiWorkflowCacheManagement.get_cache_regions_using_get(self,
    #                                                            service="workflow"
    #                                                            )

    def test_0101_get_cache_keys_using_get_1(self):
        """
        接口名称：获取空间keys;        接口地址：/wf/$VERSION$/cache/keys;    调用位置：系统管理-缓存管理-服务列表-erdcloud-workflow-app-获取keys
        """
        r = ApiWorkflowCacheManagement.get_cache_keys_using_get_1(self,
                                                                  region=WorkflowCacheManagement.region
                                                                  )
        print(r)
        # WorkflowCacheManagement.key = r["res"]["data"][0]         # 正常来说，需要获取key作为后续接口的入参，但因为缓存数据为空，所以暂时将这里注释。
        # print("WorkflowCacheManagement.key:", WorkflowCacheManagement.key)

    # def test_0101_get_cache_keys_using_get(self):
    #     """
    #     接口名称：获取空间keys;        接口地址：/$VERSION$/cache/keys;
    #     """
    #     ApiWorkflowCacheManagement.get_cache_keys_using_get(self,
    #                                                         region=WorkflowCacheManagement.region
    #                                                         )

    def test_0102_clear_all_using_get_1(self):
        """
        接口名称：清空所有空间缓存;        接口地址：/wf/$VERSION$/cache/clearAll;    调用位置：系统管理-缓存管理-服务列表-erdcloud-workflow-app-清除所有的缓存空间
        """
        r = ApiWorkflowCacheManagement.clear_all_using_get_1(self)
        print(r)

    # def test_0102_clear_all_using_get(self):
    #     """
    #     接口名称：清空所有空间缓存;        接口地址：/$VERSION$/cache/clearAll;
    #     """
    #     ApiWorkflowCacheManagement.clear_all_using_get(self)

    def test_0103_clear_using_get_1(self):
        """
        接口名称：清空缓存空间;        接口地址：/wf/$VERSION$/cache/clear;     调用位置：系统管理-缓存管理-服务列表-erdcloud-workflow-app-勾选数据-清空缓存空间
        """
        r = ApiWorkflowCacheManagement.clear_using_get_1(self,
                                                         region=WorkflowCacheManagement.region
                                                         )
        print(r)

    # def test_0103_clear_using_get(self):
    #     """
    #     接口名称：清空缓存空间;        接口地址：/$VERSION$/cache/clear;
    #     """
    #     ApiWorkflowCacheManagement.clear_using_get(self,
    #                                                region=WorkflowCacheManagement.region
    #                                                )

    def test_0104_clear_using_post_1(self):
        """
        接口名称：清空多个缓存空间;        接口地址：/wf/$VERSION$/cache/clear;       调用位置：不知道
        """
        r = ApiWorkflowCacheManagement.clear_using_post_1(self,
                                                          regions=[WorkflowCacheManagement.region]
                                                          )
        print(r)

    # def test_0104_clear_using_post(self):
    #     """
    #     接口名称：清空多个缓存空间;        接口地址：/$VERSION$/cache/clear;
    #     """
    #     ApiWorkflowCacheManagement.clear_using_post(self,
    #                                                 regions=[WorkflowCacheManagement.region]
    #                                                 )

    def test_0105_get_cache_using_get_1(self):
        """
        接口名称：获取缓存;        接口地址：/wf/$VERSION$/cache/get;     调用位置：系统管理-缓存管理-服务列表-erdcloud-workflow-app-获取keys-获取缓存
        """
        r = ApiWorkflowCacheManagement.get_cache_using_get_1(self,
                                                             key=WorkflowCacheManagement.key,
                                                             region=WorkflowCacheManagement.region
                                                             )
        print(r)

    # def test_0105_get_cache_using_get(self):
    #     """
    #     接口名称：获取缓存;        接口地址：/$VERSION$/cache/get;
    #     """
    #     ApiWorkflowCacheManagement.get_cache_using_get(self,
    #                                                    key=WorkflowCacheManagement.key,
    #                                                    region=WorkflowCacheManagement.region
    #                                                    )

    def test_0106_evict_using_post_1(self):
        """
        接口名称：清空缓存;        接口地址：/wf/$VERSION$/cache/evict;       调用位置：系统管理-缓存管理-服务列表-erdcloud-workflow-app-获取keys-勾选数据删除
        """
        r = ApiWorkflowCacheManagement.evict_using_post_1(self,
                                                          ids=[WorkflowCacheManagement.key],
                                                          region=WorkflowCacheManagement.region
                                                          )
        print(r)

    # def test_0106_evict_using_post(self):
    #     """
    #     接口名称：清空缓存;        接口地址：/$VERSION$/cache/evict;
    #     """
    #     ApiWorkflowCacheManagement.evict_using_post(self,
    #                                                 ids=[WorkflowCacheManagement.key],
    #                                                 region=WorkflowCacheManagement.region
    #                                                 )

    def test_0107_check_cache_using_get_1(self):
        """
        接口名称：判断某个key存在于哪级的缓存中;        接口地址：/wf/$VERSION$/cache/check;        调用位置：不知道
        """
        r = ApiWorkflowCacheManagement.check_cache_using_get_1(self,
                                                               key=WorkflowCacheManagement.key,
                                                               region=WorkflowCacheManagement.region
                                                               )
        print(r)

    # def test_0107_check_cache_using_get(self):
    #     """
    #     接口名称：判断某个key存在于哪级的缓存中;        接口地址：/$VERSION$/cache/check;        调用位置：不知道
    #     """
    #     ApiWorkflowCacheManagement.check_cache_using_get(self,
    #                                                      key=WorkflowCacheManagement.key,
    #                                                      region=WorkflowCacheManagement.region
    #                                                      )


if __name__ == '__main__':
    unittest.TestCase()

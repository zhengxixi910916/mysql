# -*- coding: utf-8 -*-
# @Time    : 2022/02/17
# @Author  : Chen

import unittest
from project.api import ApiCacheManagement
from project.case.file.runSql import db


class CacheManagement(unittest.TestCase):
    """缓存管理"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_getCacheRegionsUsingGET(self):
        """
        接口名称：获取空间
        接口地址：/proj/$VERSION$/cache/regions
        """
        ApiCacheManagement.getCacheRegionsUsingGET(self,
                                                   pager_name="20",
                                                   service="proj",
                                                   page_size="20",
                                                   page_index="1"
                                                   )

    def test_0200_clearUsingGET(self):
        """
        接口名称：清空缓存空间
        接口地址：/proj/$VERSION$/cache/clear
        """
        ApiCacheManagement.clearUsingGET(self,
                                         region=""
                                         )

    def test_0300_clearAllUsingGET(self):
        """
        接口名称：清空所有空间缓存
        接口地址：/proj/$VERSION$/cache/clearAll
        """
        ApiCacheManagement.clearAllUsingGET(self)

    def test_0400_getCacheKeysUsingGET(self):
        """
        接口名称：获取空间keys
        接口地址：/proj/$VERSION$/cache/keys
        """
        ApiCacheManagement.getCacheKeysUsingGET(self,
                                                region="KANBAN:CARD",
                                                page_size="20",
                                                page_index="1"
                                                )

    def test_0500_clearUsingPOST(self):
        """
        接口名称：清空多个缓存空间
        接口地址：/proj/$VERSION$/cache/clear
        """
        ApiCacheManagement.clearUsingPOST(self,
                                          regions=["", ""]
                                          )

    def test_0600_getCacheUsingGET(self):
        """
        接口名称：获取缓存
        接口地址：/proj/$VERSION$/cache/get
        """
        ApiCacheManagement.getCacheUsingGET(self,
                                            region="erdcloud:cache:sys_basic_config_all",
                                            key="cache_item_class"
                                            )

    def test_0700_evictUsingPOST(self):
        """
        接口名称：清空缓存
        接口地址：/proj/$VERSION$/cache/evict
        """
        ApiCacheManagement.evictUsingPOST(self,
                                          ids=["cache_item_class"],
                                          region="erdcloud:cache:dynamic:test"
                                          )


if __name__ == '__main__':
    unittest.main()

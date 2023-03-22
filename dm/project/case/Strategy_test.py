# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 15:04
# @Author  : Liao

import time
import unittest

# from db_fixture.mysql_db import DB
from project.api import ApiStrategy


class Strategy(unittest.TestCase):
    """战略目标管理"""
    strategy_name = ""
    strategy_id = ""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # if Strategy.strategy_id != "":
        #     DB.instance().clear_condition(section="project",
        #                                   table="ppm_elstrategy",
        #                                   condition={"id": Strategy.strategy_id})
        # if __name__ == '__main__':
        #     print("delete sql")
        #     db.delete_sql()
        pass

    def test_0100_download_template(self):
        """
        模板下载
        """
        # /decision/$VERSION$/strategies/export/template
        download_template = ApiStrategy.download_template(self)
        print(download_template)

    # def test_0200_import_strategy(self):
    #     """
    #     导入战略或战略目标
    #     """
    #     # /decision/$VERSION$/strategies/import/excel
    #     import_strategy = ApiStrategy.import_strategy(self)
    #     print(import_strategy)

    def test_0300_query_strategy_tree(self):
        """
        查询战略树
        """
        # /decision/$VERSION$/strategies/tree
        query_strategy_tree = ApiStrategy.query_strategy_tree(self)
        print(query_strategy_tree)

    def test_0400_add_strategy(self):
        """
        新增战略或战略目标
        """
        # /decision/$VERSION$/strategy
        Strategy.strategy_name = "strategy_" + time.strftime('%H%M%S', time.localtime())
        add_strategy = ApiStrategy.add_strategy(self,
                                                name=Strategy.strategy_name,
                                                description=Strategy.strategy_name
                                                )
        print(add_strategy)
        Strategy.strategy_id = str(add_strategy)
        print("strategy_id:", Strategy.strategy_id)

    def test_0500_update_strategy(self):
        """
        修改战略或战略目标
        """
        # /decision/$VERSION$/strategy
        update_strategy_name = "update_" + Strategy.strategy_name
        update_strategy = ApiStrategy.update_strategy(self,
                                                      strategy_id=Strategy.strategy_id,
                                                      strategy_name=Strategy.strategy_name,
                                                      strategy_description=Strategy.strategy_name,
                                                      name=update_strategy_name,
                                                      description=update_strategy_name,
                                                      )
        print(update_strategy)

    def test_0600_isrepeat_strategy(self):
        """
        判断名称是否重复
        """
        # /decision/$VERSION$/strategy/exist
        isrepeat_name = "strategy_name"
        isrepeat_strategy = ApiStrategy.isrepeat_strategy(self,
                                                          name=isrepeat_name,
                                                          flag="1"
                                                          )
        print(isrepeat_strategy)

    def test_0700_query_strategy_map(self):
        """
        查询战略键值对
        """
        # /decision/$VERSION$/strategy/map
        query_strategy_map = ApiStrategy.query_strategy_map(self, flag="0")
        print(query_strategy_map)

    def test_0800_query_one_strategy(self):
        """
        查询战略或战略目标
        """
        # /decision/$VERSION$/strategy/{id}
        query_one_strategy = ApiStrategy.query_one_strategy(self, strategyid=Strategy.strategy_id)
        print(query_one_strategy)

    def test_0900_delete_strategy(self):
        """
        删除战略或战略目标
        """
        # /decision/$VERSION$/strategies/{ids}
        delete_strategy = ApiStrategy.delete_strategy(self, strategyid=Strategy.strategy_id)
        print(delete_strategy)



if __name__ == '__main__':
    unittest.main()

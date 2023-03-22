# -*- coding: utf-8 -*-
# @Time    : 2021/7/15
# @Author  : Chen

import time
import unittest
from project.api import ApiVirtualorg
from project.case.file.runSql import db


class Virtualorg(unittest.TestCase):
    """
    虚拟部门
    """

    id_ = None
    parentId = None

    @classmethod
    def setUpClass(cls):
        pass

    # @classmethod
    # def tearDownClass(cls):
    #     print("delete sql")
    #     db.delete_sql()

    def test_1000_AddVirtualorgPost(self):
        """添加虚拟部门"""
        ApiVirtualorg.AddVirtualorgPost(self,
                                        name="test_" + time.strftime('%Y-%m-%d %H %M %S', time.localtime()),
                                        parentId="",
                                        leader="",
                                        pmo="",
                                        description="The time now is：" + time.strftime('%Y-%m-%d %H %M %S',
                                                                                       time.localtime())
                                        )

    def test_2000_QueryVirtualorgGet(self):
        """查询所有的虚拟部门"""
        r = ApiVirtualorg.QueryVirtualorgGet(self)
        Virtualorg.id_ = r[0]
        Virtualorg.parentId = r[1]

    def test_3000_UpdateVirtualorgPut(self):
        """修改虚拟部门"""
        ApiVirtualorg.UpdateVirtualorgPut(self,
                                          description="1",
                                          flexAttrs={},
                                          id=Virtualorg.id_,
                                          leader="",
                                          name="ceshi",
                                          parentId="",
                                          pmo="")

    def test_4000_VirtualorgGet(self):
        """根据ID查询虚拟部门详情"""
        ApiVirtualorg.VirtualorgGet(self,
                                    id=Virtualorg.id_)

    def test_5000_getVirtualchildenUsingGET(self):
        """根据id查询所有子部门"""
        ApiVirtualorg.getVirtualchildenUsingGET(self,
                                                parentId=Virtualorg.parentId)

    def test_6000_DeleteVirtualorgDelete(self):
        """删除虚拟部门"""

        ApiVirtualorg.DeleteVirtualorgDelete(self,
                                             id=Virtualorg.id_
                                             )


if __name__ == '__main__':
    unittest.main()

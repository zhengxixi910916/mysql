# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/9

import unittest
from workflow.api import ApiFormValidate


class FormValidate(unittest.TestCase):
    """管理表单验证规则"""
    id_ = ""

    def test_0100_add_validate_using(self):
        """
        接口名称：添加表单验证规则;    接口地址：/workflow/$VERSION$/form/validate；
        """
        r = ApiFormValidate.add_validate_using(self, )
        print(r)

    def test_0200_get_validates_using(self):
        """
        接口名称：分页查询表单验证规则列表;    接口地址：/workflow/$VERSION$/form/validate/list；
        """
        r = ApiFormValidate.get_validates_using(self,
                                                dto={}
                                                )
        print(r)
        FormValidate.id_ = r["res"]["data"]["records"][0]["id"]
        print("FormValidate.id_:", FormValidate.id_)

    def test_0300_get_validate_using(self):
        """
        接口名称：查询单个表单验证规则详情;    接口地址：/workflow/$VERSION$/form/validate/{id}；
        """
        r = ApiFormValidate.get_validate_using(self,
                                               id_=FormValidate.id_
                                               )
        print(r)

    def test_0400_edit_validate_using(self):
        """
         接口名称：修改表单验证规则;    接口地址：/workflow/$VERSION$/form/validate/{id}；
         """
        r = ApiFormValidate.edit_validate_using(self,
                                                id_=FormValidate.id_,
                                                dto={}
                                                )
        print(r)

    def test_0500_del_validate_using(self):
        """
        接口名称：批量删除表单验证规则;    接口地址：/workflow/$VERSION$/form/validate/{ids}；
        """
        ApiFormValidate.del_validate_using(self,
                                           id_=FormValidate.id_,
                                           )


if __name__ == '__main__':
    unittest.main()

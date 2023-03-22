# -*- coding: utf-8 -*-#
# Author:zhihuimin
# Date:2022/7/6
import unittest
import random
from project.api import ApiViewManagement, ApiProjectViewController, ApiPortfolioManage, ApiProgramManage


class ViewManagement(unittest.TestCase):
    """
    视图管理
    """
    view_id = ""
    object_id = ""
    object_id_list = []
    view_Condition = ''
    el_condition_list = []

    def test_0090_select_advanced_search(self):
        """
        接口名称：高级查询字段列表
        接口地址：/proj/basis/$VERSION$/view/{type}/advancedsearch
        """
        ApiViewManagement.select_advanced_search(self,
                                                 view_type="erd.cloud.plan.dto.EtTask"
                                                 )

    def test_0100_insert_view(self):
        """
        接口名称：新增视图
        接口地址：/proj/basis/$VERSION$/view/
        """
        r = ApiViewManagement.insert_view(self,
                                          view_name="新增视图" + str(random.randint(100, 999))
                                          )
        # 视图ID
        ViewManagement.view_id = r['id']
        print(ViewManagement.view_id)

    def test_0200_select_view_list(self):
        """
        接口名称：获取视图下拉列表
        接口地址：/proj/basis/$VERSION$/view/selectlist
        """
        ApiViewManagement.select_view_list(self)

    def test_0300_select_view_name_list(self):
        """
        接口名称：查询视图管理列表
        接口地址：/proj/basis/$VERSION$/view/list
        """
        r = ApiViewManagement.select_view_name_list(self)
        # 1-将列表中的对象ID都存到列表中，并打乱顺序，2-根据视图ID取对应的对象ID


        for i in r:
            object_id1 = i['id']
            ViewManagement.object_id_list.append(object_id1)
            if ViewManagement.view_id in i.values():
                ViewManagement.object_id = i['id']
        random.shuffle(ViewManagement.object_id_list)

    def test_0400_view_remember_state(self):
        """
        接口名称：检查是否记住状态
        接口地址：/proj/basis/$VERSION$/view/rememberstate
        """
        ApiViewManagement.view_remember_state(self)

    def test_0500_select_view(self):
        """
        接口名称：查询视图详情
        接口地址：/proj/basis/$VERSION$/view/detail
        """
        r = ApiViewManagement.select_view(self,
                                          view_id=ViewManagement.view_id,
                                          object_id=ViewManagement.object_id
                                          )
        ViewManagement.view_Condition = r['res']['ViewCondition']

    def test_0550_select_filter_list_using_post_4(self):
        """
        接口名称：项目高级查询
        接口地址：/proj/$VERSION$/project/filterlist
        """

        for i in range(len(ViewManagement.view_Condition)):
            ViewManagement.el_condition_list.append({
                "name": ViewManagement.view_Condition[i]["name"],
                "value": ViewManagement.view_Condition[i]["value"],
                "oper": ViewManagement.view_Condition[i]["oper"],
                "fieldType": ViewManagement.view_Condition[i]["fieldType"]
            })
        ApiProjectViewController.select_filter_list_using_post_4(self,
                                                                 el_condition_list=ViewManagement.el_condition_list)

    def test_0560_select_filter_list_using_post_2(self):
        """
        接口名称：项目组合高级查询
        接口地址：/portfolio/$VERSION$/portfolios/filterlist
        """

        ApiPortfolioManage.select_filter_list_using_post_2(self,
                                                           el_condition_list=ViewManagement.el_condition_list)

    def test_0570_select_filter_list_using_post_3(self):
        """
        接口名称：项目群高级查询
        接口地址：/portfolio/$VERSION$/program/filterlist
        """
        ApiProgramManage.select_filter_list_using_post_3(self,
                                                         el_condition_list=ViewManagement.el_condition_list)

    def test_0600_select_view_field(self):
        """
        接口名称：查询视图可显示字段
        接口地址：/proj/basis/$VERSION$/view/{type}/field
        """
        ApiViewManagement.select_view_field(self,
                                            view_type="erd.cloud.plan.dto.EtTask"
                                            )

    def test_0700_update_view(self):
        """
        接口名称：更新视图
        接口地址：/proj/basis/$VERSION$/view/{id}
        """
        ApiViewManagement.update_view(self,
                                      view_id=ViewManagement.view_id,
                                      view_name="更新视图" + str(random.randint(100, 999)),
                                      object_id=ViewManagement.object_id
                                      )

    def test_0800_update_view_user(self):
        """
        接口名称：配置是否禁用，是否默认，是否公共
        接口地址：/proj/basis/$VERSION$/view/updateViewUser
        """
        ApiViewManagement.update_view_user(self,
                                           object_id=ViewManagement.object_id
                                           )

    def test_0900_update_sort(self):
        """
        接口名称：排序
        接口地址：/proj/basis/$VERSION$/view/updateSort
        """
        ApiViewManagement.update_sort(self,
                                      object_id_list=ViewManagement.object_id_list
                                      )

    def test_1000_view_remember(self):
        """
        接口名称：开启关闭是否记住-记住视图
        接口地址：/proj/basis/$VERSION$/view/remember
        """
        ApiViewManagement.view_remember(self)

    def test_1800_del_view(self):
        """
        接口名称：删除视图
        接口地址：/proj/basis/$VERSION$/view/{id}
        """
        ApiViewManagement.del_view(self,
                                   object_id=ViewManagement.object_id
                                   )


if __name__ == '__main__':
    unittest.main()

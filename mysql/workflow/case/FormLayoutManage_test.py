# -*- coding: utf-8 -*-#
# Author:       ChenGuangda
# Date:         2022/5/11

import unittest
import time
from workflow.api import ApiFormLayoutManage, WF24NewApi


class FormLayoutManage(unittest.TestCase):
    """表单布局配置"""
    category = ""
    entity_id = ""
    entity_table = ""
    layout_id = ""

    # def setUp(self) -> None:
    #     # 查询所有的类型
    #     r = ApiEtCategoryControllerImpl.query_all_using_get(self)
    #     FormLayoutManage.category = r["res"]["data"][0]["categoryCode"]
    #     print("category:", FormLayoutManage.category)
    #     # 查询已经发布实体
    #     r = ApiEntityManage.query_list_using(self)
    #     FormLayoutManage.entity_id = r["res"]["data"][0]["id"]
    #     print("entity_id:", FormLayoutManage.entity_id)
    #     FormLayoutManage.entity_table = r["res"]["data"][0]["entityTable"]
    #     print("entity_table:", FormLayoutManage.entity_table)

    def test_0100_add_form_layout(self):
        """
         接口名称：新增、修改表单布局;    接口地址：/workflow/$VERSION$/formlayout；
         """
        r = ApiFormLayoutManage.add_form_layout(self,
                                                dto={"entityTable": FormLayoutManage.entity_table,
                                                     "category": FormLayoutManage.category,
                                                     "entityId": FormLayoutManage.entity_id,
                                                     "formName": "test_" + time.strftime("%H%M%S"),
                                                     "tplJson": "{\"1652262441482-0\":{\"formType\":\"text-input\",\"title\":\"单行输入框\",\"langKey\":\"single__input\",\"active\":true,\"cateType\":\"input\",\"regex\":\"/.*/\",\"regexTips\":\"\",\"cateName\":\"输入框\",\"name\":\"1652262441482-0\",\"disabled\":false,\"displayCn\":\"输入框\",\"displayEn\":\"input_box\",\"value\":\"\",\"type\":\"text\",\"placeholder\":\"\",\"max\":500,\"column\":12,\"required\":false,\"iconClazz\":\"icon-pencil\",\"items\":[{\"formType\":\"text-input\",\"title\":\"单行输入框\",\"langKey\":\"single__input\",\"active\":true},{\"formType\":\"text-icon\",\"title\":\"单行输入框（带图标）\",\"icon\":\"eliconfont icon-file\",\"langKey\":\"single_input(icon)\"},{\"formType\":\"text-addon\",\"title\":\"单行输入框（带单位）\",\"langKey\":\"single_input(unit)\",\"prefix\":\"$\",\"suffix\":\"\"}]}}"}
                                                )
        print(r)

    def test_0200_query_page_using(self):
        """
        接口名称：表单布局分页列表;    接口地址：/workflow/$VERSION$/formlayout/page；
        """
        data = {
            "formName": "",
            "layoutType": "",
            "sortBy": "",
            "orderBy": "",
            "pageSize": 20,
            "pageIndex": 1,
            "contextType": 0,
            "category": -1,
            "_": int(time.time())
        }
        r = ApiFormLayoutManage.query_page_using(data)
        self.assertEqual('200',r['code'])
        print(r)


    def test_0300_query_layout_proc(self):
        """
        接口名称：表单布局绑定的流程定义;    接口地址：/workflow/$VERSION$/formlayout/page/{layoutId}；
        """
        r = ApiFormLayoutManage.query_layout_proc(self,
                                                  layout_id=FormLayoutManage.layout_id
                                                  )
        print(r)

    def test_0400_update_form_layout(self):
        """
           接口名称：修改表单布局;    接口地址：/workflow/$VERSION$/formlayout；
           """
        r = ApiFormLayoutManage.update_form_layout(self,
                                                   dto={}
                                                   )
        print(r)

    def test_1200_query_by_id(self):
        """
        接口名称：根据ID查询表单布局;    接口地址：/workflow/$VERSION$/formlayout/{formLayoutId}；
        """
        r = ApiFormLayoutManage.query_by_id(self,
                                            layout_id="a976d4c29341cb418df7f97396423147"
                                            )
        print(r)

    # def test_1300_del_form_layout(self):
    #     """
    #     接口名称：删除表单布局;    接口地址：/workflow/$VERSION$/formlayout/{formLayoutIds}；
    #     """
    #     #创建表单
    #     WF24NewApi.createLayout()
    #     #查询表单id
    #     id=WF24NewApi.queryLayout()
    #     print(id)
    #     # #删除表单
    #     # id ='4ba71b5b9dcca2f818c1872d653d46f1'
    #     r=WF24NewApi.deleteLayout(id)
    #     self.assertEqual('200',r['code'])

if __name__ == "__main__":
    unittest.main()

import unittest
from project.api import ApiProductInformation
import time


class ProductInformation(unittest.TestCase):
    now_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    product_name = 'auto_test' + now_time
    product_id = ''
    update_name = 'update_' + product_name
    update_type = "IRB"
    user_id = "SYS_E39B20EA11E7A81AC85B767C89C1"

    @unittest.skip('3.4.RC1才运行')
    def test_0100_add_product(self):
        """
        接口名称：产品新增接口
        接口地址：/productteam/$VERSION$/product
        """
        r = ApiProductInformation.add_product(self,
                                              parent_id='-1',
                                              product_name=ProductInformation.product_name,
                                              checker=None
                                              )
        ProductInformation.product_id = r['res']['data']['id']

    @unittest.skip('3.4.RC1才运行')
    def test_0150_add_product(self):
        """
        接口名称：产品新增接口,创建子产品
        接口地址：/productteam/$VERSION$/product
        """
        ApiProductInformation.add_product(self,
                                          parent_id=ProductInformation.product_id,
                                          product_name=ProductInformation.product_name + '_child',
                                          checker=None
                                          )

    @unittest.skip('3.4.RC1才运行')
    def test_0200_update_product(self):
        """
        接口名称：产品信息修改接口
        接口地址：/productteam/$VERSION$/product/{productId}
        """
        ApiProductInformation.update_product(self,
                                             update_name=ProductInformation.update_name,
                                             update_type=ProductInformation.update_type,
                                             product_id=ProductInformation.product_id,
                                             checker=None
                                             )

    @unittest.skip('3.4.RC1才运行')
    def test_0300_save_product_member(self):
        """
        接口名称：角色新增/修改
        接口地址：/productteam/$VERSION$/product/{productId}/members
        """
        ApiProductInformation.save_product_member(self,
                                                  user_id=ProductInformation.user_id,
                                                  product_id=ProductInformation.product_id,
                                                  checker=None
                                                  )

    @unittest.skip('3.4.RC1才运行')
    def test_0400_get_product_member_1(self):
        """
        接口名称：查询团队角色或成员
        接口地址：/productteam/$VERSION$/product/{productId}/members
        """
        ApiProductInformation.get_product_member_1(self,
                                                   product_id=ProductInformation.product_id,
                                                   checker=None
                                                   )

    @unittest.skip('3.4.RC1才运行')
    def test_0500_get_product_member(self):
        """
        接口名称：产品信息查询接口(支持根据人员信息模糊分页查询)
        接口地址：/productteam/$VERSION$/product/list
        """
        ApiProductInformation.get_product_member(self,
                                                 page_index='1',
                                                 page_Size='10',
                                                 checker=None)

    @unittest.skip('3.4.RC1才运行')
    def test_0600_get_product_by(self):
        """
        接口名称：产品查询
        接口地址：/productteam/$VERSION$/product/tree
        """
        ApiProductInformation.get_product_by(self,
                                             parent_id=ProductInformation.product_id,
                                             checker=None
                                             )

    @unittest.skip('3.4.RC1才运行')
    def test_0700_get_used_count(self):
        """
        接口名称：用户在产品团队中应用的数量
        接口地址：/productteam/$VERSION$/product/{userId}/count
        """
        ApiProductInformation.get_used_count(self,
                                             user_id=ProductInformation.user_id,
                                             checker=None)

    @unittest.skip('3.4.RC1才运行')
    def test_0800_get_used_info(self):
        """
        接口名称：用户在产品团队中应用的详情信息
        接口地址：/productteam/$VERSION$/product/{userId}/info
        """
        ApiProductInformation.get_used_info(self,
                                            page_index='1',
                                            page_Size='10',
                                            user_id=ProductInformation.user_id,
                                            checker=None)

    @unittest.skip('3.4.RC1才运行')
    def test_0900_remove_product_member(self):
        """
        接口名称：删除团队
        接口地址：/productteam/$VERSION$/product/members
        """
        ApiProductInformation.remove_product_member(self,
                                                    product_id=ProductInformation.product_id,
                                                    checker=None
                                                    )

    @unittest.skip('3.4.RC1才运行')
    def test_1000_delete_product(self):
        """
        接口名称：产品软删除接口
        接口地址：/productteam/$VERSION$/product/{productId}
        """
        ApiProductInformation.delete_product(self,
                                             product_id=ProductInformation.product_id,
                                             checker=None)


if __name__ == '__main__':
    unittest.main()

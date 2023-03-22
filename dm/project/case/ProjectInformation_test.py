# -*- coding: utf-8 -*-#
# Author:zhihuimin
# Date:2022/7/7
import unittest
from project.api import ApiProjectInformation

class ProjectInformation(unittest.TestCase):
    """
    项目信息
    """

    def test_0100_update_application_config(self):
        """
        接口名称：修改系统应用配置
        接口地址：/proj/$VERSION$/basic/config/-1/update
        """
        ApiProjectInformation.update_application_config(self)
# -*- coding: utf-8 -*-
# @Time    : 2022/02/21
# @Author  : Chen

import unittest, time
from project.api import ApiGPMCSS
from project.case.file.runSql import db


class GPMCSS(unittest.TestCase):
    """获取项目成员完成状况统计"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        # db.delete_sql()
        pass


    def test_0100_getMemberCompletionStatusUsingGET(self):
        """
        接口名称：获取项目成员完成状况
        接口地址：/plan/$VERSION$/getMemberCompletionStatus
        """
        ApiGPMCSS.getMemberCompletionStatusUsingGET(self,
                                                    userId=db.user_id,
                                                    project_ids=db.project_id,
                                                    taskName="",
                                                    orgId=db.org_id,
                                                    startDate="2001-01-01",
                                                    endDate=time.strftime('%Y-%m-%d', time.localtime())
                                                    )

    def test_0200_getMemberCompletionStatusDetailsUsingGET(self):
        """
        接口名称：获取项目成员完成情况详情
        接口地址：/plan/$VERSION$/getMemberCompletionStatus/details
        """
        ApiGPMCSS.getMemberCompletionStatusDetailsUsingGET(self,
                                                           page_index="20",
                                                           page_size="1",
                                                           userId=db.user_id,
                                                           project_ids=db.project_id,
                                                           taskName="",
                                                           orgId=db.org_id,
                                                           startDate="2001-01-01",
                                                           endDate=time.strftime('%Y-%m-%d', time.localtime())
                                                           )

    def test_0300_getMemberCompletionDataUsingGET(self):
        """
        接口名称：点击报表统计数量，查询数据
        接口地址：/plan/$VERSION$/getMemberCompletionData
        """
        ApiGPMCSS.getMemberCompletionDataUsingGET(self,
                                                  endDate=time.strftime('%Y-%m-%d', time.localtime()),
                                                  orgId=db.org_id,
                                                  project_ids=db.project_id,
                                                  startDate="2001-01-01",
                                                  taskName="",
                                                  type="",
                                                  userId=db.user_id
                                                  )


if __name__ == '__main__':
    unittest.main()
